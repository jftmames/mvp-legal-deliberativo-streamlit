import random

def generate_questions(root_question, clause_text):
    return [
        f"¿Qué implicaciones tiene respecto a {root_question.lower()}?",
        f"¿Qué excepciones podrían aplicarse a esta cláusula?",
        f"¿Cómo se relaciona esta cláusula con principios generales del derecho?"
    ]

def trace_reasoning(root, subqs):
    return {
        "pregunta_raíz": root,
        "trayectoria": [
            {"subpregunta": q, "respuesta": "🧠 Respuesta hipotética a deliberar."}
            for q in subqs
        ]
    }
