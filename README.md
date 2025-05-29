
# Documentação: Sistema de Gerenciamento de Petshop

## Visão Geral

Este projeto é um sistema de gerenciamento para um petshop, desenvolvido utilizando os princípios da Programação Orientada a Objetos (POO) em Python. O sistema visa gerenciar clientes, pets, serviços oferecidos e agendamentos, proporcionando uma interface intuitiva para os usuários.

## Tecnologias Utilizadas

- Linguagem de Programação: Python
- Banco de Dados: SQLite (arquivo `petshop.db`)
- Paradigma: Programação Orientada a Objetos (POO)

## Estrutura do Projeto

O projeto possui a seguinte estrutura de diretórios e arquivos:

Projeto-de-Poo---Sistema-de-gerenciamento-de-petshop/
├── sistema_petshop/
│   ├── __init__.py
│   ├── cliente.py
│   ├── pet.py
│   ├── servico.py
│   ├── agendamento.py
│   └── main.py
├── petshop.db
└── README.md

Descrição dos principais arquivos:

- `cliente.py`: Contém a classe `Cliente`, responsável por armazenar e gerenciar informações dos clientes do petshop.
- `pet.py`: Define a classe `Pet`, que representa os animais de estimação dos clientes.
- `servico.py`: Inclui a classe `Servico`, que descreve os serviços oferecidos pelo petshop, como banho, tosa, etc.
- `agendamento.py`: Implementa a classe `Agendamento`, que gerencia os agendamentos de serviços para os pets.
- `main.py`: Arquivo principal que integra todas as funcionalidades e fornece a interface para interação com o usuário.

## Modelagem de Classes

O sistema é composto pelas seguintes classes principais:

### 1. Cliente

Representa os clientes do petshop.

Atributos:
- `id`: Identificador único do cliente.
- `nome`: Nome completo do cliente.
- `telefone`: Número de telefone para contato.
- `email`: Endereço de e-mail do cliente.

Métodos:
- `cadastrar_cliente()`: Cadastra um novo cliente no sistema.
- `editar_cliente()`: Edita as informações de um cliente existente.
- `remover_cliente()`: Remove um cliente do sistema.

### 2. Pet

Representa os animais de estimação dos clientes.

Atributos:
- `id`: Identificador único do pet.
- `nome`: Nome do pet.
- `especie`: Espécie do animal (cão, gato, etc.).
- `raca`: Raça do pet.
- `idade`: Idade do pet.
- `id_cliente`: Referência ao proprietário do pet.

Métodos:
- `cadastrar_pet()`: Adiciona um novo pet ao sistema.
- `editar_pet()`: Atualiza as informações de um pet existente.
- `remover_pet()`: Remove um pet do sistema.

### 3. Servico

Define os serviços oferecidos pelo petshop.

Atributos:
- `id`: Identificador único do serviço.
- `descricao`: Descrição do serviço (banho, tosa, etc.).
- `preco`: Preço do serviço.

Métodos:
- `cadastrar_servico()`: Adiciona um novo serviço ao sistema.
- `editar_servico()`: Atualiza as informações de um serviço existente.
- `remover_servico()`: Remove um serviço do sistema.

### 4. Agendamento

Gerencia os agendamentos de serviços para os pets.

Atributos:
- `id`: Identificador único do agendamento.
- `id_pet`: Referência ao pet que receberá o serviço.
- `id_servico`: Referência ao serviço agendado.
- `data_hora`: Data e hora do agendamento.

Métodos:
- `agendar_servico()`: Cria um novo agendamento.
- `editar_agendamento()`: Modifica um agendamento existente.
- `cancelar_agendamento()`: Cancela um agendamento.

## Funcionalidades do Sistema

- Cadastro de Clientes: Permite adicionar, editar e remover clientes.
- Cadastro de Pets: Associa pets aos seus respectivos donos, com possibilidade de edição e remoção.
- Gerenciamento de Serviços: Adiciona, edita e remove serviços oferecidos pelo petshop.
- Agendamentos: Agenda serviços para os pets, com controle de data e hora.
- Persistência de Dados: Utiliza SQLite para armazenar e gerenciar os dados de forma eficiente.

## Como Executar o Projeto

1. Clone o repositório:

   git clone https://github.com/DevArturFarrardo/Projeto-de-Poo---Sistema-de-gerenciamento-de-petshop.git
   cd Projeto-de-Poo---Sistema-de-gerenciamento-de-petshop

2. Instale as dependências:

   Certifique-se de que o Python 3 está instalado em sua máquina.

3. Execute o sistema:

   python sistema_petshop/main.py

## Considerações Finais

Este sistema foi desenvolvido com o objetivo de aplicar conceitos de Programação Orientada a Objetos em um cenário prático. A utilização de classes bem definidas e a separação de responsabilidades facilitam a manutenção e a escalabilidade do projeto. Futuramente, podem ser adicionadas funcionalidades como autenticação de usuários, geração de relatórios e uma interface gráfica para melhorar a experiência do usuário.
