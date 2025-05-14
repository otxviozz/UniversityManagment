import streamlit as st
import mysql.connector as mysql

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

def showcourse():
    st.header("Cadastro de curso")

def connect_mysql():
    return mysql.connect(
        host="localhost",
        user="root",
        password="aluno",
        database="cursos"
        )

def sendstudenttosql(nome, cpf, sexo, uf, cidade, rua, numero, telefone_fixo, telefone_celular, idade):
    try:
        conexao = connect_mysql()
        cursor = conexao.cursor()

        comando = """
            INSERT INTO aluno (
                nome, cpf, uf, cidade, rua, numero,
                telefone_fixo, telefone_celular, sexo, idade
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        valores = (
            nome, cpf, uf, cidade, rua, numero,
            telefone_fixo, telefone_celular, sexo, idade
        )

        cursor.execute(comando, valores)
        conexao.commit()

        cursor.close()
        conexao.close()

        return True

    except Exception as e:
        print(f"[ERRO SQL] Não foi possível gravar aluno: {e}")
        return False


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