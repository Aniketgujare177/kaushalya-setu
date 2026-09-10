import React from "react";
import {
  IcoDashboard,
  IcoTrends,
  IcoSkillGap,
  IcoSkills,
  IcoEmployer,
  IcoAI,
  IcoTraining,
  IcoTrainer,
  IcoPlacement,
  IcoDistrict,
  IcoReports,
  IcoUsers,
  IcoSettings,
  IcoZap,
} from "./Icons";

type Page =
  | "dashboard"
  | "demand"
  | "skillgap"
  | "curriculum"
  | "employer"
  | "ai"
  | "training"
  | "trainer"
  | "placement"
  | "district"
  | "reports"
  | "users"
  | "settings";

interface SidebarProps {
  activePage: Page;
  onNav: (p: Page) => void;
}

const navItems: {
  id: Page;
  label: string;
  Icon: React.FC<{ size?: number; className?: string }>;
}[] = [
    { id: "dashboard", label: "Dashboard", Icon: IcoDashboard },
    { id: "demand", label: "Demand & Trends", Icon: IcoTrends },
    { id: "skillgap", label: "Skill Gap Analysis", Icon: IcoSkillGap },
    { id: "curriculum", label: "Skills & Curriculum", Icon: IcoSkills },
    { id: "employer", label: "Employer Insights", Icon: IcoEmployer },
    { id: "ai", label: "AI Recommendations", Icon: IcoAI },

    { id: "training", label: "Training & Planning", Icon: IcoTraining },
    { id: "trainer", label: "Trainer Development", Icon: IcoTrainer },
    { id: "placement", label: "Placement & Outcomes", Icon: IcoPlacement },
    { id: "district", label: "District Planning", Icon: IcoDistrict },
    { id: "reports", label: "Reports & Analytics", Icon: IcoReports },

    { id: "users", label: "User Management", Icon: IcoUsers },
    { id: "settings", label: "Settings", Icon: IcoSettings },
  ];

export default function Sidebar({ activePage, onNav }: SidebarProps) {
  const renderNavItem = ({
    id,
    label,
    Icon,
  }: {
    id: Page;
    label: string;
    Icon: React.FC<{ size?: number; className?: string }>;
  }) => {
    const isActive = activePage === id;

    return (
      <button
        key={id}
        type="button"
        onClick={() => {
          console.log("Sidebar clicked:", id);
          onNav(id);
        }}
        className={`sidebar-nav-item${isActive ? " active" : ""}`}
        style={{
          width: "100%",
          display: "flex",
          alignItems: "center",
          gap: 10,
          border: "none",
          cursor: "pointer",
          textAlign: "left",
          background: isActive ? "#EFF6FF" : "transparent",
          color: isActive ? "#1D4ED8" : "#475569",
          padding: "10px 12px",
          marginBottom: 3,
          borderRadius: 7,
          fontSize: 12,
          fontWeight: isActive ? 700 : 500,
          transition: "all 0.15s ease",
        }}
      >
        <Icon size={15} />
        <span>{label}</span>
      </button>
    );
  };

  return (
    <aside
      style={{
        width: 260,
        height: "100%",
        background: "#FFFFFF",
        borderRight: "1px solid #E2E8F0",
        flexShrink: 0,
        display: "flex",
        flexDirection: "column",
        overflow: "hidden",
        position: "relative",
        zIndex: 10,
      }}
    >
      {/* ================= LOGO ================= */}
      <div
        style={{
          padding: "20px 16px 16px",
          borderBottom: "1px solid #E2E8F0",
          flexShrink: 0,
        }}
      >
        <div
          style={{
            display: "flex",
            alignItems: "center",
            gap: 8,
            marginBottom: 8,
          }}
        >
          <div
            style={{
              width: 32,
              height: 32,
              background: "linear-gradient(135deg, #1D4ED8, #0D9488)",
              borderRadius: 8,
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              flexShrink: 0,
            }}
          >
            <IcoZap size={16} className="text-white" />
          </div>

          <div>
            <div
              style={{
                fontFamily: "'DM Sans', sans-serif",
                fontSize: 13,
                fontWeight: 700,
                color: "#0F172A",
                lineHeight: 1.2,
              }}
            >
              Labour Market
            </div>

            <div
              style={{
                fontFamily: "'DM Sans', sans-serif",
                fontSize: 10,
                fontWeight: 500,
                color: "#64748B",
                lineHeight: 1.2,
              }}
            >
              Intelligence Platform
            </div>
          </div>
        </div>

        {/* SIH Badge */}
        <div
          style={{
            marginTop: 8,
            padding: "4px 8px",
            background: "#F0FDFA",
            borderRadius: 6,
            display: "inline-flex",
            alignItems: "center",
            gap: 4,
          }}
        >
          <div
            style={{
              width: 6,
              height: 6,
              background: "#059669",
              borderRadius: "50%",
            }}
          />

          <span
            style={{
              fontSize: 10,
              fontWeight: 600,
              color: "#0D9488",
            }}
          >
            SIH PS-26134
          </span>
        </div>
      </div>

      {/* ================= NAVIGATION ================= */}
      <nav
        style={{
          flex: 1,
          overflowY: "auto",
          overflowX: "hidden",
          padding: "12px 8px",
        }}
      >
        {/* Main Navigation */}
        <div
          style={{
            fontSize: 10,
            fontWeight: 600,
            color: "#94A3B8",
            letterSpacing: "0.08em",
            padding: "4px 12px",
            marginBottom: 4,
          }}
        >
          MAIN NAVIGATION
        </div>

        {navItems.slice(0, 6).map(renderNavItem)}

        {/* Management */}
        <div
          style={{
            fontSize: 10,
            fontWeight: 600,
            color: "#94A3B8",
            letterSpacing: "0.08em",
            padding: "12px 12px 4px",
          }}
        >
          MANAGEMENT
        </div>

        {navItems.slice(6, 11).map(renderNavItem)}

        {/* Admin */}
        <div
          style={{
            fontSize: 10,
            fontWeight: 600,
            color: "#94A3B8",
            letterSpacing: "0.08em",
            padding: "12px 12px 4px",
          }}
        >
          ADMIN
        </div>

        {navItems.slice(11).map(renderNavItem)}
      </nav>

      {/* ================= DATA SOURCES ================= */}
      <div
        style={{
          padding: "12px 16px",
          borderTop: "1px solid #E2E8F0",
          background: "#F8FAFC",
          flexShrink: 0,
        }}
      >
        <div
          style={{
            fontSize: 11,
            color: "#64748B",
            marginBottom: 6,
          }}
        >
          Data Sources Active
        </div>

        <div
          style={{
            display: "flex",
            gap: 4,
            flexWrap: "wrap",
          }}
        >
          {["Jobs", "Surveys", "Placement", "Census"].map((src) => (
            <span
              key={src}
              style={{
                fontSize: 10,
                padding: "2px 6px",
                background: "#ECFDF5",
                color: "#059669",
                borderRadius: 4,
                fontWeight: 600,
              }}
            >
              {src}
            </span>
          ))}
        </div>

        <div
          style={{
            fontSize: 10,
            color: "#94A3B8",
            marginTop: 6,
          }}
        >
          Last sync: 2 mins ago
        </div>
      </div>
    </aside>
  );
}