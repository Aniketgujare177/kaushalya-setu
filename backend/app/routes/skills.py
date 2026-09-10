from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import Optional


router = APIRouter()


# ============================================================
# SKILL DATA
# ============================================================

SKILLS = [
    {
        "id": 1,
        "name": "Python",
        "category": "Programming",
        "demand_score": 95,
        "supply_score": 78,
        "gap_score": 17,
        "status": "High Demand",
        "trend": "Rising",
    },
    {
        "id": 2,
        "name": "Java",
        "category": "Programming",
        "demand_score": 88,
        "supply_score": 74,
        "gap_score": 14,
        "status": "High Demand",
        "trend": "Stable",
    },
    {
        "id": 3,
        "name": "SQL",
        "category": "Database",
        "demand_score": 86,
        "supply_score": 70,
        "gap_score": 16,
        "status": "High Demand",
        "trend": "Rising",
    },
    {
        "id": 4,
        "name": "React",
        "category": "Web Development",
        "demand_score": 91,
        "supply_score": 68,
        "gap_score": 23,
        "status": "Skill Gap",
        "trend": "Rising",
    },
    {
        "id": 5,
        "name": "Machine Learning",
        "category": "Artificial Intelligence",
        "demand_score": 94,
        "supply_score": 61,
        "gap_score": 33,
        "status": "Critical Gap",
        "trend": "Rising",
    },
    {
        "id": 6,
        "name": "Generative AI",
        "category": "Artificial Intelligence",
        "demand_score": 97,
        "supply_score": 48,
        "gap_score": 49,
        "status": "Emerging",
        "trend": "Rapidly Rising",
    },
    {
        "id": 7,
        "name": "Cloud Computing",
        "category": "Cloud",
        "demand_score": 93,
        "supply_score": 63,
        "gap_score": 30,
        "status": "Skill Gap",
        "trend": "Rising",
    },
    {
        "id": 8,
        "name": "Data Analytics",
        "category": "Data",
        "demand_score": 89,
        "supply_score": 69,
        "gap_score": 20,
        "status": "High Demand",
        "trend": "Rising",
    },
]


# ============================================================
# REQUEST MODELS
# ============================================================

class SkillCreate(BaseModel):
    name: str
    category: str

    demand_score: int = Field(
        default=50,
        ge=0,
        le=100
    )

    supply_score: int = Field(
        default=50,
        ge=0,
        le=100
    )

    trend: str = "Stable"


class SkillUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None

    demand_score: Optional[int] = Field(
        default=None,
        ge=0,
        le=100
    )

    supply_score: Optional[int] = Field(
        default=None,
        ge=0,
        le=100
    )

    trend: Optional[str] = None


# ============================================================
# HELPER FUNCTION
# ============================================================

def calculate_skill_status(
    demand_score: int,
    supply_score: int,
):
    """
    Calculate skill gap and status.
    """

    gap_score = max(
        0,
        demand_score - supply_score
    )

    if gap_score >= 35:
        status = "Critical Gap"

    elif gap_score >= 20:
        status = "Skill Gap"

    elif demand_score >= 80:
        status = "High Demand"

    else:
        status = "Balanced"

    return gap_score, status


# ============================================================
# GET ALL SKILLS
# ============================================================

@router.get("/")
def get_all_skills(
    search: Optional[str] = None,
    category: Optional[str] = None,
):

    results = SKILLS.copy()

    # --------------------------------------------------------
    # SEARCH
    # --------------------------------------------------------

    if search:

        search_text = search.lower().strip()

        results = [
            skill
            for skill in results
            if (
                search_text in skill["name"].lower()
                or search_text in skill["category"].lower()
                or search_text in skill["trend"].lower()
                or search_text in skill["status"].lower()
            )
        ]

    # --------------------------------------------------------
    # CATEGORY FILTER
    # --------------------------------------------------------

    if category:

        category_text = category.lower().strip()

        results = [
            skill
            for skill in results
            if skill["category"].lower()
            == category_text
        ]

    return {
        "success": True,
        "count": len(results),
        "data": results,
    }


# ============================================================
# SKILL SUMMARY
# ============================================================

@router.get("/summary")
def skill_summary():

    total = len(SKILLS)

    if total == 0:

        return {
            "success": True,
            "data": {
                "total_skills": 0,
                "high_demand": 0,
                "critical_gaps": 0,
                "emerging_skills": 0,
                "average_demand": 0,
                "average_supply": 0,
                "average_gap": 0,
            },
        }

    high_demand = sum(
        1
        for skill in SKILLS
        if skill["demand_score"] >= 80
    )

    critical_gaps = sum(
        1
        for skill in SKILLS
        if skill["gap_score"] >= 35
    )

    emerging_skills = sum(
        1
        for skill in SKILLS
        if skill["trend"] == "Rapidly Rising"
    )

    average_demand = round(
        sum(
            skill["demand_score"]
            for skill in SKILLS
        ) / total
    )

    average_supply = round(
        sum(
            skill["supply_score"]
            for skill in SKILLS
        ) / total
    )

    average_gap = round(
        sum(
            skill["gap_score"]
            for skill in SKILLS
        ) / total
    )

    return {
        "success": True,
        "data": {
            "total_skills": total,
            "high_demand": high_demand,
            "critical_gaps": critical_gaps,
            "emerging_skills": emerging_skills,
            "average_demand": average_demand,
            "average_supply": average_supply,
            "average_gap": average_gap,
        },
    }


