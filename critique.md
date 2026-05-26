# Applegreen Go – Technical Critique

## Current Limitations

- **No Live Vision AI or Ansible Integration:**  
  The Vision AI anomaly detection and automated Ansible remediation are simulated in Python only. There is no actual AI model inference, no real-time computer vision, and no execution of infrastructure automation scripts.
- **Local State and Mock Payloads:**  
  All telemetry, health checks, and system events are generated locally within the Streamlit runtime. The app does not connect to any live network, ingest real telemetry, or interact with production infrastructure.
- **No Persistent or Distributed Data:**  
  User sessions, logs, and system states exist only in local memory or SQLite. There is no persistent, multi-user, or distributed data storage.

## Evaluation

- **Deliberate Simulation for Presentation Reliability:**  
  The choice to embed all telemetry simulation and state routing within the Streamlit app was intentional. This approach guarantees a robust, network-independent demonstration, eliminating the risk of live network failures, API downtime, or infrastructure outages during critical presentations.
- **High-Fidelity UI/UX and Log Streaming:**  
  The frontend delivers a polished, mobile-optimized experience with real-time, visually rich telemetry logs. The simulation engine provides a convincing operational narrative, including anomaly detection, self-healing countdowns, and recovery logs, all without external dependencies.

## Future Production Roadmap

To evolve this prototype into a true production system, the following engineering steps are required:

1. **Backend Migration:**  
   - Replace the embedded simulation engine with a live FastAPI backend.
   - Store and serve telemetry, logs, and system state from a PostgreSQL database.
2. **Persistent Cloud Hosting:**  
   - Deploy the backend and database to a secure, scalable cloud environment (e.g., Azure, AWS, GCP).
   - Host the Streamlit frontend as a managed web service.
3. **API Authentication and Security:**  
   - Implement OAuth2 or API key authentication for all backend endpoints.
   - Enforce role-based access controls for sensitive operations.
4. **Real Telemetry Ingestion:**  
   - Build ingestion pipelines to collect live telemetry from Applegreen’s physical sites, POS systems, payment gateways, and back-office infrastructure.
   - Integrate with real Vision AI models for anomaly detection and trigger actual Ansible playbooks for automated remediation.
5. **Distributed State and Multi-User Support:**  
   - Enable persistent user sessions, distributed logging, and multi-user dashboards.
   - Ensure all operational events and logs are stored and queryable for audit and analytics.

---

**Summary:**  
This build is a robust, presentation-grade simulation, engineered for reliability and visual clarity. Transitioning to production will require significant backend, security, and integration work to deliver true live monitoring and automated remediation
