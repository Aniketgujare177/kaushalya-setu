from fastapi import APIRouter

router = APIRouter()


# ============================================================
# HEALTH CHECK
# ============================================================

@router.get("/")
def health_check():
    return {
        "success": True,
        "status": "healthy",
        "message": "Backend API is running",
    }


# ============================================================
# API STATUS
# ============================================================

@router.get("/status")
def api_status():
    return {
        "success": True,
        "service": "Labour Market Alignment API",
        "status": "online",
    }


# ============================================================
# MODULE STATUS
# ============================================================

@router.get("/status/check")
def health_status():
    return {
        "success": True,
        "module": "health",
        "status": "working",
    }