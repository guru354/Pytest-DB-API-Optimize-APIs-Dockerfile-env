from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app import models

app = FastAPI(title="FastAPI Testing App")


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/users", status_code=201)
async def create_user(email: str, db: AsyncSession = Depends(get_db)):
    user = models.User(email=email)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return {"id": user.id, "email": user.email}