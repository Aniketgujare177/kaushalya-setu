import React, { useState } from "react";
import { IcoSpark, IcoCheck, IcoX, IcoAlert, IcoBook, IcoArrowUp } from "../components/Icons";

const courses = [
  {
    id: 1, name: "Data Analytics", institute: "NIELIT Pune", alignmentScore: 78,
    current: ["Excel", "Basic Statistics", "SQL", "Data Entry"],
    required: ["Python", "Power BI", "Advanced SQL", "Data Visualization", "ML Basics"],
    aiRec: "Add Python and Power BI modules; upgrade SQL from basic to advanced analytics.",
    actions: ["Add Python Module", "Add Power BI Module", "Remove Basic Data Entry", "Update Assessment to Project-Based"],
    status: "needs-update",
  },
  {
    id: 2, name: "Full-Stack Web Development", institute: "CDAC Bengaluru", alignmentScore: 91,
    current: ["HTML/CSS", "JavaScript", "React", "Node.js", "MongoDB"],
    required: ["TypeScript", "Next.js", "Docker", "CI/CD", "React"],
    aiRec: "Add TypeScript and Docker. Include CI/CD pipeline project as capstone.",
    actions: ["Add TypeScript", "Add Docker Basics", "Add CI/CD Lab"],
    status: "good",
  },
  {
    id: 3, name: "Digital Marketing", institute: "SSC Hyderabad", alignmentScore: 54,
    current: ["Facebook Ads", "Google Ads Basic", "Email Marketing"],
    required: ["SEO/SEM Advanced", "Analytics (GA4)", "Content Marketing", "AI Tools", "Video Marketing", "Influencer Marketing"],
    aiRec: "Major overhaul required. Add GA4 analytics, AI-powered marketing tools and video content creation.",
    actions: ["Add GA4 Analytics", "Add AI Marketing Tools", "Add Video Production", "Remove Outdated Facebook Basics"],
    status: "critical",
  },
  {
    id: 4, name: "Cloud Engineering", institute: "NASSCOM Foundation", alignmentScore: 35,
    current: ["Basic Networking", "Linux CLI", "Server Admin"],
    required: ["AWS/Azure/GCP", "Kubernetes", "Terraform", "Serverless", "Cloud Security", "DevOps"],
    aiRec: "Curriculum is severely outdated. Requires complete redesign around cloud-native technologies.",
    actions: ["Complete Curriculum Redesign", "Add AWS/Azure Hands-on Labs", "Add Kubernetes", "Add Cloud Security"],
    status: "critical",
  },
];

const statusStyle: Record<string, { color: string; bg: string; label: string }> = {
  "good": { color: "#059669", bg: "#ECFDF5", label: "Well-Aligned" },
  "needs-update": { color: "#D97706", bg: "#FFFBEB", label: "Needs Update" },
  "critical": { color: "#DC2626", bg: "#FEF2F2", label: "Critical Misalignment" },
};

const scoreColor = (score: number) => score >= 80 ? "#059669" : score >= 60 ? "#D97706" : "#DC2626";

