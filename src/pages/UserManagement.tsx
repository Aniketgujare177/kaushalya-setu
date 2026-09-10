import React from "react";
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from "recharts";
import { IcoUsers, IcoCheck, IcoAlert } from "../components/Icons";

const users = [
  { name: "Priya Sharma", role: "Government / Planner", org: "MSDE Delhi", lastActive: "2 hrs ago", status: "active" },
  { name: "Rajesh Kumar", role: "Training Institute", org: "NIELIT Pune", lastActive: "1 hr ago", status: "active" },
  { name: "Anita Mehta", role: "Employer / Industry", org: "TCS Ltd.", lastActive: "30 min ago", status: "active" },
  { name: "Suresh Patel", role: "Trainer", org: "NIMI Ahmedabad", lastActive: "4 hrs ago", status: "active" },
  { name: "Kavitha Ramesh", role: "Student / Candidate", org: "Self-enrolled", lastActive: "10 min ago", status: "active" },
  { name: "Deepak Nair", role: "Admin", org: "Platform Admin", lastActive: "Just now", status: "active" },
  { name: "Sunita Rao", role: "Government / Planner", org: "NSDC Bengaluru", lastActive: "1 day ago", status: "inactive" },
  { name: "Vikram Singh", role: "Employer / Industry", org: "Infosys Ltd.", lastActive: "3 days ago", status: "inactive" },
];

const activityData = [
  { day: "Mon", logins: 142, actions: 380 },
  { day: "Tue", logins: 168, actions: 420 },
  { day: "Wed", logins: 195, actions: 510 },
  { day: "Thu", logins: 188, actions: 490 },
  { day: "Fri", logins: 172, actions: 445 },
  { day: "Sat", logins: 84, actions: 210 },
  { day: "Sun", logins: 62, actions: 155 },
];

const roleColors: Record<string, { bg: string; color: string }> = {
  "Government / Planner": { bg: "#F5F3FF", color: "#7C3AED" },
  "Training Institute": { bg: "#EFF6FF", color: "#1D4ED8" },
  "Employer / Industry": { bg: "#F0FDFA", color: "#0D9488" },
  "Trainer": { bg: "#FFFBEB", color: "#D97706" },
  "Student / Candidate": { bg: "#ECFDF5", color: "#059669" },
  "Admin": { bg: "#FEF2F2", color: "#DC2626" },
};

const systemHealth = [
  { component: "Job Portal API", status: "Operational", uptime: "99.98%", latency: "42ms" },
  { component: "Employer Survey Service", status: "Operational", uptime: "99.91%", latency: "86ms" },
  { component: "AI Recommendation Engine", status: "Operational", uptime: "99.87%", latency: "210ms" },
  { component: "Placement Outcomes DB", status: "Operational", uptime: "99.99%", latency: "18ms" },
  { component: "District Planning Service", status: "Degraded", uptime: "98.40%", latency: "680ms" },
  { component: "Report Generation", status: "Operational", uptime: "99.72%", latency: "340ms" },
];

