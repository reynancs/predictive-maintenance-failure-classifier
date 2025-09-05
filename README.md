# Projeto Final – Manutenção Preditiva em Máquinas Rotativas Industriais  

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>


## 📌 Contextualização  
- O dataset fornecido pela empresa contém um conjunto de dados de informações coletadas a partir de dispositivos IoT sensorizando atributos
básicos de  **máquinas rotativas industriais** (exemplo considerado com escopo: **motor Elétrico de uma Bomba Centrífuga.**)
O objetivo principal do dataset é suportar estudos de manutenção preditiva, permitindo prever se a máquina vai falhar, mas também qual o tipo de falha provável. 

---

## 🎯 Objetivos do Projeto  

- **Negócio**  
  - Redução de paradas não planejadas; 
  - Aumentar a disponibilidade e confiabilidade dos equipamentos.  
  - Apoiar equipes de manutenção com diagnósticos explicáveis.  
  - Otimizar gestão de estoques de ferramentas e peças de reposição.  

- **Técnico**  
  - Construir modelos de Machine Learning para prever **falha geral** e **tipos específicos de falha**.  
  - Implementar técnicas de **Explainable AI (XAI)** para identificar quais variáveis mais impactam cada falha.  
  - Avaliar desempenho com métricas adequadas (F1-score, recall, precisão, etc.).  


## 🏆 Critérios de Sucesso

- **Negócio:** Reduzir paradas não planejadas em pelo menos 20% (simulado).
- **Técnico:** Obter Recall > 0.90 nas predições de falhas específicas.
- **Apresentação:** Storytelling claro, documentação organizada e código reprodutível.

---

## 📊 Metodologia (CRISP-DM)  

1. **Business Understanding** → definição do problema e métricas de sucesso.
2. **Data Understanding** → análise exploratória e estatística dos dados.  
3. **Data Preparation** → tratamento de outliers, normalização, balanceamento.  
4. **Modeling** → modelos de classificação binária e multirrótulo.  
5. **Evaluation** → métricas de desempenho (recall, F1, precisão).  
6. **Deployment** → API e/ou dashboard de manutenção preditiva.  

---

## 📑 Dicionário dos Dados  

### Descrição
- Cada registro representa uma observação de operação de máquina monitorada por sensores IoT.
- Cada amostra no conjunto de dados é composta por 8 atributos que descrevem o **ambiente de operação** (temperatura, umidade), as **condições da máquina** (velocidade rotacional, torque, desgaste da ferramenta) e os **eventos de falha** associados a cinco diferentes classes de defeitos (desgaste, calor, potência, tensão, falhas aleatórias).
- Para a variável `tipo` de máquina será considerado a **classificação por Grau de Proteção (IP)** de motores elétricos. [classificacao_grau_de_protecao](/docs/docs/classificacao_motores_grau_prot_ip.md)
  - `L` : Baixa Proteção (IP23)
  - `M` : Média Proteção (IP44)
  - `H` : Alta Proteção (IP55)
  - `desgaste_da_ferramenta`: Neste cenário, seria considerado como "horas de operação do selo mecânico" desde a última troca ou inspeção.
  - `temperatura_processo`: Considerado como a temperatura na carcaça do motor.

### Dicionário de Dados  

| CAMPO                    | FUNÇÃO (ATRIBUTO \| ALVO)| TIPO DE VARIÁVEL     | DESCRIÇÃO                                      |
|--------------------------|--------------------------|----------------------|------------------------------------------------|
| **id**                   | Atributo                 | Numérica (Inteiro)   | Identificador único das amostras.              |
| **id_produto**           | Atributo                 | Categórica (String)  | Identificador do produto/máquina.              |
| **tipo**                 | Atributo                 | Categórica (L, M, H) | Categoria da máquina (Low, Medium, High load). |
| **temperatura_ar**       | Atributo                 | Numérica (K)         | Temperatura ambiente.                          |
| **temperatura_processo** | Atributo                 | Numérica (K)         | Temperatura interna do processo.               |
| **umidade_relativa**     | Atributo                 | Numérica (%)         | Umidade relativa do ar.                        |
| **velocidade_rotacional**| Atributo                 | Numérica (RPM)       | Velocidade rotacional do eixo da máquina.      |
| **torque**               | Atributo                 | Numérica (Nm)        | Torque aplicado no processo de corte.          |
| **desgaste_da_ferramenta** | Atributo               | Numérica (Min)       | Tempo acumulado de uso da ferramenta.          |
| **falha_maquina**        | Alvo (Binário)           | Numérica (0/1)       | Indica falha geral (1) ou não (0).             |
| **FDF**                  | Alvo (Binário)           | Numérica (0/1)       | Falha por desgaste da ferramenta.              |
| **FDC**                  | Alvo (Binário)           | Numérica (0/1)       | Falha por dissipação de calor.                 |
| **FP**                   | Alvo (Binário)           | Numérica (0/1)       | Falha por potência.                            |
| **FTE**                  | Alvo (Binário)           | Numérica (0/1)       | Falha por tensão excessiva.                    |
| **FA**                   | Alvo (Binário)           | Numérica (0/1)       | Falha aleatória.                               |

---

## 📂 Estrutura do Repositório  
Baseado no framework Cookiecutter

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

## ⚙️ Tecnologias Utilizadas  

- Python 3.12.7  
- Pandas, Numpy, Scikit-learn
- Testes Estátisticos com a biblioteca `Stats`
- Relatório de Qualidade dos dados com Pandas Profile Report [ydata-profiling](\reports\profile-reports\)
- XGBoost, Random Forest, Logistic Regression
- Explicabilidade do Modelo (XAi) com a ferramenta [explainer-dashboard](\reports\classifier-explainer\)
---


## 👨‍💻 Autor

Renan Cardoso
Projeto desenvolvido no âmbito do Bootcamp de Ciência de Dados e IA (CDIA).