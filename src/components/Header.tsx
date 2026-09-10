import React, { useState } from "react";

import {
  IcoSearch,
  IcoBell,
  IcoUser,
  IcoMenu,
  IcoChevronDown,
} from "./Icons";

/* =========================================================
   PROPS
========================================================= */

interface HeaderProps {
  role: string;

  onRoleChange: (
    role: string
  ) => void;

  onMenuToggle: () => void;

  /* Global filters */

  search: string;

  onSearchChange: (
    value: string
  ) => void;

  state: string;

  onStateChange: (
    value: string
  ) => void;

  sector: string;

  onSectorChange: (
    value: string
  ) => void;
}

/* =========================================================
   OPTIONS
========================================================= */

const roles = [
  "Government / Planner",
  "Training Institute",
  "Employer / Industry",
  "Trainer",
  "Student / Candidate",
  "Admin",
];

const states = [
  "All States",
  "Maharashtra",
  "Karnataka",
  "Tamil Nadu",
  "Uttar Pradesh",
  "Gujarat",
  "Rajasthan",
  "Madhya Pradesh",
  "Telangana",
  "Delhi",
  "West Bengal",
  "Kerala",
  "Andhra Pradesh",
];

const sectors = [
  "All Sectors",
  "IT & Software",
  "Healthcare",
  "Manufacturing",
  "BFSI",
  "Retail",
  "Construction",
  "Automobile",
  "Education",
  "Telecommunications",
  "Logistics",
  "Agriculture",
  "Renewable Energy",
];

/* =========================================================
   COMPONENT
========================================================= */

