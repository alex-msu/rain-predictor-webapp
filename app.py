from flask import Flask, request, render_template
import pandas as pd
import pickle
import os
import sys

app = Flask(__name__)

MODEL_PATH = os.path.join("models", "modelo_rf.pkl")

# Cargar modelo
try:
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    print("✅ Modelo cargado correctamente", file=sys.stderr)
except Exception as e:
    print(f"❌ Error al cargar el modelo: {e}", file=sys.stderr)
    model = None

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    error = None

    if request.method == "POST" and model is not None:
        try:
            # 1) Leer inputs del formulario
            humidity3pm   = float(request.form["humidity3pm"])
            rainfall      = float(request.form["rainfall"])
            sunshine      = float(request.form["sunshine"])
            windgustspeed = float(request.form["windgustspeed"])
            cloud3pm      = float(request.form["cloud3pm"])

            # 2) Columnas que el modelo espera
            expected = list(model.feature_names_in_)

            # 3) Diccionario con valores por defecto
            data_dict = {col: 0 for col in expected}

            # 4) Sobrescribir con valores reales
            data_dict.update({
                'Humidity3pm':   humidity3pm,
                'Rainfall':      rainfall,
                'Sunshine':      sunshine,
                'WindGustSpeed': windgustspeed,
                'Cloud3pm':      cloud3pm
            })

            # 5) Crear DataFrame con orden correcto
            X_input = pd.DataFrame([data_dict], columns=expected)

            # 6) Obtener predicción y probabilidad
            result = model.predict(X_input)[0]
            prob_lluvia = model.predict_proba(X_input)[0][1]  # Índice 1 = clase "lloverá"

            # 7) Armar mensaje con probabilidad
            pred_text = "Sí, lloverá mañana." if result == 1 or result == "Yes" else "No, no lloverá mañana."
            prediction = f"{pred_text} (Probabilidad: {prob_lluvia*100:.2f}%)"

        except Exception as e:
            error = f"Error en la predicción: {e}"

    return render_template("index.html", prediction=prediction, error=error)

if __name__ == "__main__":
    app.run(debug=True)
