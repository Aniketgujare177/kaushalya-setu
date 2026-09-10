import React, { useState } from "react";
import { IcoSpark, IcoCheck, IcoX, IcoAlert, IcoArrowUp, IcoTrends, IcoRefresh } from "../components/Icons";

const recommendations = [
  {
    id: 1, title: "Add Cloud Computing to Data Engineering Curriculum",
    reason: "Cloud-related job postings increased 42% in the last 6 months in Pune, Bengaluru and Hyderabad districts.",
    evidence: [
      { label: "Job Postings", value: "2,340", icon: "📋" },
      { label: "Employer Responses", value: "78 firms", icon: "🏢" },
      { label: "Salary Premium", value: "+34%", icon: "💰" },
    ],
    impact: "+18% placement improvement", priority: "P1", category: "Curriculum",
    affectedInstitutes: 14, affectedStudents: 3200,
    confidence: 94, status: "pending",
  },
  {
    id: 2, title: "Reduce Basic Data Entry Training Capacity by 40%",
    reason: "Data Entry job postings declined 28% YoY. Oversupplied — 680 trained vs 220 available positions in Maharashtra.",
    evidence: [
      { label: "Placement Rate", value: "32%", icon: "📉" },
      { label: "Course Capacity", value: "680 seats", icon: "🪑" },
      { label: "Available Jobs", value: "220", icon: "💼" },
    ],
    impact: "Free 460 training seats for high-demand courses", priority: "P2", category: "Capacity",
    affectedInstitutes: 8, affectedStudents: 680,
    confidence: 91, status: "pending",
  },
  {
    id: 3, title: "Upskill 24 Trainers in Generative AI and LLM Technologies",
    reason: "GenAI job postings grew 127% in Q3. No trainers are currently certified in Generative AI across 12 institutes.",
    evidence: [
      { label: "GenAI Jobs", value: "1,840", icon: "🤖" },
      { label: "Certified Trainers", value: "0", icon: "👨‍🏫" },
      { label: "Growth Rate", value: "+127%", icon: "📈" },
    ],
    impact: "Enable training for 1,200+ students in GenAI", priority: "P1", category: "Trainer",
    affectedInstitutes: 12, affectedStudents: 1200,
    confidence: 98, status: "accepted",
  },
  {
    id: 4, title: "Launch Cybersecurity Analyst Course in Pune District",
    reason: "Pune has 380 unfilled Cybersecurity Analyst positions. Zero institutes offer this certification within 50km.",
    evidence: [
      { label: "Unfilled Positions", value: "380", icon: "🔒" },
      { label: "Average Salary", value: "₹8.4L", icon: "💰" },
      { label: "Employer Demand", value: "46 firms", icon: "🏢" },
    ],
    impact: "Address critical talent gap, improve district placement by 12%", priority: "P1", category: "New Course",
    affectedInstitutes: 3, affectedStudents: 450,
    confidence: 87, status: "pending",
  },
  {
    id: 5, title: "Update Python Curriculum from v3.8 to v3.12 Standards",
    reason: "67% of employer surveys require Python 3.10+ features. Current curriculum teaches deprecated patterns.",
    evidence: [
      { label: "Employer Feedback", value: "134 surveys", icon: "📊" },
      { label: "Mismatch Rate", value: "67%", icon: "❗" },
      { label: "Affected Courses", value: "11", icon: "📚" },
    ],
    impact: "Improve candidate-employer skill match by 23%", priority: "P2", category: "Curriculum",
    affectedInstitutes: 11, affectedStudents: 2800,
    confidence: 96, status: "review",
  },
];

const categoryColors: Record<string, { bg: string; color: string }> = {
  Curriculum: { bg: "#EFF6FF", color: "#1D4ED8" },
  Capacity: { bg: "#FFFBEB", color: "#D97706" },
  Trainer: { bg: "#F5F3FF", color: "#7C3AED" },
  "New Course": { bg: "#F0FDFA", color: "#0D9488" },
};

