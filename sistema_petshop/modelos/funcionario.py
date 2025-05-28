from sqlalchemy import Column, String, UniqueConstraint
from .pessoa import Pessoa
from tratamento_de_erros import ler_str, ler_int

class Funcionario(Pessoa):
    __tablename__ = "funcionarios"
    __table_args__ = (
        UniqueConstraint('cpf', name='uq_funcionarios_cpf'),
    )

    departamento = Column(String, nullable=False)
    contador_funcionarios = 0

    def __init__(self, nome: str, idade: int, cpf: str, departamento: str):
        super().__init__(nome, idade)
        self.cpf = cpf
        self.departamento = departamento
        Funcionario.contador_funcionarios += 1

    def exibir_detalhes(self):
        return f"""
        Funcionário ID: {self.id}
        Nome: {self.nome}
        Idade: {self.idade}
        CPF: {self.cpf}
        Departamento: {self.departamento}
        """

    @classmethod
    def total_funcionarios(cls):
        return cls.contador_funcionarios

    @staticmethod
    def inserir_funcionario(session):
        try:
            nome        = ler_str("Nome do funcionário: ")
            idade       = ler_int("Idade do funcionário: ")
            cpf         = ler_str("CPF (somente números): ")
            departamento= ler_str("Departamento: ")
            func = Funcionario(nome, idade, cpf, departamento)
            session.add(func)
            session.commit()
            print("Funcionário inserido com sucesso!")
        except Exception as e:
            print("Erro ao inserir funcionário:", e)
            session.rollback()

    @staticmethod
    def listar_funcionarios(session):
        funcionarios = session.query(Funcionario).all()
        if not funcionarios:
            print("Nenhum funcionário cadastrado.")
            return
        for f in funcionarios:
            print(f.exibir_detalhes())

    @staticmethod
    def atualizar_funcionario(session):
        Funcionario.listar_funcionarios(session)
        try:
            func_id = ler_int("ID do funcionário a ser atualizado: ")
            func = session.query(Funcionario).filter_by(id=func_id).first()
            if not func:
                print("Funcionário não encontrado.")
                return

            print("\nDeixe em branco para manter o valor atual.")
            nome         = ler_str(f"Nome atual ({func.nome}): ",
                                    allow_blank=True, default=func.nome)
            idade        = ler_int(f"Idade atual ({func.idade}): ",
                                   allow_blank=True, default=func.idade)
            cpf          = ler_str(f"CPF atual ({func.cpf}): ",
                                   allow_blank=True, default=func.cpf)
            departamento = ler_str(f"Departamento atual ({func.departamento}): ",
                                   allow_blank=True, default=func.departamento)

            func.nome        = nome
            func.idade       = idade
            func.cpf         = cpf
            func.departamento= departamento
            session.commit()
            print("Funcionário atualizado com sucesso!")
        except Exception as e:
            print("Erro ao atualizar funcionário:", e)
            session.rollback()

    @staticmethod
    def excluir_funcionario(session):
        Funcionario.listar_funcionarios(session)
        try:
            func_id = ler_int("ID do funcionário a ser excluído: ")
            func = session.query(Funcionario).filter_by(id=func_id).first()
            if not func:
                print("Funcionário não encontrado.")
                return

            session.delete(func)
            session.commit()
            print("Funcionário excluído com sucesso!")
        except Exception as e:
            print("Erro ao excluir funcionário:", e)
            session.rollback()
