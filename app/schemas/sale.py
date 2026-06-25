from pydantic import BaseModel
from datetime import datetime

class SaleBase(BaseModel):
    produto_id: int
    quantidade: int

class SaleCreate(SaleBase):
    pass

class SaleRead(SaleBase):
    id: int
    valor_total: float
    data_venda: datetime

    class Config:
        from_attributes = True
