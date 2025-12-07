import numpy as np
import streamlit as st
import pandas as pd

st.write(''' # Predicción de Finanzas Personales ''')
st.image("finanzas🤑.jpg", caption="Control financiero mensual.")

st.header('Datos de evaluación')

def user_input_features():
  Gastos = st.number_input('¿Cuánto gastas al mes?', min_value=0, step=100)
  Reinversion = st.number_input('¿Cuánto reinviertes al mes?', min_value=0, step=100)
  GananciaReinversion = st.number_input('¿Cuánto ganas de reinversiones al mes?', min_value=0, step=100)
  IngresoActual = st.number_input('¿Cuánto ganas actualmente al mes?', min_value=0, step=100)

  user_data = {'Gastos': Gastos,
               'Reinversion': Reinversion,
               'GananciaReinversion': GananciaReinversion,
               'IngresoActual': IngresoActual}

  return pd.DataFrame(user_data, index=[0])

df = user_input_features()

G = df["Gastos"].iloc[0]
R = df["Reinversion"].iloc[0]
GR = df["GananciaReinversion"].iloc[0]
IA = df["IngresoActual"].iloc[0]

# ---------- PREDICCIÓN A ----------
st.subheader('Predicción A: ¿Te alcanza el dinero?')

if IA + GR >= G:
    st.write("✔ Sí te alcanza para tus gastos.")
else:
    st.write("❌ No te alcanza con tus ingresos actuales.")

# ---------- PREDICCIÓN B ----------
st.subheader("Predicción B: Ingreso mínimo recomendado")

ingreso_necesario = G - GR
ingreso_20 = ingreso_necesario * 1.20

st.write(f"Debes ingresar al mes al menos: **${ingreso_20:.2f} MXN**")

st.info(
    f"Para mantener un equilibrio bien balanceado entre tus gastos e ingresos "
    f"y tener un 20% extra para ahorrar, necesitas ingresar al menos "
    f"**${ingreso_20:.2f} MXN** al mes."
)

# ---------- CLASIFICACIÓN DE GASTO ----------
st.subheader("Clasificación de tu nivel de gasto")

if G < 3000:
    st.write("Gasto bajo")
elif G < 9000:
    st.write("Gasto normal")
elif G < 15000:
    st.write("Gasto un poco alto")
else:
    st.write("Gasto muy alto")
