from iqoptionapi.stable_api import IQ_Option
import logging
import time
import os

# Desativar logs de debug
logging.disable(logging.DEBUG)

# Suas credenciais de login
email = os.getenv("IQ_OPTION_EMAIL")
senha = os.getenv("IQ_OPTION_PASSWORD")

# Conectar à conta IQ Option
iqoption = IQ_Option(email, senha)
iqoption.connect()

# Verificar se a conexão foi bem-sucedida
if iqoption.check_connect():
    print("Conectado com sucesso!")
else:
    print("Erro ao conectar.")

# Obter saldo da conta
saldo = iqoption.get_balance()
print(f"Saldo da conta: {saldo}")

# Fechar a conexão
iqoption.close()
