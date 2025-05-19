import streamlit as st
from student import showstudent
from course import showcourse

st.title("Gerenciador de Cursos e Alunos")

if "tela" not in st.session_state:
    st.session_state["tela"] = "principal"

st.subheader("Escolha uma opção:")

if st.button("Adicionar curso", key="menu_btn_adicionar_curso"):
    st.session_state["tela"] = "curso"

if st.button("Adicionar aluno", key="menu_btn_adicionar_aluno"):
    st.session_state["tela"] = "aluno"

if st.session_state["tela"] == "curso":
    showcourse()

elif st.session_state["tela"] == "aluno":
    showstudent()