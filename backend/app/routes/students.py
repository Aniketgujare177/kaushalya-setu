from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional


router = APIRouter()


# ============================================================
# STUDENT DATA
# ============================================================

STUDENTS = [
    {
        "id": 1,
        "name": "Aarav Sharma",
        "email": "aarav.sharma@example.com",
        "course": "Computer Engineering",
        "year": 3,
        "college": "Engineering Program",
        "skill_score": 82,
        "industry_readiness": 85,
        "status": "Industry Ready",
        "skills": [
            "Python",
            "Java",
            "SQL",
            "Problem Solving",
        ],
        "skill_gaps": [
            "Generative AI",
            "Cloud Computing",
        ],
    },
    {
        "id": 2,
        "name": "Priya Patil",
        "email": "priya.patil@example.com",
        "course": "Information Technology",
        "year": 3,
        "college": "Engineering Program",
        "skill_score": 74,
        "industry_readiness": 72,
        "status": "Developing",
        "skills": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
        ],
        "skill_gaps": [
            "Backend Development",
            "Cloud Deployment",
        ],
    },
    {
        "id": 3,
        "name": "Rahul Deshmukh",
        "email": "rahul.deshmukh@example.com",
        "course": "Computer Science",
        "year": 2,
        "college": "Engineering Program",
        "skill_score": 61,
        "industry_readiness": 58,
        "status": "Needs Training",
        "skills": [
            "Python",
            "C++",
            "Data Structures",
        ],
        "skill_gaps": [
            "Advanced DSA",
            "Machine Learning",
            "Git",
        ],
    },
    {
        "id": 4,
        "name": "Sneha Kulkarni",
        "email": "sneha.kulkarni@example.com",
        "course": "Computer Engineering",
        "year": 4,
        "college": "Engineering Program",
        "skill_score": 91,
        "industry_readiness": 94,
        "status": "Industry Ready",
        "skills": [
            "Java",
            "Spring Boot",
            "SQL",
            "REST API",
        ],
        "skill_gaps": [
            "Microservices",
        ],
    },
]


# ============================================================
# REQUEST MODELS
# ============================================================

class StudentCreate(BaseModel):
    name: str
    email: str
    course: str
    year: int
    college: str = "Engineering Program"
    skill_score: int = 50
    industry_readiness: int = 50
    skills: list[str] = []
    skill_gaps: list[str] = []


class StudentUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    course: Optional[str] = None
    year: Optional[int] = None
    college: Optional[str] = None
    skill_score: Optional[int] = None
    industry_readiness: Optional[int] = None
    skills: Optional[list[str]] = None
    skill_gaps: Optional[list[str]] = None


# ============================================================
# HELPER FUNCTION
# ============================================================

def calculate_status(industry_readiness: int) -> str:

    if industry_readiness >= 80:
        return "Industry Ready"

    elif industry_readiness >= 65:
        return "Developing"

    return "Needs Training"


# ============================================================
# GET ALL STUDENTS
# ============================================================

@router.get("/")
def get_students(
    search: Optional[str] = None,
    course: Optional[str] = None,
    status: Optional[str] = None,
):

    results = STUDENTS.copy()

    # --------------------------------------------------------
    # SEARCH
    # --------------------------------------------------------

    if search:

        text = search.lower()

        results = [
            student
            for student in results
            if text in student["name"].lower()
            or text in student["email"].lower()
            or text in student["course"].lower()
            or text in student["college"].lower()
        ]

    # --------------------------------------------------------
    # COURSE FILTER
    # --------------------------------------------------------

    if course:

        results = [
            student
            for student in results
            if student["course"].lower()
            == course.lower()
        ]

    # --------------------------------------------------------
    # STATUS FILTER
    # --------------------------------------------------------

    if status:

        results = [
            student
            for student in results
            if student["status"].lower()
            == status.lower()
        ]

    return {
        "success": True,
        "count": len(results),
        "data": results,
    }


# ============================================================
# STUDENT STATUS CHECK
# ============================================================

@router.get("/status/check")
def student_status():

    return {
        "success": True,
        "module": "students",
        "status": "working",
    }