# ============================================================
# GET SKILL BY ID
# ============================================================

@router.get("/{skill_id}")
def get_skill_by_id(skill_id: int):

    skill = next(
        (
            item
            for item in SKILLS
            if item["id"] == skill_id
        ),
        None,
    )

    if skill is None:

        return {
            "success": False,
            "message": "Skill not found",
        }

    return {
        "success": True,
        "data": skill,
    }


# ============================================================
# HIGH-DEMAND SKILLS
# ============================================================

@router.get("/analytics/high-demand")
def high_demand_skills():

    results = [
        skill
        for skill in SKILLS
        if skill["demand_score"] >= 80
    ]

    results.sort(
        key=lambda item: item["demand_score"],
        reverse=True,
    )

    return {
        "success": True,
        "count": len(results),
        "data": results,
    }


# ============================================================
# CRITICAL SKILL GAPS
# ============================================================

@router.get("/analytics/critical-gaps")
def critical_skill_gaps():

    results = [
        skill
        for skill in SKILLS
        if skill["gap_score"] >= 30
    ]

    results.sort(
        key=lambda item: item["gap_score"],
        reverse=True,
    )

    return {
        "success": True,
        "count": len(results),
        "data": results,
    }


# ============================================================
# EMERGING SKILLS
# ============================================================

@router.get("/analytics/emerging")
def emerging_skills():

    results = [
        skill
        for skill in SKILLS
        if skill["trend"] in [
            "Rising",
            "Rapidly Rising",
        ]
    ]

    results.sort(
        key=lambda item: item["demand_score"],
        reverse=True,
    )

    return {
        "success": True,
        "count": len(results),
        "data": results,
    }


# ============================================================
# SKILL CATEGORIES
# ============================================================

@router.get("/categories/list")
def skill_categories():

    categories = {}

    for skill in SKILLS:

        category = skill["category"]

        if category not in categories:
            categories[category] = 0

        categories[category] += 1

    results = [
        {
            "category": category,
            "skill_count": count,
        }
        for category, count in categories.items()
    ]

    results.sort(
        key=lambda item: item["skill_count"],
        reverse=True,
    )

    return {
        "success": True,
        "count": len(results),
        "data": results,
    }


# ============================================================
# CREATE SKILL
# ============================================================

@router.post("/")
def create_skill(
    request: SkillCreate
):

    new_id = (
        max(
            skill["id"]
            for skill in SKILLS
        ) + 1
        if SKILLS
        else 1
    )

    gap_score, status = calculate_skill_status(
        request.demand_score,
        request.supply_score,
    )

    new_skill = {
        "id": new_id,
        "name": request.name,
        "category": request.category,
        "demand_score": request.demand_score,
        "supply_score": request.supply_score,
        "gap_score": gap_score,
        "status": status,
        "trend": request.trend,
    }

    SKILLS.append(new_skill)

    return {
        "success": True,
        "message": "Skill created successfully",
        "data": new_skill,
    }


# ============================================================
# UPDATE SKILL
# ============================================================

@router.put("/{skill_id}")
def update_skill(
    skill_id: int,
    request: SkillUpdate,
):

    skill = next(
        (
            item
            for item in SKILLS
            if item["id"] == skill_id
        ),
        None,
    )

    if skill is None:

        return {
            "success": False,
            "message": "Skill not found",
        }

    update_data = request.model_dump(
        exclude_none=True
    )

    # --------------------------------------------------------
    # UPDATE PROVIDED FIELDS
    # --------------------------------------------------------

    for key, value in update_data.items():
        skill[key] = value

    # --------------------------------------------------------
    # RECALCULATE GAP AND STATUS
    # --------------------------------------------------------

    gap_score, status = calculate_skill_status(
        skill["demand_score"],
        skill["supply_score"],
    )

    skill["gap_score"] = gap_score
    skill["status"] = status

    return {
        "success": True,
        "message": "Skill updated successfully",
        "data": skill,
    }


# ============================================================
# DELETE SKILL
# ============================================================

@router.delete("/{skill_id}")
def delete_skill(
    skill_id: int
):

    skill = next(
        (
            item
            for item in SKILLS
            if item["id"] == skill_id
        ),
        None,
    )

    if skill is None:

        return {
            "success": False,
            "message": "Skill not found",
        }

    SKILLS.remove(skill)

    return {
        "success": True,
        "message": "Skill deleted successfully",
    }


# ============================================================
# MODULE STATUS
# ============================================================

@router.get("/status/check")
def skills_status():

    return {
        "success": True,
        "module": "skills",
        "status": "working",
        "total_skills": len(SKILLS),
    }