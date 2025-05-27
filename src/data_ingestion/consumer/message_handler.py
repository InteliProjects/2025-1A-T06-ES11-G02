import json
import os
from logger.logger import log_event
from cryptography.fernet import Fernet, InvalidToken

def decodificar_mensagem(body):

    try:
        decoded_message = body.decode()
        log_event(
            status=200, service="decodificar_mensagem",
            error_description=f"Mensagem recebida da fila: {decoded_message}",
            level_type="SUCCESS", context="debug"
        )

        try:
            dados = json.loads(decoded_message)
            return dados, "limpeza de dados"
        except json.JSONDecodeError:
            if decoded_message.startswith("ENC:"):
                token = decoded_message[4:]

                if token.startswith("b'") and token.endswith("'"):
                    token = token[2:-1]

                encryption_key = os.getenv("ENCRYPTION_KEY")
                if not encryption_key:
                    raise ValueError("Encryption key not defined.")

                f = Fernet(encryption_key.encode())
                try:
                    decrypted_str = f.decrypt(token.encode()).decode("utf-8")
                    dados = json.loads(decrypted_str)
                    return dados, "limpeza de dados"
                except InvalidToken:
                    raise ValueError("Token de criptografia inválido.")
            else:
                raise ValueError("Mensagem inválida e sem criptografia.")

    except Exception as e:
        log_event(
            status=None, service="decodificar_mensagem",
            error_description=str(e),
            level_type="ERROR", context="validação de mensagem"
        )
        return None, "erro na mensagem"
