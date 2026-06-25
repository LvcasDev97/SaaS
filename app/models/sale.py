from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    produto_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantidade = Column(Integer, nullable=False)
    valor_total = Column(Float, nullable=False)
    data_venda = Column(DateTime, default=func.now())

    # Relacionamento com produto
    produto = relationship("Product", back_populates="vendas")
