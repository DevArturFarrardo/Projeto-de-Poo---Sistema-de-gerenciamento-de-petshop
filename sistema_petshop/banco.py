from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelos.base import Base

# engine e sessão ficam só aqui
engine = create_engine('sqlite:///petshop.db')
Session = sessionmaker(bind=engine)

def criar_banco():
    """
    Cria todas as tabelas definidas nos modelos herdados de Base.
    Atenção: antes de chamar, certifique-se de ter importado
    todos os seus models em algum lugar (ex: no main.py).
    """
    Base.metadata.create_all(engine)
