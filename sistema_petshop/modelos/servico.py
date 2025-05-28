from sqlalchemy import Column, Integer, String, Float, UniqueConstraint
from .base import Base
from tratamento_de_erros import ler_str, ler_float

class Servico(Base):
    __tablename__ = "servicos"
    __table_args__ = (
        UniqueConstraint('nome', name='uq_servicos_nome'),
    )

    id = Column(Integer, primary_key=True)
    nome = Column(String, unique=True, nullable=False)
    descricao = Column(String, nullable=True)
    preco = Column(Float, nullable=False)
    contador_servicos = 0

    def __init__(self, nome: str, preco: float, descricao: str = None):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
        Servico.contador_servicos += 1

    def exibir_detalhes(self):
        return f"""
        Serviço ID: {self.id}
        Nome: {self.nome}
        Descrição: {self.descricao or '—'}
        Preço: R$ {self.preco:.2f}
        """

    @classmethod
    def total_servicos(cls):
        return cls.contador_servicos

    @staticmethod
    def inserir_servico(session):
        try:
            nome = ler_str("Nome do serviço: ")
            if session.query(Servico).filter_by(nome=nome).first():
                print("Já existe um serviço com esse nome.")
                return

            preco = ler_float("Preço do serviço (use ponto): ")
            descricao = ler_str("Descrição (opcional): ", allow_blank=True, default=None)

            serv = Servico(nome, preco, descricao)
            session.add(serv)
            session.commit()
            print("Serviço inserido com sucesso!")
        except Exception as e:
            print("Erro ao inserir serviço:", e)
            session.rollback()

    @staticmethod
    def listar_servicos(session):
        servicos = session.query(Servico).all()
        if not servicos:
            print("Nenhum serviço cadastrado.")
            return
        for s in servicos:
            print(s.exibir_detalhes())
