# 1. Importación de librerías
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


def entrenar_modelo():
    """
    Esta función se encarga de todo el proceso de "backend":
    1. Genera los datos sintéticos de pacientes.
    2. Define la lógica para etiquetar el riesgo.
    3. Entrena un modelo de Regresión Logística.
    4. Devuelve el modelo entrenado y los datos de prueba para evaluación.
    """
    print("🤖 Generando datos y entrenando el modelo...")
    # 2. Generación de Datos Sintéticos
    np.random.seed(42)
    num_pacientes = 200
    datos = {
        'edad': np.random.randint(18, 80, size=num_pacientes),
        'tiene_fiebre': np.random.choice([0, 1], size=num_pacientes, p=[0.7, 0.3]),
        'tiene_tos': np.random.choice([0, 1], size=num_pacientes, p=[0.6, 0.4]),
        'dolor_garganta': np.random.choice([0, 1], size=num_pacientes, p=[0.8, 0.2])
    }
    df_pacientes = pd.DataFrame(datos)

    # 3. Creación de la Etiqueta (Target)
    df_pacientes['riesgo_alto'] = np.where(
        ((df_pacientes['tiene_fiebre'] == 1) & (df_pacientes['tiene_tos'] == 1)) | (df_pacientes['edad'] > 60),
        1, 0
    )

    # 4. Preparación de los Datos y división
    X = df_pacientes[['edad', 'tiene_fiebre', 'tiene_tos', 'dolor_garganta']]
    y = df_pacientes['riesgo_alto']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 5. Creación y Entrenamiento del Modelo
    modelo = LogisticRegression()
    modelo.fit(X_train, y_train)
    print("✅ ¡Modelo entrenado con éxito!\n")

    return modelo, X_test, y_test


def ejecutar_proceso_completo(modelo, X_test, y_test):
    """
    Opción 1: Muestra la evaluación completa del modelo en los datos sintéticos.
    """
    print("\n--- Evaluación del Modelo sobre Datos Sintéticos ---")
    y_pred = modelo.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print(f"El modelo fue probado en un conjunto de {len(y_test)} pacientes que no había visto antes.")
    print(f"📊 Precisión (Accuracy): {accuracy:.2%}\n")
    print("Reporte de Clasificación Detallado:")
    print(classification_report(y_test, y_pred, target_names=['Bajo Riesgo', 'Alto Riesgo']))
    print("Este reporte muestra qué tan bien el modelo distingue entre las dos clases.")


def iniciar_prediccion_interactiva(modelo):
    """
    Opción 2: Permite al usuario introducir datos para un nuevo paciente y obtener una predicción.
    """
    print("\n--- Sistema de Predicción de Riesgo (Modo Interactivo) ---")
    print("Por favor, introduce los datos del paciente a continuación.")

    while True:
        try:
            edad = int(input("Introduce la edad del paciente (ej: 50): "))
            if 0 < edad < 120:
                break
            else:
                print("Por favor, introduce una edad realista.")
        except ValueError:
            print("Error: La edad debe ser un número entero.")

    def preguntar_sintoma(pregunta):
        while True:
            respuesta = input(f"{pregunta} (sí/no): ").lower()
            if respuesta in ["sí", "si", "s"]:
                return 1
            elif respuesta in ["no", "n"]:
                return 0
            else:
                print("Respuesta no válida. Por favor, responde 'sí' o 'no'.")

    fiebre = preguntar_sintoma("¿El paciente tiene fiebre?")
    tos = preguntar_sintoma("¿El paciente tiene tos?")
    dolor_garganta = preguntar_sintoma("¿El paciente tiene dolor de garganta?")

    paciente_nuevo = pd.DataFrame({
        'edad': [edad], 'tiene_fiebre': [fiebre], 'tiene_tos': [tos], 'dolor_garganta': [dolor_garganta]
    })

    prediccion = modelo.predict(paciente_nuevo)
    probabilidades = modelo.predict_proba(paciente_nuevo)

    print("\n-------------------------------------------")
    print("      RESULTADO DEL DIAGNÓSTICO")
    print("-------------------------------------------")
    if prediccion[0] == 1:
        resultado, prob_riesgo = "ALTO RIESGO", probabilidades[0][1]
        print(f"Resultado: 🔴 {resultado}")
    else:
        resultado, prob_riesgo = "BAJO RIESGO", probabilidades[0][0]
        print(f"Resultado: 🟢 {resultado}")
    print(f"Confianza de la predicción: {prob_riesgo:.1%}")
    print("-------------------------------------------")
    print("Nota: Este es un modelo con fines demostrativos y no debe usarse para diagnósticos médicos reales.")


def main_menu():
    """
    Muestra el menú principal al usuario y gestiona la navegación.
    """
    # Primero, entrenamos el modelo una sola vez al iniciar el programa.
    modelo, X_test, y_test = entrenar_modelo()

    while True:
        print("\n=============================================")
        print("   MENÚ PRINCIPAL DEL CLASIFICADOR")
        print("=============================================")
        print("1. Ver evaluación completa del modelo (usando datos sintéticos)")
        print("2. Predecir riesgo de un nuevo paciente (interactivo)")
        print("3. Salir")

        opcion = input("Elige una opción (1, 2 o 3): ")

        if opcion == '1':
            ejecutar_proceso_completo(modelo, X_test, y_test)
        elif opcion == '2':
            iniciar_prediccion_interactiva(modelo)
        elif opcion == '3':
            print("👋 Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("❌ Opción no válida. Por favor, elige 1, 2 o 3.")


# --- Punto de entrada del programa ---
if __name__ == "__main__":
    main_menu()