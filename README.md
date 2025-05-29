# Documentação: Sistema de Gerenciamento de Petshop

## Visão Geral

O **Sistema de Gerenciamento de Petshop** é uma aplicação de linha de comando desenvolvida em Python, que utiliza o paradigma de Programação Orientada a Objetos (POO) e o SQLAlchemy ORM para realizar operações de cadastro, consulta, atualização e remoção de clientes, pets, funcionários, produtos, serviços e pedidos em um petshop.

## Tecnologias Utilizadas

* **Linguagem de Programação:** Python 3.8+
* **ORM:** SQLAlchemy
* **Banco de Dados:** SQLite (arquivo `petshop.db`)

## Estrutura do Projeto

```
Projeto-Petshop/
├── sistema_petshop/
│   ├── banco.py                 # Criação de engine e sessão do SQLAlchemy
│   ├── tratamento_de_erros.py    # Funções utilitárias para leitura e validação de entrada
│   ├── main.py                  # Interface de menu e fluxo principal da aplicação
│   └── modelos/                 # Modelos de dados (classes e mapeamento ORM)
│       ├── base.py              # Definição da classe Base do SQLAlchemy
│       ├── pessoa.py            # Classe abstrata Pessoa
│       ├── cliente.py           # Modelo Cliente
│       ├── funcionario.py       # Modelo Funcionario
│       ├── pet.py               # Modelo Pet
│       ├── produto.py           # Modelo Produto
│       ├── servico.py           # Modelo Servico
│       └── pedido.py            # Modelo Pedido
└── petshop.db                   # Banco de dados SQLite (criado na primeira execução)
```

## Modelagem de Classes

### 1. Base

* **Descrição:** Classe base declarativa do SQLAlchemy (`declarative_base()`), usada como superclasse para todos os modelos.

### 2. Pessoa (abstrata)

* **Atributos protegidos:**

  * `id` (Integer, PK)
  * `_nome` (String)
  * `_idade` (Integer)
  * `_cpf` (String, único)
* **Métodos:**

  * `nome` (getter/setter)
  * `idade` (getter/setter)
  * `cpf` (getter/setter com validação de 11 dígitos)
  * `exibir_detalhes()` (método abstrato a ser implementado pelas subclasses)

### 3. Cliente (herda Pessoa)

* **Tabela:** `clientes`
* **Atributos adicionais:** `cpf` (validação e unicidade)
* **Métodos estáticos:**

  * `inserir_cliente(session)`
  * `listar_clientes(session)`
  * `atualizar_cliente(session)`
  * `excluir_cliente(session)`
  * `listar_clientes_por_produto(session)`
  * `exibir_detalhes(self)`

### 4. Funcionario (herda Pessoa)

* **Tabela:** `funcionarios`
* **Atributos adicionais:**

  * `departamento` (String)
* **Métodos estáticos:**

  * `inserir_funcionario(session)`
  * `listar_funcionarios(session)`
  * `atualizar_funcionario(session)`
  * `excluir_funcionario(session)`
  * `total_funcionarios(cls)`
  * `exibir_detalhes(self)`

### 5. Pet

* **Tabela:** `pets`
* **Atributos:**

  * `nome`, `especie`, `raca`, `idade`, `cliente_id` (FK para `clientes.id`)
* **Métodos estáticos:**

  * `inserir_pet(session)`
  * `listar_pets(session)`
  * `atualizar_pet(session)`
  * `excluir_pet(session)`
  * `exibir_detalhes(self)`

### 6. Produto

* **Tabela:** `produtos`
* **Atributos:** `nome` (String), `preco` (Float)
* **Métodos estáticos:**

  * `inserir_produto(session)`
  * `listar_produtos(session)`
  * `atualizar_produto(session)`
  * `excluir_produto(session)`
  * `exibir_detalhes(self)`

### 7. Servico

* **Tabela:** `servicos`
* **Atributos:** `descricao` (String), `preco` (Float)
* **Métodos estáticos:**

  * `inserir_servico(session)`
  * `listar_servicos(session)`
  * `exibir_detalhes(self)`

### 8. Pedido

* **Tabela:** `pedidos`
* **Atributos:**

  * `cliente_id` (FK para `clientes.id`)
  * `pet_id` (FK para `pets.id`, opcional)
  * `produto_id` (FK para `produtos.id`, opcional)
  * `servico_id` (FK para `servicos.id`, opcional)
* **Métodos estáticos:**

  * `inserir_pedido(session)`
  * `listar_pedidos(session)`
  * `cancelar_pedido(session)`
  * `listar_pedidos_por_cliente(session)`
  * `listar_pedidos_por_pet(session)`
  * `exibir_detalhes(self)`

## Funcionalidades do Sistema

* Menu principal com opções para gerenciar:

  1. Clientes
  2. Pets
  3. Produtos
  4. Serviços
  5. Funcionários
  6. Pedidos
  7. Sair
* Cada submenu permite inserção, listagem, atualização e remoção de registros.
* Filtros específicos: listar clientes por produto, pedidos por cliente ou pet.
* Validação de entradas (strings, inteiros, floats) para evitar erros de formato.
* Persistência de dados via SQLite e SQLAlchemy.

## Como Executar o Projeto

1. **Clone o repositório:**

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd Projeto-Petshop
   ```

2. **Instale as dependências:**

   ```bash
   pip install sqlalchemy
   ```

3. **Execute o sistema:**

   ```bash
   python sistema_petshop/main.py
   ```

4. **Na primeira execução**, o arquivo `petshop.db` e as tabelas serão criados automaticamente.

## Considerações Finais

Este projeto demonstra aplicação de conceitos de POO e ORM em um cenário prático de gerenciamento de petshop.
