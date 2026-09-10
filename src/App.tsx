import React, { useEffect, useState } from "react";

import Sidebar from "./components/Sidebar";
import Header from "./components/Header";

import Dashboard from "./pages/Dashboard";
import DemandTrends from "./pages/DemandTrends";
import SkillGapAnalysis from "./pages/SkillGapAnalysis";
import CurriculumAlignment from "./pages/CurriculumAlignment";
import EmployerInsights from "./pages/EmployerInsights";
import AIRecommendations from "./pages/AIRecommendations";
import TrainingPlanning from "./pages/TrainingPlanning";
import TrainerDevelopment from "./pages/TrainerDevelopment";
import PlacementOutcomes from "./pages/PlacementOutcomes";
import DistrictPlanning from "./pages/DistrictPlanning";
import Reports from "./pages/Reports";
import UserManagement from "./pages/UserManagement";

/* =========================================================
   PAGE TYPE
========================================================= */

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

/* =========================================================
   PAGE TITLES
========================================================= */

const pageTitles: Record<Page, string> = {
  dashboard: "Dashboard",
  demand: "Demand & Trends",
  skillgap: "Skill Gap Analysis",
  curriculum: "Skills & Curriculum",
  employer: "Employer Insights",
  ai: "AI Recommendations",
  training: "Training & Planning",
  trainer: "Trainer Development",
  placement: "Placement & Outcomes",
  district: "District Planning",
  reports: "Reports & Analytics",
  users: "User Management",
  settings: "Settings",
};

/* =========================================================
   SETTINGS PAGE
========================================================= */

