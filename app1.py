import streamlit as st
import sqlite3
import pandas as pd
import os
from datetime import datetime, timedelta

# --- Session Page Initialization ---
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "Dashboard"

# --- Session Login Gate ---
if "logged_in_user" not in st.session_state:
    st.session_state["logged_in_user"] = None

def logout():
    st.session_state["logged_in_user"] = None
    st.session_state["current_page"] = "Dashboard"
    st.rerun()

def login_screen():
    st.markdown(
        """
        <div style="display:flex;justify-content:center;align-items:center;height:70vh;">
          <div style="background:#fff;border-radius:18px;box-shadow:0 4px 24px rgba(0,0,0,0.07);padding:40px 32px;max-width:340px;width:100%;text-align:center;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/63/Applegreen_Logo.png" width="90" style="margin-bottom:18px;">
            <h2 style="color:#007A33;font-weight:800;margin-bottom:18px;">Welcome to Applegreen Go</h2>
        """,
        unsafe_allow_html=True
    )
    name = st.text_input("Enter your name:", key="login_name", max_chars=32)
    login_btn = st.button("Get Started", type="primary")
    st.markdown("</div></div>", unsafe_allow_html=True)
    if login_btn and name.strip():
        st.session_state["logged_in_user"] = name.strip()
        st.rerun()
    st.stop()

if not st.session_state["logged_in_user"]:
    login_screen()

# --- Sidebar Logout ---
with st.sidebar:
    st.write(f"Logged in as: **{st.session_state['logged_in_user']}**")
    if st.button("Logout"):
        logout()

# --- DB Connection, Migration, and Auto-Seed ---
def init_db_and_get_logs(user):
    db_path = "tracker.db"
    table = "fuel_logs"
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute(f"""
            CREATE TABLE IF NOT EXISTS {table} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                liters REAL,
                price_per_liter REAL,
                total_cost REAL,
                station TEXT,
                weather_info TEXT,
                user_name TEXT DEFAULT 'Valentin'
            )
        """)
        conn.commit()
        conn.close()
    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute(f"PRAGMA table_info({table})")
        cols = [row[1] for row in cur.fetchall()]
        if "user_name" not in cols:
            try:
                cur.execute(f"ALTER TABLE {table} ADD COLUMN user_name TEXT DEFAULT 'Valentin'")
                conn.commit()
            except Exception:
                pass
        df = pd.read_sql_query(
            f"SELECT date, liters, price_per_liter, total_cost, station, weather_info, user_name FROM {table} WHERE user_name = ? ORDER BY date DESC",
            conn,
            params=(user,)
        )
        if df.empty:
            today = datetime.now()
            mock_entries = [
                (
                    (today - timedelta(days=2)).strftime("%Y-%m-%d"),
                    45.5, 1.71, round(45.5 * 1.71, 2), "Dublin M1", "Sunny", user
                ),
                (
                    (today - timedelta(days=8)).strftime("%Y-%m-%d"),
                    38.0, 1.72, round(38.0 * 1.72, 2), "Galway Plaza", "Cloudy", user
                ),
                (
                    (today - timedelta(days=15)).strftime("%Y-%m-%d"),
                    42.1, 1.70, round(42.1 * 1.70, 2), "Enfield", "Rainy", user
                ),
            ]
            cur.executemany(
                f"INSERT INTO {table} (date, liters, price_per_liter, total_cost, station, weather_info, user_name) VALUES (?, ?, ?, ?, ?, ?, ?)",
                mock_entries
            )
            conn.commit()
            df = pd.read_sql_query(
                f"SELECT date, liters, price_per_liter, total_cost, station, weather_info, user_name FROM {table} WHERE user_name = ? ORDER BY date DESC",
                conn,
                params=(user,)
            )
        conn.close()
        if df.empty:
            return None, "empty"
        return df, "ok"
    except Exception:
        return None, "error"

st.set_page_config(page_title="Applegreen Go", page_icon="🍏", layout="centered")

