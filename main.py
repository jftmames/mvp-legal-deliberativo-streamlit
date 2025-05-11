import streamlit as st
from modules.parser import load_contract, split_contract
from modules.reasoning import generate_questions, trace_reasoning
from modules.evaluator import evaluate_deliberation
import json

st.set_page_config(page_title="MVP Legal Deliberativo", layout="wide")

st.title("⚖️ MVP Legal Deliberativo")
st.markdown("Explora, pregunta y evalúa contratos jurídicos mediante razonamiento deliberativo estructurado.")

# Cargar contratos
with open("data/contratos_demo.json", "r", encoding="utf-8") as f:
    contratos = json.load(f)

contrato_titulos = list(contratos.keys())
contrato_seleccionado = st.selectbox("📄 Selecciona un contrato", contrato_titulos)

if contrato_seleccionado:
    texto = contratos[contrato_seleccionado]
    clausulas = split_contract(texto)

    clausula_idx = st.slider("📑 Cláusula a explorar", 0, len(clausulas) - 1, 0)
    st.markdown(f"**Cláusula {clausula_idx + 1}**")
    st.code(clausulas[clausula_idx], language="markdown")

    st.divider()
    st.subheader("🔍 Indagación deliberativa")

    pregunta_raiz = st.text_input("Formula una pregunta sobre esta cláusula:", "")
    if pregunta_raiz:
        subpreguntas = generate_questions(pregunta_raiz, clausulas[clausula_idx])
        st.markdown("#### 🧩 Subpreguntas generadas:")
        for i, q in enumerate(subpreguntas):
            st.markdown(f"- {q}")

        st.divider()
        st.subheader("🧠 Trazabilidad del razonamiento")
        razonamiento = trace_reasoning(pregunta_raiz, subpreguntas)
        st.json(razonamiento)

        st.divider()
        st.subheader("📊 Evaluación epistémica")
        score = evaluate_deliberation(razonamiento)
        st.metric(label="Índice de Equilibrio Erotético (EEE)", value=f"{score:.2f}")
