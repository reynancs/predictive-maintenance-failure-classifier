# 06 – Deployment  

## 🎯 Objetivo  
Disponibilizar o modelo preditivo em ambiente de produção (ou simulado), permitindo:  
- Receber dados de sensores IoT em tempo real ou em batch.  
- Prever falhas (falha geral e tipos específicos).  
- Apoiar a equipe de manutenção com alertas e dashboards explicativos.  

---

## 🌐 Opções de Deploy  

### 1. API de Predição  
- Framework sugerido: **FastAPI** ou **Flask**.  
- Expor endpoint `/predict` que recebe JSON com atributos da máquina:  
  ```json
  {
    "temperatura_ar": 298.0,
    "temperatura_processo": 310.5,
    "umidade_relativa": 45.0,
    "velocidade_rotacional": 1500,
    "torque": 50.0,
    "desgaste_da_ferramenta": 120,
    "tipo": "M"
  }
