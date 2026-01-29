# 📊 Sistema Inteligente de Predicción de Abandono (Churn)

Este repositorio contiene un proyecto integral de Inteligencia Artificial que abarca desde la exploración de datos hasta el despliegue de una aplicación funcional. El sistema es capaz de predecir la probabilidad de que un cliente abandone un servicio basándose en patrones de comportamiento.

---

## 🎯 1. Objetivo e Importancia
El objetivo principal es reducir la tasa de "Churn" (fuga de clientes). En sectores competitivos, retener a un cliente es significativamente más económico que captar uno nuevo. Este modelo proporciona una herramienta de **analítica prescriptiva** para que el departamento de marketing pueda actuar antes de que el cliente se dé por perdido.

## 📁 2. Estructura del Proyecto
* **`Notebook_Principal.ipynb`**: Todo el pipeline de ciencia de datos (EDA, Limpieza, Entrenamiento y Validación).
* **`app.py`**: Interfaz gráfica profesional desarrollada en Streamlit.
* **`modelo_churn.pkl`**: El "cerebro" del proyecto; el modelo entrenado y exportado.
* **`requirements.txt`**: Archivo de configuración para instalar las dependencias con un solo comando.

---

## 🛠️ 3. Metodología Aplicada

### A. Exploración y Limpieza (EDA)
Se procesó el dataset *Telco Customer Churn*, realizando:
* Conversión de tipos de datos (especialmente en cargos totales).
* Tratamiento de valores nulos mediante eliminación dirigida.
* **Label Encoding** para transformar categorías en datos procesables por la IA.

### B. Entrenamiento y Prevención de Sobreajuste
Se seleccionó un **Árbol de Decisión** por su capacidad de interpretación. Para cumplir con los requisitos de la asignatura, se aplicaron:
* **Poda (Pruning):** Limitación de `max_depth` para evitar que el modelo memorice el ruido.
* **Regularización:** Uso de `min_samples_split` para asegurar que las reglas sean generales.
* **Balanceo de Clases:** Se utilizó `class_weight='balanced'` para compensar el desequilibrio de datos y detectar mejor a los clientes en riesgo.

### C. Evaluación (Línea Base)
El modelo fue comparado contra una **Línea Base (ZeroR)**. Mientras que el azar/mayoría ofrecía un acierto del ~73%, nuestro modelo optimizado no solo mejora la precisión, sino que optimiza el **Recall**, capturando la mayoría de los casos reales de abandono.

---

## 🚀 4. Guía de Instalación y Uso

### Requisitos previos
Tener Python 3.10 o superior instalado.

### Paso 1: Instalación de dependencias
Abre tu terminal en la carpeta del proyecto y ejecuta:
```bash
pip install -r requirements.txt
```

> **Nota:** Si no dispones del archivo `.txt`, puedes realizar la instalación manual de las librerías necesarias ejecutando:
> `pip install streamlit pandas scikit-learn joblib`

### 🚀 Paso 2: Ejecución de la Interfaz
Para lanzar la aplicación web en tu navegador local, abre una terminal en la carpeta del proyecto y ejecuta el siguiente comando:

```bash
streamlit run app.py
```

## 📈 5. Posible Despliegue en Ambiente Real

El diseño de este proyecto ha sido concebido para facilitar su paso a producción mediante tres vías principales:

* **☁️ Cloud Hosting:** El código es totalmente compatible para una subida inmediata a plataformas como **Streamlit Cloud**, **Heroku** o **AWS**, permitiendo el acceso global mediante una URL pública segura.
* **🔌 Integración CRM:** Gracias a su estructura modular, el modelo puede conectarse a bases de datos corporativas en tiempo real para generar **alertas automáticas** directamente en el panel de control de los agentes de ventas.
* **⚖️ Escalabilidad y Mantenimiento:** El uso de archivos serializados `.pkl` permite que el modelo sea reentrenado con nuevos datos y actualizado periódicamente **sin necesidad de modificar el código** de la interfaz de usuario.

---

## 💡 6. Conclusión

Este proyecto demuestra que la **Inteligencia Artificial** alcanza su máximo valor cuando se cierra la brecha entre el análisis de datos riguroso y la accesibilidad para el usuario final.

A través de la combinación de un **Notebook de experimentación** (donde se validaron técnicas de **regularización, poda y control de hiperparámetros**) y una **Interfaz Intuitiva**, se ha logrado un equilibrio óptimo entre complejidad técnica y utilidad práctica. El resultado cumple con los estándares actuales de la industria para el desarrollo de soluciones basadas en datos (*Data-Driven Decisions*).

---
> **Desarrollado para la Asignatura de Inteligencia Artificial - 2026**
