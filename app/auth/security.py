from passlib.context import CryptContext

# Configuração do hash com Argon2
pwd_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto"
)

MAX_PASSWORD_LENGTH = 1024

def validar_senha(senha: str) -> str:
    if not isinstance(senha, str):
        raise TypeError("Senha deve ser uma string")

    if not senha.strip():
        raise ValueError("Senha não pode ser vazia")

    if len(senha) > MAX_PASSWORD_LENGTH:
        raise ValueError("Senha muito longa")

    return senha

def hash_senha(senha: str) -> str:
    senha = validar_senha(senha)
    return pwd_context.hash(senha)

def verificar_senha(senha: str, senha_hash: str) -> bool:
    senha = validar_senha(senha)
    try:
        return pwd_context.verify(senha, senha_hash)
    except Exception:
        return False

def precisa_rehash(senha_hash: str) -> bool:
    try:
        return pwd_context.needs_update(senha_hash)
    except Exception:
        return True
