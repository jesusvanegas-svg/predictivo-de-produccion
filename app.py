import streamlit as st
import pandas as pd
import joblib # Para cargar el modelo que entrenaste en Colab

# 1. Cargar los modelos pre-entrenados (asumiendo que los guardaste antes)
# modelo_lt = joblib.load('modelo_lead_time.pkl')
# modelo_rep = joblib.load('modelo_reprocesos.pkl')

# 2. Diseño de la Interfaz Web
st.title("🏭 Dashboard Predictivo de Producción")
st.markdown("### Predicción de Lead Time y Riesgo de Reproceso")

# 3. Entradas del Usuario (Lo que llenaría el jefe de turno)
col1, col2 = st.columns(2)

with col1:
    metros = st.number_input("Metros a Fabricar (Tamaño del Lote):", min_value=100, max_value=50000, value=5000)

with col2:
    minutos_parada = st.slider("Minutos de Parada Acumulados:", min_value=0, max_value=500, value=0)

# 4. Botón de Predicción
if st.button("Calcular Proyección"):
    
    # Aquí el modelo haría el cálculo real con los datos ingresados
    # dias_proyectados = modelo_lt.predict([[metros, minutos_parada]])[0]
    # riesgo_reproceso = modelo_rep.predict_proba([[metros, minutos_parada]])[0][1]
    
    # (Simulación de resultados para el ejemplo)
    dias_proyectados = 12 + (metros * 0.001) + (minutos_parada * 0.05) 
    
    st.divider()
    st.subheader("📊 Resultados de la Predicción")
    
    # 5. Mostrar Resultados de forma visual
    res1, res2 = st.columns(2)
    
    with res1:
        if dias_proyectados <= 17:
            st.success(f"Lead Time Proyectado: {dias_proyectados:.1f} Días (Dentro de la meta)")
        else:
            st.error(f"Lead Time Proyectado: {dias_proyectados:.1f} Días (Retraso inminente)")
            
    with res2:
        if minutos_parada > 60:
            st.warning("⚠️ Alto riesgo de reproceso por paradas prolongadas.")
        else:
            st.info("✅ Flujo de producción estable.")