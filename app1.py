import streamlit as st
import sqlite3
import pandas as pd
import os

# --- Data Connection ---
def get_fuel_logs(db_path="tracker.db"):
    if not os.path.exists(db_path):
        return None, "missing"
    try:
        conn = sqlite3.connect(db_path)
        df = pd.read_sql_query(
            "SELECT date, liters, price_per_liter, total_cost, station, weather_info FROM fuel_logs ORDER BY date DESC",
            conn
        )
        conn.close()
        if df.empty:
            return None, "empty"
        return df, "ok"
    except Exception:
        return None, "error"

st.set_page_config(page_title="Applegreen Go", page_icon="🍏", layout="centered")

# --- CSS for mobile look and nav ---
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
        html, body, [class*="css"] {
            font-family: 'Inter', 'Roboto', sans-serif !important;
        }
        .header-container {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: #fff;
            padding: 18px 0 10px 0;
            margin-bottom: 18px;
        }
        .header-logo {
            height: 44px;
        }
        .profile-section {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .profile-avatar {
            width: 42px;
            height: 42px;
            border-radius: 50%;
            background: #e0e0e0;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 800;
            color: #007A33;
            font-size: 22px;
            border: 2px solid #8DC63F;
        }
        .welcome-text {
            font-family: 'Inter', 'Roboto', sans-serif;
            color: #222;
            font-size: 16px;
            font-weight: 600;
        }
        .rewards-card {
            background: #fff;
            border-radius: 24px;
            box-shadow: 0 4px 16px rgba(0,0,0,0.04);
            padding: 28px 0 18px 0;
            margin-bottom: 24px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .circular-progress {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            background: conic-gradient(#007A33 calc(var(--progress)*1%), #8DC63F 0 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 10px;
            position: relative;
        }
        .circular-progress-inner {
            width: 90px;
            height: 90px;
            border-radius: 50%;
            background: #fff;
            display: flex;
            align-items: center;
            justify-content: center;
            position: absolute;
            left: 50%; top: 50%; transform: translate(-50%,-50%);
            font-size: 32px;
            font-weight: 800;
            color: #007A33;
            font-family: 'Inter', 'Roboto', sans-serif;
        }
        .rewards-label {
            color: #007A33;
            font-size: 17px;
            font-weight: 600;
            margin-bottom: 2px;
            font-family: 'Inter', 'Roboto', sans-serif;
        }
        .rewards-progress {
            color: #666;
            font-size: 13px;
            margin-top: 2px;
            font-family: 'Inter', 'Roboto', sans-serif;
        }
        .icon-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 18px;
            max-width: 700px;
            margin: 0 auto 28px auto;
            text-align: center;
        }
        .icon-grid-item {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .icon-bg {
            background: #F2F3F5;
            border-radius: 16px;
            width: 56px;
            height: 56px;
            margin: 0 auto 8px auto;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .next-stop-card {
            background: linear-gradient(90deg, #007A33 0%, #8DC63F 100%);
            border-radius: 20px;
            color: #fff;
            padding: 22px 24px 18px 24px;
            margin: 32px 0 16px 0;
            box-shadow: 0 4px 16px rgba(0,0,0,0.04);
            font-family: 'Inter', 'Roboto', sans-serif;
        }
        .next-stop-title {
            font-size: 16px;
            font-weight: 600;
            margin-bottom: 6px;
        }
        .next-stop-station {
            font-size: 22px;
            font-weight: 800;
            margin-bottom: 2px;
        }
        .next-stop-details {
            font-size: 14px;
            margin-bottom: 2px;
        }
        .next-stop-fuel {
            font-size: 15px;
            font-weight: 600;
            margin-top: 8px;
        }
        .next-stop-fuel span {
            margin-right: 18px;
        }
        .stButton>button {
            border-radius: 20px !important;
        }
        .bottom-nav {
            position: fixed;
            left: 0;
            right: 0;
            bottom: 0;
            height: 68px;
            background: #fff;
            box-shadow: 0 -2px 12px rgba(0,0,0,0.06);
            display: flex;
            justify-content: space-around;
            align-items: center;
            z-index: 100;
        }
        .nav-btn {
            background: none;
            border: none;
            outline: none;
            padding: 0;
            margin: 0;
            cursor: pointer;
            width: 60px;
            height: 60px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        .nav-btn.selected {
            color: #007A33;
        }
        .nav-btn svg {
            margin-bottom: 4px;
        }
        .station-hero {
            width: 100%;
            max-width: 700px;
            border-radius: 24px;
            margin: 18px auto 24px auto;
            box-shadow: 0 4px 16px rgba(0,0,0,0.06);
            display: block;
        }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("""
<div class="header-container">
    <img src="https://upload.wikimedia.org/wikipedia/commons/6/63/Applegreen_Logo.png" class="header-logo" alt="Applegreen Logo">
    <div class="profile-section">
        <span class="welcome-text">Welcome, Valentin</span>
        <div class="profile-avatar">V</div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Pages and Navigation Mapping ---
pages = ["Dashboard", "Fuel Tracker", "Station Finder", "Fuel Calculator"]
nav_map = {
    "Home": "Dashboard",
    "Map": "Station Finder",
    "Rewards": "Fuel Tracker",
    "Calculator": "Fuel Calculator"
}
nav_order = ["Home", "Map", "Rewards", "Calculator"]

# --- Session State for Navigation ---
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "Dashboard"

# --- Sidebar Navigation (sync with session state) ---
current_idx = pages.index(st.session_state["current_page"])
selected_page = st.sidebar.selectbox("Navigate", pages, index=current_idx)
if selected_page != st.session_state["current_page"]:
    st.session_state["current_page"] = selected_page
    st.rerun()

# --- Bottom Navigation Bar (fully functional) ---
nav_cols = st.columns(4)
nav_icons = [
    """<svg width="28" height="28" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M4 12L14 4l10 8v10a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V12z" stroke="#007A33" stroke-width="2" fill="none"/><rect x="10" y="16" width="8" height="6" rx="2" fill="#8DC63F"/></svg>""",
    """<svg width="28" height="28" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="14" cy="14" r="10" stroke="#007A33" stroke-width="2"/><path d="M14 8v6l4 4" stroke="#8DC63F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>""",
    """<svg width="28" height="28" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="14" cy="14" r="10" stroke="#007A33" stroke-width="2"/><path d="M9 17l5-6 5 6" stroke="#8DC63F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>""",
    """<svg width="28" height="28" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="14" cy="11" r="5" stroke="#007A33" stroke-width="2"/><rect x="7" y="18" width="14" height="6" rx="3" fill="#8DC63F"/></svg>"""
]
for i, (col, nav, icon) in enumerate(zip(nav_cols, nav_order, nav_icons)):
    selected = (st.session_state["current_page"] == nav_map[nav])
    btn_label = f"{icon}<div style='font-size:12px;'>{nav}</div>"
    if col.button("", key=f"navbtn_{nav}", help=nav, use_container_width=True):
        st.session_state["current_page"] = nav_map[nav]
        st.rerun()
    col.markdown(
        f"<div class='nav-btn{' selected' if selected else ''}'>{btn_label}</div>",
        unsafe_allow_html=True
    )

# --- Main Page Routing ---
df, db_status = get_fuel_logs()

if st.session_state["current_page"] == "Dashboard":
    st.title("Applegreen Go")

    # --- Hero Image ---
    st.markdown(
        '<img src="https://applegreenstores.com/wp-content/uploads/2019/04/fuelgood-home-tile.jpg" class="station-hero" alt="Applegreen Storefront">',
        unsafe_allow_html=True
    )

    # --- Rewards Section ---
    if db_status == "ok":
        total_liters = df["liters"].sum()
        points = int(total_liters * 10)
        progress = min((points % 2500) / 2500 * 100, 100)
    else:
        points = 0
        progress = 0

    st.markdown(f"""
        <div class="rewards-card">
            <div class="rewards-label">My Rewards</div>
            <div class="circular-progress" style="--progress:{progress};">
                <div class="circular-progress-inner">{points}</div>
            </div>
            <div class="rewards-progress">{int(progress)}% to next €5 reward</div>
        </div>
    """, unsafe_allow_html=True)

    # --- Action Grid ---
    st.markdown("""
        <div class="icon-grid">
            <div class="icon-grid-item">
                <div class="icon-bg">
                    <!-- Food & Drink Icon -->
                    <svg width="32" height="32" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="16" cy="16" r="15" stroke="#007A33" stroke-width="2"/>
                        <rect x="10" y="14" width="12" height="8" rx="3" fill="#8DC63F"/>
                        <rect x="13" y="10" width="6" height="4" rx="2" fill="#007A33"/>
                    </svg>
                </div>
                <div style="font-size: 14px; color: #222;">Food & Drink</div>
            </div>
            <div class="icon-grid-item">
                <div class="icon-bg">
                    <!-- Fuel Up Icon -->
                    <svg width="32" height="32" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <rect x="8" y="8" width="16" height="16" rx="4" fill="#8DC63F" stroke="#007A33" stroke-width="2"/>
                        <rect x="14" y="12" width="4" height="8" rx="2" fill="#007A33"/>
                        <rect x="12" y="20" width="8" height="2" rx="1" fill="#007A33"/>
                    </svg>
                </div>
                <div style="font-size: 14px; color: #222;">Fuel Up</div>
            </div>
            <div class="icon-grid-item">
                <div class="icon-bg">
                    <!-- Car Wash Icon -->
                    <svg width="32" height="32" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <ellipse cx="16" cy="20" rx="8" ry="4" fill="#8DC63F"/>
                        <rect x="10" y="8" width="12" height="8" rx="4" fill="#007A33"/>
                        <circle cx="16" cy="12" r="2" fill="#fff"/>
                    </svg>
                </div>
                <div style="font-size: 14px; color: #222;">Car Wash</div>
            </div>
            <div class="icon-grid-item">
                <div class="icon-bg">
                    <!-- Shop Offers Icon -->
                    <svg width="32" height="32" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <rect x="8" y="10" width="16" height="12" rx="4" fill="#8DC63F" stroke="#007A33" stroke-width="2"/>
                        <circle cx="16" cy="16" r="3" fill="#007A33"/>
                        <rect x="14" y="20" width="4" height="2" rx="1" fill="#007A33"/>
                    </svg>
                </div>
                <div style="font-size: 14px; color: #222;">Shop Offers</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # --- Next Stop Feature ---
    if db_status == "ok" and not df.empty:
        latest_station = df.iloc[0]["station"]
    else:
        latest_station = "No recent station"
    st.markdown(f"""
        <div class="next-stop-card">
            <div class="next-stop-title">Your Next Stop</div>
            <div class="next-stop-station">{latest_station}</div>
            <div class="next-stop-details">4.2 km away</div>
            <div class="next-stop-fuel">
                <span>Unleaded: <b>€1.72</b></span>
                <span>Diesel: <b>€1.65</b></span>
            </div>
        </div>
    """, unsafe_allow_html=True)

elif st.session_state["current_page"] == "Fuel Tracker":
    st.title("⛽ My Fuel Logs")

    if st.button("Refresh Data"):
        st.rerun()

    df, db_status = get_fuel_logs()

    if db_status == "missing":
        st.warning("Please run tracker.py to initialize data.")
    elif db_status == "empty":
        st.warning("No fuel logs found. Please add data using tracker.py.")
    elif db_status == "error":
        st.error("Could not read tracker.db. Please check your database.")
    else:
        total_liters = df["liters"].sum()
        total_spend = df["total_cost"].sum()
        col1, col2 = st.columns(2)
        col1.metric("Total Liters", f"{total_liters:.1f} L")
        col2.metric("Total Spend (€)", f"€{total_spend:.2f}")
        st.dataframe(df, width='stretch')

elif st.session_state["current_page"] == "Station Finder":
    st.title("Find a Station")
    city = st.text_input("Enter city or town name")
    show_map = False
    if city.strip():
        show_map = True

    # Show contextual station image
    st.markdown(
        '<img src="https://applegreenstores.com/wp-content/uploads/2018/06/about-hero.jpg" class="station-hero" alt="Applegreen Forecourt">',
        unsafe_allow_html=True
    )

    # Live Map Integration
    if show_map:
        map_url = f"https://maps.google.com/maps?q={city.strip().replace(' ', '%20')}+Applegreen&t=&z=13&ie=UTF8&iwloc=&output=embed"
        st.iframe(
            f'<iframe width="100%" height="340" style="border-radius:18px;border:none;" src="{map_url}"></iframe>',
            height=360
        )
    else:
        st.info("Type an Irish city or town name above to see Applegreen locations on the map.")

elif st.session_state["current_page"] == "Fuel Calculator":
    st.title("Fuel Cost Calculator")
    litres = st.number_input("Litres", min_value=0.0, step=1.0)
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel"])
    prices = {"Petrol": 1.75, "Diesel": 1.65}
    if st.button("Calculate Cost"):
        if litres > 0:
            cost = litres * prices[fuel_type]
            st.success(f"{litres}L of {fuel_type} will cost €{cost:.2f}")
        else:
            st.error("Please enter a positive number of litres.")


