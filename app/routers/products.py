from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductRead

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/", response_model=ProductRead)
def criar_produto(produto: ProductCreate, db: Session = Depends(get_db)):
    novo_produto = Product(
        nome=produto.nome,
        marca=produto.marca,   # agora obrigatório
        preco=produto.preco
    )
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    return novo_produto
