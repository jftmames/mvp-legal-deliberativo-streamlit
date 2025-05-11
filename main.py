import streamlit as st
import json
from modules.reasoning import generate_questions, trace_reasoning
from modules.evaluator import evaluate_deliberation

st.set_page_config(page_title="Deliberador PI", layout="wide")

st.title("📚 Deliberador de Propiedad Intelectual")
st.markdown("Explora casos reales, formula preguntas y evalúa razonamientos jurídicos sobre derechos de autor, uso indebido y licencias.")

# Cargar casos
with open("data/casos_pi.json", "r", encoding="utf-8") as f:
    casos = json.load(f)

caso_titulos = list(casos.keys())
caso_seleccionado = st.selectbox("🧠 Selecciona un caso", caso_titulos)

if caso_seleccionado:
    texto = casos[caso_seleccionado]
    st.markdown(f"### {caso_seleccionado}")
    st.write(texto)

    st.subheader("🔍 Formula una pregunta inicial")
    pregunta_raiz = st.text_input("Pregunta deliberativa:", "")

    if pregunta_raiz:
        subpreguntas = generate_questions(pregunta_raiz, texto)
        st.markdown("#### 🧩 Subpreguntas generadas:")
        for q in subpreguntas:
            st.markdown(f"- {q}")

        st.divider()
        st.subheader("🧠 Trazabilidad del razonamiento")
        razonamiento = trace_reasoning(pregunta_raiz, subpreguntas)
        st.json(razonamiento)

        st.divider()
        st.subheader("📊 Evaluación epistémica")
        score = evaluate_deliberation(razonamiento)
        st.metric(label="Índice de Equilibrio Erotético (EEE)", value=f"{score:.2f}")
