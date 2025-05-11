# 📚 MVP Legal Deliberativo: Propiedad Intelectual

Este proyecto implementa un sistema deliberativo interactivo para explorar casos reales de **propiedad intelectual**, formulando preguntas abiertas, generando razonamiento epistémico trazable y evaluando la calidad de la deliberación jurídica mediante una métrica basada en el **Equilibrio Erotético (EEE)**.

---

## 🎯 Objetivo

Transformar la exploración de casos legales en un proceso guiado por preguntas jerárquicas y navegación epistémica estructurada. El sistema permite:

- Formular preguntas iniciales sobre un caso de PI.
- Generar subpreguntas automáticamente.
- Visualizar una trayectoria de razonamiento.
- Evaluar la deliberación con una métrica epistémica simple.

---

## ⚙️ Funcionalidades principales

| Módulo                     | Descripción                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| `data/casos_pi.json`      | Casos de propiedad intelectual listos para analizar.                        |
| `main.py`                 | Interfaz Streamlit con navegación por casos, razonamiento y evaluación.     |
| `modules/reasoning.py`    | Lógica de generación de preguntas y trazado del razonamiento.               |
| `modules/evaluator.py`    | Cálculo del índice de equilibrio erotético (EEE) de cada indagación.        |

---

## 🧠 Ejemplos de casos

- **Plagio académico**: trabajo no publicado con coincidencia alta.
- **Uso de imagen en redes sociales sin permiso**.
- **Software open source reutilizado sin atribución.**

---

## 🚀 Despliegue en Streamlit Cloud

1. Haz fork de este repositorio.
2. Entra a [https://streamlit.io/cloud](https://streamlit.io/cloud).
3. Selecciona el repositorio y el archivo principal `main.py`.
4. (Opcional) Añade `OPENAI_API_KEY` en "Secrets" si deseas integrar IA generativa.
5. Haz clic en "Deploy".

---
