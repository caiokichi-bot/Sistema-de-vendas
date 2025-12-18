from conexao import Conexao  # Ajuste o nome do arquivo se necessário

class ClienteRepository:
    def __init__(self):
        self.conexao = Conexao()  # Armazena instância completa da Conexao

    def find_all(self):
            cursor = self.conexao.get_cursor()  # dictionary=True já configurado
            cursor.execute("SELECT ClienteID as id, Nome as nome, CPF as cpf, Email as email, Telefone as telefone, Endereco as endereco, Cidade as cidade, Estado as estado, CEP as cep FROM Cliente ORDER BY ClienteID")
            return cursor.fetchall()


    def find_by_id(self, cliente_id):
            cursor = self.conexao.get_cursor()
            cursor.execute(
                "SELECT ClienteID as id, Nome as nome, CPF as cpf, Email as email, Telefone as telefone, Endereco as endereco, Cidade as cidade, Estado as estado, CEP as cep FROM Cliente WHERE ClienteID = %s",
                (cliente_id,)
            )
            return cursor.fetchone()

    def create(self, nome, cpf, email, telefone, endereco, cidade, estado, cep=""):
        """Insere novo registro (ID auto-increment)."""
        cursor = None
        try:
            cursor = self.conexao.get_cursor()
            cursor.execute(
                "INSERT INTO Cliente (Nome, CPF, Email, Telefone, Endereco, Cidade, Estado, CEP) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (nome, cpf, email, telefone, endereco, cidade, estado, cep)
            )
            self.conexao.get_conexao().commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"Erro ao criar categoria: {e}")
            self.conexao.get_conexao().rollback()
            return None
        finally:
            if cursor:
                cursor.close()

    def delete(self, cliente_id):
        """Remove registro pelo ID."""
        cursor = None
        try:
            cursor = self.conexao.get_cursor()
            cursor.execute("DELETE FROM Cliente WHERE ClienteID = %s", (cliente_id,))
            self.conexao.get_conexao().commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Erro ao deletar cliente {cliente_id}: {e}")
            self.conexao.get_conexao().rollback()
            return False
        finally:
            if cursor:
                cursor.close()