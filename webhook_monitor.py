import random
from datetime import datetime

# Simula endpoints de webhook ERP/WMS
ENDPOINTS = [
    {"nome": "Bling ERP - Pedidos",    "url": "https://api.bling.com.br/webhook/pedidos"},
    {"nome": "SmartGo WMS - Estoque",  "url": "https://api.smartgo.com.br/webhook/estoque"},
    {"nome": "Mercado Livre - Status", "url": "https://api.mercadolibre.com/webhook/orders"},
    {"nome": "Shopee - Notificações",  "url": "https://api.shopee.com.br/webhook/notify"},
]

def verificar_endpoint(endpoint):
    """Simula verificação de health check do webhook."""
    # Simula 90% de sucesso, 10% de falha
    status_code = 200 if random.random() > 0.10 else random.choice([500, 503, 408])
    latencia_ms = random.randint(50, 800)
    return status_code, latencia_ms

def monitorar():
    print("\n====== WEBHOOK MONITOR ======")
    print(f"Verificacao: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")

    falhas = []

    for ep in ENDPOINTS:
        status, latencia = verificar_endpoint(ep)
        icone = "✅" if status == 200 else "❌"
        print(f"{icone} {ep['nome']:<30} | HTTP {status} | {latencia}ms")

        if status != 200:
            falhas.append({"endpoint": ep["nome"], "status": status, "latencia": latencia})

    print("\n--- Resumo ---")
    if falhas:
        print(f"⚠️  {len(falhas)} falha(s) detectada(s):")
        for f in falhas:
            print(f"   >> {f['endpoint']} retornou HTTP {f['status']}")
    else:
        print("✅ Todos os endpoints respondendo normalmente.")

    print("==============================\n")

if __name__ == "__main__":
    monitorar()
