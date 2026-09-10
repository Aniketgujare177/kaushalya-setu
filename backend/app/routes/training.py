from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter()


# ============================================================
# TRAINING DATA
# ============================================================

TRAINING_PROGRAMS = [
    {
        "id": 1,
        "title": "Advanced Python & AI",
        "provider": "Industry Training Partner",
        "category": "Artificial Intelligence",
        "duration": "8 Weeks",
        "mode": "Online",
        "level": "Intermediate",
        "enrolled": 124,
        "completion_rate": 86,
        "industry_alignment": 94,
        "status": "Active",
        "skills": [
            "Python",
            "Machine Learning",
            "Generative AI",
        ],
    },
    {
        "id": 2,
        "title": "Cloud Computing Fundamentals",
        "provider": "Industry Training Partner",
        "category": "Cloud",
        "duration": "6 Weeks",
        "mode": "Hybrid",
        "level": "Beginner",
        "enrolled": 98,
        "completion_rate": 81,
        "industry_alignment": 89,
        "status": "Active",
        "skills": [
            "Cloud Computing",
            "AWS",
            "Deployment",
        ],
    },
    {
        "id": 3,
        "title": "Modern Web Development",
        "provider": "Technical Training Center",
        "category": "Web Development",
        "duration": "10 Weeks",
        "mode": "Offline",
        "level": "Intermediate",
        "enrolled": 76,
        "completion_rate": 78,
        "industry_alignment": 84,
        "status": "Active",
        "skills": [
            "React",
            "JavaScript",
            "APIs",
        ],
    },
    {
        "id": 4,
        "title": "Cybersecurity Essentials",
        "provider": "Security Training Partner",
        "category": "Cybersecurity",
        "duration": "7 Weeks",
        "mode": "Online",
        "level": "Beginner",
        "enrolled": 65,
        "completion_rate": 88,
        "industry_alignment": 91,
        "status": "Active",
        "skills": [
            "Network Security",
            "Cybersecurity",
            "Security Testing",
        ],
    },
]


# ============================================================
# REQUEST MODELS
# ============================================================

class TrainingCreate(BaseModel):
    title: str
    provider: str
    category: str
    duration: str
    mode: str = "Online"
    level: str = "Beginner"
    enrolled: int = 0
    completion_rate: int = 0
    industry_alignment: int = 50
    skills: list[str] = []


class TrainingUpdate(BaseModel):
    title: Optional[str] = None
    provider: Optional[str] = None
    category: Optional[str] = None
    duration: Optional[str] = None
    mode: Optional[str] = None
    level: Optional[str] = None
    enrolled: Optional[int] = None
    completion_rate: Optional[int] = None
    industry_alignment: Optional[int] = None
    status: Optional[str] = None
    skills: Optional[list[str]] = None


# ============================================================
# GET ALL TRAINING PROGRAMS
# ============================================================

@router.get("/")
def get_training_programs(
    search: Optional[str] = None,
    category: Optional[str] = None,
    mode: Optional[str] = None,
):

    results = TRAINING_PROGRAMS

    if search:
        text = search.lower()

        results = [
            item
            for item in results
            if text in item["title"].lower()
            or text in item["provider"].lower()
            or text in item["category"].lower()
        ]

    if category:
        results = [
            item
            for item in results
            if item["category"].lower()
            == category.lower()
        ]

    if mode:
        results = [
            item
            for item in results
            if item["mode"].lower()
            == mode.lower()
        ]

    return {
        "success": True,
        "count": len(results),
        "data": results,
    }


# ============================================================
# TRAINING SUMMARY
# ============================================================

@router.get("/analytics/summary")
def training_summary():

    if not TRAINING_PROGRAMS:
        return {
            "success": True,
            "data": {
                "total_programs": 0,
                "total_enrolled": 0,
                "average_completion_rate": 0,
                "average_industry_alignment": 0,
            },
        }

    total_enrolled = sum(
        item["enrolled"]
        for item in TRAINING_PROGRAMS
    )

    average_completion = round(
        sum(
            item["completion_rate"]
            for item in TRAINING_PROGRAMS
        )
        / len(TRAINING_PROGRAMS)
    )

    average_alignment = round(
        sum(
            item["industry_alignment"]
            for item in TRAINING_PROGRAMS
        )
        / len(TRAINING_PROGRAMS)
    )

    return {
        "success": True,
        "data": {
            "total_programs": len(TRAINING_PROGRAMS),
            "total_enrolled": total_enrolled,
            "average_completion_rate": average_completion,
            "average_industry_alignment": average_alignment,
        },
    }


