# app.py
# -----------------------------------------------------------
# Dashboard EDA (página única) - Manutenção Preditiva em CNC
# - Filtros: tipo, tipo_falha, falha_maquina
# - Objetivo: entender impacto da falha (0/1) e quais tipos
#   de falha (categoria) mais se relacionam com variáveis
#   numéricas (correlação ponto-biserial e eta-squared).
# Nível: básico (código comentado e direto ao ponto)
# -----------------------------------------------------------

import os
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="EDA - Manutenção Preditiva (CNC)", page_icon="🛠️", layout="wide")

# =========================
# Utilitários de carregamento e normalização
# =========================
@st.cache_data(show_spinner=False)
def load_data():
    """Carrega data_cleaned.csv ou bootcamp_train.csv (o que existir)."""
    candidates = [
        "../data/processed/data_cleaned.csv", "../data/raw/bootcamp_train.csv",
        "/data/processed/data_cleaned.csv", "/data/raw/bootcamp_train.csv"
    ]
    for c in candidates:
        if os.path.exists(c):
            df = pd.read_csv(c)
            return df, os.path.basename(c)
    return None, None

def rename_common_columns(df):
    """Normaliza nomes comuns das colunas para facilitar o uso no app."""
    aliases = {
        "temperatura_ar": ["temperatura_ar", "temperatura_ar", "air_temperature", "temp_ar"],
        "temperatura_processo": ["temperatura_processo", "temperatura_processo", "process_temperature", "temp_proc"],
        "umidade_relativa": ["umidade_relativa", "umidade_relativa", "relative_humidity"],
        "velocidade_rotacional": ["velocidade_rotacional", "velocidade_rotacional", "rotational_speed"],
        "torque": ["torque", "torque"],
        "desgaste_da_ferramenta": ["desgaste_da_ferramenta", "desgaste_da_ferramenta", "tool_wear"],
        "falha_maquina": ["falha_maquina", "machine_failure", "falha"],
        "tipo_falha": ["tipo_falha", "failure_type"],
        "tipo": ["tipo", "type"]
    }
    rename_map = {}
    for std, cand in aliases.items():
        for c in cand:
            if c in df.columns:
                rename_map[c] = std
                break
    return df.rename(columns=rename_map)

def coerce_numeric(df, cols):
    """Garante que as colunas listadas sejam numéricas, quando existirem."""
    for c in cols:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")
    return df

# =========================
# Métricas de relação
# =========================
def point_biserial_corr(y_binary, x_numeric):
    """
    Correlação ponto-biserial (equivalente à Pearson com y∈{0,1}).
    Implementação simples para evitar dependências extras.
    Retorna np.nan quando não for possível calcular.
    """
    s = pd.DataFrame({"y": y_binary, "x": x_numeric}).dropna()
    if s["y"].nunique() != 2 or s["x"].nunique() <= 1:
        return np.nan
    y = s["y"].astype(float).values
    x = s["x"].astype(float).values
    # Pearson entre y (0/1) e x
    if np.std(x) == 0 or np.std(y) == 0:
        return np.nan
    return np.corrcoef(y, x)[0, 1]

def correlation_ratio_eta_squared(categories, values):
    """
    Razão de correlação (η² / eta-squared) entre variável categórica e numérica.
    Mede quanto da variância de 'values' é explicada por 'categories'.
    Retorna 0..1 (quanto maior, mais associado).
    """
    s = pd.DataFrame({"cat": categories, "val": values}).dropna()
    if s["cat"].nunique() <= 1 or s["val"].nunique() <= 1:
        return np.nan
    # Média global
    grand_mean = s["val"].mean()
    # Soma dos quadrados entre grupos (SS_between)
    ss_between = 0.0
    ss_total = ((s["val"] - grand_mean) ** 2).sum()
    for g, gdf in s.groupby("cat"):
        n_g = len(gdf)
        mean_g = gdf["val"].mean()
        ss_between += n_g * (mean_g - grand_mean) ** 2
    if ss_total == 0:
        return np.nan
    eta2 = ss_between / ss_total
    return float(eta2)

# =========================
# Carregamento de dados
# =========================
df, src = load_data()
if df is None:
    st.error("Não encontrei `data_cleaned.csv` ou `bootcamp_train.csv` na pasta. Adicione o arquivo e recarregue o app.")
    st.stop()

df = rename_common_columns(df)
df = coerce_numeric(df, [
    "temperatura_ar","temperatura_processo","umidade_relativa",
    "velocidade_rotacional","torque","desgaste_da_ferramenta","falha_maquina"
])

