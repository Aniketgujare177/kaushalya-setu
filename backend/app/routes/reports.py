from fastapi import APIRouter
from datetime import datetime

from .students import STUDENTS
from .curriculum import CURRICULUM
from .jobs import JOBS
from .skills import SKILLS


router = APIRouter()


# ============================================================
# REPORT OVERVIEW
# ============================================================

@router.get("/overview")
def report_overview():

    total_students = len(STUDENTS)
    total_curriculum = len(CURRICULUM)
    total_jobs = len(JOBS)
    total_skills = len(SKILLS)

    # --------------------------------------------------------
    # Student analytics
    # --------------------------------------------------------

    if total_students > 0:

        average_readiness = round(
            sum(
                student.get("industry_readiness", 0)
                for student in STUDENTS
            ) / total_students
        )

        industry_ready = sum(
            1
            for student in STUDENTS
            if student.get("industry_readiness", 0) >= 80
        )

    else:

        average_readiness = 0
        industry_ready = 0

    # --------------------------------------------------------
    # Curriculum analytics
    # --------------------------------------------------------

    if total_curriculum > 0:

        average_alignment = round(
            sum(
                item.get("alignment_score", 0)
                for item in CURRICULUM
            ) / total_curriculum
        )

        courses_needing_update = sum(
            1
            for item in CURRICULUM
            if item.get("alignment_score", 0) < 70
        )

    else:

        average_alignment = 0
        courses_needing_update = 0

    return {
        "success": True,
        "data": {
            "generated_at": datetime.now().isoformat(),

            "students": {
                "total": total_students,
                "industry_ready": industry_ready,
                "average_readiness": average_readiness,
            },

            "curriculum": {
                "total": total_curriculum,
                "average_alignment": average_alignment,
                "courses_needing_update": courses_needing_update,
            },

            "jobs": {
                "total": total_jobs,
            },

            "skills": {
                "total": total_skills,
            },
        },
    }


# ============================================================
# STUDENT REPORT
# ============================================================

@router.get("/students")
def student_report():

    total = len(STUDENTS)

    if total == 0:

        return {
            "success": True,
            "data": {
                "total_students": 0,
                "industry_ready": 0,
                "developing": 0,
                "needs_training": 0,
                "average_skill_score": 0,
                "average_industry_readiness": 0,
            },
        }

    industry_ready = 0
    developing = 0
    needs_training = 0

    total_skill_score = 0
    total_readiness = 0

    for student in STUDENTS:

        skill_score = student.get("skill_score", 0)
        readiness = student.get("industry_readiness", 0)

        total_skill_score += skill_score
        total_readiness += readiness

        if readiness >= 80:

            industry_ready += 1

        elif readiness >= 65:

            developing += 1

        else:

            needs_training += 1

    return {
        "success": True,
        "data": {
            "total_students": total,

            "industry_ready": industry_ready,

            "developing": developing,

            "needs_training": needs_training,

            "average_skill_score": round(
                total_skill_score / total
            ),

            "average_industry_readiness": round(
                total_readiness / total
            ),
        },
    }


# ============================================================
# CURRICULUM REPORT
# ============================================================

@router.get("/curriculum")
def curriculum_report():

    total = len(CURRICULUM)

    if total == 0:

        return {
            "success": True,
            "data": {
                "total_courses": 0,
                "good_alignment": 0,
                "needs_improvement": 0,
                "needs_update": 0,
                "average_alignment": 0,
                "average_skill_gap": 0,
            },
        }

    good_alignment = 0
    needs_improvement = 0
    needs_update = 0

    total_alignment = 0
    total_gap = 0

    for item in CURRICULUM:

        alignment = item.get(
            "alignment_score",
            0
        )

        gap = item.get(
            "skill_gap",
            0
        )

        total_alignment += alignment
        total_gap += gap

        if alignment >= 80:

            good_alignment += 1

        elif alignment >= 70:

            needs_improvement += 1

        else:

            needs_update += 1

    return {
        "success": True,
        "data": {
            "total_courses": total,

            "good_alignment": good_alignment,

            "needs_improvement": needs_improvement,

            "needs_update": needs_update,

            "average_alignment": round(
                total_alignment / total
            ),

            "average_skill_gap": round(
                total_gap / total
            ),
        },
    }


# ============================================================
# JOB MARKET REPORT
# ============================================================

@router.get("/jobs")
def job_report():

    total_jobs = len(JOBS)

    if total_jobs == 0:

        return {
            "success": True,
            "data": {
                "total_jobs": 0,
                "high_demand_jobs": 0,
                "sectors": [],
            },
        }

    high_demand_jobs = 0
    sectors = {}

    for job in JOBS:

        demand = job.get(
            "demand",
            job.get("demand_score", 0)
        )

        if isinstance(demand, (int, float)):

            if demand >= 80:
                high_demand_jobs += 1

        sector = job.get(
            "sector",
            "Other"
        )

        if sector not in sectors:
            sectors[sector] = 0

        sectors[sector] += 1

    sector_data = [
        {
            "sector": sector,
            "job_count": count,
        }
        for sector, count in sectors.items()
    ]

    sector_data.sort(
        key=lambda item: item["job_count"],
        reverse=True,
    )

    return {
        "success": True,
        "data": {
            "total_jobs": total_jobs,

            "high_demand_jobs": high_demand_jobs,

            "sectors": sector_data,
        },
    }


# ============================================================
# SKILL REPORT
# ============================================================

@router.get("/skills")
def skill_report():

    skill_usage = {}

    for student in STUDENTS:

        student_skills = student.get(
            "skills",
            []
        )

        for skill in student_skills:

            if skill not in skill_usage:
                skill_usage[skill] = 0

            skill_usage[skill] += 1

    results = [
        {
            "skill": skill,
            "student_count": count,
        }
        for skill, count in skill_usage.items()
    ]

    results.sort(
        key=lambda item: item["student_count"],
        reverse=True,
    )

    return {
        "success": True,
        "count": len(results),
        "data": results,
    }


# ============================================================
# EXECUTIVE SUMMARY
# ============================================================

@router.get("/executive-summary")
def executive_summary():

    total_students = len(STUDENTS)
    total_courses = len(CURRICULUM)

    # --------------------------------------------------------
    # Student readiness
    # --------------------------------------------------------

    if total_students:

        average_readiness = round(
            sum(
                student.get(
                    "industry_readiness",
                    0
                )
                for student in STUDENTS
            ) / total_students
        )

    else:

        average_readiness = 0

    # --------------------------------------------------------
    # Curriculum alignment
    # --------------------------------------------------------

    if total_courses:

        average_alignment = round(
            sum(
                item.get(
                    "alignment_score",
                    0
                )
                for item in CURRICULUM
            ) / total_courses
        )

    else:

        average_alignment = 0

    # --------------------------------------------------------
    # Overall status
    # --------------------------------------------------------

    overall_score = round(
        (
            average_readiness
            + average_alignment
        ) / 2
    )

    if overall_score >= 80:

        status = "Strong"

    elif overall_score >= 65:

        status = "Moderate"

    else:

        status = "Needs Attention"

    return {
        "success": True,
        "data": {
            "overall_score": overall_score,

            "status": status,

            "student_readiness": average_readiness,

            "curriculum_alignment": average_alignment,

            "total_students": total_students,

            "total_courses": total_courses,

            "generated_at": datetime.now().isoformat(),
        },
    }


# ============================================================
# REPORT STATUS
# ============================================================

@router.get("/status/check")
def reports_status():

    return {
        "success": True,
        "module": "reports",
        "status": "working",
    }