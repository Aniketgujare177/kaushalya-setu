from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional


router = APIRouter()


# ============================================================
# JOB MARKET DATA
# ============================================================

JOBS = [
    {
        "id": 1,
        "title": "Python Developer",
        "company": "Tech Solutions",
        "location": "Pune",
        "job_type": "Full Time",
        "experience": "0-2 Years",
        "demand": 92,
        "skills": [
            "Python",
            "FastAPI",
            "SQL",
            "REST API",
        ],
    },
    {
        "id": 2,
        "title": "Full Stack Developer",
        "company": "Digital Systems",
        "location": "Bangalore",
        "job_type": "Full Time",
        "experience": "1-3 Years",
        "demand": 89,
        "skills": [
            "JavaScript",
            "React",
            "Node.js",
            "SQL",
        ],
    },
    {
        "id": 3,
        "title": "AI/ML Engineer",
        "company": "AI Innovations",
        "location": "Hyderabad",
        "job_type": "Full Time",
        "experience": "1-3 Years",
        "demand": 95,
        "skills": [
            "Python",
            "Machine Learning",
            "Generative AI",
            "LLMs",
        ],
    },
    {
        "id": 4,
        "title": "Data Analyst",
        "company": "Analytics Hub",
        "location": "Mumbai",
        "job_type": "Full Time",
        "experience": "0-2 Years",
        "demand": 84,
        "skills": [
            "SQL",
            "Python",
            "Excel",
            "Power BI",
        ],
    },
    {
        "id": 5,
        "title": "Cloud Engineer",
        "company": "Cloud Technologies",
        "location": "Pune",
        "job_type": "Full Time",
        "experience": "1-3 Years",
        "demand": 87,
        "skills": [
            "AWS",
            "Docker",
            "Kubernetes",
            "Linux",
        ],
    },
]


# ============================================================
# REQUEST MODEL
# ============================================================

class JobCreate(BaseModel):
    title: str
    company: str
    location: str
    job_type: str = "Full Time"
    experience: str = "0-2 Years"
    demand: int = 50
    skills: list[str] = []


class JobUpdate(BaseModel):
    title: Optional[str] = None
    company: Optional[str] = None
    location: Optional[str] = None
    job_type: Optional[str] = None
    experience: Optional[str] = None
    demand: Optional[int] = None
    skills: Optional[list[str]] = None


# ============================================================
# GET ALL JOBS
# ============================================================

@router.get("/")
def get_all_jobs(
    search: Optional[str] = None,
    location: Optional[str] = None,
    job_type: Optional[str] = None,
):
    results = JOBS.copy()

    if search:
        text = search.lower()

        results = [
            job
            for job in results
            if text in job["title"].lower()
            or text in job["company"].lower()
            or any(
                text in skill.lower()
                for skill in job["skills"]
            )
        ]

    if location:
        results = [
            job
            for job in results
            if job["location"].lower()
            == location.lower()
        ]

    if job_type:
        results = [
            job
            for job in results
            if job["job_type"].lower()
            == job_type.lower()
        ]

    return {
        "success": True,
        "count": len(results),
        "data": results,
    }


# ============================================================
# GET JOB BY ID
# ============================================================

@router.get("/{job_id}")
def get_job_by_id(job_id: int):

    job = next(
        (
            item
            for item in JOBS
            if item["id"] == job_id
        ),
        None,
    )

    if job is None:
        return {
            "success": False,
            "message": "Job not found",
        }

    return {
        "success": True,
        "data": job,
    }


# ============================================================
# TOP JOBS BY DEMAND
# ============================================================

@router.get("/analytics/top-demand")
def get_top_demand_jobs():

    results = sorted(
        JOBS,
        key=lambda job: job["demand"],
        reverse=True,
    )

    return {
        "success": True,
        "data": results,
    }


# ============================================================
# JOB MARKET SUMMARY
# ============================================================

@router.get("/analytics/summary")
def job_market_summary():

    if not JOBS:
        return {
            "success": True,
            "data": {
                "total_jobs": 0,
                "average_demand": 0,
                "high_demand_jobs": 0,
            },
        }

    average_demand = round(
        sum(
            job["demand"]
            for job in JOBS
        )
        / len(JOBS)
    )

    high_demand_jobs = sum(
        1
        for job in JOBS
        if job["demand"] >= 85
    )

    return {
        "success": True,
        "data": {
            "total_jobs": len(JOBS),
            "average_demand": average_demand,
            "high_demand_jobs": high_demand_jobs,
        },
    }


# ============================================================
# MOST DEMANDED SKILLS
# ============================================================

@router.get("/analytics/skills")
def get_demanded_skills():

    skill_counts = {}

    for job in JOBS:

        for skill in job["skills"]:

            skill_counts[skill] = (
                skill_counts.get(skill, 0) + 1
            )

    results = [
        {
            "skill": skill,
            "job_count": count,
        }
        for skill, count in skill_counts.items()
    ]

    results.sort(
        key=lambda item: item["job_count"],
        reverse=True,
    )

    return {
        "success": True,
        "data": results,
    }


# ============================================================
# JOBS BY LOCATION
# ============================================================

@router.get("/analytics/locations")
def jobs_by_location():

    location_counts = {}

    for job in JOBS:

        location = job["location"]

        location_counts[location] = (
            location_counts.get(location, 0) + 1
        )

    results = [
        {
            "location": location,
            "job_count": count,
        }
        for location, count in location_counts.items()
    ]

    results.sort(
        key=lambda item: item["job_count"],
        reverse=True,
    )

    return {
        "success": True,
        "data": results,
    }


# ============================================================
# CREATE JOB
# ============================================================

@router.post("/")
def create_job(request: JobCreate):

    new_id = (
        max(
            job["id"]
            for job in JOBS
        ) + 1
        if JOBS
        else 1
    )

    new_job = {
        "id": new_id,
        "title": request.title,
        "company": request.company,
        "location": request.location,
        "job_type": request.job_type,
        "experience": request.experience,
        "demand": request.demand,
        "skills": request.skills,
    }

    JOBS.append(new_job)

    return {
        "success": True,
        "message": "Job created successfully",
        "data": new_job,
    }


# ============================================================
# UPDATE JOB
# ============================================================

@router.put("/{job_id}")
def update_job(
    job_id: int,
    request: JobUpdate,
):

    job = next(
        (
            item
            for item in JOBS
            if item["id"] == job_id
        ),
        None,
    )

    if job is None:
        return {
            "success": False,
            "message": "Job not found",
        }

    update_data = request.model_dump(
        exclude_none=True
    )

    for key, value in update_data.items():
        job[key] = value

    return {
        "success": True,
        "message": "Job updated successfully",
        "data": job,
    }


# ============================================================
# DELETE JOB
# ============================================================

@router.delete("/{job_id}")
def delete_job(job_id: int):

    job = next(
        (
            item
            for item in JOBS
            if item["id"] == job_id
        ),
        None,
    )

    if job is None:
        return {
            "success": False,
            "message": "Job not found",
        }

    JOBS.remove(job)

    return {
        "success": True,
        "message": "Job deleted successfully",
    }


# ============================================================
# MODULE STATUS
# ============================================================

@router.get("/status/check")
def jobs_status():

    return {
        "success": True,
        "module": "jobs",
        "status": "working",
    }