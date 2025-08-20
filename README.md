# Modelo de Clasificación Binaria de Riesgo de Pacientes

Este repositorio contiene el código para un modelo simple de Machine Learning construido en Python. El programa clasifica a los pacientes en "riesgo bajo" o "riesgo alto" y presenta una interfaz de menú interactiva en la consola.

El propósito de este proyecto es demostrar la lógica de programación, el flujo de trabajo de un proyecto de IA y el desarrollo de una aplicación de consola modular y amigable con el usuario.

---

## 🏛️ Arquitectura y Flujo del Programa

El programa sigue una arquitectura modular y un flujo controlado por el usuario.

1.  **Inicialización y Entrenamiento**: Al ejecutar `main.py`, el programa primero genera un dataset sintético y entrena un modelo de **Regresión Logística**. Este modelo queda listo en memoria para ser utilizado.

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
    git clone https://github.com/AudielVenturaM/patient-risk-classification
    cd patient-risk-classification
    ```
    https://github.com/AudielVenturaM/patient-risk-classification

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