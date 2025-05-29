from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from .cliente import Cliente
from .pet import Pet
from .produto import Produto
from .servico import Servico
from tratamento_de_erros import ler_int

class Pedido(Base):
    __tablename__ = "pedidos"

    id         = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    pet_id     = Column(Integer, ForeignKey("pets.id"),     nullable=True)
    produto_id = Column(Integer, ForeignKey("produtos.id"), nullable=True)
    servico_id = Column(Integer, ForeignKey("servicos.id"), nullable=True)

    cliente = relationship("Cliente", backref="pedidos")
    pet     = relationship("Pet",     backref="pedidos")
    produto = relationship("Produto", backref="pedidos")
    servico = relationship("Servico", backref="pedidos")

    def __init__(self, cliente, pet=None, produto=None, servico=None):
        self.cliente = cliente
        self.pet     = pet
        self.produto = produto
        self.servico = servico

    def exibir_detalhes(self):
        partes = [
            f"Pedido ID: {self.id}",
            f"Cliente: {self.cliente.nome} (ID: {self.cliente.id})",
        ]
        if self.pet:
            partes.append(f"Pet: {self.pet.nome} (ID: {self.pet.id})")
        if self.servico:
            partes.append(f"Serviço: {self.servico.nome} (ID: {self.servico.id})")
        if self.produto:
            partes.append(f"Produto: {self.produto.nome} (ID: {self.produto.id})")
        return "\n".join(partes)

    @staticmethod
    def inserir_pedido(session):
        try:
            Cliente.listar_clientes(session)
            cid = ler_int("ID do cliente que faz o pedido: ")
            cliente = session.query(Cliente).get(cid)
            if not cliente:
                print("Cliente não encontrado.")
                return

            print("Tipo de pedido:")
            print(" 1 - Produto")
            print(" 2 - Serviço (vinculado a um pet)")
            tipo = input("Escolha 1 ou 2: ").strip()

            produto = None
            servico = None
            pet     = None

            if tipo == "1":
                Produto.listar_produtos(session)
                prid = ler_int("ID do produto: ")
                produto = session.query(Produto).get(prid)
                if not produto:
                    print("Produto não encontrado.")
                    return

            elif tipo == "2":
                Pet.listar_pets(session)
                pid = ler_int("ID do pet para o serviço: ")
                pet = session.query(Pet).get(pid)
                if not pet:
                    print("Pet não encontrado.")
                    return

                Servico.listar_servicos(session)
                sid = ler_int("ID do serviço: ")
                servico = session.query(Servico).get(sid)
                if not servico:
                    print("Serviço não encontrado.")
                    return

            else:
                print("Opção inválida.")
                return

            pedido = Pedido(cliente, pet=pet, produto=produto, servico=servico)
            session.add(pedido)
            session.commit()
            print("Pedido inserido com sucesso!")

        except Exception as e:
            print("Erro ao inserir pedido:", e)
            session.rollback()

    @staticmethod
    def listar_pedidos(session):
        pedidos = session.query(Pedido).all()
        if not pedidos:
            print("Nenhum pedido cadastrado.")
            return
        for p in pedidos:
            print(p.exibir_detalhes())

    @staticmethod
    def cancelar_pedido(session):
        Pedido.listar_pedidos(session)
        try:
            pid = ler_int("ID do pedido a ser cancelado: ")
            pedido = session.query(Pedido).get(pid)
            if not pedido:
                print("Pedido não encontrado.")
                return

            session.delete(pedido)
            session.commit()
            print("Pedido cancelado com sucesso!")
        except Exception as e:
            print("Erro ao cancelar pedido:", e)
            session.rollback()

    @staticmethod
    def listar_pedidos_por_cliente(session):
        Cliente.listar_clientes(session)
        cid = ler_int("ID do cliente para listar pedidos: ")
        cliente = session.query(Cliente).get(cid)
        if not cliente:
            print("Cliente não encontrado.")
            return

        print(f"\nPedidos para o cliente {cliente.nome}:")
        pedidos = session.query(Pedido).filter_by(cliente_id=cliente.id).all()
        if not pedidos:
            print("Nenhum pedido para este cliente.")
            return

        for pedido in pedidos:
            print(f"Pedido ID: {pedido.id}")
            print(f"  Cliente: {pedido.cliente.nome} (ID: {pedido.cliente.id})")
            print(f"  Pet: {pedido.pet.nome if pedido.pet else '—'}")
            if pedido.servico:
                print(f"  Serviço: {pedido.servico.nome} — R$ {pedido.servico.preco:.2f}")
            if pedido.produto:
                print(f"  Produto: {pedido.produto.nome} — R$ {pedido.produto.preco:.2f}")
            print("-" * 40)

    @staticmethod
    def listar_pedidos_por_pet(session):
        Pet.listar_pets(session)
        pet_id = ler_int("ID do pet para listar pedidos: ")
        pet = session.query(Pet).get(pet_id)
        if not pet:
            print("Pet não encontrado.")
            return

        print(f"\nPedidos para o pet {pet.nome}:")
        pedidos = session.query(Pedido).filter_by(pet_id=pet.id).all()
        if not pedidos:
            print("Nenhum pedido para este pet.")
            return

        for pedido in pedidos:
            print(f"Pedido ID: {pedido.id}")
            print(f"  Cliente: {pedido.cliente.nome} (ID: {pedido.cliente.id})")
            print(f"  Pet: {pedido.pet.nome} (ID: {pedido.pet.id})")
            if pedido.servico:
                print(f"  Serviço: {pedido.servico.nome} (ID: {pedido.servico.id}) — R$ {pedido.servico.preco:.2f}")
            else:
                print("  Serviço: —")
            if pedido.produto:
                print(f"  Produto: {pedido.produto.nome} (ID: {pedido.produto.id}) — R$ {pedido.produto.preco:.2f}")
            print("-" * 40)