import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


# ============================================================
# POSTGRESQL CONFIGURATION
# ============================================================
# You can set these values using environment variables.
#
# Default local PostgreSQL configuration:
#
# Database : labour_market_db
# User     : postgres
# Password : postgres
# Host     : localhost
# Port     : 5432
#
# Change the values if your PostgreSQL installation
# uses different credentials.
# ============================================================

POSTGRES_USER = os.getenv(
    "POSTGRES_USER",
    "postgres",
)

POSTGRES_PASSWORD = os.getenv(
    "POSTGRES_PASSWORD",
    "2760",
)

POSTGRES_HOST = os.getenv(
    "POSTGRES_HOST",
    "localhost",
)

POSTGRES_PORT = os.getenv(
    "POSTGRES_PORT",
    "5432",
)

POSTGRES_DB = os.getenv(
    "POSTGRES_DB",
    "labour_market_db",
)


# ============================================================
# DATABASE URL
# ============================================================

DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{POSTGRES_USER}:"
    f"{POSTGRES_PASSWORD}@"
    f"{POSTGRES_HOST}:"
    f"{POSTGRES_PORT}/"
    f"{POSTGRES_DB}"
)


# ============================================================
# SQLALCHEMY ENGINE
# ============================================================

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=300,
)


# ============================================================
# DATABASE SESSION
# ============================================================

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


# ============================================================
# BASE MODEL
# ============================================================

Base = declarative_base()


# ============================================================
# DATABASE DEPENDENCY
# ============================================================
# FastAPI routes will use this function to obtain a database
# session.
#
# Example:
#
# @router.get("/dashboard")
# def dashboard(db: Session = Depends(get_db)):
#     ...
# ============================================================

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()