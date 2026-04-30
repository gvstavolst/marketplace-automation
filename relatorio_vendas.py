import csv
from datetime import datetime
from collections import defaultdict

ARQUIVO = "data/exemplo_dados.csv"

def carregar_dados(arquivo):
    vendas = []
    with open(arquivo, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            vendas.append(row)
    return vendas

def calcular_kpis(vendas):
    total_receita   = 0.0
    total_pedidos   = len(vendas)
    por_plataforma  = defaultdict(float)
    por_produto     = defaultdict(int)

    for v in vendas:
        receita = float(v["valor"])
        total_receita += receita
        por_plataforma[v["plataforma"]] += receita
        por_produto[v["produto"]] += 1

    ticket_medio = total_receita / total_pedidos if total_pedidos else 0

    return {
        "total_pedidos":  total_pedidos,
        "total_receita":  round(total_receita, 2),
        "ticket_medio":   round(ticket_medio, 2),
        "por_plataforma": dict(por_plataforma),
        "top_produto":    max(por_produto, key=por_produto.get)
    }

def exibir_relatorio(kpis):
    print("\n========== RELATORIO DE VENDAS ==========")
    print(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print(f"Total de pedidos : {kpis['total_pedidos']}")
    print(f"Receita total    : R$ {kpis['total_receita']:,.2f}")
    print(f"Ticket medio     : R$ {kpis['ticket_medio']:,.2f}")
    print(f"Produto destaque : {kpis['top_produto']}")
    print("\nReceita por plataforma:")
    for plat, val in kpis['por_plataforma'].items():
        print(f"  {plat:<20} R$ {val:,.2f}")
    print("========================================\n")

if __name__ == "__main__":
    vendas = carregar_dados(ARQUIVO)
    kpis   = calcular_kpis(vendas)
    exibir_relatorio(kpis)
