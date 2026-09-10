import React, { useState } from "react";
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis, Radar } from "recharts";
import { IcoFilter, IcoDownload, IcoAlert, IcoSpark } from "../components/Icons";

const gapData = [
  { skill: "Python", required: 90, available: 55, gap: 35 },
  { skill: "Cloud", required: 80, available: 30, gap: 50 },
  { skill: "ML/AI", required: 75, available: 25, gap: 50 },
  { skill: "SQL", required: 85, available: 80, gap: 5 },
  { skill: "Power BI", required: 70, available: 40, gap: 30 },
  { skill: "DevOps", required: 65, available: 28, gap: 37 },
  { skill: "React", required: 72, available: 60, gap: 12 },
  { skill: "Excel", required: 85, available: 90, gap: -5 },
];

const radarData = [
  { skill: "Technical", industry: 85, supply: 55 },
  { skill: "Digital", industry: 80, supply: 45 },
  { skill: "Analytical", industry: 75, supply: 60 },
  { skill: "Communication", industry: 70, supply: 72 },
  { skill: "Management", industry: 60, supply: 55 },
  { skill: "Domain", industry: 78, supply: 50 },
];

const tableData = [
  { skill: "Cloud Computing", role: "Cloud Architect", district: "Pune", reqProf: "Advanced", currProf: "Beginner", gap: "Critical", demand: 1620, supply: 180, priority: "P1", course: "AWS/Azure Fundamentals" },
  { skill: "Machine Learning", role: "AI/ML Engineer", district: "Bengaluru", reqProf: "Intermediate", currProf: "Basic", gap: "Critical", demand: 1120, supply: 95, priority: "P1", course: "ML Engineering Cert." },
  { skill: "Python (Advanced)", role: "Data Engineer", district: "Hyderabad", reqProf: "Advanced", currProf: "Intermediate", gap: "High", demand: 1840, supply: 920, priority: "P2", course: "Advanced Python for Data" },
  { skill: "Power BI", role: "Data Analyst", district: "Mumbai", reqProf: "Intermediate", currProf: "Beginner", gap: "High", demand: 980, supply: 340, priority: "P2", course: "Power BI Professional" },
  { skill: "DevOps / CI-CD", role: "DevOps Engineer", district: "Chennai", reqProf: "Intermediate", currProf: "None", gap: "High", demand: 760, supply: 120, priority: "P2", course: "DevOps with Docker & K8s" },
  { skill: "SQL (Advanced)", role: "Data Analyst", district: "Kolkata", reqProf: "Advanced", currProf: "Intermediate", gap: "Medium", demand: 840, supply: 580, priority: "P3", course: "Advanced SQL & Analytics" },
  { skill: "React.js", role: "Frontend Dev", district: "Ahmedabad", reqProf: "Intermediate", currProf: "Intermediate", gap: "Low", demand: 620, supply: 490, priority: "P4", course: "React Advanced Patterns" },
  { skill: "Excel / Spreadsheets", role: "Data Analyst", district: "Jaipur", reqProf: "Advanced", currProf: "Advanced", gap: "None", demand: 540, supply: 680, priority: "P5", course: "—" },
];

const gapColors: Record<string, string> = {
  Critical: "badge-critical",
  High: "badge-high",
  Medium: "badge-medium",
  Low: "badge-low",
  None: "badge-teal",
};

const summaryCards = [
  { label: "Critical Gaps", count: 2, color: "#DC2626", bg: "#FEF2F2" },
  { label: "High Gaps", count: 3, color: "#D97706", bg: "#FFFBEB" },
  { label: "Medium Gaps", count: 1, color: "#1D4ED8", bg: "#EFF6FF" },
  { label: "Low / No Gap", count: 2, color: "#059669", bg: "#ECFDF5" },
];

