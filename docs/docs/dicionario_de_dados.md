# 📘 Dicionário dos Dados  

## Descrição  

>O dataset fornecido pela empresa contém um conjunto de dados de informações coletadas a partir de dispositivos IoT sensorizando atributos
básicos de  **máquinas rotativas industriais** (como equipamentos de usinagem, bombas e compressores). Para este escopo será considerando Centros de Usinagem.
Cada registro representa uma observação de operação de máquina monitorada por sensores IoT. 
Cada amostra no conjunto de dados é composta por 8 atributos que descrevem o **ambiente de operação** (temperatura, umidade), as **condições da máquina** (velocidade rotacional, torque, desgaste da ferramenta) e os **eventos de falha** associados a cinco diferentes classes de defeitos (desgaste, calor, potência, tensão, falhas aleatórias).

O objetivo principal do dataset é suportar estudos de manutenção preditiva, permitindo prever não apenas se a máquina vai falhar, mas também qual o tipo de falha provável.  

---

## 📑 Dicionário de Dados  

| CAMPO                   | FUNÇÃO (ATRIBUTO \| ALVO) | TIPO DE VARIÁVEL | DESCRIÇÃO |
|--------------------------|---------------------------|------------------|-----------|
| **id**                  | Atributo                 | Numérica (Inteiro) | Identificador único das amostras do banco de dados. Não possui significado físico, usado apenas para indexação. |
| **id_produto**           | Atributo                 | Categórica (String) | Identificador do produto/máquina, combinação da variável `tipo` com um número sequencial. Representa diferentes unidades operacionais. |
| **tipo**                 | Atributo                 | Categórica (L, M, H) | Tipo de produto/máquina, definido por categoria de carga: **L** (Low), **M** (Medium), **H** (High). No dataset AI4I, isso simula variação entre diferentes condições de produção. |
| **temperatura_ar**       | Atributo                 | Numérica (Contínua) | Temperatura ambiente medida em Kelvin. Importante para avaliar condições externas que influenciam o desempenho térmico da máquina. |
| **temperatura_processo** | Atributo                 | Numérica (Contínua) | Temperatura do processo (interno à máquina). No dataset AI4I, valores mais altos estão associados a falhas de dissipação de calor (FDC). |
| **umidade_relativa**     | Atributo                 | Numérica (Contínua) | Umidade relativa do ar (%). No AI4I, usada como fator ambiental que pode impactar falhas de isolamento elétrico e desgaste acelerado. |
| **velocidade_rotacional**| Atributo                 | Numérica (Contínua) | Velocidade rotacional da máquina em rotações por minuto (RPM). Valores anormais podem indicar problemas de balanceamento ou sobrecarga. |
| **torque**               | Atributo                 | Numérica (Contínua) | Torque da máquina em Newton-metro. No AI4I, varia entre ~3.0 a 76.0 Nm. Torques elevados podem levar a falhas de potência (FP). |
| **desgaste_da_ferramenta** | Atributo               | Numérica (Contínua) | Tempo acumulado de uso da ferramenta (minutos). Aumenta linearmente com a operação e está diretamente associado a falhas por desgaste (FDF). |
| **falha_maquina**        | Alvo (Binário)           | Numérica (0/1) | Variável binária indicando se houve falha geral na máquina (1) ou não (0). Serve como rótulo consolidado de falha. |
| **FDF** (Falha Desgaste Ferramenta) | Alvo (Binário) | Numérica (0/1) | Indica falha por desgaste excessivo da ferramenta de corte. Associada ao tempo de uso (`desgaste_da_ferramenta`) e às condições de torque/RPM. |
| **FDC** (Falha Dissipação Calor) | Alvo (Binário)   | Numérica (0/1) | Indica falha térmica por dissipação inadequada de calor. Relacionada principalmente a `temperatura_processo` elevada em relação à `temperatura_ar`. |
| **FP** (Falha Potência) | Alvo (Binário)           | Numérica (0/1) | Indica falha por potência insuficiente ou sobrecarga da máquina. Frequentemente correlacionada com variações de torque e rotação. |
| **FTE** (Falha Tensão Excessiva) | Alvo (Binário)   | Numérica (0/1) | Indica falha elétrica devido à sobretensão ou condições anômalas de operação elétrica. |
| **FA** (Falha Aleatória) | Alvo (Binário)           | Numérica (0/1) | Indica falha aleatória sem padrão determinístico. No dataset, essas falhas são geradas para simular eventos não explicados por variáveis medidas. |

---
