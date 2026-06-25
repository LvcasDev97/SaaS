from sqlalchemy.orm import Session
from app.models.sale import Sale
from app.models.product import Product

def criar_venda(produto_id: int, quantidade: int, db: Session):
    produto = db.query(Product).filter(Product.id == produto_id).first()
    if not produto:
        raise ValueError("Produto não encontrado")
    if produto.quantidade < quantidade:
        raise ValueError("Estoque insuficiente")

    produto.quantidade -= quantidade
    valor_total = produto.preco * quantidade

    venda = Sale(produto_id=produto_id, quantidade=quantidade, valor_total=valor_total)
    db.add(venda)
    db.commit()
    db.refresh(venda)
    return venda
