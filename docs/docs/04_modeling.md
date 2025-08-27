# 04 – Modeling  

## 🎯 Objetivo  
Construir, treinar e comparar modelos de Machine Learning capazes de prever:  
1. **Falha geral da máquina** (`falha_maquina`, classificação binária).  
2. **Tipos específicos de falhas** (`FDF`, `FDC`, `FP`, `FTE`, `FA`, classificação multirrótulo).  

O objetivo é selecionar o modelo que atenda melhor aos critérios de negócio e técnicos definidos no **Business Understanding**.  

---

## 📂 Entrada  
- Dados preparados conforme descrito em [`03_data_preparation.md`](./03_data_preparation.md).  
- Conjuntos de treino e validação salvos em `data/interim/` e `data/processed/`.  

---

## ⚙️ Modelos Testados  

### 🔹 Baseline  
- **Regressão Logística (One-vs-Rest)**  
  - Justificativa: modelo simples e interpretável, útil como benchmark inicial.  

### 🔹 Árvores de Decisão / Ensembles  
- **Random Forest Classifier**  
  - Justificativa: robusto, lida bem com não linearidade e variáveis correlacionadas.  
- **XGBoost / Gradient Boosting**  
  - Justificativa: alta performance em dados tabulares e competições de ML.  

### 🔹 Outros modelos candidatos (opcional)  
- SVM, KNN, Redes Neurais — se houver tempo para exploração.  

---

## 📏 Métricas de Avaliação  

- **Acurácia** (para baseline, não suficiente em dados desbalanceados).  
- **Precisão, Recall, F1-score** (métricas principais para avaliar falhas).  
- **ROC-AUC** (avalia separabilidade das classes).  
- **Hamming Loss / Subset Accuracy** (para multirrótulo).  

---

## 🧾 Estratégia  

- **Cross-validation** k-fold estratificada para `falha_maquina`.  
- Divisão treino/validação estratificada para multirrótulo.  
- Balanceamento aplicado **apenas no treino** (ex.: SMOTE).  
- Comparação justa entre modelos com os mesmos splits.  

---

## 🧪 Resultados Preliminares  

| Modelo            | Target            | F1-score | Recall | Precision | ROC-AUC |
|-------------------|------------------|----------|--------|-----------|---------|
| Logistic Regression | falha_maquina   | 0.xx     | 0.xx   | 0.xx      | 0.xx    |
| Random Forest       | falha_maquina   | 0.xx     | 0.xx   | 0.xx      | 0.xx    |
| XGBoost             | falha_maquina   | 0.xx     | 0.xx   | 0.xx      | 0.xx    |
| Random Forest       | Multirrótulo    | 0.xx     | 0.xx   | 0.xx      | –       |
| XGBoost             | Multirrótulo    | 0.xx     | 0.xx   | 0.xx      | –       |

*(valores serão preenchidos após execução dos notebooks)*  

---

## 🔍 Explicabilidade (XAI)  

- **Feature Importance (árvores)**: torque, temperatura_processo e desgaste_da_ferramenta aparecem como variáveis mais relevantes.  
- **SHAP Values**: permitem entender impacto de variáveis em predições individuais (ex.: desgaste alto → probabilidade maior de FDF).  
- **LIME (opcional)**: explicações locais para casos de falha/não falha.  

---

## ✅ Seleção do Modelo Final  

Critérios para escolha:  
- Melhor equilíbrio entre **Recall e F1-score** (evitar falsos negativos em falhas).  
- Estabilidade e interpretabilidade para stakeholders de manutenção.  
- Performance consistente em validação cruzada.  

> Modelo selecionado: **[preencher após análise]**  

---

## 📂 Saídas  

- Pipeline do modelo salvo em `data/processed/model_final.joblib`.  
- Notebook `notebooks/modeling.ipynb` documenta os testes e comparações.  
- Resultados consolidados prontos para fase de [`05_evaluation.md`](./05_evaluation.md).  
