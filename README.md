# Modelo de Clasificación Binaria de Riesgo de Pacientes

Este repositorio contiene el código para un modelo simple de Machine Learning construido en Python. El programa clasifica a los pacientes en "riesgo bajo" o "riesgo alto" y presenta una interfaz de menú interactiva en la consola.

El propósito de este proyecto es demostrar la lógica de programación, el flujo de trabajo de un proyecto de IA y el desarrollo de una aplicación de consola modular y amigable con el usuario.

---

## 🏛️ Arquitectura y Flujo del Programa

El programa sigue una arquitectura modular y un flujo controlado por el usuario.

### Arquitectura de la Aplicación

La arquitectura se puede describir de la siguiente manera:

* **Modular en un solo script**: Aunque todo el código reside en un único archivo (`main.py`), está estructurado en funciones con responsabilidades claras y únicas (una para entrenar, una para evaluar, una para predecir, etc.).
* **Interfaz de Consola (CLI)**: Toda la interacción con el usuario ocurre a través del `main_menu()`, que actúa como el controlador principal de la aplicación.
* **Procesamiento en Memoria**: El conjunto de datos y el modelo de Machine Learning se generan, entrenan y almacenan en la memoria RAM solo durante la ejecución del programa. No se guardan en disco, por lo que el estado se reinicia cada vez que se ejecuta el script.

### Flujo de Datos Detallado

1.  **Inicialización y Entrenamiento**: Al ejecutar `main.py`, el programa primero genera un dataset sintético y entrena un modelo de **Regresión Logística**. Este modelo queda listo en memoria para ser utilizado. El flujo de datos, desde su creación hasta la predicción final, sigue estos pasos:
    1.  **Generación y Etiquetado**: Se crea un `DataFrame` de `pandas` con 200 registros de pacientes sintéticos y se añade la columna objetivo `riesgo_alto` aplicando una regla lógica.
    2.  **División de Datos (Split)**: El `DataFrame` se divide en un conjunto de **Entrenamiento (80%)** y uno de **Prueba (20%)**.
    3.  **Entrenamiento del Modelo**: El conjunto de entrenamiento se pasa al modelo de **Regresión Logística** para que aprenda los patrones.
    4.  **Inferencia (Uso del Modelo)**: El modelo entrenado se usa para evaluar con los datos de prueba o para predecir con nuevos datos del usuario.

2.  **Menú Principal**: Se presenta un menú al usuario con tres opciones claras que guían la interacción.

3.  **Flujos de Usuario**:
    * **Opción 1 - Evaluación Completa**: Muestra la precisión del modelo usando datos de prueba que no se usaron en el entrenamiento, dando una idea clara de su rendimiento.
    * **Opción 2 - Predicción Interactiva**: Permite al usuario introducir datos de un nuevo paciente para obtener una predicción en tiempo real.
    * **Opción 3 - Salir**: Termina la ejecución del programa de forma limpia.

---

## 🚀 Cómo Ejecutar el Proyecto

Para clonar y ejecutar este proyecto en tu máquina local, sigue estos pasos:

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/AudielVenturaM/patient-risk-classification](https://github.com/AudielVenturaM/patient-risk-classification)
    cd patient-risk-classification
    ```

2.  **Crea un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecuta el script principal:**
    ```bash
    python main.py
    ```

5.  **Interactúa con el menú:**
    Elige una de las opciones que se muestran en la consola (1, 2 o 3) y presiona Enter.