import csv
from datetime import datetime


def gerar_dashboard(arquivo_entrada, arquivo_saida):
    metricas = {
        "data_geracao":  datetime.now().strftime('%d/%m/%Y %H:%M'),
        "total_pedidos": 0,
        "receita_total": 0.0,
        "plataformas":   set(),
    }

    with open(arquivo_entrada, newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            metricas["total_pedidos"] += 1
            metricas["receita_total"] += float(row["valor"])
            metricas["plataformas"].add(row["plataforma"])

    metricas["ticket_medio"] = round(
        metricas["receita_total"] / metricas["total_pedidos"], 2
    ) if metricas["total_pedidos"] else 0

    with open(arquivo_saida, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Indicador", "Valor"])
        writer.writerow(["Data",              metricas["data_geracao"]])
        writer.writerow(["Total Pedidos",      metricas["total_pedidos"]])
        writer.writerow(["Receita Total (R$)", f"{metricas['receita_total']:.2f}"])
        writer.writerow(["Ticket Medio (R$)",  f"{metricas['ticket_medio']:.2f}"])
        writer.writerow(["Plataformas",        ", ".join(sorted(metricas["plataformas"]))])

    print(f"Dashboard exportado: {arquivo_saida}")


if __name__ == "__main__":
    gerar_dashboard("data/exemplo_dados.csv", "data/dashboard_output.csv")
