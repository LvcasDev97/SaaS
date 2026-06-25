from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from app.core.settings import get_settings

settings = get_settings()

def criar_token(data: dict) -> str:
    dados = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    dados.update({"exp": expire})
    token = jwt.encode(dados, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return token

def validar_token(token: str) -> dict | None:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        return None
