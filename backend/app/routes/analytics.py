from fastapi import APIRouter

from .students import STUDENTS
from .curriculum import CURRICULUM


router = APIRouter()


# ============================================================
# OVERALL DASHBOARD ANALYTICS
# ============================================================

@router.get("/dashboard")
def dashboard_analytics():

    total_students = len(STUDENTS)
    total_curriculum = len(CURRICULUM)

    if total_students > 0:

        average_skill_score = round(
            sum(
                student["skill_score"]
                for student in STUDENTS
            )
            / total_students
        )

        average_industry_readiness = round(
            sum(
                student["industry_readiness"]
                for student in STUDENTS
            )
            / total_students
        )

        industry_ready = sum(
            1
            for student in STUDENTS
            if student["industry_readiness"] >= 80
        )

        needs_training = sum(
            1
            for student in STUDENTS
            if student["industry_readiness"] < 65
        )

    else:

        average_skill_score = 0
        average_industry_readiness = 0
        industry_ready = 0
        needs_training = 0

    if total_curriculum > 0:

        average_alignment = round(
            sum(
                item["alignment_score"]
                for item in CURRICULUM
            )
            / total_curriculum
        )

        average_skill_gap = round(
            sum(
                item["skill_gap"]
                for item in CURRICULUM
            )
            / total_curriculum
        )

        courses_needing_update = sum(
            1
            for item in CURRICULUM
            if item["alignment_score"] < 70
        )

    else:

        average_alignment = 0
        average_skill_gap = 0
        courses_needing_update = 0

    return {
        "success": True,
        "data": {
            "students": {
                "total": total_students,
                "industry_ready": industry_ready,
                "needs_training": needs_training,
                "average_skill_score": average_skill_score,
                "average_industry_readiness":
                    average_industry_readiness,
            },
            "curriculum": {
                "total": total_curriculum,
                "average_alignment":
                    average_alignment,
                "average_skill_gap":
                    average_skill_gap,
                "courses_needing_update":
                    courses_needing_update,
            },
        },
    }


# ============================================================
# INDUSTRY READINESS DISTRIBUTION
# ============================================================

@router.get("/readiness")
def readiness_distribution():

    industry_ready = 0
    developing = 0
    needs_training = 0

    for student in STUDENTS:

        score = student["industry_readiness"]

        if score >= 80:
            industry_ready += 1

        elif score >= 65:
            developing += 1

        else:
            needs_training += 1

    return {
        "success": True,
        "data": [
            {
                "status": "Industry Ready",
                "count": industry_ready,
            },
            {
                "status": "Developing",
                "count": developing,
            },
            {
                "status": "Needs Training",
                "count": needs_training,
            },
        ],
    }


# ============================================================
# CURRICULUM ALIGNMENT DISTRIBUTION
# ============================================================

@router.get("/curriculum-alignment")
def curriculum_alignment():

    good_alignment = 0
    needs_improvement = 0
    needs_update = 0

    for item in CURRICULUM:

        score = item["alignment_score"]

        if score >= 80:
            good_alignment += 1

        elif score >= 70:
            needs_improvement += 1

        else:
            needs_update += 1

    return {
        "success": True,
        "data": [
            {
                "status": "Good Alignment",
                "count": good_alignment,
            },
            {
                "status": "Needs Improvement",
                "count": needs_improvement,
            },
            {
                "status": "Needs Update",
                "count": needs_update,
            },
        ],
    }


# ============================================================
# COURSE-WISE ANALYTICS
# ============================================================

@router.get("/courses")
def course_analytics():

    courses = {}

    for student in STUDENTS:

        course = student["course"]

        if course not in courses:

            courses[course] = {
                "course": course,
                "student_count": 0,
                "total_readiness": 0,
                "total_skill_score": 0,
            }

        courses[course]["student_count"] += 1

        courses[course]["total_readiness"] += (
            student["industry_readiness"]
        )

        courses[course]["total_skill_score"] += (
            student["skill_score"]
        )

    results = []

    for course, data in courses.items():

        count = data["student_count"]

        results.append(
            {
                "course": course,
                "student_count": count,
                "average_industry_readiness": round(
                    data["total_readiness"] / count
                ),
                "average_skill_score": round(
                    data["total_skill_score"] / count
                ),
            }
        )

    return {
        "success": True,
        "count": len(results),
        "data": results,
    }


# ============================================================
# TOP INDUSTRY SKILLS
# ============================================================

@router.get("/skills")
def skill_analytics():

    skills = {}

    for student in STUDENTS:

        for skill in student["skills"]:

            if skill not in skills:
                skills[skill] = 0

            skills[skill] += 1

    results = [
        {
            "skill": skill,
            "student_count": count,
        }
        for skill, count in skills.items()
    ]

    results.sort(
        key=lambda item: item["student_count"],
        reverse=True,
    )

    return {
        "success": True,
        "data": results,
    }


# ============================================================
# ANALYTICS STATUS
# ============================================================

@router.get("/status/check")
def analytics_status():

    return {
        "success": True,
        "module": "analytics",
        "status": "working",
    }