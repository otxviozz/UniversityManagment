import mysql.connector as mysql

def connect_mysql():
    return mysql.connect(
        host="localhost",
        user="root",
        password="aluno",
        database="cursos"
    )

def sendcoursetosql(nome, aulas, valor, turno):
    try:
        conexao = connect_mysql()
        cursor = conexao.cursor()

        comando = """
            INSERT INTO curso (
                nome, aulas, valor, turno
            ) VALUES (%s, %s, %s, %s)
        """

        valores = (nome, aulas, valor, turno)

        cursor.execute(comando, valores)
        conexao.commit()

        cursor.close()
        conexao.close()

        return True

    except Exception as e:
        print(f"[ERRO SQL] Não foi possível gravar curso: {e}")
        return False

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