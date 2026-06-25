from pydantic import BaseModel

class ProductBase(BaseModel):
    nome: str
    marca: str
    preco: float

class ProductCreate(ProductBase):
    pass

class ProductRead(ProductBase):
    id: int

    class Config:
        from_attributes = True
