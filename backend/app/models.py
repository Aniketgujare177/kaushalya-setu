from datetime import datetime

from sqlalchemy import (
    Boolean,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base


# ============================================================
# LOCATION
# ============================================================

class Location(Base):
    __tablename__ = "locations"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    state: Mapped[str] = mapped_column(
        String(100),
        index=True,
    )

    district: Mapped[str] = mapped_column(
        String(100),
        index=True,
    )

    city: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    demands = relationship(
        "JobDemand",
        back_populates="location",
    )

    candidates = relationship(
        "Candidate",
        back_populates="location",
    )


# ============================================================
# INDUSTRY SECTOR
# ============================================================

class Sector(Base):
    __tablename__ = "sectors"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        index=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    growth_rate: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    job_demands = relationship(
        "JobDemand",
        back_populates="sector",
    )

    employers = relationship(
        "Employer",
        back_populates="sector",
    )


# ============================================================
# JOB ROLE
# ============================================================

class JobRole(Base):
    __tablename__ = "job_roles"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(150),
        index=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    sector_id: Mapped[int | None] = mapped_column(
        ForeignKey("sectors.id"),
        nullable=True,
    )

    required_experience: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    average_salary: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    sector = relationship(
        "Sector",
    )

    job_demands = relationship(
        "JobDemand",
        back_populates="job_role",
    )


# ============================================================
# SKILL
# ============================================================

class Skill(Base):
    __tablename__ = "skills"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        index=True,
    )

    category: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    is_emerging: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    is_obsolete: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    demand_records = relationship(
        "SkillDemand",
        back_populates="skill",
    )

    gap_records = relationship(
        "SkillGap",
        back_populates="skill",
    )


# ============================================================
# JOB MARKET DEMAND
# ============================================================

class JobDemand(Base):
    __tablename__ = "job_demands"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    job_role_id: Mapped[int] = mapped_column(
        ForeignKey("job_roles.id"),
        index=True,
    )

    sector_id: Mapped[int] = mapped_column(
        ForeignKey("sectors.id"),
        index=True,
    )

    location_id: Mapped[int] = mapped_column(
        ForeignKey("locations.id"),
        index=True,
    )

    posting_count: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    growth_rate: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    salary_min: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    salary_max: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    demand_level: Mapped[str] = mapped_column(
        String(50),
        default="Medium",
    )

    period: Mapped[str] = mapped_column(
        String(30),
        index=True,
    )

    source: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    job_role = relationship(
        "JobRole",
        back_populates="job_demands",
    )

    sector = relationship(
        "Sector",
        back_populates="job_demands",
    )

    location = relationship(
        "Location",
        back_populates="demands",
    )


# ============================================================
# SKILL DEMAND
# ============================================================

class SkillDemand(Base):
    __tablename__ = "skill_demands"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    skill_id: Mapped[int] = mapped_column(
        ForeignKey("skills.id"),
        index=True,
    )

    job_role_id: Mapped[int | None] = mapped_column(
        ForeignKey("job_roles.id"),
        nullable=True,
    )

    location_id: Mapped[int | None] = mapped_column(
        ForeignKey("locations.id"),
        nullable=True,
    )

    required_proficiency: Mapped[str] = mapped_column(
        String(50),
    )

    demand_count: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    growth_rate: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    period: Mapped[str] = mapped_column(
        String(30),
    )

    skill = relationship(
        "Skill",
        back_populates="demand_records",
    )


# ============================================================
# SKILL GAP
# ============================================================

class SkillGap(Base):
    __tablename__ = "skill_gaps"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    skill_id: Mapped[int] = mapped_column(
        ForeignKey("skills.id"),
        index=True,
    )

    job_role_id: Mapped[int | None] = mapped_column(
        ForeignKey("job_roles.id"),
        nullable=True,
    )

    location_id: Mapped[int | None] = mapped_column(
        ForeignKey("locations.id"),
        nullable=True,
    )

    required_proficiency: Mapped[str] = mapped_column(
        String(50),
    )

    current_proficiency: Mapped[str] = mapped_column(
        String(50),
    )

    demand_count: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    available_candidates: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    gap_score: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    priority: Mapped[str] = mapped_column(
        String(50),
        default="Medium",
    )

    recommended_course: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
    )

    skill = relationship(
        "Skill",
        back_populates="gap_records",
    )


# ============================================================
# COURSE
# ============================================================

class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(200),
        index=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    sector_id: Mapped[int | None] = mapped_column(
        ForeignKey("sectors.id"),
        nullable=True,
    )

    qualification: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
    )

    duration_months: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    training_capacity: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    enrolled_students: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    placement_rate: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    alignment_score: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    demand_level: Mapped[str] = mapped_column(
        String(50),
        default="Medium",
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="Active",
    )

    last_updated: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    curriculum = relationship(
        "Curriculum",
        back_populates="course",
    )


# ============================================================
# CURRICULUM
# ============================================================

class Curriculum(Base):
    __tablename__ = "curriculums"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    course_id: Mapped[int] = mapped_column(
        ForeignKey("courses.id"),
        index=True,
    )

    version: Mapped[str] = mapped_column(
        String(50),
    )

    current_content: Mapped[str] = mapped_column(
        Text,
    )

    industry_requirements: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    alignment_score: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    update_required: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    course = relationship(
        "Course",
        back_populates="curriculum",
    )


