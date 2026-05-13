import pandas as pd
import random
from datetime import datetime, timedelta

quantidade_registros = 1000

ips = [f"192.168.0.{i}" for i in range(1, 51)]
protocolos = ["TCP", "UDP", "HTTP", "HTTPS"]
portas = [21, 22, 80, 443, 3306, 8080]
status_lista = ["PERMITIDO", "BLOQUEADO"]

dados = []
agora = datetime.now()

for _ in range(quantidade_registros):
    registro = {
        "timestamp": agora - timedelta(minutes=random.randint(0, 1440)),
        "ip_origem": random.choice(ips),
        "ip_destino": random.choice(ips),
        "porta": random.choice(portas),
        "protocolo": random.choice(protocolos),
        "tamanho_pacote": random.randint(40, 1500),
        "status": random.choices(status_lista, weights=[0.85, 0.15])[0]
    }
    dados.append(registro)

df = pd.DataFrame(dados)
df.to_csv("logs_rede.csv", index=False)

print("Arquivo logs_rede.csv criado com sucesso!")
