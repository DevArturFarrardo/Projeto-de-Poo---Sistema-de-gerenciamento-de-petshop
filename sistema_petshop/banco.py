from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelos.base import Base

engine = create_engine('sqlite:///petshop.db')
Session = sessionmaker(bind=engine)

def criar_banco():
    Base.metadata.create_all(engine)