export default function Header({
  role,
  onRoleChange,
  onMenuToggle,

  search,
  onSearchChange,

  state,
  onStateChange,

  sector,
  onSectorChange,

}: HeaderProps) {

  const [showRoleMenu, setShowRoleMenu] =
    useState(false);

  /* =======================================================
     SEARCH
  ======================================================= */

  const handleSearchChange = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {

    onSearchChange(
      event.target.value
    );
  };

  /* =======================================================
     CLEAR SEARCH
  ======================================================= */

  const clearSearch = () => {
    onSearchChange("");
  };

  /* =======================================================
     RENDER
  ======================================================= */

  return (

    <div
      style={{
        height: 56,
        background: "white",
        borderBottom:
          "1px solid #E2E8F0",
        display: "flex",
        alignItems: "center",
        padding: "0 20px",
        gap: 12,
        flexShrink: 0,
        position: "relative",
        zIndex: 40,
      }}
    >

      {/* =================================================
          MENU
      ================================================= */}

      <button
        className="btn-secondary"
        type="button"
        style={{
          padding: "6px 8px",
          border: "none",
          background: "none",
        }}
        onClick={onMenuToggle}
      >
        <IcoMenu
          size={18}
          className="text-slate-500"
        />
      </button>


      {/* =================================================
          SEARCH
      ================================================= */}

      <div
        style={{
          flex: "1 1 320px",
          maxWidth: 460,
          minWidth: 180,
          position: "relative",
        }}
      >

        {/* SEARCH ICON */}

        <IcoSearch
          size={14}
          className="text-slate-400"
          style={{
            position: "absolute",
            left: 10,
            top: "50%",
            transform:
              "translateY(-50%)",
            pointerEvents: "none",
          } as React.CSSProperties}
        />


        {/* SEARCH INPUT */}

        <input
          type="search"
          value={search}

          onChange={
            handleSearchChange
          }

          placeholder={
            "Search jobs, skills, courses, districts..."
          }

          autoComplete="off"

          style={{
            width: "100%",
            boxSizing: "border-box",

            padding:
              search.trim().length > 0
                ? "7px 34px 7px 32px"
                : "7px 12px 7px 32px",

            border:
              "1px solid #E2E8F0",

            borderRadius: 8,

            fontSize: 13,

            color: "#334155",

            background: "#F8FAFC",

            outline: "none",

            transition:
              "all 0.15s ease",
          }}

          onFocus={(event) => {

            event.currentTarget.style.borderColor =
              "#1D4ED8";

            event.currentTarget.style.background =
              "white";

          }}

          onBlur={(event) => {

            event.currentTarget.style.borderColor =
              "#E2E8F0";

            event.currentTarget.style.background =
              "#F8FAFC";

          }}

          onKeyDown={(event) => {

            if (
              event.key === "Escape"
            ) {
              clearSearch();
            }

          }}
        />


        {/* CLEAR SEARCH BUTTON */}

        {search.trim().length > 0 && (

          <button
            type="button"

            onClick={clearSearch}

            aria-label="Clear search"

            style={{
              position: "absolute",
              right: 7,
              top: "50%",
              transform:
                "translateY(-50%)",

              width: 22,
              height: 22,

              border: "none",
              background: "transparent",

              color: "#94A3B8",

              cursor: "pointer",

              fontSize: 16,

              lineHeight: 1,

              display: "flex",
              alignItems: "center",
              justifyContent: "center",

              borderRadius: 5,
            }}

            onMouseEnter={(event) => {
              event.currentTarget.style.background =
                "#F1F5F9";

              event.currentTarget.style.color =
                "#334155";
            }}

            onMouseLeave={(event) => {
              event.currentTarget.style.background =
                "transparent";

              event.currentTarget.style.color =
                "#94A3B8";
            }}
          >
            ×
          </button>

        )}

      </div>


      {/* =================================================
          STATE FILTER
      ================================================= */}

      <select
        value={state}

        onChange={(event) =>
          onStateChange(
            event.target.value
          )
        }

        className="select-input"

        style={{
          fontSize: 12,
          minWidth: 130,
          cursor: "pointer",
        }}
      >

        {states.map((item) => (

          <option
            key={item}
            value={item}
          >
            {item}
          </option>

        ))}

      </select>


      {/* =================================================
          SECTOR FILTER
      ================================================= */}

      <select
        value={sector}

        onChange={(event) =>
          onSectorChange(
            event.target.value
          )
        }

        className="select-input"

        style={{
          fontSize: 12,
          minWidth: 135,
          cursor: "pointer",
        }}
      >

        {sectors.map((item) => (

          <option
            key={item}
            value={item}
          >
            {item}
          </option>

        ))}

      </select>


      {/* =================================================
          SPACER
      ================================================= */}

      <div
        style={{
          flex: 1,
        }}
      />


      {/* =================================================
          DATE
      ================================================= */}

      <span
        style={{
          fontSize: 12,
          color: "#64748B",
          fontFamily:
            "'JetBrains Mono', monospace",
          whiteSpace: "nowrap",
        }}
      >
        Sep 2026
      </span>


      {/* =================================================
          NOTIFICATIONS
      ================================================= */}

      <div
        style={{
          position: "relative",
          cursor: "pointer",
        }}
      >

        <IcoBell
          size={18}
          className="text-slate-500"
        />

        <div
          style={{
            position: "absolute",
            top: -3,
            right: -3,
            width: 8,
            height: 8,
            background: "#DC2626",
            borderRadius: "50%",
            border:
              "1.5px solid white",
          }}
        />

      </div>


      {/* =================================================
          ROLE SELECTOR
      ================================================= */}

      <div
        style={{
          position: "relative",
        }}
      >

        <button
          type="button"

          onClick={() =>
            setShowRoleMenu(
              (previous) => !previous
            )
          }

          style={{
            display: "flex",
            alignItems: "center",
            gap: 8,

            padding: "6px 10px",

            border:
              "1px solid #E2E8F0",

            borderRadius: 8,

            background: "white",

            cursor: "pointer",

            fontSize: 12,

            fontWeight: 500,

            color: "#334155",
          }}
        >

          <div
            style={{
              width: 26,
              height: 26,

              background:
                "linear-gradient(135deg, #1D4ED8, #0D9488)",

              borderRadius: "50%",

              display: "flex",

              alignItems: "center",

              justifyContent: "center",
            }}
          >

            <IcoUser
              size={13}
              className="text-white"
            />

          </div>


          <span>
            {role.split(" / ")[0]}
          </span>


          <IcoChevronDown
            size={12}
            className="text-slate-400"
          />

        </button>


        {/* =================================================
            ROLE DROPDOWN
        ================================================= */}

        {showRoleMenu && (

          <div
            style={{
              position: "absolute",

              right: 0,

              top:
                "calc(100% + 4px)",

              background: "white",

              border:
                "1px solid #E2E8F0",

              borderRadius: 10,

              boxShadow:
                "0 8px 24px rgba(0,0,0,0.1)",

              width: 210,

              zIndex: 100,

              overflow: "hidden",
            }}
          >

            {roles.map((item) => (

              <div
                key={item}

                onClick={() => {

                  onRoleChange(item);

                  setShowRoleMenu(false);

                }}

                style={{
                  padding:
                    "9px 14px",

                  fontSize: 13,

                  color:
                    item === role
                      ? "#1D4ED8"
                      : "#334155",

                  fontWeight:
                    item === role
                      ? 600
                      : 400,

                  cursor: "pointer",

                  background:
                    item === role
                      ? "#EFF6FF"
                      : "transparent",
                }}

                onMouseEnter={(event) => {

                  if (
                    item !== role
                  ) {

                    event.currentTarget.style.background =
                      "#F8FAFC";

                  }

                }}

                onMouseLeave={(event) => {

                  if (
                    item !== role
                  ) {

                    event.currentTarget.style.background =
                      "transparent";

                  }

                }}
              >

                {item}

              </div>

            ))}

          </div>

        )}

      </div>

    </div>
  );
}