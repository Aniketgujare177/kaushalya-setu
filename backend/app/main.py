from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# ============================================================
# ROUTES
# ============================================================

from .routes import jobs
from .routes import skills
from .routes import students
from .routes import dashboard
from .routes import skill_gap
from .routes import employers
from .routes import recommendations
from .routes import training
from .routes import reports
from .routes import notifications
from .routes import auth
from .routes import industries
from .routes import curriculum
from .routes import health


# ============================================================
# FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="Smart Labour Market Intelligence Platform",
    description=(
        "Backend API for the Smart Labour Market Intelligence "
        "and Curriculum Alignment Platform"
    ),
    version="1.0.0",
)


# ============================================================
# CORS
# ============================================================
# Development configuration.
# Allows React/Vite frontend to communicate with FastAPI.
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# ROOT
# ============================================================

@app.get("/")
def root():
    return {
        "success": True,
        "platform": "Smart Labour Market Intelligence Platform",
        "problem_statement": "SIH 26134",
        "status": "Backend is running",
    }


# ============================================================
# HEALTH CHECK
# ============================================================

@app.get("/api/health")
def health_check():
    return {
        "success": True,
        "status": "healthy",
        "service": "FastAPI",
    }


# ============================================================
# SYSTEM STATUS
# ============================================================

@app.get("/api/system/status")
def system_status():
    return {
        "success": True,

        "backend": {
            "name": "FastAPI",
            "status": "online",
        },

        "database": {
            "name": "PostgreSQL",
            "status": "not configured",
        },

        "frontend": {
            "name": "React / Vite",
            "status": "ready",
        },
    }


# ============================================================
# API INFORMATION
# ============================================================

@app.get("/api")
def api_info():
    return {
        "success": True,
        "name": "Smart Labour Market Intelligence API",
        "version": "1.0.0",

        "modules": [
            "dashboard",
            "jobs",
            "skills",
            "students",
            "curriculum",
            "skill-gap",
            "employers",
            "recommendations",
            "training",
            "reports",
            "notifications",
            "authentication",
            "industries",
            "health",
        ],
    }


# ============================================================
# HEALTH ROUTER
# ============================================================

app.include_router(
    health.router,
    prefix="/api/health",
    tags=["Health"],
)


# ============================================================
# JOBS
# ============================================================

app.include_router(
    jobs.router,
    prefix="/api/jobs",
    tags=["Jobs"],
)


# ============================================================
# SKILLS
# ============================================================

app.include_router(
    skills.router,
    prefix="/api/skills",
    tags=["Skills"],
)


# ============================================================
# STUDENTS
# ============================================================

app.include_router(
    students.router,
    prefix="/api/students",
    tags=["Students"],
)


# ============================================================
# DASHBOARD
# ============================================================

app.include_router(
    dashboard.router,
    prefix="/api/dashboard",
    tags=["Dashboard"],
)


# ============================================================
# SKILL GAP
# ============================================================

app.include_router(
    skill_gap.router,
    prefix="/api/skill-gap",
    tags=["Skill Gap Analysis"],
)


# ============================================================
# EMPLOYERS
# ============================================================

app.include_router(
    employers.router,
    prefix="/api/employers",
    tags=["Employers"],
)


# ============================================================
# RECOMMENDATIONS
# ============================================================

app.include_router(
    recommendations.router,
    prefix="/api/recommendations",
    tags=["Recommendations"],
)


# ============================================================
# TRAINING
# ============================================================

app.include_router(
    training.router,
    prefix="/api/training",
    tags=["Training"],
)


# ============================================================
# REPORTS
# ============================================================

app.include_router(
    reports.router,
    prefix="/api/reports",
    tags=["Reports"],
)


# ============================================================
# NOTIFICATIONS
# ============================================================

app.include_router(
    notifications.router,
    prefix="/api/notifications",
    tags=["Notifications"],
)


# ============================================================
# AUTHENTICATION
# ============================================================

app.include_router(
    auth.router,
    prefix="/api/auth",
    tags=["Authentication"],
)


# ============================================================
# INDUSTRIES
# ============================================================

app.include_router(
    industries.router,
    prefix="/api/industries",
    tags=["Industries"],
)


# ============================================================
# CURRICULUM
# ============================================================

app.include_router(
    curriculum.router,
    prefix="/api/curriculum",
    tags=["Curriculum"],
)


# ============================================================
# STARTUP MESSAGE
# ============================================================

@app.on_event("startup")
async def startup_event():
    print("=" * 60)
    print("SMART LABOUR MARKET INTELLIGENCE PLATFORM")
    print("=" * 60)
    print("Backend: FastAPI")
    print("Database: Not connected yet")
    print("Authentication: Demo mode")
    print("API: http://127.0.0.1:8000")
    print("Docs: http://127.0.0.1:8000/docs")
    print("=" * 60)