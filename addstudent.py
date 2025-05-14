from app import sendstudenttosql
import mysql.connector as mysql
import streamlit as st

def show():
    st.header("Cadastro de Aluno")

    st.markdown("Preencha os dados abaixo:")

    with st.form("form_aluno"):
        col1, col2 = st.columns(2)

        with col1:
            nome = st.text_input("Nome")
            cpf = st.text_input("CPF")
            sexo = st.selectbox("Sexo", ["Escolher...", "Masculino", "Feminino", "Outro"])
            uf = st.selectbox("Estado", ["Escolher...", "AL", "BA", "CE", "SP", "RJ", "MG"])
            cidade = st.text_input("Cidade")

        with col2:
            rua = st.text_input("Rua")
            numero = st.text_input("Número da Casa")
            telefone_fixo = st.text_input("Telefone Fixo")
            telefone_celular = st.text_input("Telefone Celular")
            idade = st.number_input("Idade", min_value=0, max_value=120, step=1)

        col_btn1, col_btn2 = st.columns([1, 1])

        with col_btn1:
            if st.form_submit_button("Gravar"):
                sucesso = sendstudenttosql(nome, cpf, sexo, uf, cidade, rua, numero, telefone_fixo, telefone_celular, idade)

                if sucesso:
                    st.success("Aluno gravado com sucesso!")
            else:
                st.error("Erro ao gravar aluno.")