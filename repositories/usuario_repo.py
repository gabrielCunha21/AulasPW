from models.usuario_model import Usuario
from sql.usuario_sql import *
from util.db import obter_conexao


class UsuarioRepo:
    @classmethod
    def criar_tabela(cls):
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_CRIAR_TABELA)

    @classmethod
    def inserir_usuario(cls, usuario: Usuario) -> bool:
        with obter_conexao() as db:
            cursor = db.cursor()
            resultado = cursor.execute(SQL_INSERIR_USUARIO,(usuario.nome, usuario.email, usuario.telefone, usuario.senha, usuario.perfil))
            return resultado.rowcount > 0

    @classmethod
    def atualizar_token(cls, email: str, token: str) -> bool:
        with obter_conexao() as db:
            cursor = db.cursor()
            resultado = cursor.execute(SQL_ATUALIZAR_TOKEN, (token, email))
            return resultado.rowcount > 0
        
    @classmethod
    def atualizar_senha(cls, email: str, senha: str) -> bool:
        with obter_conexao() as db:
            cursor = db.cursor()
            resultado = cursor.execute(SQL_ATUALIZAR_SENHA, (senha, email))
            return resultado.rowcount > 0
        
    @classmethod
    def atualizar_tema(cls, email: str, tema: str) -> bool:
        with obter_conexao() as db:
            cursor = db.cursor()
            resultado = cursor.execute(SQL_ATUALIZAR_TEMA, (tema, email))
            return resultado.rowcount > 0
        
    @classmethod
    def atualizar_dados(cls, nome: str, email: str, telefone: str) -> bool:
        with obter_conexao() as db:
            cursor = db.cursor()
            resultado = cursor.execute(SQL_ATUALIZAR_DADOS, (nome, email, telefone, email))
            return resultado.rowcount > 0

    @classmethod
    def checar_credenciais(cls, email: str, senha : str) -> bool:
            with obter_conexao() as db:
                cursor = db.cursor()
                resultado = cursor.execute(SQL_CHECAR_CREDENCIAIS, (email, senha))
                return resultado.rowcount > 0

    @classmethod
    def excluir_usuario(cls, email: str) -> bool:
            with obter_conexao() as db:
                cursor = db.cursor()
                resultado = cursor.execute(SQL_EXCLUIR_USUARIO, (email,))
                return resultado.rowcount > 0
            
    
    @classmethod
    def obter_perfil(cls, email: str) -> int:
        with obter_conexao() as db:
            cursor = db.cursor()
            resultado = cursor.execute(
                SQL_OBTER_PERFIL, (email,))
            return resultado.fetchone()[0]