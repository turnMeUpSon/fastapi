from typing import List
from uuid import UUID

from fastapi import FastAPI
from fastapi import HTTPException

from models import Gender
from models import Role
from models import User
from models import userUpdateRequest

app = FastAPI()

db: List[User] = [
    User(
        first_name='Jan',
        last_name='Miller',
        gender=Gender.male,
        roles=[Role.admin],
    ),
    User(
        first_name='Arthur',
        last_name='Miller',
        gender=Gender.male,
        roles=[Role.student],
    ),
    User(
        first_name='Alexey',
        last_name='Krokhin',
        gender=Gender.male,
        roles=[Role.user],
    ),
    User(
        first_name='Maxim',
        last_name='Krutonog',
        gender=Gender.male,
        roles=[Role.user],
    ),
]


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.get("/api/v1/users")
async def fetch_users():
    return db


@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist",
    )


@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: userUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.roles is not None:
                user.roles = user_update.roles
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist",
    )