const statusBadge: Record<string, { bg: string; color: string; label: string }> = {
  pending: { bg: "#F1F5F9", color: "#475569", label: "Pending Review" },
  accepted: { bg: "#ECFDF5", color: "#059669", label: "Accepted" },
  review: { bg: "#FFFBEB", color: "#D97706", label: "Under Review" },
  rejected: { bg: "#FEF2F2", color: "#DC2626", label: "Rejected" },
};

export default function AIRecommendations() {
  const [statuses, setStatuses] = useState<Record<number, string>>(
    Object.fromEntries(recommendations.map(r => [r.id, r.status]))
  );

  const updateStatus = (id: number, status: string) => {
    setStatuses(s => ({ ...s, [id]: status }));
  };

  const counts = {
    total: recommendations.length,
    accepted: Object.values(statuses).filter(s => s === "accepted").length,
    pending: Object.values(statuses).filter(s => s === "pending").length,
  };

  return (
    <div style={{ padding: 24, display: "flex", flexDirection: "column", gap: 20 }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
        <div>
          <h1 className="font-display" style={{ fontSize: 22, fontWeight: 700, color: "#0F172A", marginBottom: 4 }}>AI Recommendation Engine</h1>
          <p style={{ fontSize: 13, color: "#64748B" }}>Explainable AI recommendations backed by real labour market evidence</p>
        </div>
        <button className="btn-ai"><IcoRefresh size={13} />Regenerate Insights</button>
      </div>

      {/* Stats */}
      <div style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: 12 }}>
        {[
          { label: "Total Recommendations", value: counts.total, color: "#7C3AED", bg: "#F5F3FF" },
          { label: "Accepted", value: counts.accepted, color: "#059669", bg: "#ECFDF5" },
          { label: "Pending Review", value: counts.pending, color: "#D97706", bg: "#FFFBEB" },
          { label: "Avg. Confidence", value: "93%", color: "#1D4ED8", bg: "#EFF6FF" },
        ].map(s => (
          <div key={s.label} className="kpi-card" style={{ borderLeft: `3px solid ${s.color}` }}>
            <div style={{ fontSize: 26, fontWeight: 700, color: s.color, fontFamily: "'DM Sans', sans-serif" }}>{s.value}</div>
            <div style={{ fontSize: 12, fontWeight: 600, color: "#334155", marginTop: 4 }}>{s.label}</div>
          </div>
        ))}
      </div>

      {/* Recommendation Cards */}
      {recommendations.map(rec => {
        const cat = categoryColors[rec.category];
        const st = statusBadge[statuses[rec.id]];
        return (
          <div key={rec.id} className="chart-card" style={{ borderLeft: `4px solid ${rec.priority === "P1" ? "#7C3AED" : "#1D4ED8"}` }}>
            {/* Header */}
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", marginBottom: 14 }}>
              <div style={{ display: "flex", gap: 10, alignItems: "flex-start" }}>
                <div style={{ width: 36, height: 36, background: "linear-gradient(135deg, #7C3AED, #1D4ED8)", borderRadius: 8, display: "flex", alignItems: "center", justifyContent: "center", flexShrink: 0 }}>
                  <IcoSpark size={16} className="text-white" />
                </div>
                <div>
                  <div style={{ fontSize: 15, fontWeight: 700, color: "#0F172A", marginBottom: 4 }}>{rec.title}</div>
                  <div style={{ display: "flex", gap: 6, flexWrap: "wrap" }}>
                    <span style={{ padding: "2px 8px", background: cat.bg, color: cat.color, borderRadius: 4, fontSize: 11, fontWeight: 600 }}>{rec.category}</span>
                    <span style={{ padding: "2px 8px", background: rec.priority === "P1" ? "#F5F3FF" : "#EFF6FF", color: rec.priority === "P1" ? "#7C3AED" : "#1D4ED8", borderRadius: 4, fontSize: 11, fontWeight: 700 }}>{rec.priority}</span>
                    <span style={{ padding: "2px 8px", background: st.bg, color: st.color, borderRadius: 4, fontSize: 11, fontWeight: 600 }}>{st.label}</span>
                  </div>
                </div>
              </div>
              <div style={{ textAlign: "right" }}>
                <div style={{ fontSize: 20, fontWeight: 700, color: "#7C3AED", fontFamily: "'JetBrains Mono', monospace" }}>{rec.confidence}%</div>
                <div style={{ fontSize: 10, color: "#64748B" }}>AI Confidence</div>
              </div>
            </div>

            {/* Reason */}
            <div style={{ background: "#F8FAFC", borderRadius: 8, padding: "10px 14px", marginBottom: 14 }}>
              <div style={{ fontSize: 11, fontWeight: 700, color: "#64748B", marginBottom: 4, textTransform: "uppercase", letterSpacing: "0.06em" }}>Reason</div>
              <div style={{ fontSize: 13, color: "#334155", lineHeight: 1.5 }}>{rec.reason}</div>
            </div>

            {/* Evidence */}
            <div style={{ marginBottom: 14 }}>
              <div style={{ fontSize: 11, fontWeight: 700, color: "#64748B", marginBottom: 8, textTransform: "uppercase", letterSpacing: "0.06em" }}>Data Evidence</div>
              <div style={{ display: "flex", gap: 10 }}>
                {rec.evidence.map(ev => (
                  <div key={ev.label} style={{ flex: 1, background: "#F5F3FF", borderRadius: 8, padding: "10px 14px", textAlign: "center" }}>
                    <div style={{ fontSize: 18 }}>{ev.icon}</div>
                    <div style={{ fontSize: 16, fontWeight: 700, color: "#4C1D95", fontFamily: "'JetBrains Mono', monospace" }}>{ev.value}</div>
                    <div style={{ fontSize: 11, color: "#7C3AED" }}>{ev.label}</div>
                  </div>
                ))}
              </div>
            </div>

            {/* Impact + Scope */}
            <div style={{ display: "flex", gap: 12, marginBottom: 16 }}>
              <div style={{ flex: 1, background: "#ECFDF5", borderRadius: 8, padding: "10px 14px" }}>
                <div style={{ fontSize: 11, fontWeight: 700, color: "#059669", marginBottom: 2 }}>POTENTIAL IMPACT</div>
                <div style={{ fontSize: 13, fontWeight: 600, color: "#065F46" }}>{rec.impact}</div>
              </div>
              <div style={{ flex: 1, background: "#EFF6FF", borderRadius: 8, padding: "10px 14px" }}>
                <div style={{ fontSize: 11, fontWeight: 700, color: "#1D4ED8", marginBottom: 2 }}>SCOPE</div>
                <div style={{ fontSize: 13, fontWeight: 600, color: "#1E40AF" }}>{rec.affectedInstitutes} Institutes · {rec.affectedStudents.toLocaleString()} Students</div>
              </div>
            </div>

            {/* Actions */}
            <div style={{ display: "flex", gap: 8 }}>
              <button className="btn-primary" style={{ fontSize: 12 }} onClick={() => updateStatus(rec.id, "accepted")}>
                <IcoCheck size={12} />Accept
              </button>
              <button className="btn-secondary" style={{ fontSize: 12 }} onClick={() => updateStatus(rec.id, "review")}>
                Review
              </button>
              <button style={{ padding: "7px 14px", fontSize: 12, fontWeight: 600, border: "1px solid #FECACA", background: "#FEF2F2", color: "#DC2626", borderRadius: 8, cursor: "pointer", display: "flex", alignItems: "center", gap: 6 }} onClick={() => updateStatus(rec.id, "rejected")}>
                <IcoX size={12} />Reject
              </button>
              <button className="btn-secondary" style={{ fontSize: 12, marginLeft: "auto" }}>
                Generate Report
              </button>
            </div>
          </div>
        );
      })}
    </div>
  );
}
