import os
import io
import csv
import xml.etree.ElementTree as ET
import uvicorn
from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from manual_ingestion import DataIngestionModule, custom_json_ingest

load_dotenv()
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST")
RABBITMQ_QUEUE = os.getenv("RABBITMQ_QUEUE")

if not RABBITMQ_HOST or not RABBITMQ_QUEUE:
    raise Exception("As variáveis RABBITMQ_HOST e RABBITMQ_QUEUE devem estar definidas no .env.")

ingestion = DataIngestionModule()

app = FastAPI(
    title="API de Ingestão Manual de Dados para Data Lake",
    description=(
        "Esta API possibilita a ingestão manual e automatizada de dados em alguns formatos "
        "(JSON, CSV e XML) para o Data Lake. O módulo permite a customização dos dados antes "
        "de publicá-los na fila RabbitMQ."
    )
)

class CustomJSONRequest(BaseModel):
    data: dict
    custom_fields: dict = None

@app.post("/ingest/json")
async def ingest_json(request: CustomJSONRequest):
    try:
        custom_data = custom_json_ingest(request.data, request.custom_fields)
        
        ingestion.publish_to_rabbitmq(custom_data)
        return {"message": "JSON processado e publicado na fila RabbitMQ com sucesso."}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/ingest/csv")
async def ingest_csv(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        contents_str = contents.decode("utf-8")
        csv_file = io.StringIO(contents_str)
        reader = csv.DictReader(csv_file)
        data = [row for row in reader]
        ingestion.publish_to_rabbitmq(data)
        return {"message": "CSV processado e publicado na fila RabbitMQ com sucesso."}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/ingest/xml")
async def ingest_xml(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        root = ET.fromstring(contents.decode("utf-8"))
        data = ingestion._xml_to_dict(root)
        ingestion.publish_to_rabbitmq(data)
        return {"message": "XML processado e publicado na fila RabbitMQ com sucesso."}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("manual_ingestion_api:app", host="0.0.0.0", port=8000, reload=True)
