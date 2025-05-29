import sys
from banco import criar_banco, Session
from modelos.cliente import Cliente
from modelos.funcionario import Funcionario
from modelos.pet import Pet
from modelos.produto import Produto
from modelos.pedido import Pedido
from modelos.servico import Servico
from tratamento_de_erros import ler_int

def main():
    criar_banco()
    session = Session()
    try:
        while True:
            print("""
            ==== Sistema Petshop ====
            1 - Gerenciar Clientes
            2 - Gerenciar Funcionários
            3 - Gerenciar Pets
            4 - Gerenciar Produtos
            5 - Gerenciar Pedidos
            6 - Gerenciar Servico
            0 - Sair
            """)
            opcao = ler_int("Escolha uma opção: ")

            if opcao == 1:
                menu_clientes(session)
            elif opcao == 2:
                menu_funcionarios(session)
            elif opcao == 3:
                menu_pets(session)
            elif opcao == 4:
                menu_produtos(session)
            elif opcao == 5:
                menu_pedidos(session)
            elif opcao == 6:
                menu_servico(session)
            elif opcao == 0:
                print("Saindo...")
                break
            else:
                print("Opção inválida, tente novamente.")
    finally:
        session.close()
        sys.exit()

def menu_clientes(session):
    while True:
        print("""
        ==== Gerenciamento de Clientes ====
        1 - Inserir Cliente
        2 - Listar Clientes
        3 - Atualizar Cliente
        4 - Excluir Cliente
        5 - Listar Clientes por Produto
        0 - Voltar
        """)
        opcao = ler_int("Escolha uma opção: ")

        if opcao == 1:
            Cliente.inserir_cliente(session)
        elif opcao == 2:
            Cliente.listar_clientes(session)
        elif opcao == 3:
            Cliente.atualizar_cliente(session)
        elif opcao == 4:
            Cliente.excluir_cliente(session)
        elif opcao == 5:
            Cliente.listar_clientes_por_produto(session)
        elif opcao == 0:
            break
        else:
            print("Opção inválida, tente novamente.")

def menu_funcionarios(session):
    while True:
        print("""
        ==== Gerenciamento de Funcionários ====
        1 - Inserir Funcionário
        2 - Listar Funcionários
        3 - Atualizar Funcionário
        4 - Excluir Funcionário
        0 - Voltar
        """)
        opcao = ler_int("Escolha uma opção: ")

        if opcao == 1:
            Funcionario.inserir_funcionario(session)
        elif opcao == 2:
            Funcionario.listar_funcionarios(session)
        elif opcao == 3:
            Funcionario.atualizar_funcionario(session)
        elif opcao == 4:
            Funcionario.excluir_funcionario(session)
        elif opcao == 0:
            break
        else:
            print("Opção inválida, tente novamente.")

def menu_pets(session):
    while True:
        print("""
        ==== Gerenciamento de Pets ====
        1 - Inserir Pet
        2 - Listar Pets
        3 - Atualizar Pet
        4 - Excluir Pet
        0 - Voltar
        """)
        opcao = ler_int("Escolha uma opção: ")

        if opcao == 1:
            Pet.inserir_pet(session)
        elif opcao == 2:
            Pet.listar_pets(session)
        elif opcao == 3:
            Pet.atualizar_pet(session)
        elif opcao == 4:
            Pet.excluir_pet(session)
        elif opcao == 0:
            break
        else:
            print("Opção inválida, tente novamente.")

def menu_produtos(session):
    while True:
        print("""
        ==== Gerenciamento de Produtos ====
        1 - Inserir Produto
        2 - Listar Produtos
        3 - Atualizar Produto
        4 - Excluir Produto
        0 - Voltar
        """)
        opcao = ler_int("Escolha uma opção: ")

        if opcao == 1:
            Produto.inserir_produto(session)
        elif opcao == 2:
            Produto.listar_produtos(session)
        elif opcao == 3:
            Produto.atualizar_produto(session)
        elif opcao == 4:
            Produto.excluir_produto(session)
        elif opcao == 0:
            break
        else:
            print("Opção inválida, tente novamente.")

def menu_pedidos(session):
    while True:
        print("""
        ==== Gerenciamento de Pedidos ====
        1 - Inserir Pedido
        2 - Listar Pedidos
        3 - Cancelar Pedido
        4 - Listar Pedidos por Cliente
        5 - Listar Pedidos por Pet
        0 - Voltar
        """)
        opcao = ler_int("Escolha uma opção: ")

        if opcao == 1:
            Pedido.inserir_pedido(session)
        elif opcao == 2:
            Pedido.listar_pedidos(session)
        elif opcao == 3:
            Pedido.cancelar_pedido(session)
        elif opcao == 4:
            Pedido.listar_pedidos_por_cliente(session)
        elif opcao == 5:
            Pedido.listar_pedidos_por_pet(session)
        elif opcao == 0:
            break
        else:
            print("Opção inválida, tente novamente.")

def menu_servico(session):
    while True:
        print("""
        ==== Gerenciamento de Servico ====
        1 - Inserir Servico
        2 - Listar Servico
        0 - Voltar
        """)
        opcao = ler_int("Escolha uma opção: ")

        if opcao == 1:
            Servico.inserir_servico(session)
        elif opcao == 2:
            Servico.listar_servicos(session)
        elif opcao == 0:
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
