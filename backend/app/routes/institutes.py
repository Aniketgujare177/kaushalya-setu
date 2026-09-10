from fastapi import APIRouter, Depends
from fastapi.security import HTTPAuthorizationCredentials
from app.utils.auth_utils import security, verify_token

router = APIRouter(
    prefix="/institutes",
    tags=["Institutes"]
)


@router.get("/")
def get_institutes(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    user = verify_token(credentials)

    return {
        "message": "Institutes API is protected",
        "user": user,
        "institutes": []
    }


@router.get("/{institute_id}")
def get_institute(
    institute_id: int,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    user = verify_token(credentials)

    return {
        "message": "Institute API is protected",
        "user": user,
        "institute_id": institute_id
    }


@router.get("/{institute_id}/courses")
def get_institute_courses(
    institute_id: int,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    user = verify_token(credentials)

    return {
        "user": user,
        "institute_id": institute_id,
        "courses": []
    }