export default function SkillGapAnalysis() {
  const [activeFilter, setActiveFilter] = useState("All");

  return (
    <div style={{ padding: 24, display: "flex", flexDirection: "column", gap: 20 }}>
      {/* Header */}
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
        <div>
          <h1 className="font-display" style={{ fontSize: 22, fontWeight: 700, color: "#0F172A", marginBottom: 4 }}>Skill Gap Analysis</h1>
          <p style={{ fontSize: 13, color: "#64748B" }}>Industry Demand vs Training Supply vs Candidate Skills</p>
        </div>
        <div style={{ display: "flex", gap: 8 }}>
          <button className="btn-secondary"><IcoFilter size={13} />Filters</button>
          <button className="btn-secondary"><IcoDownload size={13} />Export</button>
          <button className="btn-ai"><IcoSpark size={13} />AI Gap Analysis</button>
        </div>
      </div>

      {/* Summary Cards */}
      <div style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: 12 }}>
        {summaryCards.map(s => (
          <div key={s.label} className="kpi-card" style={{ borderTop: `3px solid ${s.color}` }}>
            <div style={{ fontSize: 28, fontWeight: 700, color: s.color, fontFamily: "'DM Sans', sans-serif" }}>{s.count}</div>
            <div style={{ fontSize: 13, fontWeight: 600, color: "#334155" }}>{s.label}</div>
            <div style={{ marginTop: 8, height: 4, background: `${s.color}20`, borderRadius: 2 }}>
              <div style={{ height: "100%", width: `${(s.count / 8) * 100}%`, background: s.color, borderRadius: 2 }} />
            </div>
          </div>
        ))}
      </div>

      {/* Charts Row */}
      <div style={{ display: "grid", gridTemplateColumns: "3fr 2fr", gap: 16 }}>
        <div className="chart-card">
          <div className="section-header" style={{ fontSize: 15, marginBottom: 4 }}>Skill Demand vs Supply Gap</div>
          <div className="section-sub" style={{ marginBottom: 16 }}>Proficiency level comparison (0–100 scale)</div>
          <ResponsiveContainer width="100%" height={240}>
            <BarChart data={gapData} layout="vertical">
              <CartesianGrid strokeDasharray="3 3" stroke="#F1F5F9" horizontal={false} />
              <XAxis type="number" domain={[0, 100]} tick={{ fontSize: 10, fill: "#94A3B8" }} axisLine={false} tickLine={false} />
              <YAxis type="category" dataKey="skill" tick={{ fontSize: 11, fill: "#334155" }} axisLine={false} tickLine={false} width={70} />
              <Tooltip contentStyle={{ fontSize: 12, borderRadius: 8, border: "1px solid #E2E8F0" }} />
              <Legend wrapperStyle={{ fontSize: 11 }} />
              <Bar dataKey="required" fill="#1D4ED8" name="Industry Required" radius={[0, 3, 3, 0]} />
              <Bar dataKey="available" fill="#0D9488" name="Currently Available" radius={[0, 3, 3, 0]} />
            </BarChart>
          </ResponsiveContainer>
        </div>
        <div className="chart-card">
          <div className="section-header" style={{ fontSize: 15, marginBottom: 4 }}>Competency Radar</div>
          <div className="section-sub" style={{ marginBottom: 8 }}>Industry demand vs training supply across domains</div>
          <ResponsiveContainer width="100%" height={240}>
            <RadarChart data={radarData}>
              <PolarGrid stroke="#E2E8F0" />
              <PolarAngleAxis dataKey="skill" tick={{ fontSize: 10, fill: "#64748B" }} />
              <PolarRadiusAxis angle={90} domain={[0, 100]} tick={{ fontSize: 9, fill: "#94A3B8" }} />
              <Radar name="Industry Demand" dataKey="industry" stroke="#1D4ED8" fill="#1D4ED8" fillOpacity={0.15} />
              <Radar name="Training Supply" dataKey="supply" stroke="#0D9488" fill="#0D9488" fillOpacity={0.15} />
              <Legend wrapperStyle={{ fontSize: 11 }} />
              <Tooltip contentStyle={{ fontSize: 12, borderRadius: 8 }} />
            </RadarChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* Gap Table */}
      <div className="chart-card">
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 16 }}>
          <div>
            <div className="section-header" style={{ fontSize: 15 }}>Skill Gap Detail Table</div>
            <div className="section-sub">District-level demand, supply and priority recommendations</div>
          </div>
          <div style={{ display: "flex", gap: 6 }}>
            {["All", "Critical", "High", "Medium", "Low"].map(f => (
              <button key={f} onClick={() => setActiveFilter(f)}
                style={{ padding: "4px 12px", fontSize: 11, fontWeight: 600, borderRadius: 20, cursor: "pointer", border: f === activeFilter ? "none" : "1px solid #E2E8F0", background: f === activeFilter ? "#1D4ED8" : "white", color: f === activeFilter ? "white" : "#64748B" }}>
                {f}
              </button>
            ))}
          </div>
        </div>
        <div style={{ overflowX: "auto" }}>
          <table style={{ width: "100%", borderCollapse: "collapse" }}>
            <thead>
              <tr style={{ background: "#F8FAFC" }}>
                {["Skill", "Job Role", "District", "Required Proficiency", "Current Proficiency", "Gap", "Demand", "Supply", "Priority", "Recommended Course"].map(h => (
                  <th key={h} style={{ padding: "8px 12px", textAlign: "left", fontSize: 11, fontWeight: 600, color: "#64748B", borderBottom: "1px solid #E2E8F0", whiteSpace: "nowrap" }}>{h}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {tableData
                .filter(r => activeFilter === "All" || r.gap === activeFilter || (activeFilter === "Low" && (r.gap === "Low" || r.gap === "None")))
                .map((row, i) => (
                  <tr key={i} className="table-row" style={{ borderBottom: "1px solid #F1F5F9" }}>
                    <td style={{ padding: "10px 12px", fontSize: 13, fontWeight: 600, color: "#0F172A" }}>{row.skill}</td>
                    <td style={{ padding: "10px 12px", fontSize: 12, color: "#334155" }}>{row.role}</td>
                    <td style={{ padding: "10px 12px", fontSize: 12, color: "#334155" }}>{row.district}</td>
                    <td style={{ padding: "10px 12px" }}>
                      <span style={{ fontSize: 11, padding: "2px 8px", background: "#EFF6FF", color: "#1D4ED8", borderRadius: 4, fontWeight: 600 }}>{row.reqProf}</span>
                    </td>
                    <td style={{ padding: "10px 12px" }}>
                      <span style={{ fontSize: 11, padding: "2px 8px", background: "#F0FDFA", color: "#0D9488", borderRadius: 4, fontWeight: 600 }}>{row.currProf}</span>
                    </td>
                    <td style={{ padding: "10px 12px" }}>
                      <span className={`badge ${gapColors[row.gap]}`}>{row.gap}</span>
                    </td>
                    <td style={{ padding: "10px 12px", fontSize: 12, fontFamily: "'JetBrains Mono', monospace", fontWeight: 600, color: "#0F172A" }}>{row.demand.toLocaleString()}</td>
                    <td style={{ padding: "10px 12px", fontSize: 12, fontFamily: "'JetBrains Mono', monospace", color: "#64748B" }}>{row.supply.toLocaleString()}</td>
                    <td style={{ padding: "10px 12px" }}>
                      <span style={{ fontSize: 11, padding: "2px 8px", borderRadius: 4, fontWeight: 700, background: row.priority === "P1" ? "#FEF2F2" : row.priority === "P2" ? "#FFFBEB" : "#F8FAFC", color: row.priority === "P1" ? "#DC2626" : row.priority === "P2" ? "#D97706" : "#64748B" }}>{row.priority}</span>
                    </td>
                    <td style={{ padding: "10px 12px", fontSize: 12, color: "#475569" }}>{row.course}</td>
                  </tr>
                ))}
            </tbody>
          </table>
        </div>
      </div>

      {/* AI Insight Box */}
      <div className="ai-card">
        <div style={{ display: "flex", gap: 10, alignItems: "flex-start" }}>
          <div style={{ width: 32, height: 32, background: "#7C3AED", borderRadius: 8, display: "flex", alignItems: "center", justifyContent: "center", flexShrink: 0 }}>
            <IcoSpark size={16} className="text-white" />
          </div>
          <div>
            <div style={{ fontSize: 13, fontWeight: 700, color: "#4C1D95", marginBottom: 4 }}>AI Skill Gap Insight</div>
            <div style={{ fontSize: 13, color: "#334155", lineHeight: 1.6 }}>
              <strong>Cloud Computing</strong> and <strong>ML/AI</strong> show critical supply shortfalls across Pune, Bengaluru and Hyderabad — combined unmet demand of <strong>2,740 positions</strong>. Immediate curriculum additions and trainer upskilling in these two areas could yield an estimated <strong>+22% placement improvement</strong> within 2 quarters.
            </div>
            <div style={{ display: "flex", gap: 8, marginTop: 10 }}>
              <button className="btn-ai" style={{ fontSize: 12 }}><IcoSpark size={12} />Generate District Plan</button>
              <button className="btn-secondary" style={{ fontSize: 12 }}>View Curriculum Recommendations</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
