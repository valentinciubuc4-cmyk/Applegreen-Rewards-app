import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Applegreen Rewards", page_icon="🍏")

# --- Custom CSS for styling ---
st.markdown("""
    <style>
        body, .stButton>button, .nav-item, .welcome-text, .profile-avatar, input, .header-container, .profile-section {
            font-family: 'Inter', 'Roboto', sans-serif !important;
        }
        .stButton>button {
            border-radius: 20px !important;
        }
        button, [type="button"] {
            border-radius: 20px !important;
            font-family: 'Inter', 'Roboto', sans-serif !important;
        }
        .nav-item {
            font-family: 'Inter', 'Roboto', sans-serif !important;
        }
        input[type="text"] {
            font-family: 'Inter', 'Roboto', sans-serif !important;
            border-radius: 20px !important;
        }
        .header-logo {
            font-family: 'Inter', 'Roboto', sans-serif !important;
        }
        .profile-avatar {
            font-family: 'Inter', 'Roboto', sans-serif !important;
        }
        .header-container {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: #fff;
            padding: 16px 0 8px 0;
            margin-bottom: 24px;
        }
        .header-logo {
            height: 48px;
        }
        .profile-section {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .profile-avatar {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: #e0e0e0;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            color: #007A33;
            font-size: 20px;
        }
        .welcome-text {
            font-family: 'Inter', 'Roboto', sans-serif;
            color: #222;
            font-size: 16px;
            font-weight: 500;
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
        .nav-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            color: #007A33;
            font-size: 12px;
            font-family: 'Inter', 'Roboto', sans-serif;
            text-decoration: none;
            font-weight: 500;
        }
        .nav-item svg {
            margin-bottom: 4px;
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

# --- Session State for Points ---
if 'points' not in st.session_state:
    st.session_state.points = 1850

# --- Sidebar Navigation ---
page = st.sidebar.selectbox("Navigate", ["Dashboard", "Station Finder", "Fuel Calculator"])

# --- Dashboard Page ---
if page == "Dashboard":
    st.title("Applegreen Dashboard")
    st.markdown("### Loyalty Points")
    st.markdown(f"<h1 style='color:#007A33;font-size:64px'>{st.session_state.points}</h1>", unsafe_allow_html=True)
    if st.button("Add 100 Points"):
        st.session_state.points += 100
        st.rerun()

    # --- Loyalty Card with Gradient ---
    st.markdown("""
        <div style="
            background: linear-gradient(90deg, #007A33 0%, #8DC63F 100%);
            border-radius: 24px;
            padding: 32px 24px 24px 24px;
            margin-bottom: 32px;
            box-shadow: 0 4px 16px rgba(0,0,0,0.04);
            display: flex;
            flex-direction: column;
            align-items: center;
            ">
            <div style="color: white; font-size: 18px; font-weight: 500; margin-bottom: 8px; font-family: 'Inter', 'Roboto', sans-serif;">
                Loyalty Points
            </div>
            <div style="color: white; font-size: 56px; font-weight: bold; margin-bottom: 8px; font-family: 'Inter', 'Roboto', sans-serif;">
                1,850
            </div>
            <div style="width: 100%; max-width: 260px; margin-bottom: 12px;">
                <div style="background: rgba(255,255,255,0.3); border-radius: 4px; height: 8px; width: 100%;">
                    <div style="background: white; height: 8px; border-radius: 4px; width: 74%;"></div>
                </div>
                <div style="color: white; font-size: 12px; margin-top: 4px; text-align: right;">
                    74% to next reward
                </div>
            </div>
            <button style="
                background: white;
                color: #007A33;
                border: none;
                border-radius: 20px;
                padding: 10px 32px;
                font-size: 16px;
                font-weight: bold;
                margin-top: 8px;
                cursor: pointer;
                font-family: 'Inter', 'Roboto', sans-serif;
            ">
                View Rewards
            </button>
        </div>
    """, unsafe_allow_html=True)

    # --- Search Bar ---
    st.markdown("""
        <div style="
            width: 100%;
            max-width: 400px;
            margin: 24px auto 0 auto;
        ">
            <input 
                type="text" 
                placeholder="Search fuel, food, stores..." 
                style="
                    width: 100%;
                    padding: 12px 18px;
                    border-radius: 20px;
                    border: none;
                    background: #F2F3F5;
                    font-size: 16px;
                    font-family: 'Inter', 'Roboto', sans-serif;
                    outline: none;
                    box-sizing: border-box;
                "
            />
        </div>
    """, unsafe_allow_html=True)

    # --- Hero Image with Overlay Button ---
    st.markdown("""
        <div style="position: relative; width: 100%; max-width: 700px; margin: 32px auto 0 auto; border-radius: 24px; overflow: hidden; box-shadow: 0 4px 16px rgba(0,0,0,0.06);">
            <img src="https://img.resized.co/checkout/eyJkYXRhIjoie1widXJsXCI6XCJodHRwczpcXFwvXFxcL21lZGlhLm1hZGlzb25wdWJsaWNhdGlvbnMuZXVcXFwvdXBsb2Fkc1xcXC8yMDE4XFxcLzA2XFxcLzA2MDk1ODU4XFxcL0FwcGxlZ3JlZW5OYXZhbi05MzIyLTEwMjR4NTQyLmpwZ1wiLFwid2lkdGhcIjo2MDAsXCJoZWlnaHRcIjo0MDAsXCJkZWZhdWx0XCI6XCJodHRwczpcXFwvXFxcL3d3dy5jaGVja291dC5pZVxcXC9pXFxcL25vaW1hZ2UucG5nXCIsXCJvcHRpb25zXCI6e1wib3V0cHV0XCI6XCJhdmlmXCJ9fSIsImhhc2giOiJkODZlZjc4ZWM3NWUxZmZiMjg5YTkzYTAwYWUwNDJlNWNlYzkwZWUwIn0=/applegreen-reports-strong-start-in-first-five-months-ahead-of-agm.jpg"
                 alt="Applegreen Storefront"
                 style="width: 100%; display: block; object-fit: cover; min-height: 180px; max-height: 260px;">
            <a href="#Station-Finder" style="position: absolute; left: 50%; bottom: 24px; transform: translateX(-50%); text-decoration: none;">
                <div style="
                    display: flex;
                    align-items: center;
                    gap: 10px;
                    background: rgba(0,0,0,0.8);
                    color: #fff;
                    border-radius: 20px;
                    padding: 12px 28px;
                    font-size: 18px;
                    font-weight: 600;
                    font-family: 'Inter', 'Roboto', sans-serif;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.18);
                    cursor: pointer;
                    border: none;
                ">
                    <svg width="22" height="22" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="11" cy="11" r="10" stroke="#8DC63F" stroke-width="2"/>
                        <path d="M11 6v5l3 3" stroke="#8DC63F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    Find a Station
                </div>
            </a>
        </div>
    """, unsafe_allow_html=True)

    # --- Icon Grid ---
    st.markdown("""
        <div style="
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 18px;
            max-width: 700px;
            margin: 32px auto 0 auto;
            text-align: center;
        ">
            <div>
                <div style="background: #F2F3F5; border-radius: 16px; width: 56px; height: 56px; margin: 0 auto 8px auto; display: flex; align-items: center; justify-content: center;">
                    <!-- Food & Drink Icon -->
                    <svg width="32" height="32" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="16" cy="16" r="15" stroke="#007A33" stroke-width="2"/>
                        <rect x="10" y="14" width="12" height="8" rx="3" fill="#8DC63F"/>
                        <rect x="13" y="10" width="6" height="4" rx="2" fill="#007A33"/>
                    </svg>
                </div>
                <div style="font-size: 14px; color: #222; font-family: 'Inter', 'Roboto', sans-serif;">Food & Drink</div>
            </div>
            <div>
                <div style="background: #F2F3F5; border-radius: 16px; width: 56px; height: 56px; margin: 0 auto 8px auto; display: flex; align-items: center; justify-content: center;">
                    <!-- Fuel Up Icon -->
                    <svg width="32" height="32" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <rect x="8" y="8" width="16" height="16" rx="4" fill="#8DC63F" stroke="#007A33" stroke-width="2"/>
                        <rect x="14" y="12" width="4" height="8" rx="2" fill="#007A33"/>
                        <rect x="12" y="20" width="8" height="2" rx="1" fill="#007A33"/>
                    </svg>
                </div>
                <div style="font-size: 14px; color: #222; font-family: 'Inter', 'Roboto', sans-serif;">Fuel Up</div>
            </div>
            <div>
                <div style="background: #F2F3F5; border-radius: 16px; width: 56px; height: 56px; margin: 0 auto 8px auto; display: flex; align-items: center; justify-content: center;">
                    <!-- Car Wash Icon -->
                    <svg width="32" height="32" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <ellipse cx="16" cy="20" rx="8" ry="4" fill="#8DC63F"/>
                        <rect x="10" y="8" width="12" height="8" rx="4" fill="#007A33"/>
                        <circle cx="16" cy="12" r="2" fill="#fff"/>
                    </svg>
                </div>
                <div style="font-size: 14px; color: #222; font-family: 'Inter', 'Roboto', sans-serif;">Car Wash</div>
            </div>
            <div>
                <div style="background: #F2F3F5; border-radius: 16px; width: 56px; height: 56px; margin: 0 auto 8px auto; display: flex; align-items: center; justify-content: center;">
                    <!-- Shop Offers Icon -->
                    <svg width="32" height="32" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <rect x="8" y="10" width="16" height="12" rx="4" fill="#8DC63F" stroke="#007A33" stroke-width="2"/>
                        <circle cx="16" cy="16" r="3" fill="#007A33"/>
                        <rect x="14" y="20" width="4" height="2" rx="1" fill="#007A33"/>
                    </svg>
                </div>
                <div style="font-size: 14px; color: #222; font-family: 'Inter', 'Roboto', sans-serif;">Shop Offers</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # --- Fixed Bottom Navigation Bar ---
    st.markdown("""
        <div class="bottom-nav">
            <div class="nav-item">
                <!-- Home Icon -->
                <svg width="28" height="28" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M4 12L14 4l10 8v10a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V12z" stroke="#007A33" stroke-width="2" fill="none"/>
                    <rect x="10" y="16" width="8" height="6" rx="2" fill="#8DC63F"/>
                </svg>
                Home
            </div>
            <div class="nav-item">
                <!-- Find Fuel Icon -->
                <svg width="28" height="28" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <circle cx="14" cy="14" r="10" stroke="#007A33" stroke-width="2"/>
                    <path d="M14 8v6l4 4" stroke="#8DC63F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                Find Fuel
            </div>
            <div class="nav-item">
                <!-- Rewards Icon -->
                <svg width="28" height="28" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <circle cx="14" cy="14" r="10" stroke="#007A33" stroke-width="2"/>
                    <path d="M9 17l5-6 5 6" stroke="#8DC63F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                Rewards
            </div>
            <div class="nav-item">
                <!-- Offers Icon -->
                <svg width="28" height="28" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <rect x="6" y="8" width="16" height="12" rx="4" fill="#8DC63F" stroke="#007A33" stroke-width="2"/>
                    <circle cx="14" cy="14" r="3" fill="#007A33"/>
                </svg>
                Offers
            </div>
            <div class="nav-item">
                <!-- Profile Icon -->
                <svg width="28" height="28" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <circle cx="14" cy="11" r="5" stroke="#007A33" stroke-width="2"/>
                    <rect x="7" y="18" width="14" height="6" rx="3" fill="#8DC63F"/>
                </svg>
                Profile
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- Station Finder Page ---
elif page == "Station Finder":
    st.title("Find a Station")
    city = st.text_input("Enter city name")
    stations = {
        "dublin": "123 Main St, Dublin",
        "cork": "456 River Rd, Cork",
        "galway": "789 Ocean Ave, Galway",
        "limerick": "101 City Rd, Limerick",
        "waterford": "202 Quay St, Waterford",
        "kilkenny": "303 Castle Rd, Kilkenny",
        "wexford": "404 Main St, Wexford",
        "sligo": "505 Riverbank, Sligo",
        "athlone": "606 Central Ave, Athlone",
        "letterkenny": "707 Market Sq, Letterkenny",
        "drogheda": "808 Bridge St, Drogheda",
        "navan": "909 Abbey Rd, Navan",
        "ennis": "111 Market St, Ennis",
        "tralee": "222 Oakpark, Tralee",
        "clonmel": "333 Suir Rd, Clonmel",
        "carlow": "444 Tullow St, Carlow",
        "naas": "555 Blessington Rd, Naas",
        "newbridge": "666 Main St, Newbridge",
        "portlaoise": "777 Ridge Rd, Portlaoise",
        "mullingar": "888 Green Rd, Mullingar",
        "castlebar": "999 Main St, Castlebar",
        "thurles": "121 Liberty Sq, Thurles",
        "cavan": "232 Farnham St, Cavan",
        "roscommon": "343 Abbeytown, Roscommon",
        "monaghan": "454 Broad Rd, Monaghan",
        "tullamore": "565 High St, Tullamore",
        "longford": "676 Main St, Longford",
        "ballina": "787 Ridgepool Rd, Ballina",
        "kells": "898 Headfort Rd, Kells",
        "dunboyne": "909 Main St, Dunboyne"
    }
    if st.button("Find Station"):
        address = stations.get(city.strip().lower())
        if address:
            st.success(f"Applegreen Station: {address}")
        else:
            st.error("No Applegreen station found in that city.")

# --- Fuel Calculator Page ---
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