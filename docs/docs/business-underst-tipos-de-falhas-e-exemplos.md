# Tipos de Falhas e Exemplos Industriais

> Com base no exemplo dos atributos do dataset fornecido, são consideradas cinco classes principais de falhas em máquinas rotativas industriais.  
> Abaixo estão exemplos de como cada tipo de falha ocorre em cenários reais, relacionando os atributos coletados (torque, velocidade, temperaturas, desgaste e condições ambientais) às aplicações práticas.

Código | Descrição do tipo de falha industrial | Atributos Relacionados           | Exemplos de Aplicação Real                      | Impacto Industrial
------ | ------------------------------------- | -------------------------------- | ------------------------------------------------ | -------------------------------------------------
**FDF** | Desgaste da Ferramenta               | Tool Wear, Torque, RPM           | Usinagem CNC, indústria automotiva, aeronáutica | Peças fora de tolerância, quebra de ferramentas
**FDC** | Dissipação de Calor                  | Temperatura do processo e do ar  | Motores, compressores, usinagem CNC             | Sobreaquecimento, redução da vida útil, queima
**FP**  | Potência                             | Torque, RPM, Potência            | Bombas, turbinas, motores industriais           | Perda de eficiência, sobrecorrente, parada súbita
**FTE** | Tensão Excessiva                     | Torque, RPM, condições elétricas | Motores, inversores, bombas elétricas submersas | Queima de enrolamentos, falhas elétricas graves
**FA**  | Aleatória                            | Qualquer variável                | Rolamentos, compressores, sistemas CNC          | Falhas imprevisíveis, alta criticidade

```mermaid

flowchart TD
  A[Maquinas Rotativas - Tipos de Falha]

  A --> FDF[FDF - Desgaste da Ferramenta]
  A --> FDC[FDC - Dissipacao de Calor]
  A --> FP[FP - Falha de Potencia]
  A --> FTE[FTE - Tensao Excessiva]
  A --> FA[FA - Aleatoria]

  FDF --> FDF_att[Atributos: Tool Wear, Torque, RPM]
  FDC --> FDC_att[Atributos: Temp de Processo e de Ar]
  FP  --> FP_att[Atributos: Torque, RPM, Potencia derivada]
  FTE --> FTE_att[Atributos: RPM, Condicoes eletricas]
  FA  --> FA_att[Atributos: Qualquer variavel]

  FDF_att --> FDF_ex[Exemplos: CNC - tornos e fresas; setor automotivo; setor aeroespacial]
  FDC_att --> FDC_ex[Exemplos: Motores; Compressores; CNC]
  FP_att  --> FP_ex[Exemplos: Bombas; Turbinas; Motores industriais]
  FTE_att --> FTE_ex[Exemplos: Motores; Inversores; Bombas eletricas submersas]
  FA_att  --> FA_ex[Exemplos: Rolamentos; Compressores; Sistemas CNC]

  FDF_ex --> FDF_imp[Impactos: Peca fora de tolerancia; Quebra de ferramenta; Parada]
  FDC_ex --> FDC_imp[Impactos: Sobreaquecimento; Queima; Reducao da vida util]
  FP_ex  --> FP_imp[Impactos: Perda de eficiencia; Sobrecorrente; Parada subita]
  FTE_ex --> FTE_imp[Impactos: Queima de enrolamentos; Falhas eletricas graves]
  FA_ex  --> FA_imp[Impactos: Falhas imprevisiveis; Alta criticidade]
```