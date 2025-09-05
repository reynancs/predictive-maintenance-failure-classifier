# Análise Exploratória de Dados (EDA)

## 1. Análise de Variáveis Categóricas

### 1.1 Variável Alvo (falha_maquina)
- **Desbalanceamento Significativo**: 
  - Classe 0 (Sem Falha): 98.45%
  - Classe 1 (Com Falha): 1.55%
  - Desafio para modelagem: poucos registros de falhas (<2%)

### 1.2 Tipos de Falha
- **Distribuição das Falhas** (Análise Pareto):
  1. Dissipação de Calor (FDC): 47.8%
  2. Tensão Excessiva (FTE): 31.6%
  3. Desgaste de Ferramenta (FDF): 13.5%
  4. Falha de Potência (FP): 6.9%
  - Falha Aleatória (FA): 0.2% (removida por baixa representatividade)

### 1.3 Tipo de Produto/Máquina
- **Distribuição por Categoria**:
  - Baixa: 66.88% (majoritária)
  - Média: 24.59%
  - Alta: 7.22% (minoritária)
- Acumulado das classes "Baixa" e "Média": 91.47%
- Casos de falha no tipo "Alta": <1% do total

### 1.4 Associações Categóricas
- **Associações Significativas**:
  - Forte associação entre tipos de máquina: `tipo_Baixa` vs `tipo_Média` (V=0.84)
  - Correlação moderada entre `falha_maquina` e tipos específicos de falha:
    - FDC: 0.68
    - FTE: 0.57
    - FDF: 0.36
    - FP: 0.25

### 1.5 Testes Estatísticos - Categóricos
1. **O tipo de máquina "Baixa" influencia a ocorrência de falhas de "Tensão Excessiva(FTE)" - Associação Tipo Baixa vs FTE**
   - Resultado: Existe associação estatisticamente significativa
   - p-valor < 0.05

2. **O tipo de máquina Baixa influencia a ocorrência de falhas de Tensão Excessiva(FTE) - Impacto da Remoção de FA**:
   - Variação na taxa de falha: 0.0029%
   - Conclusão: Remoção não impacta significativamente a distribuição

## 2. Análise de Variáveis Numéricas

### 2.1 Distribuições e Outliers
- Variáveis com distribuição aproximadamente normal:
  - temperatura_ar
  - temperatura_processo
  - velocidade_rotacional
  - torque
- Presença de outliers mantidos por representarem variabilidade natural do processo

### 2.2 Correlações Principais
1. **temperatura_ar vs temperatura_processo** (ρ ≈ 0.77):
   - Correlação forte positiva
   - Temperatura ambiente influencia significativamente a temperatura do processo
   - Pode impactar na dissipação de calor e falhas térmicas (FDC)

2. **velocidade_rotacional vs torque** (ρ ≈ -0.74):
   - Correlação forte negativa
   - Comportamento físico esperado
   - Útil para detectar anomalias em carga mecânica

3. **temperatura_ar vs desgaste_da_ferramenta** (ρ ≈ 0.03):
   - Correlação muito fraca positiva
   - Possível relação entre temperatura e desgaste

### 2.3 Testes Estatísticos - Numéricos
1. **Torque está associado à ocorrência de falha? (Torque vs Falha):**:
   - p-valor < 0: Rejeita a Hipótese Nula
   - Conclusão: Distribuição significativamente diferente entre grupos

2. **A velocidade de rotação tem distribuição diferente entre máquinas com e sem falha? (Velocidade Rotacional vs Falha)**:
   - p-valor < 0: Rejeita Hipótese Nula
   - Conclusão: Comportamento significativamente diferente em falhas

3. **Máquinas com falha operam com maior temperatura de processo? (Temperatura de Processo vs Falha)**:
   - p-valor < 0: Rejeita a Hipótese Nula
   - Conclusão: Máquinas com falha operam com temperaturas significativamente diferentes

## 3. Feature Engineering

### 3.1 Novas Features Criadas
1. **gradiente_termico**: 
   - Diferença entre temperatura de processo e ambiente
   
2. **potencia_maquina**: 
   - Potência mecânica estimada (W)
   - Fórmula: τ * ω (ω em rad/s)

3. **coef_transferencia_calor**:
   - Eficiência térmica (W/K)
   - Relevante para FDC

4. **eficiencia_termica**:
   - Percentual de eficiência térmica
   - Fórmula: 1 - (Gradiente Térmico / Temperatura Processo)

5. **carga_mecanica_especifica**:
   - Indicativo de FTE
   - Fórmula: Torque / Velocidade Rotacional

6. **indice_severidade**:
   - Indicador de situações críticas
   - Combina desgaste, potência e gradiente térmico

### 3.2 Correlações das Novas Features
- **Recomendações de Remoção**:
  1. Remover `gradiente_termico` (manter `eficiencia_termica`)
  2. Remover `desgaste_da_ferramenta` (manter `indice_severidade`)
  3. Manter ambas `potencia_maquina` e `carga_mecanica_especifica` por representarem aspectos diferentes:
     - `potencia_maquina`: energia total (FP)
     - `carga_mecanica_especifica`: esforço relativo (FTE)
---

## Conclusões para Modelagem

1. **Desafios Identificados**:
   - Desbalanceamento severo da variável alvo
   - Multicolinearidade entre variáveis de temperatura e velocidade/torque

2. **Features Relevantes**:
   - Variáveis originais com forte poder preditivo

3. **Estratégias Sugeridas**:
   - Técnicas de balanceamento para classe minoritária
   - Avaliação de VIF para confirmar multicolinearidade
