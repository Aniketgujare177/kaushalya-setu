import React from "react";
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Legend } from "recharts";
import { IcoSpark, IcoAlert, IcoCheck } from "../components/Icons";

const infraData = [
  { district: "Pune", required: 250, available: 130, gpuReq: 20, gpuAvail: 4, labs: 5, trainers: 12 },
  { district: "Bengaluru", required: 380, available: 260, gpuReq: 35, gpuAvail: 12, labs: 8, trainers: 18 },
  { district: "Hyderabad", required: 280, available: 180, gpuReq: 22, gpuAvail: 6, labs: 6, trainers: 14 },
  { district: "Mumbai", required: 200, available: 160, gpuReq: 10, gpuAvail: 8, labs: 4, trainers: 10 },
  { district: "Jaipur", required: 140, available: 80, gpuReq: 8, gpuAvail: 1, labs: 3, trainers: 6 },
  { district: "Ahmedabad", required: 180, available: 100, gpuReq: 12, gpuAvail: 2, labs: 4, trainers: 8 },
];

const courseIntelligence = [
  { course: "Cloud Engineering", demand: "Very High", capacity: 480, placement: "78%", status: "high-demand", enrolment: 420 },
  { course: "AI/ML Engineering", demand: "Very High", capacity: 320, placement: "82%", status: "high-demand", enrolment: 310 },
  { course: "Data Analytics", demand: "High", capacity: 680, placement: "71%", status: "growing", enrolment: 580 },
  { course: "Full Stack Dev", demand: "High", capacity: 720, placement: "68%", status: "growing", enrolment: 640 },
  { course: "Cybersecurity", demand: "High", capacity: 280, placement: "75%", status: "high-demand", enrolment: 220 },
  { course: "Digital Marketing", demand: "Medium", capacity: 480, placement: "56%", status: "low-demand", enrolment: 310 },
  { course: "Basic Data Entry", demand: "Low", capacity: 680, placement: "32%", status: "oversupplied", enrolment: 540 },
  { course: "MS Office Basic", demand: "Low", capacity: 540, placement: "28%", status: "obsolete", enrolment: 420 },
];

const statusConfig: Record<string, { bg: string; color: string; label: string }> = {
  "high-demand": { bg: "#ECFDF5", color: "#059669", label: "High Demand" },
  "growing": { bg: "#EFF6FF", color: "#1D4ED8", label: "Growing" },
  "low-demand": { bg: "#FFFBEB", color: "#D97706", label: "Low Demand" },
  "oversupplied": { bg: "#FEF2F2", color: "#DC2626", label: "Oversupplied" },
  "obsolete": { bg: "#FEF2F2", color: "#DC2626", label: "Obsolete" },
};