function SettingsPage() {
  const settings = [
    {
      label: "Platform Settings",
      desc: "Configure data refresh intervals, API connections, and system defaults",
    },
    {
      label: "Role & Permission Management",
      desc: "Manage user roles, permissions and access control",
    },
    {
      label: "Data Source Configuration",
      desc: "Add, remove and validate data sources including job portals and APIs",
    },
    {
      label: "Notification Settings",
      desc: "Configure alerts, email notifications and escalation rules",
    },
    {
      label: "AI Model Configuration",
      desc: "Tune AI recommendation engine parameters and confidence thresholds",
    },
    {
      label: "Report Templates",
      desc: "Customize report templates and automated generation schedules",
    },
  ];

  return (
    <div style={{ padding: 24 }}>
      <h1
        className="font-display"
        style={{
          fontSize: 22,
          fontWeight: 700,
          color: "#0F172A",
          marginBottom: 16,
        }}
      >
        Settings
      </h1>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "1fr 1fr",
          gap: 16,
        }}
      >
        {settings.map((item) => (
          <div key={item.label} className="chart-card">
            <div
              style={{
                fontSize: 14,
                fontWeight: 700,
                color: "#0F172A",
                marginBottom: 6,
              }}
            >
              {item.label}
            </div>

            <div
              style={{
                fontSize: 12,
                color: "#64748B",
                marginBottom: 12,
              }}
            >
              {item.desc}
            </div>

            <button
              className="btn-secondary"
              type="button"
              style={{ fontSize: 12 }}
            >
              Configure
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}

/* =========================================================
   APP
========================================================= */

export default function App() {
  /* -------------------------------------------------------
     NAVIGATION
  ------------------------------------------------------- */

  const [activePage, setActivePage] =
    useState<Page>("dashboard");

  const [role, setRole] =
    useState("Government / Planner");

  const [sidebarCollapsed, setSidebarCollapsed] =
    useState(false);

  /* -------------------------------------------------------
     GLOBAL FILTERS
  ------------------------------------------------------- */

  const [stateFilter, setStateFilter] =
    useState("All States");

  const [sectorFilter, setSectorFilter] =
    useState("All Sectors");

  /*
    searchInput = what user is typing
    search       = actual search sent to dashboard
  */

  const [searchInput, setSearchInput] =
    useState("");

  const [search, setSearch] =
    useState("");

  /* -------------------------------------------------------
     SEARCH DEBOUNCE
  ------------------------------------------------------- */

  useEffect(() => {
    const value = searchInput.trim();

    const timer = window.setTimeout(() => {
      setSearch(value);
    }, 400);

    return () => {
      window.clearTimeout(timer);
    };
  }, [searchInput]);

  /* -------------------------------------------------------
     PAGE RENDER
  ------------------------------------------------------- */

  const renderPage = () => {
    switch (activePage) {
      case "dashboard":
        return (
          <Dashboard
            role={role}
            state={stateFilter}
            sector={sectorFilter}
            search={search}
            onNavigate={setActivePage}
          />
        );

      case "demand":
        return <DemandTrends />;

      case "skillgap":
        return <SkillGapAnalysis />;

      case "curriculum":
        return <CurriculumAlignment />;

      case "employer":
        return <EmployerInsights />;

      case "ai":
        return <AIRecommendations />;

      case "training":
        return <TrainingPlanning />;

      case "trainer":
        return <TrainerDevelopment />;

      case "placement":
        return <PlacementOutcomes />;

      case "district":
        return <DistrictPlanning />;

      case "reports":
        return <Reports />;

      case "users":
        return <UserManagement />;

      case "settings":
        return <SettingsPage />;

      default:
        return (
          <Dashboard
            role={role}
            state={stateFilter}
            sector={sectorFilter}
            search={search}
            onNavigate={setActivePage}
          />
        );
    }
  };

  /* -------------------------------------------------------
     RENDER
  ------------------------------------------------------- */

  return (
    <div
      style={{
        display: "flex",
        height: "100%",
        background: "#F0F4F8",
        overflow: "hidden",
      }}
    >
      {/* SIDEBAR */}

      {!sidebarCollapsed && (
        <Sidebar
          activePage={activePage}
          onNav={(page) =>
            setActivePage(page as Page)
          }
        />
      )}

      {/* MAIN AREA */}

      <div
        style={{
          flex: 1,
          display: "flex",
          flexDirection: "column",
          overflow: "hidden",
        }}
      >
        {/* HEADER */}

        <Header
          role={role}
          onRoleChange={setRole}
          onMenuToggle={() =>
            setSidebarCollapsed(
              (previous) => !previous
            )
          }
          search={searchInput}
          onSearchChange={setSearchInput}
          state={stateFilter}
          onStateChange={setStateFilter}
          sector={sectorFilter}
          onSectorChange={setSectorFilter}
        />

        {/* BREADCRUMB */}

        <div
          style={{
            padding: "8px 24px",
            background: "white",
            borderBottom: "1px solid #F1F5F9",
            display: "flex",
            alignItems: "center",
            gap: 6,
          }}
        >
          <span
            style={{
              fontSize: 12,
              color: "#94A3B8",
            }}
          >
            Labour Market Platform
          </span>

          <span
            style={{
              fontSize: 12,
              color: "#CBD5E1",
            }}
          >
            ›
          </span>

          <span
            style={{
              fontSize: 12,
              fontWeight: 600,
              color: "#334155",
            }}
          >
            {pageTitles[activePage]}
          </span>

          <div
            style={{
              marginLeft: "auto",
              display: "flex",
              gap: 6,
              alignItems: "center",
            }}
          >
            <div
              style={{
                width: 6,
                height: 6,
                background: "#059669",
                borderRadius: "50%",
                animation: "pulse 2s infinite",
              }}
            />

            <span
              style={{
                fontSize: 11,
                color: "#059669",
                fontWeight: 600,
              }}
            >
              Live Data
            </span>

            <span
              style={{
                fontSize: 11,
                color: "#94A3B8",
              }}
            >
              ·
            </span>

            <span
              style={{
                fontSize: 11,
                color: "#64748B",
              }}
            >
              Role:{" "}
              <strong
                style={{
                  color: "#1D4ED8",
                }}
              >
                {role}
              </strong>
            </span>
          </div>
        </div>

        {/* PAGE CONTENT */}

        <div
          style={{
            flex: 1,
            overflowY: "auto",
          }}
        >
          {renderPage()}
        </div>
      </div>
    </div>
  );
}