# Identifica colunas numéricas e categóricas
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
categorical_cols = [c for c in df.columns if c not in numeric_cols]

# =========================
# Sidebar (Filtros)
# =========================
st.sidebar.title("⚙️ Filtros")
st.sidebar.caption(f"Fonte de dados: **{src}**")

# Filtro: tipo
if "tipo" in df.columns:
    tipos = sorted(df["tipo"].dropna().astype(str).unique())
    sel_tipos = st.sidebar.multiselect("Filtrar por tipo (máquina):", tipos, default=tipos)
else:
    sel_tipos = None

# Filtro: tipo_falha
if "tipo_falha" in df.columns:
    tipos_falha = sorted(df["tipo_falha"].dropna().astype(str).unique())
    sel_tipos_falha = st.sidebar.multiselect("Filtrar por tipo_falha:", tipos_falha, default=tipos_falha)
else:
    sel_tipos_falha = None

# Filtro: falha_maquina
opt_falha = "Todos"
if "falha_maquina" in df.columns:
    opt_falha = st.sidebar.selectbox("Filtrar por falha_maquina:", ["Todos", "Falha = 1", "Falha = 0"])

# Aplica filtros
dff = df.copy()
if sel_tipos is not None:
    dff = dff[dff["tipo"].astype(str).isin(sel_tipos)]
if sel_tipos_falha is not None:
    dff = dff[dff["tipo_falha"].astype(str).isin(sel_tipos_falha)]
if "falha_maquina" in dff.columns:
    if opt_falha == "Falha = 1":
        dff = dff[dff["falha_maquina"] == 1]
    elif opt_falha == "Falha = 0":
        dff = dff[dff["falha_maquina"] == 0]

# =========================
# Cabeçalho
# =========================
st.title("🛠️ EDA - Manutenção Preditiva (CNC)")
st.caption("Página única focada em **impacto da falha (0/1)** e **associação de `tipo_falha` com variáveis numéricas**.")

# =========================
# KPIs rápidos
# =========================
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric("Amostras (após filtros)", f"{len(dff):,}".replace(",", "."))
with c2:
    if "falha_maquina" in dff.columns and len(dff) > 0:
        st.metric("Taxa de falha (%)", f"{100*dff['falha_maquina'].mean():.2f}%")
    else:
        st.metric("Taxa de falha (%)", "–")
with c3:
    st.metric("Qtd. tipos_falha", dff["tipo_falha"].nunique() if "tipo_falha" in dff.columns else "–")
with c4:
    st.metric("Qtd. tipos (máquina)", dff["tipo"].nunique() if "tipo" in dff.columns else "–")

st.divider()

# ============================================================
# 1) Impacto da FALHA (0/1) nas variáveis numéricas
#    -> Correlação ponto-biserial | Boxplots por falha
# ============================================================
st.subheader("1) Impacto da **falha_maquina (0/1)** nas variáveis numéricas")

if "falha_maquina" in dff.columns and dff["falha_maquina"].nunique() == 2:
    # Seleciona numéricas úteis (var > 0)
    num_ok = [c for c in dff.select_dtypes(include=[np.number]).columns if c != "falha_maquina" and dff[c].std(skipna=True) > 0]
    # Calcula correlações ponto-biseriais
    corr_rows = []
    for col in num_ok:
        r = point_biserial_corr(dff["falha_maquina"], dff[col])
        corr_rows.append((col, r))
    corr_df = pd.DataFrame(corr_rows, columns=["variavel", "corr_ponto_biserial"]).dropna()
    corr_df["abs_corr"] = corr_df["corr_ponto_biserial"].abs()
    corr_df = corr_df.sort_values("abs_corr", ascending=False)

    # Tabela (top 12 por |corr|)
    st.markdown("**Top variáveis mais relacionadas (|correlação ponto-biserial|)**")
    st.dataframe(corr_df.head(12).style.format({"corr_ponto_biserial": "{:.3f}", "abs_corr": "{:.3f}"}), use_container_width=True)

    # Barra das top 10
    if not corr_df.empty:
        fig, ax = plt.subplots(figsize=(6, 3.5))
        plot_df = corr_df.head(10).sort_values("abs_corr")
        ax.barh(plot_df["variavel"], plot_df["abs_corr"])
        ax.set_xlabel("|correlação| (ponto-biserial)")
        ax.set_ylabel("variável")
        ax.set_title("Impacto da falha (0/1) – top 10 |correlações|")
        st.pyplot(fig)

    # Boxplots por falha para uma variável escolhida
    if len(num_ok) > 0:
        var_escolhida = st.selectbox("Visualizar distribuição por falha de:", num_ok, index=0)
        fig, ax = plt.subplots()
        sns.boxplot(x=dff["falha_maquina"].astype(str), y=dff[var_escolhida], ax=ax)
        ax.set_xlabel("falha_maquina (0 = não, 1 = sim)")
        ax.set_title(f"Boxplot de {var_escolhida} por falha")
        st.pyplot(fig)
