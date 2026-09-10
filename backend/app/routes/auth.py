from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

from ..utils.auth_utils import (
    create_access_token,
    verify_token,
)


router = APIRouter()


# ============================================================
# DEMO USERS
# ============================================================

USERS = [
    {
        "id": 1,
        "name": "Government Planner",
        "email": "government@example.com",
        "password": "government123",
        "role": "government",
    },
    {
        "id": 2,
        "name": "Training Provider",
        "email": "training@example.com",
        "password": "training123",
        "role": "training_provider",
    },
    {
        "id": 3,
        "name": "Trainer",
        "email": "trainer@example.com",
        "password": "trainer123",
        "role": "trainer",
    },
    {
        "id": 4,
        "name": "Employer",
        "email": "employer@example.com",
        "password": "employer123",
        "role": "employer",
    },
    {
        "id": 5,
        "name": "Administrator",
        "email": "admin@example.com",
        "password": "admin123",
        "role": "admin",
    },
     {
        "id": 1,
        "name": "Ritesh",
        "email": "ritesh@gmail.com",
        "password": "123456",
        "role": "admin",
    },
    {
        "id": 2,
        "name": "Faculty User",
        "email": "faculty@example.com",
        "password": "faculty123",
        "role": "faculty",
    },
]


# ============================================================
# REQUEST MODELS
# ============================================================

class LoginRequest(BaseModel):
    email: str
    password: str


class RegisterRequest(BaseModel):
    name: str
    email: str
    password: str
    role: str = "student"


class TokenRequest(BaseModel):
    token: str


# ============================================================
# LOGIN
# ============================================================

@router.post("/login")
def login(request: LoginRequest):

    user = next(
        (
            user
            for user in USERS
            if user["email"].lower() == request.email.lower()
            and user["password"] == request.password
        ),
        None,
    )

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    access_token = create_access_token(
        data={
            "sub": str(user["id"]),
            "email": user["email"],
            "role": user["role"],
        }
    )

    return {
        "success": True,
        "message": "Login successful",
        "data": {
            "access_token": access_token,
            "token_type": "bearer",
            "user": {
                "id": user["id"],
                "name": user["name"],
                "email": user["email"],
                "role": user["role"],
            },
        },
    }


# ============================================================
# REGISTER
# ============================================================

@router.post("/register")
def register(request: RegisterRequest):

    existing_user = next(
        (
            user
            for user in USERS
            if user["email"].lower()
            == request.email.lower()
        ),
        None,
    )

    if existing_user is not None:
        raise HTTPException(
            status_code=400,
            detail="Email already registered",
        )

    new_id = (
        max(user["id"] for user in USERS) + 1
        if USERS
        else 1
    )

    new_user = {
        "id": new_id,
        "name": request.name,
        "email": request.email,
        "password": request.password,
        "role": request.role,
    }

    USERS.append(new_user)

    return {
        "success": True,
        "message": "Registration successful",
        "data": {
            "id": new_user["id"],
            "name": new_user["name"],
            "email": new_user["email"],
            "role": new_user["role"],
        },
    }


# ============================================================
# VERIFY TOKEN
# ============================================================

@router.post("/verify")
def verify_access_token(request: TokenRequest):

    payload = verify_token(request.token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token",
        )

    return {
        "success": True,
        "message": "Token is valid",
        "data": payload,
    }


# ============================================================
# CURRENT USER
# ============================================================

@router.post("/me")
def current_user(request: TokenRequest):

    payload = verify_token(request.token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token",
        )

    user_id = payload.get("sub")

    user = next(
        (
            user
            for user in USERS
            if str(user["id"]) == str(user_id)
        ),
        None,
    )

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    return {
        "success": True,
        "data": {
            "id": user["id"],
            "name": user["name"],
            "email": user["email"],
            "role": user["role"],
        },
    }


# ============================================================
# LOGOUT
# ============================================================

@router.post("/logout")
def logout():

    return {
        "success": True,
        "message": "Logout successful",
    }


# ============================================================
# AUTH STATUS
# ============================================================

@router.get("/status/check")
def auth_status():

    return {
        "success": True,
        "module": "auth",
        "status": "working",
    }