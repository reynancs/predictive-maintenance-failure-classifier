# predictive-maintenance-ml-classifier

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>


# 🛠️ Projeto Final – Manutenção Preditiva em Máquinas Rotativas Industriais  

## 📌 Contextualização  
Uma empresa do setor industrial contratou a criação de um sistema inteligente de **manutenção preditiva** para suas máquinas rotativas.  

Essas máquinas são monitoradas por dispositivos **IoT**, que coletam informações do ambiente e da própria operação (como torque, velocidade, desgaste e temperatura). O objetivo é prever **falhas futuras** e identificar **qual tipo de falha ocorrerá**, permitindo planejamento de manutenção, redução de downtime e melhor gestão de peças de reposição.  

> Neste projeto, o escopo foi adaptado para **Centros de Usinagem CNC**, onde os sensores monitoram parâmetros de corte, desgaste da ferramenta e condições ambientais.  

---

## 🎯 Objetivos do Projeto  

- **Negócio**  
  - Reduzir falhas inesperadas em máquinas CNC.  
  - Aumentar a disponibilidade e confiabilidade dos equipamentos.  
  - Apoiar equipes de manutenção com diagnósticos explicáveis.  
  - Otimizar gestão de estoques de ferramentas e peças de reposição.  

- **Técnico**  
  - Construir modelos de Machine Learning para prever **falha geral** e **tipos específicos de falha**.  
  - Implementar técnicas de **Explainable AI (XAI)** para identificar quais variáveis mais impactam cada falha.  
  - Avaliar desempenho com métricas adequadas (F1-score, recall, precisão, etc.).  


## 🏆 Critérios de Sucesso

- **Negócio:** Reduzir paradas não planejadas em pelo menos 20% (simulado).
- **Técnico:** Obter F1-score > 0.90 nas predições de falhas específicas.
- **Apresentação:** Storytelling claro, documentação organizada e código reprodutível.

---

## 🔎 Tipos de Falhas Monitoradas  

O dataset permite identificar cinco classes de falhas industriais:  

| Código | Descrição                   | Exemplos de Aplicação | Impacto |
|--------|-----------------------------|------------------------|---------|
| **FDF** | Desgaste da Ferramenta      | CNC, automotivo, aeroespacial | Quebra da ferramenta, peças fora de tolerância |
| **FDC** | Dissipação de Calor         | Motores, compressores, usinagem | Sobreaquecimento, queima, redução da vida útil |
| **FP**  | Falha de Potência           | Bombas, turbinas, motores | Perda de eficiência, sobrecorrente, parada súbita |
| **FTE** | Tensão Excessiva            | Motores, inversores, bombas elétricas | Queima de enrolamentos, falhas elétricas graves |
| **FA**  | Falha Aleatória             | Rolamentos, compressores, CNC | Falhas imprevisíveis, alta criticidade |

---

## 📑 Dicionário dos Dados  

### Descrição  
O dataset contém registros coletados via IoT em **máquinas rotativas industriais**, simulando **Centros de Usinagem CNC**.  

Cada linha representa uma observação com atributos de ambiente, condições de operação e ocorrência de falhas.  

> O objetivo é prever não apenas **se a máquina vai falhar**, mas também **qual o tipo de falha provável**, apoiando estratégias de manutenção preditiva.  

### Estrutura dos Dados  

| CAMPO                   | FUNÇÃO (ATRIBUTO \| ALVO) | TIPO DE VARIÁVEL | DESCRIÇÃO |
|--------------------------|---------------------------|------------------|-----------|
| **id**                  | Atributo                 | Numérica (Inteiro) | Identificador único das amostras. |
| **id_produto**           | Atributo                 | Categórica (String) | Identificador do produto/máquina. |
| **tipo**                 | Atributo                 | Categórica (L, M, H) | Categoria da máquina (Low, Medium, High load). |
| **temperatura_ar**       | Atributo                 | Numérica (K) | Temperatura ambiente. |
| **temperatura_processo** | Atributo                 | Numérica (K) | Temperatura interna do processo. |
| **umidade_relativa**     | Atributo                 | Numérica (%) | Umidade relativa do ar. |
| **velocidade_rotacional**| Atributo                 | Numérica (RPM) | Velocidade rotacional do eixo da máquina. |
| **torque**               | Atributo                 | Numérica (Nm) | Torque aplicado no processo de corte. |
| **desgaste_da_ferramenta** | Atributo               | Numérica (Min) | Tempo acumulado de uso da ferramenta. |
| **falha_maquina**        | Alvo (Binário)           | Numérica (0/1) | Indica falha geral (1) ou não (0). |
| **FDF**                  | Alvo (Binário)           | Numérica (0/1) | Falha por desgaste da ferramenta. |
| **FDC**                  | Alvo (Binário)           | Numérica (0/1) | Falha por dissipação de calor. |
| **FP**                   | Alvo (Binário)           | Numérica (0/1) | Falha por potência. |
| **FTE**                  | Alvo (Binário)           | Numérica (0/1) | Falha por tensão excessiva. |
| **FA**                   | Alvo (Binário)           | Numérica (0/1) | Falha aleatória. |

---

## 📂 Estrutura do Repositório  

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         src and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── src   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes src a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```


---

## 📊 Metodologia (CRISP-DM)  

1. **Business Understanding** → definição do problema e métricas de sucesso.  
2. **Data Understanding** → análise exploratória e estatística dos dados.  
3. **Data Preparation** → tratamento de outliers, normalização, balanceamento.  
4. **Modeling** → modelos de classificação binária e multirrótulo.  
5. **Evaluation** → métricas de desempenho (F1, recall, precisão).  
6. **Deployment** → API e/ou dashboard de manutenção preditiva.  

---

## ⚙️ Tecnologias Utilizadas  

- Python 3.10+  
- Pandas, Numpy, Scikit-learn  
- XGBoost, Random Forest, Logistic Regression  
- SHAP e LIME para explicabilidade  
- Streamlit (dashboard)  
- FastAPI (API de predição)  
- Docker (implantação)  

---

## 📈 Avaliação  

O desempenho final do modelo será avaliado via **API Bootcamp CDIA**, que retorna métricas de classificação para cada tipo de falha.  

Exemplo de endpoint:  

```python
import requests

headers = {"X-API-Key": "<seu_token>"}
files = {"file": open("predicoes.csv", "rb")}
params = {"threshold": 0.5}

response = requests.post(
    "http://34.193.187.218:5000/evaluate/multilabel_metrics",
    headers=headers,
    files=files,
    params=params,
)

print(response.json())
```


## 👨‍💻 Autor
Renan Cardoso
Projeto desenvolvido no âmbito do Bootcamp de Ciência de Dados e IA (CDIA).