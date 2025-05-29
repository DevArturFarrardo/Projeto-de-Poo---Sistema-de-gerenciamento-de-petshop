import re
from abc import abstractmethod
from sqlalchemy import Column, Integer, String
from .base import Base

class Pessoa(Base):
    __abstract__ = True

    id     = Column(Integer, primary_key=True)
    _nome  = Column("nome", String,  nullable=False)
    _idade = Column("idade", Integer, nullable=False)
    _cpf   = Column("cpf",   String,  nullable=False, unique=True)

    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, valor: str):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("Nome não pode ficar em branco.")
        self._nome = valor.strip()

    @property
    def idade(self) -> int:
        return self._idade

    @idade.setter
    def idade(self, valor: int):
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("Idade deve ser um número inteiro não-negativo.")
        self._idade = valor

    @property
    def cpf(self) -> str:
        return self._cpf

    @cpf.setter
    def cpf(self, valor: str):
        if not isinstance(valor, str):
            raise ValueError("CPF deve ser uma string de 11 dígitos numéricos.")
        valor_filtrado = re.sub(r"\D", "", valor)
        if len(valor_filtrado) != 11:
            raise ValueError("CPF deve conter exatamente 11 dígitos numéricos.")
        self._cpf = valor_filtrado

    @abstractmethod
    def exibir_detalhes(self):
        pass
