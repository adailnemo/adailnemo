from iqoptionapi.stable_api import IQ_Option
import logging
import time

# Desativar logs de debug
logging.disable(logging.DEBUG)

# Suas credenciais de login
email = "adailnemoforex@gmail.com"
senha = "@Sus2007nemo3481"

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
