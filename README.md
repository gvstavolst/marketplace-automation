# Marketplace Automation

Scripts Python para automação operacional em e-commerce: consolidação de dados de vendas, monitoramento de webhooks e integração de APIs ERP/WMS.

## Sobre o projeto

Desenvolvido durante atuação como Analista de Marketplace para eliminar processos manuais, reduzir erros operacionais e garantir rastreabilidade de dados em ambiente de e-commerce. Os scripts foram utilizados em produção com integração entre ERP (Bling) e WMS (SmartGo).

Resultados obtidos:
- Redução de aproximadamente 30% no tempo de análise operacional
- Eliminação de erros de reporte manual
- Monitoramento em tempo real de falhas em webhooks de API

## Estrutura

```
marketplace-automation/
├── relatorio_vendas.py        # Consolida dados de vendas em relatorio
├── webhook_monitor.py         # Monitora falhas em webhooks de API
├── dashboard_export.py        # Exporta KPIs para CSV
├── data/
│   └── exemplo_dados.csv          # Dados anonimizados para teste
├── requirements.txt
└── README.md
```

## Como usar

```bash
git clone https://github.com/gvstavolst/marketplace-automation
cd marketplace-automation
pip install -r requirements.txt

# Gerar relatorio de vendas
python relatorio_vendas.py

# Monitorar webhooks
python webhook_monitor.py
```

## Scripts

| Script | Funcao |
|---|---|
| `relatorio_vendas.py` | Le CSV de vendas, calcula KPIs e exporta sumario |
| `webhook_monitor.py` | Monitora endpoints e detecta falhas de sincronizacao |
| `dashboard_export.py` | Consolida indicadores e gera relatorio final |

## Conexao com seguranca da informacao

O projeto envolve praticas relacionadas a seguranca de sistemas:

- Monitoramento de webhooks com deteccao de anomalias em logs
- Integracao de APIs REST com autenticacao, validacao e tratamento de erros
- Controle de integridade e rastreabilidade do fluxo de dados

## Tecnologias

- Python
- Pandas
- API REST (Bling, SmartGo)

## Autor

Gustavo Lemos Souto
[linkedin.com/in/gustavolemossouto](https://linkedin.com/in/gustavolemossouto)