export default function TrainingPlanning() {
  return (
    <div style={{ padding: 24, display: "flex", flexDirection: "column", gap: 20 }}>
      <div>
        <h1 className="font-display" style={{ fontSize: 22, fontWeight: 700, color: "#0F172A", marginBottom: 4 }}>Training & Capacity Planning</h1>
        <p style={{ fontSize: 13, color: "#64748B" }}>Infrastructure gaps, course demand intelligence, and training capacity by district</p>
      </div>

      {/* Course Intelligence */}
      <div className="chart-card">
        <div className="section-header" style={{ fontSize: 15, marginBottom: 4 }}>Course Demand Intelligence</div>
        <div className="section-sub" style={{ marginBottom: 16 }}>Identify high-demand, growing, low-demand, oversupplied and obsolete courses</div>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: 10, marginBottom: 16 }}>
          {[
            { label: "High Demand", count: 3, color: "#059669" },
            { label: "Growing", count: 2, color: "#1D4ED8" },
            { label: "Low Demand", count: 1, color: "#D97706" },
            { label: "Oversupplied / Obsolete", count: 2, color: "#DC2626" },
          ].map(s => (
            <div key={s.label} style={{ padding: "10px 14px", background: "#F8FAFC", borderRadius: 8, borderLeft: `3px solid ${s.color}` }}>
              <div style={{ fontSize: 20, fontWeight: 700, color: s.color, fontFamily: "'DM Sans', sans-serif" }}>{s.count}</div>
              <div style={{ fontSize: 12, color: "#334155" }}>{s.label}</div>
            </div>
          ))}
        </div>

        <table style={{ width: "100%", borderCollapse: "collapse" }}>
          <thead>
            <tr style={{ background: "#F8FAFC" }}>
              {["Course", "Market Demand", "Capacity (seats)", "Enrolment", "Placement Rate", "Status", "Action"].map(h => (
                <th key={h} style={{ padding: "8px 12px", textAlign: "left", fontSize: 11, fontWeight: 600, color: "#64748B", borderBottom: "1px solid #E2E8F0" }}>{h}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {courseIntelligence.map((row, i) => {
              const sc = statusConfig[row.status];
              const utilisation = Math.round((row.enrolment / row.capacity) * 100);
              return (
                <tr key={i} className="table-row" style={{ borderBottom: "1px solid #F1F5F9" }}>
                  <td style={{ padding: "10px 12px", fontSize: 13, fontWeight: 600, color: "#0F172A" }}>{row.course}</td>
                  <td style={{ padding: "10px 12px", fontSize: 12, color: "#334155" }}>{row.demand}</td>
                  <td style={{ padding: "10px 12px", fontSize: 12, fontFamily: "'JetBrains Mono', monospace" }}>{row.capacity}</td>
                  <td style={{ padding: "10px 12px" }}>
                    <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
                      <div className="progress-bar" style={{ width: 60 }}>
                        <div className="progress-fill" style={{ width: `${utilisation}%`, background: utilisation > 90 ? "#DC2626" : "#1D4ED8" }} />
                      </div>
                      <span style={{ fontSize: 11, fontFamily: "'JetBrains Mono', monospace" }}>{utilisation}%</span>
                    </div>
                  </td>
                  <td style={{ padding: "10px 12px", fontSize: 12, fontWeight: 600, color: parseFloat(row.placement) >= 60 ? "#059669" : "#DC2626" }}>{row.placement}</td>
                  <td style={{ padding: "10px 12px" }}>
                    <span style={{ padding: "2px 8px", background: sc.bg, color: sc.color, borderRadius: 4, fontSize: 11, fontWeight: 600 }}>{sc.label}</span>
                  </td>
                  <td style={{ padding: "10px 12px" }}>
                    {(row.status === "oversupplied" || row.status === "obsolete") ? (
                      <button style={{ fontSize: 11, padding: "3px 8px", background: "#FEF2F2", color: "#DC2626", border: "1px solid #FECACA", borderRadius: 6, cursor: "pointer", fontWeight: 600 }}>Reduce Capacity</button>
                    ) : row.status === "high-demand" ? (
                      <button style={{ fontSize: 11, padding: "3px 8px", background: "#ECFDF5", color: "#059669", border: "1px solid #BBF7D0", borderRadius: 6, cursor: "pointer", fontWeight: 600 }}>Scale Up</button>
                    ) : (
                      <button style={{ fontSize: 11, padding: "3px 8px", background: "#EFF6FF", color: "#1D4ED8", border: "1px solid #BFDBFE", borderRadius: 6, cursor: "pointer", fontWeight: 600 }}>Monitor</button>
                    )}
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>

      {/* Infrastructure Chart */}
      <div className="chart-card">
        <div className="section-header" style={{ fontSize: 15, marginBottom: 4 }}>District Infrastructure Gap — Computers</div>
        <div className="section-sub" style={{ marginBottom: 16 }}>Required vs available computing infrastructure per district</div>
        <ResponsiveContainer width="100%" height={220}>
          <BarChart data={infraData}>
            <CartesianGrid strokeDasharray="3 3" stroke="#F1F5F9" />
            <XAxis dataKey="district" tick={{ fontSize: 11, fill: "#94A3B8" }} axisLine={false} tickLine={false} />
            <YAxis tick={{ fontSize: 10, fill: "#94A3B8" }} axisLine={false} tickLine={false} />
            <Tooltip contentStyle={{ fontSize: 12, borderRadius: 8, border: "1px solid #E2E8F0" }} />
            <Legend wrapperStyle={{ fontSize: 11 }} />
            <Bar dataKey="required" fill="#1D4ED8" name="Required Computers" radius={[4, 4, 0, 0]} />
            <Bar dataKey="available" fill="#0D9488" name="Available Computers" radius={[4, 4, 0, 0]} />
          </BarChart>
        </ResponsiveContainer>
      </div>

      {/* Infrastructure Table */}
      <div className="chart-card">
        <div className="section-header" style={{ fontSize: 15, marginBottom: 16 }}>Full Infrastructure Planning Table</div>
        <table style={{ width: "100%", borderCollapse: "collapse" }}>
          <thead>
            <tr style={{ background: "#F8FAFC" }}>
              {["District", "Computers Reqd.", "Computers Avail.", "GPU Reqd.", "GPU Avail.", "Labs Reqd.", "Trainers Reqd.", "Status"].map(h => (
                <th key={h} style={{ padding: "8px 12px", textAlign: "left", fontSize: 11, fontWeight: 600, color: "#64748B", borderBottom: "1px solid #E2E8F0", whiteSpace: "nowrap" }}>{h}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {infraData.map((row, i) => {
              const pcGap = row.required - row.available;
              const gpuGap = row.gpuReq - row.gpuAvail;
              const isCritical = pcGap > 100 || gpuGap > 15;
              return (
                <tr key={i} className="table-row" style={{ borderBottom: "1px solid #F1F5F9" }}>
                  <td style={{ padding: "10px 12px", fontSize: 13, fontWeight: 600, color: "#0F172A" }}>{row.district}</td>
                  <td style={{ padding: "10px 12px", fontSize: 12, fontFamily: "'JetBrains Mono', monospace" }}>{row.required}</td>
                  <td style={{ padding: "10px 12px", fontSize: 12, fontFamily: "'JetBrains Mono', monospace", color: "#059669" }}>{row.available}</td>
                  <td style={{ padding: "10px 12px", fontSize: 12, fontFamily: "'JetBrains Mono', monospace" }}>{row.gpuReq}</td>
                  <td style={{ padding: "10px 12px", fontSize: 12, fontFamily: "'JetBrains Mono', monospace", color: gpuGap > 10 ? "#DC2626" : "#059669" }}>{row.gpuAvail}</td>
                  <td style={{ padding: "10px 12px", fontSize: 12, fontFamily: "'JetBrains Mono', monospace" }}>{row.labs}</td>
                  <td style={{ padding: "10px 12px", fontSize: 12, fontFamily: "'JetBrains Mono', monospace" }}>{row.trainers}</td>
                  <td style={{ padding: "10px 12px" }}>
                    <span style={{ padding: "2px 8px", background: isCritical ? "#FEF2F2" : "#FFFBEB", color: isCritical ? "#DC2626" : "#D97706", borderRadius: 4, fontSize: 11, fontWeight: 600 }}>
                      {isCritical ? "Critical Gap" : "Moderate Gap"}
                    </span>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
}