export default function CurriculumAlignment() {
  const [expanded, setExpanded] = useState<number | null>(1);
  const [accepted, setAccepted] = useState<Record<string, boolean>>({});

  return (
    <div style={{ padding: 24, display: "flex", flexDirection: "column", gap: 20 }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
        <div>
          <h1 className="font-display" style={{ fontSize: 22, fontWeight: 700, color: "#0F172A", marginBottom: 4 }}>Curriculum Alignment Engine</h1>
          <p style={{ fontSize: 13, color: "#64748B" }}>AI-powered comparison of current curricula vs industry requirements with actionable recommendations</p>
        </div>
        <button className="btn-ai"><IcoSpark size={13} />Run Alignment Analysis</button>
      </div>

      {/* Summary */}
      <div style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: 12 }}>
        {[
          { label: "Avg. Alignment Score", value: "64%", color: "#D97706" },
          { label: "Courses Analyzed", value: "47", color: "#1D4ED8" },
          { label: "Courses Needing Update", value: "12", color: "#DC2626" },
          { label: "AI Recommendations", value: "34", color: "#7C3AED" },
        ].map(s => (
          <div key={s.label} className="kpi-card">
            <div style={{ fontSize: 28, fontWeight: 700, color: s.color, fontFamily: "'DM Sans', sans-serif" }}>{s.value}</div>
            <div style={{ fontSize: 12, fontWeight: 600, color: "#334155", marginTop: 4 }}>{s.label}</div>
          </div>
        ))}
      </div>

      {/* Course Cards */}
      {courses.map(course => {
        const isOpen = expanded === course.id;
        const st = statusStyle[course.status];
        const sc = scoreColor(course.alignmentScore);
        return (
          <div key={course.id} className="chart-card" style={{ cursor: "pointer" }}>
            <div onClick={() => setExpanded(isOpen ? null : course.id)} style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
              <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
                <div style={{ width: 40, height: 40, background: "#F8FAFC", borderRadius: 10, display: "flex", alignItems: "center", justifyContent: "center" }}>
                  <IcoBook size={18} style={{ color: "#1D4ED8" }} />
                </div>
                <div>
                  <div style={{ fontSize: 15, fontWeight: 700, color: "#0F172A" }}>{course.name}</div>
                  <div style={{ fontSize: 12, color: "#64748B" }}>{course.institute}</div>
                </div>
              </div>
              <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
                {/* Score Arc */}
                <div style={{ textAlign: "center" }}>
                  <div style={{ fontSize: 22, fontWeight: 700, color: sc, fontFamily: "'DM Sans', sans-serif" }}>{course.alignmentScore}%</div>
                  <div style={{ fontSize: 10, color: "#64748B" }}>Alignment</div>
                </div>
                <div style={{ width: 1, height: 36, background: "#E2E8F0" }} />
                <span style={{ padding: "4px 10px", background: st.bg, color: st.color, borderRadius: 6, fontSize: 12, fontWeight: 600 }}>{st.label}</span>
                <span style={{ fontSize: 16, color: "#94A3B8" }}>{isOpen ? "▲" : "▼"}</span>
              </div>
            </div>

            {isOpen && (
              <div style={{ marginTop: 20, paddingTop: 20, borderTop: "1px solid #F1F5F9" }}>
                {/* Progress bar */}
                <div style={{ marginBottom: 16 }}>
                  <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 6 }}>
                    <span style={{ fontSize: 12, fontWeight: 600, color: "#334155" }}>Curriculum Alignment Score</span>
                    <span style={{ fontSize: 13, fontWeight: 700, color: sc, fontFamily: "'JetBrains Mono', monospace" }}>{course.alignmentScore}/100</span>
                  </div>
                  <div className="progress-bar">
                    <div className="progress-fill" style={{ width: `${course.alignmentScore}%`, background: sc }} />
                  </div>
                </div>

                <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 16, marginBottom: 16 }}>
                  {/* Current Skills */}
                  <div style={{ background: "#F8FAFC", borderRadius: 10, padding: 16 }}>
                    <div style={{ fontSize: 12, fontWeight: 700, color: "#64748B", marginBottom: 10, textTransform: "uppercase", letterSpacing: "0.05em" }}>Current Curriculum</div>
                    <div style={{ display: "flex", flexWrap: "wrap", gap: 6 }}>
                      {course.current.map(s => (
                        <span key={s} style={{ padding: "4px 10px", background: "#E2E8F0", color: "#475569", borderRadius: 20, fontSize: 12, fontWeight: 500 }}>{s}</span>
                      ))}
                    </div>
                  </div>
                  {/* Required Skills */}
                  <div style={{ background: "#EFF6FF", borderRadius: 10, padding: 16 }}>
                    <div style={{ fontSize: 12, fontWeight: 700, color: "#1D4ED8", marginBottom: 10, textTransform: "uppercase", letterSpacing: "0.05em" }}>Industry Requirements</div>
                    <div style={{ display: "flex", flexWrap: "wrap", gap: 6 }}>
                      {course.required.map(s => {
                        const isInCurrent = course.current.some(c => c.toLowerCase().includes(s.toLowerCase().split(" ")[0]));
                        return (
                          <span key={s} style={{ padding: "4px 10px", background: isInCurrent ? "#ECFDF5" : "#DBEAFE", color: isInCurrent ? "#059669" : "#1D4ED8", borderRadius: 20, fontSize: 12, fontWeight: 600 }}>
                            {isInCurrent ? "✓ " : "+ "}{s}
                          </span>
                        );
                      })}
                    </div>
                  </div>
                </div>

                {/* AI Recommendation */}
                <div className="ai-card" style={{ marginBottom: 16 }}>
                  <div style={{ display: "flex", gap: 10 }}>
                    <div style={{ width: 28, height: 28, background: "#7C3AED", borderRadius: 6, display: "flex", alignItems: "center", justifyContent: "center", flexShrink: 0 }}>
                      <IcoSpark size={14} className="text-white" />
                    </div>
                    <div>
                      <div style={{ fontSize: 12, fontWeight: 700, color: "#4C1D95", marginBottom: 4 }}>AI Recommendation</div>
                      <div style={{ fontSize: 13, color: "#334155" }}>{course.aiRec}</div>
                    </div>
                  </div>
                </div>

                {/* Actions */}
                <div>
                  <div style={{ fontSize: 12, fontWeight: 700, color: "#334155", marginBottom: 10 }}>Recommended Actions</div>
                  <div style={{ display: "flex", flexWrap: "wrap", gap: 8 }}>
                    {course.actions.map(action => {
                      const key = `${course.id}-${action}`;
                      const done = accepted[key];
                      return (
                        <button key={action} onClick={e => { e.stopPropagation(); setAccepted(a => ({ ...a, [key]: !done })); }}
                          style={{ display: "flex", alignItems: "center", gap: 6, padding: "6px 12px", borderRadius: 8, fontSize: 12, fontWeight: 600, cursor: "pointer", border: done ? "none" : "1px dashed #CBD5E1", background: done ? "#ECFDF5" : "white", color: done ? "#059669" : "#475569" }}>
                          {done ? <IcoCheck size={12} /> : <IcoArrowUp size={12} />}
                          {action}
                        </button>
                      );
                    })}
                  </div>
                </div>

                <div style={{ display: "flex", gap: 8, marginTop: 16 }}>
                  <button className="btn-primary" style={{ fontSize: 12 }}>Accept All Recommendations</button>
                  <button className="btn-secondary" style={{ fontSize: 12 }}>Generate Update Report</button>
                  <button className="btn-secondary" style={{ fontSize: 12 }}>Review</button>
                </div>
              </div>
            )}
          </div>
        );
      })}
    </div>
  );
}
