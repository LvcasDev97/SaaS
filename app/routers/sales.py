from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.core.database import get_db
from app.models.sale import Sale
from app.models.product import Product
from app.schemas.sale import SaleCreate, SaleRead

router = APIRouter(prefix="/sales", tags=["Sales"])

@router.post("/", response_model=SaleRead)
def criar_venda(venda: SaleCreate, db: Session = Depends(get_db)):
    produto = db.query(Product).filter(Product.id == venda.produto_id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    valor_total = produto.preco * venda.quantidade

    nova_venda = Sale(
        produto_id=venda.produto_id,
        quantidade=venda.quantidade,
        valor_total=valor_total,
        data_venda=func.now()   # preenchido automaticamente
    )
    db.add(nova_venda)
    db.commit()
    db.refresh(nova_venda)
    return nova_venda
