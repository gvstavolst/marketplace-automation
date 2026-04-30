# ⚙️ Marketplace Automation

> Scripts Python para **automação operacional** em e-commerce: consolidação de dados, monitoramento de webhooks e integração de APIs ERP/WMS.

---

## 📌 Sobre o Projeto

Desenvolvido durante atuação como **Analista de Marketplace** para eliminar processos manuais, reduzir erros operacionais e garantir rastreabilidade de dados em ambiente de e-commerce.

**Impacto gerado:**
- ⏱️ Redução de ~30% no tempo de análise operacional
- ❌ Eliminação de erros de reporte manual
- 🔄 Monitoramento em tempo real de falhas em webhooks de API

---

## 🛠️ Tecnologias

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![API REST](https://img.shields.io/badge/API_REST-FF6C37?style=for-the-badge&logo=postman&logoColor=white)

---

## 📁 Estrutura

```
marketplace-automation/
├── relatorio_vendas.py      # Consolida dados de vendas em relatório
├── webhook_monitor.py       # Monitora falhas em webhooks de API
├── dashboard_export.py      # Exporta KPIs para Google Sheets / CSV
├── data/
│   └── exemplo_dados.csv      # Dados anonimizados para teste
├── requirements.txt
└── README.md
```

---

## 🚀 Como Usar

```bash
# Clonar
git clone https://github.com/gvstavolst/marketplace-automation
cd marketplace-automation

# Instalar dependências
pip install -r requirements.txt

# Gerar relatório de vendas
python relatorio_vendas.py

# Monitorar webhooks
python webhook_monitor.py
```

---

## 📊 Scripts

| Script | Função |
|---|---|
| `relatorio_vendas.py` | Lê CSV de vendas, calcula KPIs e exporta sumário |
| `webhook_monitor.py` | Simula monitoramento de endpoints e detecta falhas |
| `dashboard_export.py` | Consolida indicadores e gera relatório final |

---

## 🔐 Conexão com Segurança da Informação

Este projeto envolve práticas diretamente relacionadas à área de segurança:

- **Monitoramento de webhooks** → análise de logs e detecção de anomalias
- **Integração de APIs REST** → autenticação, validação e tratamento de erros
- **Integridade de dados** → rastreabilidade e controle de fluxo de informações

---

## 👤 Autor

**Gustavo Lemos Souto** — [linkedin.com/in/gustavolemossouto](https://linkedin.com/in/gustavolemossouto)
