from sqlalchemy import Column, Integer, String
from .base import Base
from tratamento_de_erros import ler_str, ler_int

class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)
    especie = Column(String, nullable=False)
    contador_pets = 0

    def __init__(self, nome: str, idade: int, especie: str):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        Pet.contador_pets += 1

    def exibir_detalhes(self):
        return f"""
        Pet ID: {self.id}
        Nome: {self.nome}
        Idade: {self.idade}
        Espécie: {self.especie}
        """

    @classmethod
    def total_pets(cls):
        return cls.contador_pets

    @staticmethod
    def inserir_pet(session):
        try:
            nome = ler_str("Nome do pet: ")
            idade = ler_int("Idade do pet: ")
            especie = ler_str("Espécie do pet: ")
            pet = Pet(nome, idade, especie)
            session.add(pet)
            session.commit()
            print("Pet inserido com sucesso!")
        except Exception as e:
            print("Erro ao inserir pet:", e)
            session.rollback()

    @staticmethod
    def listar_pets(session):
        pets = session.query(Pet).all()
        if not pets:
            print("Nenhum pet cadastrado.")
            return
        for p in pets:
            print(p.exibir_detalhes())

    @staticmethod
    def atualizar_pet(session):
        Pet.listar_pets(session)
        try:
            pet_id = ler_int("ID do pet a ser atualizado: ")
            pet = session.query(Pet).filter_by(id=pet_id).first()
            if not pet:
                print("Pet não encontrado.")
                return

            print("\nDeixe em branco para manter o valor atual.")
            nome = ler_str(f"Nome atual ({pet.nome}): ", allow_blank=True, default=pet.nome)
            idade = ler_int(f"Idade atual ({pet.idade}): ", allow_blank=True, default=pet.idade)
            especie = ler_str(f"Espécie atual ({pet.especie}): ", allow_blank=True, default=pet.especie)

            pet.nome = nome
            pet.idade = idade
            pet.especie = especie
            session.commit()
            print("Pet atualizado com sucesso!")
        except Exception as e:
            print("Erro ao atualizar pet:", e)
            session.rollback()

    @staticmethod
    def excluir_pet(session):
        Pet.listar_pets(session)
        try:
            pet_id = ler_int("ID do pet a ser excluído: ")
            pet = session.query(Pet).filter_by(id=pet_id).first()
            if not pet:
                print("Pet não encontrado.")
                return

            session.delete(pet)
            session.commit()
            print("Pet excluído com sucesso!")
        except Exception as e:
            print("Erro ao excluir pet:", e)
            session.rollback()
