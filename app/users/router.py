from fastapi import APIRouter, Depends
from fastapi import Response

from app.exceptions import UserAlreadyExists, IncorrectLogin
from app.users.auth import get_password_hash, authenticate_user, create_access_token
from app.users.dao import UserDAO
from app.users.models import Users
from app.users.dependencies import current_user, current_adm_user
from app.users.schemas import SUserAuth

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


@router.post("/registration")
async def register_user(user_data: SUserAuth):
    existing_user = await UserDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExists
    hashed_password = get_password_hash(user_data.password)
    await UserDAO.insert_data(email=user_data.email, password=hashed_password)


@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise IncorrectLogin
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("booking_access_token", access_token, httponly=True)
    return access_token

@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("booking_access_token")

@router.get("/me")
async def me(current_user: Users = Depends(current_user)):
    return current_user

@router.get("/all")
async def all(current_user: Users = Depends(current_adm_user)):
    return await UserDAO.find_all()