else:
    st.info("É necessário ter a coluna `falha_maquina` com valores 0/1 para esta análise.")

st.divider()

# ============================================================
# 2) Quais **tipos de falha** estão mais associados às variáveis numéricas?
#    -> Correlação por razão de correlação (eta-squared)
#    -> Heatmap de médias padronizadas por tipo_falha
# ============================================================
st.subheader("2) Associação de **tipo_falha** com variáveis numéricas (η²)")

if "tipo_falha" in dff.columns and dff["tipo_falha"].nunique() >= 2:
    # Seleciona numéricas úteis
    num_ok = [c for c in dff.select_dtypes(include=[np.number]).columns if dff[c].std(skipna=True) > 0]

    # Calcula eta-squared (0..1) para cada variável numérica explicada por tipo_falha
    eta_rows = []
    for col in num_ok:
        eta2 = correlation_ratio_eta_squared(dff["tipo_falha"].astype(str), dff[col])
        eta_rows.append((col, eta2))
    eta_df = pd.DataFrame(eta_rows, columns=["variavel", "eta2"]).dropna()
    eta_df = eta_df.sort_values("eta2", ascending=False)

    st.markdown("**Top variáveis com maior η² (razão de correlação)** – quanto maior, mais a variação da métrica é explicada por `tipo_falha`.")
    st.dataframe(eta_df.head(12).style.format({"eta2": "{:.3f}"}), use_container_width=True)

    # Barra das top 10
    if not eta_df.empty:
        fig, ax = plt.subplots(figsize=(6, 3.5))
        plot_df = eta_df.head(10).sort_values("eta2")
        ax.barh(plot_df["variavel"], plot_df["eta2"])
        ax.set_xlabel("eta² (0..1)")
        ax.set_ylabel("variável")
        ax.set_title("Associação de tipo_falha – top 10 (eta²)")
        st.pyplot(fig)

    # Heatmap de médias padronizadas (z-score) por tipo_falha (apenas top variáveis)
    top_vars = eta_df.head(8)["variavel"].tolist() if len(eta_df) > 0 else []
    if top_vars:
        # calcula z-score global para comparabilidade
        zdf = dff[top_vars].apply(lambda s: (s - s.mean()) / (s.std(ddof=0) if s.std(ddof=0) != 0 else 1.0))
        zdf["tipo_falha"] = dff["tipo_falha"].astype(str).values
        mean_by_failtype = zdf.groupby("tipo_falha")[top_vars].mean()
        fig, ax = plt.subplots(figsize=(6, 3.8))
        sns.heatmap(mean_by_failtype, annot=True, fmt=".2f", cmap="coolwarm", center=0, ax=ax)
        ax.set_title("Médias padronizadas (z-score) por tipo_falha – variáveis mais discriminantes")
        st.pyplot(fig)

        st.info("💡 Leitura do heatmap: valores positivos (vermelho) indicam **acima da média** geral; negativos (azul), **abaixo da média**. "
                "Os padrões por linha sugerem quais sensores/variáveis se elevam ou caem em cada `tipo_falha`.")
else:
    st.info("Para esta análise, é necessário ter `tipo_falha` com 2 ou mais categorias.")

st.divider()

# ============================================================
# 3) Correlações entre variáveis numéricas (contexto geral)
# ============================================================
st.subheader("3) Correlação entre variáveis numéricas (contexto geral)")
num_for_corr = dff.select_dtypes(include=[np.number])
if num_for_corr.shape[1] >= 2:
    corr = num_for_corr.corr(numeric_only=True)
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="viridis", ax=ax)
    ax.set_title("Matriz de Correlação (Pearson)")
    st.pyplot(fig)
else:
    st.info("Não há variáveis numéricas suficientes para calcular a correlação.")

# =========================
# Notas finais (guias de leitura)
# =========================
st.caption(
    "📝 **Guia rápido**: "
    "1) Use as tabelas de ranking para focar nas variáveis mais relacionadas à falha/ao tipo de falha. "
    "2) Use o boxplot para entender **como** a distribuição muda quando há falha. "
    "3) O heatmap (η²) ajuda a identificar quais sensores melhor distinguem os tipos de falha."
)