# ============================================================
# EMPLOYER
# ============================================================

class Employer(Base):
    __tablename__ = "employers"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    company_name: Mapped[str] = mapped_column(
        String(200),
        index=True,
    )

    industry: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True,
    )

    sector_id: Mapped[int | None] = mapped_column(
        ForeignKey("sectors.id"),
        nullable=True,
    )

    location: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
    )

    company_size: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    sector = relationship(
        "Sector",
        back_populates="employers",
    )

    surveys = relationship(
        "EmployerSurvey",
        back_populates="employer",
    )


# ============================================================
# EMPLOYER SURVEY
# ============================================================

class EmployerSurvey(Base):
    __tablename__ = "employer_surveys"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    employer_id: Mapped[int] = mapped_column(
        ForeignKey("employers.id"),
        index=True,
    )

    job_role: Mapped[str] = mapped_column(
        String(200),
    )

    required_skills: Mapped[str] = mapped_column(
        Text,
    )

    required_proficiency: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    experience_required: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    technology_used: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    expected_hiring: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    salary_min: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    salary_max: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    future_skill_demand: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    hiring_difficulty: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    employer = relationship(
        "Employer",
        back_populates="surveys",
    )


# ============================================================
# TRAINER
# ============================================================

class Trainer(Base):
    __tablename__ = "trainers"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(200),
    )

    institute: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
    )

    current_skills: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    industry_required_skills: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    skill_gap: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    certifications: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    upskilling_recommendation: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    capacity: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )


# ============================================================
# INFRASTRUCTURE
# ============================================================

class Infrastructure(Base):
    __tablename__ = "infrastructure"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    district: Mapped[str] = mapped_column(
        String(100),
        index=True,
    )

    course: Mapped[str] = mapped_column(
        String(200),
    )

    students: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    training_seats: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    computers_required: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    computers_available: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    gpu_required: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    gpu_available: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    labs_required: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    labs_available: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    trainers_required: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    trainers_available: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    internet_required: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    software_requirements: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )


# ============================================================
# DISTRICT TRAINING PLAN
# ============================================================

class DistrictTrainingPlan(Base):
    __tablename__ = "district_training_plans"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    district: Mapped[str] = mapped_column(
        String(100),
        index=True,
    )

    priority_industries: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    priority_job_roles: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    priority_skills: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    recommended_courses: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    student_capacity: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    trainer_capacity: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    equipment_requirements: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    institute_allocation: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    expected_placement: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    generated_by_ai: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )


# ============================================================
# CANDIDATE
# ============================================================

class Candidate(Base):
    __tablename__ = "candidates"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(200),
    )

    location_id: Mapped[int | None] = mapped_column(
        ForeignKey("locations.id"),
        nullable=True,
    )

    education: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
    )

    skills: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    target_job: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
    )

    career_readiness_score: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    experience_years: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    certifications: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    location = relationship(
        "Location",
        back_populates="candidates",
    )


# ============================================================
# PLACEMENT OUTCOME
# ============================================================

class PlacementOutcome(Base):
    __tablename__ = "placement_outcomes"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    candidate_id: Mapped[int] = mapped_column(
        ForeignKey("candidates.id"),
        index=True,
    )

    course_id: Mapped[int | None] = mapped_column(
        ForeignKey("courses.id"),
        nullable=True,
    )

    employer_name: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
    )

    placed: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    salary: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    skill_match_score: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    retention_months: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    employer_satisfaction: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    placement_date: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )


# ============================================================
# AI RECOMMENDATION
# ============================================================

class AIRecommendation(Base):
    __tablename__ = "ai_recommendations"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    title: Mapped[str] = mapped_column(
        String(300),
    )

    recommendation: Mapped[str] = mapped_column(
        Text,
    )

    reason: Mapped[str] = mapped_column(
        Text,
    )

    data_evidence: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    expected_impact: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    priority: Mapped[str] = mapped_column(
        String(50),
        default="Medium",
    )

    action: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="Pending",
    )

    confidence_score: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    generated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )


# ============================================================
# EMPLOYER FEEDBACK
# ============================================================

class EmployerFeedback(Base):
    __tablename__ = "employer_feedback"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    employer_id: Mapped[int] = mapped_column(
        ForeignKey("employers.id"),
        index=True,
    )

    candidate_id: Mapped[int | None] = mapped_column(
        ForeignKey("candidates.id"),
        nullable=True,
    )

    skill_match_score: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    satisfaction_score: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    feedback: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    recommended_skill_changes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )


# ============================================================
# DATA SOURCE
# ============================================================

class DataSource(Base):
    __tablename__ = "data_sources"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(200),
    )

    source_type: Mapped[str] = mapped_column(
        String(100),
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="Active",
    )

    record_count: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    reliability_score: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    last_updated: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    validation_status: Mapped[str] = mapped_column(
        String(100),
        default="Pending",
    )


# ============================================================
# USER
# ============================================================

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(200),
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
    )

    role: Mapped[str] = mapped_column(
        String(100),
        index=True,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )