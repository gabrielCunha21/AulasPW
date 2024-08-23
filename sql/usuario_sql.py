SQL_CRIAR_TABELA = """CREATE TABLE IF NOT EXISTS usuario(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    telefone TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL,
    token TEXT,
    tema TEXT NOT NULL,
    perfil INTEGER NOT NULL)"""

SQL_INSERIR_USUARIO = """INSERT INTO usuario
    (nome, email, telefone, senha, tema, perfil)
    VALUES(?,?,?,?,"default", ?)"""

SQL_ATUALIZAR_TOKEN = """UPDATE usuario
    SET token = ?
    WHERE email = ?"""

SQL_ATUALIZAR_SENHA = """UPDATE usuario
    SET senha = ?
    WHERE email = ?"""

SQL_CHECAR_CREDENCIAIS = """SELECT email, senha
    FROM usuario
    WHERE email = ? AND senha = ?"""

SQL_ATUALIZAR_DADOS = """UPDATE usuario
    SET nome = ?, email = ?, telefone = ?
    WHERE email = ?"""

SQL_ATUALIZAR_TEMA = """UPDATE usuario
    SET tema = ?
    WHERE email = ?"""

SQL_EXCLUIR_USUARIO = """DELETE FROM usuario
    WHERE email = ?"""

SQL_OBTER_PERFIL = """
    SELECT perfil
    FROM usuario
    WHERE email = ?
"""

