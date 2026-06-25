from app.auth.security import hash_senha
from app.core.database import SessionLocal
from app.core.settings import get_settings
from app.models import User

def seed_admin():
    settings = get_settings()
    db = SessionLocal()

    try:
        admin = db.query(User).filter(User.username == "admin").first()

        if not admin:
            admin = User(
                username="admin",
                password=hash_senha(settings.ADMIN_PASSWORD),
                is_superadmin=True,
            )
            db.add(admin)
            db.commit()
            db.refresh(admin)
            print("Admin criado com sucesso!")
        else:
            print("Admin já existe.")
    finally:
        db.close()

if __name__ == "__main__":
    seed_admin()
