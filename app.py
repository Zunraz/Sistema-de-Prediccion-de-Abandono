import streamlit as st
import pandas as pd
import joblib
import numpy as np

# 1. Configuración de la página
st.set_page_config(page_title="IA de Retención de Clientes", page_icon="📊")

st.title("🛡️ Sistema de Predicción de Abandono (Churn)")
st.markdown("""
Esta aplicación utiliza un modelo de **Inteligencia Artificial** para predecir si un cliente cancelará su servicio.
""")

# 2. Cargar el modelo entrenado
@st.cache_resource
def load_model():
    return joblib.load('modelo_churn.pkl')

model = load_model()

# 3. Formulario de entrada de datos en la barra lateral
st.sidebar.header("Datos del Cliente")

def user_input_features():
    tenure = st.sidebar.slider("Antigüedad (meses)", 0, 72, 12)
    monthly_charges = st.sidebar.slider("Cargo Mensual ($)", 18, 120, 50)
    total_charges = tenure * monthly_charges
    
    contract = st.sidebar.selectbox("Tipo de Contrato", ("Mes a mes", "Un año", "Dos años"))
    contract_val = 0 if contract == "Mes a mes" else (1 if contract == "Un año" else 2)
    
    online_security = st.sidebar.radio("¿Tiene Seguridad Online?", ("No", "Sí"))
    security_val = 1 if online_security == "Sí" else 0

    # Creamos un DataFrame con el formato que el modelo espera
    # NOTA: Asegúrate de que las columnas coincidan con las de tu X_train
    data = {
        'tenure': tenure,
        'MonthlyCharges': monthly_charges,
        'TotalCharges': total_charges,
        'Contract': contract_val,
        'OnlineSecurity': security_val,
        # Añade aquí el resto de variables si tu modelo usa más
    }
    return pd.DataFrame(data, index=[0])

df_input = user_input_features()

# 4. Mostrar datos ingresados y Predicción
st.subheader("Análisis del Cliente")
st.write(df_input)

if st.button("🚀 Calcular Riesgo"):
    # Hacemos la predicción (ajustando a las columnas que espera tu modelo)
    # Aquí un truco: el modelo espera todas las columnas del entrenamiento. 
    # Para este ejemplo simplificado, rellenamos las que faltan con ceros:
    features_completas = np.zeros((1, model.n_features_in_))
    # (En un proyecto real, pasarías todas las variables del formulario)
    
    prediction = model.predict(df_input) # Si usaste solo esas 5 variables
    probabilidad = model.predict_proba(df_input)

    st.divider()
    
    if prediction[0] == 1:
        st.error(f"### ⚠️ ALTA PROBABILIDAD DE ABANDONO")
        st.metric("Riesgo estimado", f"{probabilidad[0][1]*100:.2f}%")
        st.write("👉 **Acción recomendada:** Ofrecer descuento inmediato o mejora de contrato.")
    else:
        st.success(f"### ✅ CLIENTE FIEL")
        st.metric("Probabilidad de permanencia", f"{probabilidad[0][0]*100:.2f}%")
        st.write("👉 **Acción recomendada:** Mantener servicio estándar.")

st.sidebar.info("Proyecto de IA - Grado en Ingeniería")