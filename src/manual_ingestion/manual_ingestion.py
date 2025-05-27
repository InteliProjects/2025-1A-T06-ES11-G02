import csv
import json
import xml.etree.ElementTree as ET
import os
from dotenv import load_dotenv
import pika
from cryptography.fernet import Fernet

load_dotenv()
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST")
RABBITMQ_QUEUE = os.getenv("RABBITMQ_QUEUE")
ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY") or Fernet.generate_key().decode()

class DataIngestionModule:
    def __init__(self):
        pass

    def read_csv(self, file_path: str, delimiter: str = ','):
        data = []
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=delimiter)
            for row in reader:
                data.append(row)
        return data

    def read_json(self, file_path: str):
        with open(file_path, 'r', encoding='utf-8') as jsonfile:
            data = json.load(jsonfile)
        return data

    def read_xml(self, file_path: str):
        tree = ET.parse(file_path)
        root = tree.getroot()
        data = self._xml_to_dict(root)
        return data

    def _xml_to_dict(self, element):
        node = {}
        node.update(element.attrib)
        
        for child in element:
            child_dict = self._xml_to_dict(child)
            if child.tag in node:
                if isinstance(node[child.tag], list):
                    node[child.tag].append(child_dict)
                else:
                    node[child.tag] = [node[child.tag], child_dict]
            else:
                node[child.tag] = child_dict
        text = element.text.strip() if element.text is not None else ''
        if text:
            if node:
                node['text'] = text
            else:
                node = text
        return node

    def export_data(self, data, file_path: str, format: str = 'json'):
        if format.lower() == 'json':
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
        elif format.lower() == 'csv':
            if isinstance(data, list) and data and isinstance(data[0], dict):
                with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
                    fieldnames = data[0].keys()
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    for row in data:
                        writer.writerow(row)
            else:
                raise ValueError("Formato de dados não suportado para exportação em CSV.")
        elif format.lower() == 'xml':
            root = ET.Element("root")
            self._dict_to_xml(root, data)
            tree = ET.ElementTree(root)
            tree.write(file_path, encoding='utf-8', xml_declaration=True)
        else:
            raise ValueError("Formato de exportação não suportado.")

    def _dict_to_xml(self, parent, data):
        if isinstance(data, dict):
            for key, value in data.items():
                elem = ET.SubElement(parent, key)
                self._dict_to_xml(elem, value)
        elif isinstance(data, list):
            for item in data:
                item_elem = ET.SubElement(parent, "item")
                self._dict_to_xml(item_elem, item)
        else:
            parent.text = str(data)

    def encrypt_data(self, data: dict) -> bytes:
        json_data = json.dumps(data)
        fernet = Fernet(ENCRYPTION_KEY.encode())
        encrypted_data = fernet.encrypt(json_data.encode('utf-8'))
        encrypted_data = f"ENC:{encrypted_data}"
        print(encrypted_data)
        return encrypted_data

    def publish_to_rabbitmq(self, data: dict):
        encrypted_data = self.encrypt_data(data)
        print(encrypted_data)

        connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
        channel = connection.channel()
        
        channel.queue_declare(queue=RABBITMQ_QUEUE)
        
        channel.basic_publish(
            exchange='',
            routing_key=RABBITMQ_QUEUE,
            body=encrypted_data,
            properties=pika.BasicProperties(
                delivery_mode=2
            )
        )
        connection.close()
        print("Mensagem publicada na fila RabbitMQ com sucesso.")

def custom_json_ingest(json_data: dict, custom_fields: dict = None) -> dict:
    if custom_fields:
        json_data.update(custom_fields)
    return json_data
