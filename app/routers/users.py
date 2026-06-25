from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.user import User
from app.auth.security import hash_senha, verificar_senha
from app.schemas.user import UserCreate, UserRead, UserLogin

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserRead)
def criar_usuario(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.username == user.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Usuário já existe")

    novo_user = User(username=user.username, password=hash_senha(user.password))
    db.add(novo_user)
    db.commit()
    db.refresh(novo_user)
    return novo_user

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    usuario = db.query(User).filter(User.username == user.username).first()
    if not usuario or not verificar_senha(user.password, usuario.password):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    # Sem token, apenas mensagem de sucesso
    return {"msg": f"Login realizado com sucesso para {usuario.username}"}

@router.get("/", response_model=list[UserRead])
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(User).all()
