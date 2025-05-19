import streamlit as st
from db_utils import sendcoursetosql

def showcourse():
    st.header("Cadastro de Curso")
    st.markdown("Preencha os dados abaixo:")

    with st.form("form_curso", clear_on_submit=True):
        col1, col2 = st.columns(2)

        with col1:
            nome = st.text_input("Nome do Curso")
            aulas = st.number_input("Quantidade de Aulas", min_value=1)
        
        with col2:
            valor = st.number_input("Valor do Curso (R$)", min_value=0.0, format="%.2f")
            turno = st.selectbox("Turno", ["Escolher...", "Matutino", "Vespertino", "Noturno"])

        col_btn1, _ = st.columns([1, 1])

        with col_btn1:
            gravar = st.form_submit_button("Gravar", type="primary")

        if gravar:
            if nome and turno != "Escolher...":
                sucesso = sendcoursetosql(nome, aulas, valor, turno)
                if sucesso:
                    st.success("Curso gravado com sucesso!")
                else:
                    st.error("Erro ao gravar curso.")
            else:
                st.warning("Nome do curso e turno são obrigatórios!")