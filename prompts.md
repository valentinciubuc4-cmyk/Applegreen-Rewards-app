# Applegreen Go – Developer Ledger & Architectural Design

## Architectural Overview

This Streamlit application (`app1.py`) is architected as a **self-contained, high-fidelity vertical slice** for safe, network-independent demonstration and presentation.  
**No live or cloud-hosted production server is required or used.**  
Instead, all telemetry, health checks, and operational events are simulated directly within the Python runtime.

---

## Telemetry Simulation Engine

- **Embedded Python Simulation:**  
  The app includes a built-in telemetry simulation engine that mimics real-world site monitoring and operational health checks.
- **Simulated JSON Payloads:**  
  The engine generates simulated JSON telemetry data for 120+ sites, each representing a retail location or system endpoint.
- **Randomized Glitch Injection:**  
  At random intervals, the simulation triggers operational glitches such as POS (Aloha/NCR) failures, payment gateway (Payzone) outages, or SMS back-office issues.
- **Internal Clock & Event Timeline:**  
  The simulation tracks an internal clock, logging events with timestamps (e.g., "60s: Anomaly detected on POS terminal").
- **Self-Healing Automation:**  
  When a failure is detected, a 90-second self-healing countdown is initiated, mimicking the execution of an Ansible runbook.  
  After the countdown, the affected system is automatically restored to a healthy (green) status, and a recovery log is generated (e.g., "90s: Ansible runbook successful. System restored.").
- **Live Log Streaming:**  
  All events and status changes are streamed live to the user interface, providing real-time feedback and transparency.

---

## Requirements & Presentation Mode

- **No External Dependencies:**  
  The simulation does not require any external network connections, APIs, or cloud services. All logic and data are generated locally.
- **Safe for Demo & Training:**  
  The design ensures that the app can be safely run in classrooms, demo environments, or offline presentations without risk or dependency on production infrastructure.
- **Vertical Slice Fidelity:**  
  The simulation engine, UI, and navigation together provide a realistic, end-to-end demonstration of operational monitoring, anomaly detection, and automated remediation as would be seen in a full-scale production deployment.

---

## Key Features

- **Session-safe navigation and login**
- **Automated data seeding for user dashboards**
- **Mobile-optimized, flexbox-anchored navigation bar**
- **Vision AI Live Logs with real-time anomaly and recovery events**
- **Dynamic error injection and self-healing for critical systems**
- **2026-compliant Streamlit layout and element usage**

---

This architecture enables rapid, reliable, and visually rich demonstration of Applegreen Go's operational monitoring and self-healing capabilities—entirely within a single
