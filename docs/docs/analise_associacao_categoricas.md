
## 🔍 Análise de Associação entre Variáveis Categóricas

### 🎯 Variáveis analisadas:
- `falha_maquina`: variável alvo binária (0: sem falha, 1: com falha)
- `tipo_falha`: tipo da falha identificada (FDC, FTE, FDF, FP, FA)
- `tipo`: categoria da máquina (Baixa, Média, Alta rotação)

---

### 📊 Matriz de Associação Categórica (Cramér's V)

| Associação               | Cramér's V | Interpretação                                       |
|--------------------------|------------|-----------------------------------------------------|
| `falha_maquina` × `tipo_falha` | 0.92       | Associação muito forte (esperado)                   |
| `tipo_falha` × `tipo`          | 0.03       | Associação muito fraca                              |
| `falha_maquina` × `tipo`       | 0.01       | Nenhuma associação relevante                        |

---

### 🧪 Testes Estatísticos de Hipótese (Qui-quadrado)

**1. `falha_maquina` × `tipo`**  
- Valor-p = p > 0.05 → ✅ Não rejeitamos H0  
- **Conclusão:** O tipo de máquina **não influencia** a ocorrência de falha.

**2. `tipo_falha` × `tipo`**  
- Valor-p = p > 0.05 → ✅ Não rejeitamos H0  
- **Conclusão:** O tipo de máquina **não influencia** o tipo de falha.

---

### 🔎 Avaliação da Remoção das Falhas Aleatórias (FA)

**Distribuição da variável `falha_maquina`**:

| Situação     | Classe 0 | Classe 1 | Taxa de falha (%) |
|--------------|----------|----------|--------------------|
| Com FA       | 98.47%   | 1.53%    | ~1.53%             |
| Sem FA       | 98.50%   | 1.50%    | ~1.50%             |

- 📉 Diferença: **redução de apenas 0.03 p.p.** na taxa de falhas
- ✅ Justifica-se a exclusão da classe `FA` por:
  - Baixíssima ocorrência (~0.2%)
  - Falta de padrão físico
  - Ruído potencial no aprendizado supervisionado

---

