# Marketplace Automation

Scripts Python para automação operacional em e-commerce: consolidação de dados de vendas, monitoramento de webhooks e integração de APIs ERP/WMS.

## Sobre o projeto

Desenvolvido durante minha atuação como Analista de Marketplace para reduzir tarefas manuais repetitivas e melhorar a rastreabilidade de dados. Os scripts foram usados em produção com integração entre ERP (Bling) e WMS (SmartGo).

Alguns resultados durante o uso:

- Redução de cerca de 30% no tempo de análise operacional
- Eliminação de erros de reporte manual
- Monitoramento em tempo real de falhas em webhooks

## Estrutura

```
marketplace-automation/
├── relatorio_vendas.py
├── webhook_monitor.py
├── dashboard_export.py
├── data/
│   └── exemplo_dados.csv
├── requirements.txt
└── README.md
```

## Como usar

```bash
git clone https://github.com/gvstavolst/marketplace-automation
cd marketplace-automation
pip install -r requirements.txt

python relatorio_vendas.py
python webhook_monitor.py
```

## Scripts

| Script | O que faz |
|---|---|
| `relatorio_vendas.py` | Le CSV de vendas, calcula KPIs e exporta sumário |
| `webhook_monitor.py` | Monitora endpoints e detecta falhas de sincronização |
| `dashboard_export.py` | Consolida indicadores e gera relatório final |

## Relação com segurança da informação

Algumas práticas aplicadas nesse projeto têm relação direta com segurança de sistemas:

- Monitoramento de webhooks com detecção de anomalias em logs
- Integração de APIs REST com autenticação e validação de erros
- Controle de integridade e rastreabilidade do fluxo de dados

## Tecnologias

- Python
- Pandas
- API REST (Bling, SmartGo)

## Autor

Gustavo Lemos Souto
[linkedin.com/in/gustavolemossouto](https://linkedin.com/in/gustavolemossouto)
