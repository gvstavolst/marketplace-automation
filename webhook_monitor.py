import random
from datetime import datetime

ENDPOINTS = [
    {"nome": "Bling ERP - Pedidos",    "url": "https://api.bling.com.br/webhook/pedidos"},
    {"nome": "SmartGo WMS - Estoque",  "url": "https://api.smartgo.com.br/webhook/estoque"},
    {"nome": "Mercado Livre - Status", "url": "https://api.mercadolibre.com/webhook/orders"},
    {"nome": "Shopee - Notificacoes",  "url": "https://api.shopee.com.br/webhook/notify"},
]


def verificar_endpoint(endpoint):
    # Simula health check: 90% de sucesso, 10% de falha
    status_code = 200 if random.random() > 0.10 else random.choice([500, 503, 408])
    latencia_ms = random.randint(50, 800)
    return status_code, latencia_ms


def monitorar():
    print(f"\nWebhook Monitor - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("-" * 60)

    falhas = []

    for ep in ENDPOINTS:
        status, latencia = verificar_endpoint(ep)
        status_label = "OK" if status == 200 else "FALHA"
        print(f"[{status_label}] {ep['nome']:<30}  HTTP {status}  {latencia}ms")

        if status != 200:
            falhas.append({"endpoint": ep["nome"], "status": status, "latencia": latencia})

    print()
    if falhas:
        print(f"{len(falhas)} falha(s) detectada(s):")
        for f in falhas:
            print(f"  {f['endpoint']} retornou HTTP {f['status']}")
    else:
        print("Todos os endpoints respondendo normalmente.")
    print()


if __name__ == "__main__":
    monitorar()