# ============================================================
# TOP TRAINING PROGRAMS
# ============================================================

@router.get("/analytics/top")
def top_training_programs():

    results = sorted(
        TRAINING_PROGRAMS,
        key=lambda item: item["industry_alignment"],
        reverse=True,
    )

    return {
        "success": True,
        "data": results,
    }


# ============================================================
# TRAINING BY CATEGORY
# ============================================================

@router.get("/analytics/categories")
def training_categories():

    categories = {}

    for item in TRAINING_PROGRAMS:

        category = item["category"]

        if category not in categories:
            categories[category] = {
                "category": category,
                "program_count": 0,
                "total_enrolled": 0,
                "average_alignment": 0,
            }

        categories[category]["program_count"] += 1

        categories[category]["total_enrolled"] += (
            item["enrolled"]
        )

        categories[category]["average_alignment"] += (
            item["industry_alignment"]
        )

    results = []

    for category, data in categories.items():

        data["average_alignment"] = round(
            data["average_alignment"]
            / data["program_count"]
        )

        results.append(data)

    return {
        "success": True,
        "data": results,
    }


# ============================================================
# ACTIVE TRAINING PROGRAMS
# ============================================================

@router.get("/analytics/active")
def active_training_programs():

    results = [
        item
        for item in TRAINING_PROGRAMS
        if item["status"].lower() == "active"
    ]

    return {
        "success": True,
        "count": len(results),
        "data": results,
    }


# ============================================================
# MODULE STATUS
# ============================================================

@router.get("/status/check")
def training_status():

    return {
        "success": True,
        "module": "training",
        "status": "working",
    }


# ============================================================
# GET TRAINING PROGRAM BY ID
# ============================================================

@router.get("/{training_id}")
def get_training_by_id(training_id: int):

    item = next(
        (
            training
            for training in TRAINING_PROGRAMS
            if training["id"] == training_id
        ),
        None,
    )

    if item is None:
        return {
            "success": False,
            "message": "Training program not found",
        }

    return {
        "success": True,
        "data": item,
    }


# ============================================================
# CREATE TRAINING PROGRAM
# ============================================================

@router.post("/")
def create_training(
    request: TrainingCreate,
):

    new_id = (
        max(
            item["id"]
            for item in TRAINING_PROGRAMS
        ) + 1
        if TRAINING_PROGRAMS
        else 1
    )

    new_item = {
        "id": new_id,
        "title": request.title,
        "provider": request.provider,
        "category": request.category,
        "duration": request.duration,
        "mode": request.mode,
        "level": request.level,
        "enrolled": request.enrolled,
        "completion_rate": request.completion_rate,
        "industry_alignment": request.industry_alignment,
        "status": "Active",
        "skills": request.skills,
    }

    TRAINING_PROGRAMS.append(new_item)

    return {
        "success": True,
        "message": "Training program created successfully",
        "data": new_item,
    }


# ============================================================
# UPDATE TRAINING PROGRAM
# ============================================================

@router.put("/{training_id}")
def update_training(
    training_id: int,
    request: TrainingUpdate,
):

    item = next(
        (
            training
            for training in TRAINING_PROGRAMS
            if training["id"] == training_id
        ),
        None,
    )

    if item is None:
        return {
            "success": False,
            "message": "Training program not found",
        }

    update_data = request.model_dump(
        exclude_none=True
    )

    for key, value in update_data.items():
        item[key] = value

    return {
        "success": True,
        "message": "Training program updated successfully",
        "data": item,
    }


# ============================================================
# DELETE TRAINING PROGRAM
# ============================================================

@router.delete("/{training_id}")
def delete_training(training_id: int):

    item = next(
        (
            training
            for training in TRAINING_PROGRAMS
            if training["id"] == training_id
        ),
        None,
    )

    if item is None:
        return {
            "success": False,
            "message": "Training program not found",
        }

    TRAINING_PROGRAMS.remove(item)

    return {
        "success": True,
        "message": "Training program deleted successfully",
    }