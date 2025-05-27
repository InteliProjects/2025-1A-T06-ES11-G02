import os
import random
import time
import sys
from producer.csv_handler import carregar_csv, selecionar_linha_aleatoria
from producer.rabbit_handler import conectar_fila, enviar_para_fila


CSV_ARQUIVOS = {
    "InteliResultados": "data/InteliResultados.csv",
    "InteliVeiculo": "data/InteliVeiculo.csv",
    "InteliFalhas": "data/InteliFalhas.csv",
    "InteliStatus": "data/InteliStatus.csv"
}

def iniciar_producer():
    """Inicia o processo de ingestão e envio de dados para a fila."""
    start_time = time.time()
    contador = 0


    dados_csvs = {nome: carregar_csv(caminho) for nome, caminho in CSV_ARQUIVOS.items()}


    connection, channel = conectar_fila()
    if not connection or not channel:
        return

    print("\nDados enviados:", end=" ", flush=True)

    while True:
        for nome_csv, df in dados_csvs.items():
            linha = selecionar_linha_aleatoria(df)
            if linha:
                mensagem = {
                    "dados": linha,
                    "fonte": nome_csv
                }
                enviar_para_fila(mensagem, channel)

                contador += 1
                sys.stdout.write(f"\rDados enviados: {contador} ")
                sys.stdout.flush()

        delay = random.randint(1, 5)
        time.sleep(delay)

    connection.close()

if __name__ == "__main__":
    iniciar_producer()
