# 05 – Evaluation  

## 🎯 Objetivo  
Avaliar o(s) modelo(s) construído(s) na fase de [04_modeling.md](./04_modeling.md), verificando se os resultados atingem os **critérios de sucesso** definidos no Business Understanding:  
- **Negócio**: reduzir paradas não planejadas (downtime) em pelo menos 20% (simulação).  
- **Técnico**: alcançar F1-score ≥ 0.90 para as predições de falhas.  

---

## 📊 Comparação de Modelos  

| Modelo            | Target            | F1-score | Recall | Precision | ROC-AUC | Observações |
|-------------------|------------------|----------|--------|-----------|---------|-------------|
| Logistic Regression | falha_maquina   | 0.xx     | 0.xx   | 0.xx      | 0.xx    | baseline interpretável |
| Random Forest       | falha_maquina   | 0.xx     | 0.xx   | 0.xx      | 0.xx    | bom recall, risco de overfitting |
| XGBoost             | falha_maquina   | 0.xx     | 0.xx   | 0.xx      | 0.xx    | melhor equilíbrio entre recall e precisão |
| Random Forest       | Multirrótulo    | 0.xx     | 0.xx   | 0.xx      | –       | dificuldade em prever FTE |
| XGBoost             | Multirrótulo    | 0.xx     | 0.xx   | 0.xx      | –       | melhor desempenho global |

*(valores serão preenchidos a partir dos resultados do `notebooks/evaluation.ipynb`)*  

---

## 📉 Análise de Erros  

- **Falhas mais difíceis de prever**:  
  - FTE (Tensão Excessiva) — casos raros, desbalanceamento impacta recall.  
  - FA (Aleatória) — natureza imprevisível, difícil obter padrão claro.  

- **Erros comuns**:  
  - Confusão entre FDC (calor) e FP (potência), pois ambos se manifestam em torque/temperatura.  
  - Alta taxa de falsos negativos em cenários com torque muito baixo.  

---

## 📈 Visualizações  

- **Matriz de Confusão** para cada classe (falha/não falha e falhas específicas).  
- **Curvas ROC** para `falha_maquina`.  
- **Curvas Precision-Recall** para cada falha multirrótulo.  

*(inserir gráficos gerados no `notebooks/evaluation.ipynb`)*  

---

## ✅ Critérios de Sucesso  

- **Negócio**: O modelo atende ao critério de reduzir falhas inesperadas (simulação)?  
- **Técnico**: Algum modelo atingiu F1 ≥ 0.90?  

> Exemplo:  
> - Random Forest multirrótulo alcançou F1 = 0.92 → critério atendido.  
> - Recall elevado garante menos falhas perdidas (menos falsos negativos).  

---

## 📝 Discussão  

- **Pontos fortes**:  
  - Modelo robusto, boa explicabilidade com SHAP.  
  - Variáveis mais importantes: `desgaste_da_ferramenta`, `torque`, `temperatura_processo`.  

- **Limitações**:  
  - Dados sintéticos → podem não refletir completamente a realidade industrial.  
  - Classe FA (Aleatória) segue difícil de prever (baixa precisão/recall).  

- **Próximos passos**:  
  - Testar modelos em dados reais de sensores IoT.  
  - Implementar técnicas de detecção de anomalias para eventos raros (autoencoders, isolation forest).  
  - Re-treinar periodicamente para refletir novas condições operacionais.  

---

## 📂 Saídas  

- Relatório de avaliação com métricas e gráficos salvos em `reports/evaluation/`.  
- Arquivo de submissão final (`bootcamp_submission.csv`) em `data/processed/`.  
- Documentação atualizada neste arquivo (`05_evaluation.md`).  
