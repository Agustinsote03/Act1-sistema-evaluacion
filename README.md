# Sistema de Evaluacion de Proyectos Estudiantiles

## Contexto Académico
 UNIVERSIDAD NACIONAL DE LA PLATA
 Taller de Lenguajes Python - Segundo Semestre 2025

### Descripción
Sistema desarrollado en Python para evaluar proyectos en una feria de ciencias escolar. Procesa múltiples rondas de evaluación y genera rankings en tiempo real

#### Estructura del proyecto

Act1-sistema-evaluacion/
├── src/
│   └── funciones.py           # Módulo principal con todas las funciones
├── notebooks/
│   └── Actividad1.ipynb       # Jupyter notebook de análisis
└── README.md                  # Este archivo

## Instalacion
DEPENDENCIAS: Python 3.8+ , Jupyter Notebook, ipykernel>= 6.0.0

# Clonar el repositorio
git clone https://github.com/tuusuario/Act1-sistema-evaluacion.git
cd Act1-sistema-evaluacion

# Ejecutar notebook
jupyter notebook notebooks/Actividad1.ipynb

# Funciones principales
procesar_evaluaciones_completo(evaluaciones) - Acumula e imprime
mostrar_tabla_de_resultados(resultados['puntajes_acumulados']) - Recibe un diccionario generado en el recorrido y lo imprime