# --- App CSS (including mobile nav and flex row fix) ---
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
        .main-content-pad {
            padding-bottom: 90px;
        }
        .station-hero {
            width: 100%;
            max-width: 700px;
            border-radius: 24px;
            margin: 18px auto 24px auto;
            box-shadow: 0 4px 16px rgba(0,0,0,0.06);
            display: block;
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
        .empty-state-card {
            background: #fff;
            border-radius: 18px;
            box-shadow: 0 4px 24px rgba(0,0,0,0.07);
            padding: 48px 28px 36px 28px;
            max-width: 420px;
            margin: 48px auto 32px auto;
            text-align: center;
        }
        .empty-state-card .icon {
            margin-bottom: 18px;
        }
        .empty-state-title {
            font-size: 21px;
            font-weight: 700;
            color: #007A33;
            margin-bottom: 8px;
        }
        .empty-state-desc {
            color: #444;
            font-size: 15px;
            margin-bottom: 18px;
        }
        .empty-state-script {
            background: #F2F3F5;
            border-radius: 8px;
            font-family: monospace;
            font-size: 14px;
            color: #007A33;
            padding: 8px 14px;
            margin: 0 auto 0 auto;
            display: inline-block;
        }
        /* --- Horizontal Row Dock Layout Fix for st.columns --- */
        div[data-testid="stHorizontalBlock"] {
            display: flex !important;
            flex-direction: row !important;
            flex-wrap: nowrap !important;
            gap: 6px !important;
            width: 100% !important;
        }
        div[data-testid="stHorizontalBlock"] > div {
            width: 25% !important;
            min-width: 20% !important;
            flex: 1 1 0% !important;
        }
        div[data-testid="stHorizontalBlock"] .stButton > button {
            background-color: rgba(141, 198, 63, 0.15) !important;
            color: #007A33 !important;
            border: 1px solid rgba(141, 198, 63, 0.25) !important;
            border-radius: 14px !important;
            min-height: 54px !important;
            width: 100% !important;
            font-size: 12px !important;
            font-weight: 700 !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            transition: all 0.15s ease-in-out !important;
        }
        div[data-testid="stHorizontalBlock"] .stButton > button:hover {
            background-color: rgba(141, 198, 63, 0.30) !important;
            transform: scale(0.96) !important;
        }
        .bottom-nav-wrapper {
            position: fixed;
            left: 0;
            right: 0;
            bottom: 0;
            width: 100%;
            z-index: 99999;
            background: #ffffff;
            border-top: 1px solid rgba(0,0,0,0.08);
            padding: 10px 12px 24px 12px;
            box-shadow: 0 -4px 20px rgba(0,0,0,0.06);
        }
        .stAppViewContainer, .main, .block-container {
            padding-bottom: 140px !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- Personalized Header ---
user = st.session_state["logged_in_user"]
avatar_letter = user[0].upper() if user else "U"
st.markdown(f"""
<div class="header-container">
    <img src="https://upload.wikimedia.org/wikipedia/commons/6/63/Applegreen_Logo.png" class="header-logo" alt="Applegreen Logo">
    <div class="profile-section">
        <span class="welcome-text">Welcome, {user}</span>
        <div class="profile-avatar">{avatar_letter}</div>
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

# --- Main Content Padding ---
st.markdown('<div class="main-content-pad">', unsafe_allow_html=True)

# --- Main Page Routing ---
df, db_status = init_db_and_get_logs(user)
page = st.session_state["current_page"]

if page == "Dashboard":
    st.title("Applegreen Go")
    st.image(
        "https://applegreenstores.com/wp-content/uploads/2019/04/fuelgood-home-tile.jpg",
        caption=None,
        width='stretch'
    )
    if db_status == "ok":
        total_liters = df["liters"].sum()
        points = int(total_liters * 10)
        progress = min((points % 2500) / 2500 * 100, 100)
    else:
        points = 0
        progress = 0
    deg = int((progress / 100) * 360)
    st.markdown(f"""
        <div class="rewards-card">
            <div class="rewards-label">My Rewards</div>
            <div class="circular-progress" style="background:conic-gradient(#007A33 {deg}deg, #8DC63F {deg}deg 360deg);">
                <div class="circular-progress-inner">{points}</div>
            </div>
            <div class="rewards-progress">{int(progress)}% to next €5 reward</div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div class="icon-grid">
            <div class="icon-grid-item">
                <div class="icon-bg">🍔</div>
                <div style="font-size: 14px; color: #222;">Food & Drink</div>
            </div>
            <div class="icon-grid-item">
                <div class="icon-bg">⛽</div>
                <div style="font-size: 14px; color: #222;">Fuel Up</div>
            </div>
            <div class="icon-grid-item">
                <div class="icon-bg">🚗</div>
                <div style="font-size: 14px; color: #222;">Car Wash</div>
            </div>
            <div class="icon-grid-item">
                <div class="icon-bg">🛒</div>
                <div style="font-size: 14px; color: #222;">Shop Offers</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
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

elif page == "Fuel Tracker":
    st.title("⛽ My Fuel Logs")
    df, db_status = init_db_and_get_logs(user)
    if db_status == "missing":
        st.markdown("""
            <div class="empty-state-card">
                <div class="icon">⛽</div>
                <div class="empty-state-title">No Database Found</div>
                <div class="empty-state-desc">Please run the developer script below to initialize your fuel log database.</div>
                <div class="empty-state-script">python tracker.py</div>
            </div>
        """, unsafe_allow_html=True)
    elif db_status == "empty":
        st.markdown("""
            <div class="empty-state-card">
                <div class="icon">⛽</div>
                <div class="empty-state-title">No Fuel Logs Yet</div>
                <div class="empty-state-desc">Your fuel log is empty. Add records using the developer script, then refresh your dashboard.</div>
                <div class="empty-state-script">python tracker.py</div>
            </div>
        """, unsafe_allow_html=True)
    elif db_status == "error":
        st.error("Could not read tracker.db. Please check your database.")
    else:
        total_liters = df["liters"].sum()
        total_spend = df["total_cost"].sum()
        col1, col2 = st.columns(2)
        col1.metric("Total Liters", f"{total_liters:.1f} L")
        col2.metric("Total Spend (€)", f"€{total_spend:.2f}")
        st.dataframe(df, width='stretch')

elif page == "Station Finder":
    st.title("Find a Station")
    city = st.text_input("Enter city or town name")
    show_map = False
    if city.strip():
        show_map = True
    st.image(
        "https://applegreenstores.com/wp-content/uploads/2018/06/about-hero.jpg",
        caption=None,
        width='stretch'
    )
    if show_map:
        map_url = f"https://maps.google.com/maps?q={city.strip().replace(' ', '%20')}+Applegreen&t=&z=13&ie=UTF8&iwloc=&output=embed"
        # ✅ FIX: Removed 'use_container_width=True' argument to clear the TypeError crash
        st.iframe(src=map_url, height=360)
    else:
        st.info("Type an Irish city or town name above to see Applegreen locations on the map.")

elif page == "Fuel Calculator":
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

st.markdown("</div>", unsafe_allow_html=True)

# --- Native Streamlit Button Bottom Navbar (locked horizontal row) ---
st.markdown('<div class="bottom-nav-wrapper">', unsafe_allow_html=True)
nav_cols = st.columns(4)
with nav_cols[0]:
    if st.button(" <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-house" viewBox="0 0 16 16">
  <path d="M8.707 1.5a1 1 0 0 0-1.414 0L.646 8.146a.5.5 0 0 0 .708.708L2 8.207V13.5A1.5 1.5 0 0 0 3.5 15h9a1.5 1.5 0 0 0 1.5-1.5V8.207l.646.647a.5.5 0 0 0 .708-.708L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293zM13 7.207V13.5a.5.5 0 0 1-.5.5h-9a.5.5 0 0 1-.5-.5V7.207l5-5z"/>
</svg> Home", key="nav_home"):
        st.session_state["current_page"] = "Dashboard"
        st.rerun()
with nav_cols[1]:
    if st.button("📍 Map", key="nav_map"):
        st.session_state["current_page"] = "Station Finder"
        st.rerun()
with nav_cols[2]:
    if st.button("⛽ Logs", key="nav_logs"):
        st.session_state["current_page"] = "Fuel Tracker"
        st.rerun()
with nav_cols[3]:
    if st.button("🧮 Calc", key="nav_calc"):
        st.session_state["current_page"] = "Fuel Calculator"
        st.rerun()
st.markdown('</div>', unsafe_allow_html=True)
