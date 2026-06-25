from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.core.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    marca = Column(String, nullable=False)
    preco = Column(Float, nullable=False)

    # Relacionamento com vendas
    vendas = relationship("Sale", back_populates="produto")
