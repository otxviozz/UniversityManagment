import streamlit as st
import mysql.connector as mysql
import addcourse
import addstudent

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
        print(f"Erro ao inserir aluno no banco: {e}")
        return False


st.title("Gerenciador de Cursos e Alunos")

if "tela" not in st.session_state:
    st.session_state["tela"] = "principal"

st.subheader("Escolha uma opção:")

if st.button("Adicionar curso", key="btn_adicionar_curso"):
    st.session_state["tela"] = "curso"

if st.button("Adicionar aluno", key="btn_adicionar_aluno"):
    st.session_state["tela"] = "aluno"

if st.session_state["tela"] == "curso":
    addcourse.show()

elif st.session_state["tela"] == "aluno":
    addstudent.show()