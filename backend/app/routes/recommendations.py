from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

from .students import STUDENTS
from .curriculum import CURRICULUM


router = APIRouter()


# ============================================================
# REQUEST MODEL
# ============================================================

class RecommendationRequest(BaseModel):
    student_id: Optional[int] = None
    course: Optional[str] = None
    skills: list[str] = []


# ============================================================
# SKILL RECOMMENDATION LOGIC
# ============================================================

def generate_recommendations(
    student_skills: list[str],
    course: Optional[str] = None,
):
    """
    Generate recommended skills by comparing
    existing student skills with curriculum
    recommended skills.
    """

    current_skills = {
        skill.lower()
        for skill in student_skills
    }

    recommendations = []

    for curriculum in CURRICULUM:

        if course:

            if curriculum["course"].lower() != course.lower():
                continue

        for skill in curriculum["recommended_skills"]:

            if skill.lower() not in current_skills:

                if skill not in recommendations:
                    recommendations.append(skill)

    return recommendations


# ============================================================
# GET RECOMMENDATIONS FOR A STUDENT
# ============================================================

@router.get("/student/{student_id}")
def get_student_recommendations(
    student_id: int,
):

    student = next(
        (
            item
            for item in STUDENTS
            if item["id"] == student_id
        ),
        None,
    )

    if student is None:

        return {
            "success": False,
            "message": "Student not found",
        }

    recommendations = generate_recommendations(
        student["skills"],
        student["course"],
    )

    return {
        "success": True,
        "student": {
            "id": student["id"],
            "name": student["name"],
            "course": student["course"],
        },
        "current_skills": student["skills"],
        "recommended_skills": recommendations,
        "count": len(recommendations),
    }


# ============================================================
# GET RECOMMENDATIONS BY COURSE
# ============================================================

@router.get("/course/{course}")
def get_course_recommendations(
    course: str,
):

    matching_curriculum = [
        item
        for item in CURRICULUM
        if item["course"].lower() == course.lower()
    ]

    if not matching_curriculum:

        return {
            "success": False,
            "message": "Course not found",
        }

    recommendations = []

    for curriculum in matching_curriculum:

        for skill in curriculum["recommended_skills"]:

            if skill not in recommendations:
                recommendations.append(skill)

    return {
        "success": True,
        "course": course,
        "recommended_skills": recommendations,
        "count": len(recommendations),
    }


# ============================================================
# GET ALL RECOMMENDED SKILLS
# ============================================================

@router.get("/")
def get_all_recommendations():

    recommendations = {}

    for curriculum in CURRICULUM:

        course = curriculum["course"]

        if course not in recommendations:
            recommendations[course] = []

        for skill in curriculum["recommended_skills"]:

            if skill not in recommendations[course]:
                recommendations[course].append(skill)

    return {
        "success": True,
        "data": recommendations,
    }


# ============================================================
# SKILL GAP RECOMMENDATIONS
# ============================================================

@router.get("/skill-gap/{student_id}")
def get_skill_gap(
    student_id: int,
):

    student = next(
        (
            item
            for item in STUDENTS
            if item["id"] == student_id
        ),
        None,
    )

    if student is None:

        return {
            "success": False,
            "message": "Student not found",
        }

    current_skills = {
        skill.lower()
        for skill in student["skills"]
    }

    course_curriculum = [
        item
        for item in CURRICULUM
        if item["course"].lower()
        == student["course"].lower()
    ]

    required_skills = []
    missing_skills = []

    for curriculum in course_curriculum:

        for skill in (
            curriculum["skills"]
            + curriculum["recommended_skills"]
        ):

            if skill not in required_skills:
                required_skills.append(skill)

    for skill in required_skills:

        if skill.lower() not in current_skills:

            if skill not in missing_skills:
                missing_skills.append(skill)

    return {
        "success": True,
        "student": {
            "id": student["id"],
            "name": student["name"],
            "course": student["course"],
        },
        "current_skills": student["skills"],
        "required_skills": required_skills,
        "missing_skills": missing_skills,
        "skill_gap_count": len(missing_skills),
    }


# ============================================================
# PERSONALIZED RECOMMENDATION
# ============================================================

@router.post("/generate")
def generate_personalized_recommendation(
    request: RecommendationRequest,
):

    student_skills = request.skills

    student = None

    if request.student_id is not None:

        student = next(
            (
                item
                for item in STUDENTS
                if item["id"] == request.student_id
            ),
            None,
        )

        if student is None:

            return {
                "success": False,
                "message": "Student not found",
            }

        student_skills = student["skills"]

        if request.course is None:
            request.course = student["course"]

    recommendations = generate_recommendations(
        student_skills,
        request.course,
    )

    return {
        "success": True,
        "message": "Recommendations generated successfully",
        "data": {
            "student_id": (
                student["id"]
                if student
                else None
            ),
            "course": request.course,
            "current_skills": student_skills,
            "recommended_skills": recommendations,
            "count": len(recommendations),
        },
    }


# ============================================================
# RECOMMENDATION STATUS
# ============================================================

@router.get("/status/check")
def recommendation_status():

    return {
        "success": True,
        "module": "recommendations",
        "status": "working",
    }