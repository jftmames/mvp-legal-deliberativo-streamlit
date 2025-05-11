def generate_questions(root_question, context_text):
    return [
        f"¿Qué derechos están implicados en relación con '{root_question}'?",
        f"¿Qué excepciones legales podrían aplicarse?",
        f"¿Existe jurisprudencia relevante sobre este tipo de caso?"
    ]

def trace_reasoning(root, subqs):
    return {
        "pregunta_raíz": root,
        "trayectoria": [
            {"subpregunta": q, "respuesta": "🧠 Respuesta simulada en análisis epistémico."}
            for q in subqs
        ]
    }
