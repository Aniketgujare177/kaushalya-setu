from fastapi import APIRouter
from typing import Optional

from .students import STUDENTS
from .skills import SKILLS


router = APIRouter()


# ============================================================
# SKILL GAP ANALYSIS
# ============================================================

@router.get("/")
def get_skill_gaps(
    course: Optional[str] = None,
    skill: Optional[str] = None,
):
    """
    Return skill-gap information based on student skills.
    """

    skill_counts = {}

    students = STUDENTS

    # --------------------------------------------------------
    # Filter by course
    # --------------------------------------------------------

    if course:
        students = [
            student
            for student in students
            if student.get("course", "").lower()
            == course.lower()
        ]

    # --------------------------------------------------------
    # Count skills
    # --------------------------------------------------------

    for student in students:

        for student_skill in student.get("skills", []):

            if student_skill not in skill_counts:
                skill_counts[student_skill] = 0

            skill_counts[student_skill] += 1

    # --------------------------------------------------------
    # Build results
    # --------------------------------------------------------

    results = []

    for skill_name, student_count in skill_counts.items():

        if skill and skill.lower() not in skill_name.lower():
            continue

        # Simple gap calculation
        if student_count <= 2:
            gap_level = "High"
        elif student_count <= 5:
            gap_level = "Medium"
        else:
            gap_level = "Low"

        results.append(
            {
                "skill": skill_name,
                "student_count": student_count,
                "gap_level": gap_level,
            }
        )

    results.sort(
        key=lambda item: item["student_count"]
    )

    return {
        "success": True,
        "count": len(results),
        "data": results,
    }


# ============================================================
# HIGH PRIORITY SKILL GAPS
# ============================================================

@router.get("/high-priority")
def high_priority_skill_gaps():

    skill_counts = {}

    for student in STUDENTS:

        for skill in student.get("skills", []):

            if skill not in skill_counts:
                skill_counts[skill] = 0

            skill_counts[skill] += 1

    results = []

    for skill, count in skill_counts.items():

        if count <= 2:

            results.append(
                {
                    "skill": skill,
                    "student_count": count,
                    "priority": "High",
                    "recommendation": (
                        f"Increase training coverage for {skill}"
                    ),
                }
            )

    return {
        "success": True,
        "count": len(results),
        "data": results,
    }


# ============================================================
# COURSE-WISE SKILL GAPS
# ============================================================

@router.get("/courses")
def course_skill_gaps():

    courses = {}

    for student in STUDENTS:

        course = student.get(
            "course",
            "Unknown"
        )

        if course not in courses:

            courses[course] = {
                "course": course,
                "student_count": 0,
                "skills": {},
            }

        courses[course]["student_count"] += 1

        for skill in student.get("skills", []):

            if skill not in courses[course]["skills"]:
                courses[course]["skills"][skill] = 0

            courses[course]["skills"][skill] += 1

    results = []

    for course, data in courses.items():

        skill_data = []

        for skill, count in data["skills"].items():

            if count <= 2:
                level = "High"
            elif count <= 5:
                level = "Medium"
            else:
                level = "Low"

            skill_data.append(
                {
                    "skill": skill,
                    "student_count": count,
                    "gap_level": level,
                }
            )

        skill_data.sort(
            key=lambda item: item["student_count"]
        )

        results.append(
            {
                "course": course,
                "student_count": data["student_count"],
                "skill_gaps": skill_data,
            }
        )

    return {
        "success": True,
        "count": len(results),
        "data": results,
    }


# ============================================================
# SKILL GAP SUMMARY
# ============================================================

@router.get("/summary")
def skill_gap_summary():

    total_students = len(STUDENTS)

    skill_counts = {}

    for student in STUDENTS:

        for skill in student.get("skills", []):

            if skill not in skill_counts:
                skill_counts[skill] = 0

            skill_counts[skill] += 1

    high = 0
    medium = 0
    low = 0

    for count in skill_counts.values():

        if count <= 2:
            high += 1

        elif count <= 5:
            medium += 1

        else:
            low += 1

    return {
        "success": True,
        "data": {
            "total_students": total_students,
            "total_skills": len(skill_counts),
            "high_priority_gaps": high,
            "medium_priority_gaps": medium,
            "low_priority_gaps": low,
        },
    }


# ============================================================
# SKILL GAP BY STUDENT
# ============================================================

@router.get("/student/{student_id}")
def student_skill_gap(student_id: int):

    student = next(
        (
            item
            for item in STUDENTS
            if item.get("id") == student_id
        ),
        None,
    )

    if student is None:

        return {
            "success": False,
            "message": "Student not found",
        }

    current_skills = student.get(
        "skills",
        []
    )

    # --------------------------------------------------------
    # Try to find recommended skills
    # --------------------------------------------------------

    recommended_skills = student.get(
        "recommended_skills",
        []
    )

    missing_skills = [
        skill
        for skill in recommended_skills
        if skill not in current_skills
    ]

    return {
        "success": True,
        "data": {
            "student_id": student.get("id"),
            "student_name": student.get(
                "name",
                "Unknown"
            ),
            "course": student.get(
                "course",
                "Unknown"
            ),
            "current_skills": current_skills,
            "recommended_skills": recommended_skills,
            "skill_gaps": missing_skills,
            "skill_gap_count": len(missing_skills),
        },
    }


# ============================================================
# SKILL GAP STATUS
# ============================================================

@router.get("/status/check")
def skill_gap_status():

    return {
        "success": True,
        "module": "skill_gap",
        "status": "working",
    }