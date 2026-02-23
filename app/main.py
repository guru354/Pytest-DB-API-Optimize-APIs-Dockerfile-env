from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app import models
from app.schemas import UserCreate

app = FastAPI(title="FastAPI Testing App")


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/users", status_code=200)
async def create_user(
    user: UserCreate,                      # ✅ BODY
    db: AsyncSession = Depends(get_db)
):
    new_user = models.User(
        name=user.name,
        email=user.email
    )

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return {
        "id": new_user.id,
        "name": new_user.name,
        "email": new_user.email
    }