# ============================================================
# STUDENT STATISTICS
# ============================================================

@router.get("/analytics/summary")
def student_summary():

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

    industry_ready = sum(
        1
        for student in STUDENTS
        if student["industry_readiness"] >= 80
    )

    developing = sum(
        1
        for student in STUDENTS
        if 65 <= student["industry_readiness"] < 80
    )

    needs_training = sum(
        1
        for student in STUDENTS
        if student["industry_readiness"] < 65
    )

    average_skill_score = round(
        sum(
            student["skill_score"]
            for student in STUDENTS
        ) / total
    )

    average_industry_readiness = round(
        sum(
            student["industry_readiness"]
            for student in STUDENTS
        ) / total
    )

    return {
        "success": True,
        "data": {
            "total_students": total,
            "industry_ready": industry_ready,
            "developing": developing,
            "needs_training": needs_training,
            "average_skill_score": average_skill_score,
            "average_industry_readiness":
                average_industry_readiness,
        },
    }


# ============================================================
# INDUSTRY READY STUDENTS
# ============================================================

@router.get("/analytics/industry-ready")
def industry_ready_students():

    results = [
        student
        for student in STUDENTS
        if student["industry_readiness"] >= 80
    ]

    return {
        "success": True,
        "count": len(results),
        "data": results,
    }


# ============================================================
# STUDENTS NEEDING TRAINING
# ============================================================

@router.get("/analytics/needs-training")
def students_needing_training():

    results = [
        student
        for student in STUDENTS
        if student["industry_readiness"] < 65
    ]

    return {
        "success": True,
        "count": len(results),
        "data": results,
    }


# ============================================================
# TOP STUDENTS
# ============================================================

@router.get("/analytics/top")
def top_students():

    results = sorted(
        STUDENTS,
        key=lambda student:
            student["industry_readiness"],
        reverse=True,
    )

    return {
        "success": True,
        "count": len(results),
        "data": results,
    }


# ============================================================
# GET STUDENT BY ID
# ============================================================

@router.get("/{student_id}")
def get_student_by_id(student_id: int):

    student = next(
        (
            item
            for item in STUDENTS
            if item["id"] == student_id
        ),
        None,
    )

    if student is None:

        raise HTTPException(
            status_code=404,
            detail="Student not found",
        )

    return {
        "success": True,
        "data": student,
    }


# ============================================================
# CREATE STUDENT
# ============================================================

@router.post("/")
def create_student(
    request: StudentCreate,
):

    new_id = (
        max(
            student["id"]
            for student in STUDENTS
        ) + 1
        if STUDENTS
        else 1
    )

    status = calculate_status(
        request.industry_readiness
    )

    new_student = {
        "id": new_id,
        "name": request.name,
        "email": request.email,
        "course": request.course,
        "year": request.year,
        "college": request.college,
        "skill_score": request.skill_score,
        "industry_readiness":
            request.industry_readiness,
        "status": status,
        "skills": request.skills,
        "skill_gaps": request.skill_gaps,
    }

    STUDENTS.append(new_student)

    return {
        "success": True,
        "message": "Student created successfully",
        "data": new_student,
    }


# ============================================================
# UPDATE STUDENT
# ============================================================

@router.put("/{student_id}")
def update_student(
    student_id: int,
    request: StudentUpdate,
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

        raise HTTPException(
            status_code=404,
            detail="Student not found",
        )

    update_data = request.model_dump(
        exclude_none=True
    )

    for key, value in update_data.items():

        student[key] = value

    # Recalculate status after update
    student["status"] = calculate_status(
        student["industry_readiness"]
    )

    return {
        "success": True,
        "message": "Student updated successfully",
        "data": student,
    }


# ============================================================
# DELETE STUDENT
# ============================================================

@router.delete("/{student_id}")
def delete_student(student_id: int):

    student = next(
        (
            item
            for item in STUDENTS
            if item["id"] == student_id
        ),
        None,
    )

    if student is None:

        raise HTTPException(
            status_code=404,
            detail="Student not found",
        )

    STUDENTS.remove(student)

    return {
        "success": True,
        "message": "Student deleted successfully",
    }