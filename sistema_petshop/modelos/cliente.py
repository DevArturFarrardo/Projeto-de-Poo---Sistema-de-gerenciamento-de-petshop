from sqlalchemy import Column, Integer, String, UniqueConstraint
from .pessoa import Pessoa
from tratamento_de_erros import ler_str, ler_int

class Cliente(Pessoa):
    __tablename__ = "clientes"
    __table_args__ = (
        UniqueConstraint('cpf', name='uq_clientes_cpf'),
    )

    contador_clientes = 0

    def __init__(self, nome: str, idade: int, cpf: str):
        super().__init__(nome, idade)
        self.cpf = cpf
        Cliente.contador_clientes += 1

    def exibir_detalhes(self):
        return f"""
        Cliente ID: {self.id}
        Nome: {self.nome}
        Idade: {self.idade}
        CPF: {self.cpf}
        """

    @classmethod
    def total_clientes(cls):
        return cls.contador_clientes

    @staticmethod
    def inserir_cliente(session):
        try:
            nome = ler_str("Nome do cliente: ")
            idade = ler_int("Idade do cliente: ")
            cpf   = ler_str("CPF (somente números): ")
            cliente = Cliente(nome, idade, cpf)
            session.add(cliente)
            session.commit()
            print("Cliente inserido com sucesso!")
        except Exception as e:
            print("Erro ao inserir cliente:", e)
            session.rollback()

    @staticmethod
    def listar_clientes(session):
        clientes = session.query(Cliente).all()
        if not clientes:
            print("Nenhum cliente cadastrado.")
            return
        for c in clientes:
            print(c.exibir_detalhes())

    @staticmethod
    def atualizar_cliente(session):
        Cliente.listar_clientes(session)
        try:
            cliente_id = ler_int("ID do cliente a ser atualizado: ")
            cliente = session.query(Cliente).filter_by(id=cliente_id).first()
            if not cliente:
                print("Cliente não encontrado.")
                return

            print("\nDeixe em branco para manter o valor atual.")
            nome = ler_str(f"Nome atual ({cliente.nome}): ", allow_blank=True, default=cliente.nome)
            idade = ler_int(f"Idade atual ({cliente.idade}): ", allow_blank=True, default=cliente.idade)
            cpf   = ler_str(f"CPF atual ({cliente.cpf}): ", allow_blank=True, default=cliente.cpf)

            cliente.nome = nome
            cliente.idade = idade
            cliente.cpf = cpf
            session.commit()
            print("Cliente atualizado com sucesso!")
        except Exception as e:
            print("Erro ao atualizar cliente:", e)
            session.rollback()

    @staticmethod
    def excluir_cliente(session):
        Cliente.listar_clientes(session)
        try:
            cliente_id = ler_int("ID do cliente a ser excluído: ")
            cliente = session.query(Cliente).filter_by(id=cliente_id).first()
            if not cliente:
                print("Cliente não encontrado.")
                return

            session.delete(cliente)
            session.commit()
            print("Cliente excluído com sucesso!")
        except Exception as e:
            print("Erro ao excluir cliente:", e)
            session.rollback()

    @staticmethod
    def listar_clientes_por_produto(session):
        from .pedido import Pedido
        from .produto import Produto

        Produto.listar_produtos(session)
        produto_id = ler_int("ID do produto para filtrar clientes: ")
        produto = session.query(Produto).filter_by(id=produto_id).first()
        if not produto:
            print("Produto não encontrado.")
            return

        print(f"\nClientes que compraram o produto {produto.nome}:")
        pedidos = session.query(Pedido).filter_by(produto_id=produto.id).all()
        if not pedidos:
            print("Nenhum pedido encontrado para este produto.")
            return

        for pedido in pedidos:
            print(pedido.cliente.exibir_detalhes())
