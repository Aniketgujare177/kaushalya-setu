import React, { useState } from "react";

const API_URL =
    import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

interface LoginProps {
    onLogin: () => void;
}

interface LoginResponse {
    success: boolean;
    message: string;
    data?: {
        access_token: string;
        token_type: string;
        user: {
            id: number;
            name: string;
            email: string;
            role: string;
        };
    };
}

export default function Login({ onLogin }: LoginProps) {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    async function handleLogin(
        event: React.FormEvent<HTMLFormElement>
    ) {
        event.preventDefault();

        setError("");

        if (!email.trim()) {
            setError("Please enter your email.");
            return;
        }

        if (!password) {
            setError("Please enter your password.");
            return;
        }

        try {
            setLoading(true);

            const response = await fetch(
                `${API_URL}/api/auth/login`,
                {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json",
                        Accept: "application/json",
                    },

                    body: JSON.stringify({
                        email: email.trim(),
                        password,
                    }),
                }
            );

            const data: LoginResponse = await response.json();

            console.log("LOGIN STATUS:", response.status);
            console.log("LOGIN RESPONSE:", data);

            if (!response.ok) {
                throw new Error(
                    typeof data?.message === "string"
                        ? data.message
                        : "Invalid email or password"
                );
            }

            const accessToken =
                data?.data?.access_token;

            const user =
                data?.data?.user;

            if (!accessToken) {
                throw new Error(
                    "Login successful, but token was not received."
                );
            }

            // Save authentication
            localStorage.setItem(
                "access_token",
                accessToken
            );

            // Save user
            if (user) {
                localStorage.setItem(
                    "user",
                    JSON.stringify(user)
                );

                // Save backend role
                localStorage.setItem(
                    "role",
                    user.role
                );
            }

            console.log("LOGIN SUCCESS");
            console.log("USER:", user);

            // Tell App.tsx to show dashboard
            onLogin();

        } catch (error: any) {
            console.error(
                "LOGIN ERROR:",
                error
            );

            setError(
                error?.message ||
                "Unable to connect to backend."
            );

        } finally {
            setLoading(false);
        }
    }

    return (
        <div
            style={{
                minHeight: "100vh",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                background: "#F0F4F8",
                padding: 24,
            }}
        >
            <div
                style={{
                    width: "100%",
                    maxWidth: 420,
                    background: "#FFFFFF",
                    borderRadius: 16,
                    padding: 32,
                    boxShadow:
                        "0 10px 30px rgba(15, 23, 42, 0.10)",
                    border: "1px solid #E2E8F0",
                }}
            >

                {/* LOGO */}

                <div
                    style={{
                        textAlign: "center",
                        marginBottom: 28,
                    }}
                >
                    <div
                        style={{
                            width: 52,
                            height: 52,
                            margin: "0 auto 14px",
                            borderRadius: 14,
                            background: "#1D4ED8",
                            color: "#FFFFFF",
                            display: "flex",
                            alignItems: "center",
                            justifyContent: "center",
                            fontSize: 22,
                            fontWeight: 700,
                        }}
                    >
                        LM
                    </div>

                    <h1
                        style={{
                            margin: 0,
                            fontSize: 24,
                            fontWeight: 700,
                            color: "#0F172A",
                        }}
                    >
                        Labour Market Platform
                    </h1>

                    <p
                        style={{
                            marginTop: 8,
                            marginBottom: 0,
                            fontSize: 13,
                            color: "#64748B",
                        }}
                    >
                        Sign in to continue
                    </p>
                </div>

                {/* ERROR */}

                {error && (
                    <div
                        style={{
                            marginBottom: 18,
                            padding: "10px 12px",
                            borderRadius: 8,
                            background: "#FEF2F2",
                            border: "1px solid #FECACA",
                            color: "#B91C1C",
                            fontSize: 13,
                        }}
                    >
                        {error}
                    </div>
                )}

                {/* FORM */}

                <form onSubmit={handleLogin}>

                    {/* EMAIL */}

                    <div
                        style={{
                            marginBottom: 16,
                        }}
                    >
                        <label
                            style={{
                                display: "block",
                                marginBottom: 7,
                                fontSize: 13,
                                fontWeight: 600,
                                color: "#334155",
                            }}
                        >
                            Email
                        </label>

                        <input
                            type="email"
                            value={email}
                            onChange={(event) =>
                                setEmail(event.target.value)
                            }
                            placeholder="Enter your email"
                            autoComplete="email"
                            disabled={loading}
                            style={{
                                width: "100%",
                                boxSizing: "border-box",
                                padding: "11px 12px",
                                border: "1px solid #CBD5E1",
                                borderRadius: 8,
                                outline: "none",
                                fontSize: 14,
                                color: "#0F172A",
                            }}
                        />
                    </div>

                    {/* PASSWORD */}

                    <div
                        style={{
                            marginBottom: 22,
                        }}
                    >
                        <label
                            style={{
                                display: "block",
                                marginBottom: 7,
                                fontSize: 13,
                                fontWeight: 600,
                                color: "#334155",
                            }}
                        >
                            Password
                        </label>

                        <input
                            type="password"
                            value={password}
                            onChange={(event) =>
                                setPassword(event.target.value)
                            }
                            placeholder="Enter your password"
                            autoComplete="current-password"
                            disabled={loading}
                            style={{
                                width: "100%",
                                boxSizing: "border-box",
                                padding: "11px 12px",
                                border: "1px solid #CBD5E1",
                                borderRadius: 8,
                                outline: "none",
                                fontSize: 14,
                                color: "#0F172A",
                            }}
                        />
                    </div>

                    {/* LOGIN BUTTON */}

                    <button
                        type="submit"
                        disabled={loading}
                        style={{
                            width: "100%",
                            border: "none",
                            borderRadius: 8,
                            padding: "12px 16px",
                            background: loading
                                ? "#93C5FD"
                                : "#1D4ED8",
                            color: "#FFFFFF",
                            fontSize: 14,
                            fontWeight: 600,
                            cursor: loading
                                ? "not-allowed"
                                : "pointer",
                        }}
                    >
                        {loading
                            ? "Signing in..."
                            : "Sign In"}
                    </button>

                </form>

                {/* DEMO LOGIN */}

                <div
                    style={{
                        marginTop: 20,
                        padding: 12,
                        background: "#F8FAFC",
                        borderRadius: 8,
                        fontSize: 11,
                        color: "#64748B",
                    }}
                >
                    <strong>Demo Login</strong>

                    <div style={{ marginTop: 5 }}>
                        Email: admin@example.com
                    </div>

                    <div>
                        Password: admin123
                    </div>
                </div>

            </div>
        </div>
    );
}