import streamlit as st
from db_utils import sendstudenttosql

def showstudent():
    st.header("Cadastro de Aluno")
    st.markdown("Preencha os dados abaixo:")

    with st.form("form_aluno", clear_on_submit=True):
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
            idade = st.number_input("Idade", min_value=1, max_value=120)

        col_btn1, col_btn2 = st.columns([1, 1])

        with col_btn1:
            gravar = st.form_submit_button("Gravar", type="primary")

        if gravar:
            if nome and cpf:
                cpf = cpf.replace(".", "").replace("-", "").strip()
                if sexo == "Masculino":
                    sexo = "M"
                elif sexo == "Feminino":
                    sexo = "F"
                elif sexo == "Outro":
                    sexo = "O"
                else:
                    sexo = None
                sucesso = sendstudenttosql(nome, cpf, sexo, uf, cidade, rua, numero, telefone_fixo, telefone_celular, idade)
                if sucesso:
                    st.success("Aluno gravado com sucesso!")
                else:
                    st.error("Erro ao gravar aluno.")
            else:
                st.warning("Nome e CPF são obrigatórios!")