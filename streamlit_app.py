import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Dashboard Interattiva con Streamlit")

# Caricamento file CSV
uploaded_file = st.file_uploader("Carica un file CSV", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Anteprima dati:")
    st.dataframe(df.head())

    # Selezione colonna per filtro
    col_filter = st.selectbox("Scegli la colonna per filtrare", df.columns)

    # Valori unici per filtro
    valori = df[col_filter].unique()
    filtro = st.multiselect(f"Filtra valori di {col_filter}", valori, default=valori)

    # Applicazione filtro
    df_filtrato = df[df[col_filter].isin(filtro)]

    st.write(f"Dati filtrati ({len(df_filtrato)} righe):")
    st.dataframe(df_filtrato)

    # Selezione colonne per grafico
    col_x = st.selectbox("Seleziona colonna X per grafico", df.columns)
    col_y = st.selectbox("Seleziona colonna Y per grafico", df.columns)

    # Creazione grafico a dispersione con Plotly
    fig = px.scatter(df_filtrato, x=col_x, y=col_y, title=f"Grafico {col_y} vs {col_x}")
    st.plotly_chart(fig)
else:
    st.info("Carica un file CSV per iniziare.")
