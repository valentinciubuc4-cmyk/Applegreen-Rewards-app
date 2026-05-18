# Applegreen Go – Prototype Critique (Refined)

## Strengths

- **Station Finder Overhaul:**  
  The app now features a live, interactive map for station search, replacing all static city-to-address text dictionaries. Users can enter any Irish town or region and instantly view real Applegreen locations via a Google Maps iframe, greatly enhancing realism and utility.

- **Loyalty & Interface Architecture:**  
  All loyalty points, rewards progress, and "Next Stop" features are dynamically computed from the SQLite database. The interface leverages robust session state logic for both sidebar and bottom navigation, ensuring seamless, conflict-free page routing and a true multi-page experience.

- **Visual Authenticity:**  
  The dashboard and station views use real-world Applegreen forecourt imagery, eliminating placeholder text and static mockups. This delivers a high-fidelity, customer-facing look and feel.

- **Modern Compliance:**  
  All Streamlit API calls use up-to-date parameters (e.g., `use_container_width=True` for dataframes, `st.rerun()` for navigation), ensuring compatibility with Python 3.14 and current Streamlit releases.

## Limitations

- **Local Database Scope:**  
  The app remains tied to a local SQLite file, which restricts it to single-user or demo scenarios. For production, a cloud-hosted, multi-user database would be required.

- **No User Authentication:**  
  There is no login or user account system; all data is global and not user-specific. Adding authentication and user data partitioning is a necessary next step for real deployments.

- **CSS Injection Reliance:**  
  Custom navigation and button styling depend on injected CSS, which, while effective, may be brittle if Streamlit's DOM structure changes in future releases.

- **No Native Mobile App:**  
  The interface is mobile-friendly in the browser but is not a true native mobile application.

---

**Summary:**  
This prototype systematically minimizes static mockups, replacing them with live, data-driven and interactive components. It demonstrates a strong foundation for a branded, dynamic dashboard. For real-world scaling, future work should focus on cloud database integration, user authentication, and more robust UI componentization.
