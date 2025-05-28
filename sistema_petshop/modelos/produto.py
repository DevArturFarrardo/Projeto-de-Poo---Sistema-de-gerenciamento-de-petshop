from sqlalchemy import Column, Integer, String, Float, UniqueConstraint
from .base import Base
from tratamento_de_erros import ler_str, ler_int, ler_float

class Produto(Base):
    __tablename__ = "produtos"
    __table_args__ = (
        UniqueConstraint('nome', name='uq_produtos_nome'),
    )

    id = Column(Integer, primary_key=True)
    nome = Column(String, unique=True, nullable=False)
    descricao = Column(String, nullable=True)
    preco = Column(Float, nullable=False)
    estoque = Column(Integer, nullable=False)
    contador_produtos = 0

    def __init__(self, nome: str, preco: float, estoque: int, descricao: str = None):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.descricao = descricao
        Produto.contador_produtos += 1

    def exibir_detalhes(self):
        return f"""
        Produto ID: {self.id}
        Nome: {self.nome}
        Descrição: {self.descricao or '—'}
        Preço: R$ {self.preco:.2f}
        Estoque: {self.estoque}
        """

    @classmethod
    def total_produtos(cls):
        return cls.contador_produtos

    @staticmethod
    def inserir_produto(session):
        try:
            nome = ler_str("Nome do produto: ")
            if session.query(Produto).filter_by(nome=nome).first():
                print("Já existe um produto com esse nome.")
                return

            preco = ler_float("Preço do produto (ex: 49.90): ")
            estoque = ler_int("Quantidade em estoque: ")
            descricao = ler_str("Descrição (opcional): ", allow_blank=True, default=None)

            produto = Produto(nome, preco, estoque, descricao)
            session.add(produto)
            session.commit()
            print("Produto inserido com sucesso!")
        except Exception as e:
            print("Erro ao inserir produto:", e)
            session.rollback()

    @staticmethod
    def listar_produtos(session):
        produtos = session.query(Produto).all()
        if not produtos:
            print("Nenhum produto cadastrado.")
            return
        for p in produtos:
            print(p.exibir_detalhes())

    @staticmethod
    def atualizar_produto(session):
        Produto.listar_produtos(session)
        try:
            pid = ler_int("ID do produto a ser atualizado: ")
            produto = session.query(Produto).filter_by(id=pid).first()
            if not produto:
                print("Produto não encontrado.")
                return

            print("\nDeixe em branco para manter o valor atual.")
            nome = ler_str(f"Nome atual ({produto.nome}): ",
                           allow_blank=True, default=produto.nome)
            if nome != produto.nome and session.query(Produto).filter_by(nome=nome).first():
                print("Já existe outro produto com esse nome.")
                return

            preco = ler_float(f"Preço atual (R$ {produto.preco:.2f}): ",
                              allow_blank=True, default=produto.preco)
            estoque = ler_int(f"Estoque atual ({produto.estoque}): ",
                              allow_blank=True, default=produto.estoque)
            descricao = ler_str(f"Descrição atual ({produto.descricao or '—'}): ",
                                allow_blank=True, default=produto.descricao)

            produto.nome = nome
            produto.preco = preco
            produto.estoque = estoque
            produto.descricao = descricao
            session.commit()
            print("Produto atualizado com sucesso!")
        except Exception as e:
            print("Erro ao atualizar produto:", e)
            session.rollback()

    @staticmethod
    def excluir_produto(session):
        Produto.listar_produtos(session)
        try:
            pid = ler_int("ID do produto a ser excluído: ")
            produto = session.query(Produto).filter_by(id=pid).first()
            if not produto:
                print("Produto não encontrado.")
                return

            confirm = ler_str(f"Confirma exclusão de '{produto.nome}'? (s/n): ")
            if confirm.lower() != 's':
                print("Operação cancelada.")
                return

            session.delete(produto)
            session.commit()
            print("Produto excluído com sucesso!")
        except Exception as e:
            print("Erro ao excluir produto:", e)
            session.rollback()
