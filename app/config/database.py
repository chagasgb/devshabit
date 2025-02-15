from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:///banco.db"  # Caminho do banco de dados

# Criando o engine para conexão com o banco de dados
db = create_engine(DATABASE_URL)  # echo=True para log de SQL

# Criando a base para os modelos (comum a todos os modelos)
Base = declarative_base()

# Criando a fábrica de sessões para interagir com o banco
SessionLocal = sessionmaker(autoflush=False, bind=db)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()