# 🌧️ Predicción de Lluvia en Australia con Machine Learning

Este proyecto aplica técnicas de aprendizaje automático para predecir si lloverá mañana en distintas ciudades de Australia. Combina un modelo de clasificación con una interfaz web construida en Flask, ideal para presentaciones educativas, prototipos o demostraciones personales.

---

## 📊 Dataset

Se utilizó el dataset ["WeatherAUS"](https://www.kaggle.com/datasets/trisha2094/weatheraus) de Kaggle, que contiene datos meteorológicos históricos de varias estaciones en Australia. Incluye variables como temperatura, humedad, nubosidad, velocidad del viento y precipitaciones.

---

## 🧠 Selección de Variables

Durante la fase de exploración y entrenamiento, se usó un modelo **Random Forest** para identificar las variables más influyentes. A partir del análisis de `feature_importances_`, se eligieron las siguientes 5 variables clave:

- `Humidity3pm`
- `Rainfall`
- `Sunshine`
- `WindGustSpeed`
- `Cloud3pm`

Estas fueron seleccionadas por su alta correlación con la variable objetivo `RainTomorrow`. Esta reducción de dimensionalidad permitió mantener el rendimiento del modelo sin sobreajuste ni complejidad innecesaria.

---

## ⚙️ Tecnologías utilizadas

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![HTML](https://img.shields.io/badge/HTML-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![CSS](https://img.shields.io/badge/CSS-639.svg?style=for-the-badge&logo=css&logoColor=white)     


[//]: # "- Python 3"
[//]: # "- Flask"
[//]: # "- scikit-learn"
[//]: # "- pandas"
[//]: # "- HTML + CSS"

---

## 🖥️ Interfaz Web

La aplicación cuenta con una interfaz web simple y clara. El usuario puede ingresar las variables meteorológicas y obtener una predicción con probabilidad:

![screenshot](screenshot.png)

---

## 📁 Estructura del proyecto

```

├── app.py
├── models/
│   └── modelo_rf.pkl
├── templates/
│   └── index.html
├── static/
│   └── styles.css
├── requirements.txt
├── .gitignore
├── README.md
└── screenshot.png

````

---

## 🚀 ¿Cómo correr la app?

1. Clona este repositorio:
   ```
   git clone https://github.com/alex-msu/rain-predictor-webapp.git
   cd rain-predictor-webapp

2. Crea un entorno virtual (opcional pero recomendado):

   ```
   python -m venv venv
   venv\Scripts\activate  # En Windows

3. Instala las dependencias:

   ```
   pip install -r requirements.txt

4. Ejecuta la app:

   ```
   python app.py

5. Abre tu navegador y visita:

   ```
   http://localhost:5000

> ⚠️ **Este repositorio utiliza [Git LFS](https://git-lfs.github.com/)** para almacenar el modelo entrenado (`modelo_rf.pkl`).
> Si vas a clonar este repositorio, asegúrate de tener Git LFS instalado y ejecuta:
>
> ```
> git lfs install
> git lfs pull

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT.

---

## 👤 Autores

Proyecto individual desarrollado por Alexis Martínez, Benjamín Briceño y Joaquín Parada como parte de un curso universitario. Se utilizó aprendizaje automático, ingeniería de características y una API web ligera para la predicción meteorológica.