export default function UserManagement() {
  return (
    <div style={{ padding: 24, display: "flex", flexDirection: "column", gap: 20 }}>
      <div>
        <h1 className="font-display" style={{ fontSize: 22, fontWeight: 700, color: "#0F172A", marginBottom: 4 }}>User Management & Admin</h1>
        <p style={{ fontSize: 13, color: "#64748B" }}>Platform users, system health, data sources and audit logs</p>
      </div>

      {/* User Stats */}
      <div style={{ display: "grid", gridTemplateColumns: "repeat(6, 1fr)", gap: 12 }}>
        {[
          { label: "Total Users", value: "2,842", color: "#1D4ED8" },
          { label: "Students", value: "1,680", color: "#059669" },
          { label: "Employers", value: "284", color: "#0D9488" },
          { label: "Institutes", value: "142", color: "#7C3AED" },
          { label: "Trainers", value: "186", color: "#D97706" },
          { label: "Govt. Planners", value: "38", color: "#DC2626" },
        ].map(s => (
          <div key={s.label} className="kpi-card">
            <div style={{ fontSize: 20, fontWeight: 700, color: s.color, fontFamily: "'DM Sans', sans-serif" }}>{s.value}</div>
            <div style={{ fontSize: 11, fontWeight: 600, color: "#334155", marginTop: 4 }}>{s.label}</div>
          </div>
        ))}
      </div>

      <div style={{ display: "grid", gridTemplateColumns: "2fr 1fr", gap: 16 }}>
        {/* Users Table */}
        <div className="chart-card">
          <div className="section-header" style={{ fontSize: 15, marginBottom: 16 }}>Active Users</div>
          <table style={{ width: "100%", borderCollapse: "collapse" }}>
            <thead>
              <tr style={{ background: "#F8FAFC" }}>
                {["Name", "Role", "Organisation", "Last Active", "Status"].map(h => (
                  <th key={h} style={{ padding: "8px 12px", textAlign: "left", fontSize: 11, fontWeight: 600, color: "#64748B", borderBottom: "1px solid #E2E8F0" }}>{h}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {users.map((u, i) => {
                const rc = roleColors[u.role];
                return (
                  <tr key={i} className="table-row" style={{ borderBottom: "1px solid #F1F5F9" }}>
                    <td style={{ padding: "10px 12px" }}>
                      <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
                        <div style={{ width: 28, height: 28, background: rc.bg, borderRadius: "50%", display: "flex", alignItems: "center", justifyContent: "center", fontSize: 11, fontWeight: 700, color: rc.color }}>
                          {u.name.charAt(0)}
                        </div>
                        <span style={{ fontSize: 13, fontWeight: 600, color: "#0F172A" }}>{u.name}</span>
                      </div>
                    </td>
                    <td style={{ padding: "10px 12px" }}>
                      <span style={{ padding: "2px 8px", background: rc.bg, color: rc.color, borderRadius: 4, fontSize: 11, fontWeight: 600 }}>{u.role}</span>
                    </td>
                    <td style={{ padding: "10px 12px", fontSize: 12, color: "#64748B" }}>{u.org}</td>
                    <td style={{ padding: "10px 12px", fontSize: 11, color: "#94A3B8", fontFamily: "'JetBrains Mono', monospace" }}>{u.lastActive}</td>
                    <td style={{ padding: "10px 12px" }}>
                      <span style={{ display: "flex", alignItems: "center", gap: 4, fontSize: 11, fontWeight: 600, color: u.status === "active" ? "#059669" : "#94A3B8" }}>
                        <div style={{ width: 6, height: 6, borderRadius: "50%", background: u.status === "active" ? "#059669" : "#94A3B8" }} />
                        {u.status === "active" ? "Active" : "Inactive"}
                      </span>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>

        {/* Activity + System Health */}
        <div style={{ display: "flex", flexDirection: "column", gap: 16 }}>
          <div className="chart-card">
            <div className="section-header" style={{ fontSize: 14, marginBottom: 12 }}>Weekly Activity</div>
            <ResponsiveContainer width="100%" height={160}>
              <BarChart data={activityData}>
                <CartesianGrid strokeDasharray="3 3" stroke="#F1F5F9" />
                <XAxis dataKey="day" tick={{ fontSize: 10, fill: "#94A3B8" }} axisLine={false} tickLine={false} />
                <YAxis tick={{ fontSize: 10, fill: "#94A3B8" }} axisLine={false} tickLine={false} />
                <Tooltip contentStyle={{ fontSize: 12, borderRadius: 8 }} />
                <Bar dataKey="logins" fill="#1D4ED8" name="Logins" radius={[3, 3, 0, 0]} />
                <Bar dataKey="actions" fill="#0D9488" name="Actions" radius={[3, 3, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>

          <div className="chart-card">
            <div className="section-header" style={{ fontSize: 14, marginBottom: 12 }}>System Health</div>
            {systemHealth.map(s => (
              <div key={s.component} style={{ display: "flex", justifyContent: "space-between", alignItems: "center", padding: "6px 0", borderBottom: "1px solid #F1F5F9" }}>
                <div>
                  <div style={{ fontSize: 12, fontWeight: 500, color: "#334155" }}>{s.component}</div>
                  <div style={{ fontSize: 10, color: "#94A3B8", fontFamily: "'JetBrains Mono', monospace" }}>{s.uptime} · {s.latency}</div>
                </div>
                <span style={{ fontSize: 11, fontWeight: 600, color: s.status === "Operational" ? "#059669" : "#D97706", padding: "2px 6px", background: s.status === "Operational" ? "#ECFDF5" : "#FFFBEB", borderRadius: 4 }}>
                  {s.status}
                </span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
