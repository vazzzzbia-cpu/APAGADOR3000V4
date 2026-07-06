import time

def iniciar_bot(main_func):

    while True:

        try:

            print("☠ Iniciando APAGADOR 3000 V3...")
            main_func()

        except KeyboardInterrupt:
            print("🛑 Bot encerrado pelo usuário.")
            break

        except Exception as erro:
            print(f"⚠ Erro: {erro}")
            print("🔄 Reiniciando em 5 segundos...")
            time.sleep(5)
