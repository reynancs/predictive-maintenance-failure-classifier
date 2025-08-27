# 03 – Data Preparation  

## 🎯 Objetivo  
Preparar os dados para a etapa de modelagem, aplicando as correções e transformações necessárias conforme os problemas identificados no **Profile Report** e no checklist de qualidade.  

---

## 📋 Checklist → Ações Executadas  

| Variável                 | Problema Identificado                          | Ação Recomendada                     | Ação Executada (no projeto) |
|---------------------------|-----------------------------------------------|--------------------------------------|------------------------------|
| `umidade_relativa`        | Pequenos percentuais de valores ausentes      | Imputação (mediana/média)            | Preenchido com mediana       |
| `temperatura_processo`    | Valores extremos (outliers) e caudas longas   | Winsorization ou tratamento          | Aplicada Winsorization 1%    |
| `velocidade_rotacional`   | Outliers em condições de operação anormais    | Normalização após limpeza            | Aplicado RobustScaler        |
| `torque`                  | Correlação forte com RPM e outliers extremos  | Escalonamento + análise de outliers  | Aplicado StandardScaler      |
| `desgaste_da_ferramenta`  | Distribuição assimétrica                      | Criar bins + normalização log        | Criados 4 bins (quartis)     |
| `tipo (L/M/H)`            | Desbalanceamento entre categorias             | Reamostragem estratificada ou pesos  | Mantido, class_weight no modelo |
| Rótulos de falha (FDF…FA) | Desbalanceamento severo entre classes         | Técnicas de balanceamento            | SMOTE aplicado (treino)      |

---

## 🧹 Limpeza dos Dados  
- Tratamento de valores ausentes (`umidade_relativa`).  
- Remoção ou imputação de outliers em `temperatura_processo` e `torque`.  

## 🔧 Transformações  
- Normalização e escalonamento (`velocidade_rotacional`, `torque`).  
- Log-transform ou bins (`desgaste_da_ferramenta`).  

## 🛠️ Feature Engineering  
- Criação de `torque_por_rpm` (razão torque/velocidade).  
- Criação de `delta_temp` (temperatura_processo - temperatura_ar).  
- Variável categórica `desgaste_bins`.  

## ✂️ Divisão de Dados  
- Split em treino (80%) e validação (20%), estratificado por `falha_maquina`.  

## ⚖️ Balanceamento  
- Classes de falha (multirrótulo) são desbalanceadas.  
- Utilizado **SMOTE** apenas no conjunto de treino.  
- Avaliação com métricas robustas (F1-score, Recall).  

---

## ✅ Saídas desta etapa  
- Arquivos processados salvos em `data/interim/` (X_train, y_train, X_valid, y_valid).  
- Conjunto final pronto para modelagem salvo em `data/processed/`.  
- Documentação clara das decisões de preparação para rastreabilidade.  
