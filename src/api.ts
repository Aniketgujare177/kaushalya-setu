const API_BASE_URL = "http://127.0.0.1:8000/api";

async function request<T>(
    endpoint: string,
    options: RequestInit = {}
): Promise<T> {
    const response = await fetch(
        `${API_BASE_URL}${endpoint}`,
        {
            headers: {
                "Content-Type": "application/json",
                ...(options.headers || {}),
            },
            ...options,
        }
    );

    if (!response.ok) {
        const errorText = await response.text();

        throw new Error(
            errorText || `API Error: ${response.status}`
        );
    }

    return response.json();
}


// ============================================================
// HEALTH
// ============================================================

export const healthAPI = {
    check: () =>
        request("/health"),
};


// ============================================================
// DASHBOARD
// ============================================================

export const dashboardAPI = {
    getAnalytics: () =>
        request("/dashboard"),
};


// ============================================================
// STUDENTS
// ============================================================

export const studentsAPI = {
    getAll: (search?: string) =>
        request(
            search
                ? `/students/?search=${encodeURIComponent(search)}`
                : "/students/"
        ),

    getById: (id: number) =>
        request(`/students/${id}`),
};


// ============================================================
// CURRICULUM
// ============================================================

export const curriculumAPI = {
    getAll: (search?: string, course?: string) => {
        const params = new URLSearchParams();

        if (search) {
            params.append("search", search);
        }

        if (course) {
            params.append("course", course);
        }

        const query = params.toString();

        return request(
            `/curriculum/${query ? `?${query}` : ""}`
        );
    },

    getById: (id: number) =>
        request(`/curriculum/${id}`),

    getSummary: () =>
        request("/curriculum/analytics/summary"),

    getNeedsUpdate: () =>
        request("/curriculum/analytics/needs-update"),

    getTopAligned: () =>
        request("/curriculum/analytics/top-aligned"),
};


// ============================================================
// SKILLS
// ============================================================

export const skillsAPI = {
    getAll: () =>
        request("/skills/"),

    getById: (id: number) =>
        request(`/skills/${id}`),
};


// ============================================================
// JOBS
// ============================================================

export const jobsAPI = {
    getAll: () =>
        request("/jobs/"),

    getById: (id: number) =>
        request(`/jobs/${id}`),
};


// ============================================================
// ANALYTICS
// ============================================================

export const analyticsAPI = {
    dashboard: () =>
        request("/analytics/dashboard"),

    readiness: () =>
        request("/analytics/readiness"),

    curriculumAlignment: () =>
        request("/analytics/curriculum-alignment"),

    courses: () =>
        request("/analytics/courses"),

    skills: () =>
        request("/analytics/skills"),
};


// ============================================================
// AUTHENTICATION
// ============================================================

export const authAPI = {
    login: (email: string, password: string) =>
        request("/auth/login", {
            method: "POST",
            body: JSON.stringify({
                email,
                password,
            }),
        }),

    register: (
        name: string,
        email: string,
        password: string,
        role = "student"
    ) =>
        request("/auth/register", {
            method: "POST",
            body: JSON.stringify({
                name,
                email,
                password,
                role,
            }),
        }),

    verify: (token: string) =>
        request("/auth/verify", {
            method: "POST",
            body: JSON.stringify({
                token,
            }),
        }),

    me: (token: string) =>
        request("/auth/me", {
            method: "POST",
            body: JSON.stringify({
                token,
            }),
        }),

    logout: () =>
        request("/auth/logout", {
            method: "POST",
        }),
};