import sqlite3
from datetime import datetime, timedelta
import random

DB_NAME = "tracker.db"
TABLE_NAME = "fuel_logs"
INPUT_FILE = "input.txt"

def mock_weather():
    return random.choice(["Sunny", "Cloudy", "Rainy", "Windy", "Foggy"])

def setup_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            liters REAL,
            price_per_liter REAL,
            total_cost REAL,
            station TEXT,
            weather_info TEXT
        )
    """)
    conn.commit()
    conn.close()

def process_input():
    entries = []
    with open(INPUT_FILE, "r") as f:
        for line in f:
            parts = [p.strip() for p in line.strip().split(",")]
            if len(parts) != 4:
                continue
            date, liters, price_per_liter, station = parts
            try:
                liters = float(liters)
                price_per_liter = float(price_per_liter)
                total_cost = round(liters * price_per_liter, 2)
                weather = mock_weather()
                entries.append((date, liters, price_per_liter, total_cost, station, weather))
            except ValueError:
                continue
    return entries

def insert_entries(entries):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.executemany(f"""
        INSERT INTO {TABLE_NAME} (date, liters, price_per_liter, total_cost, station, weather_info)
        VALUES (?, ?, ?, ?, ?, ?)
    """, entries)
    conn.commit()
    conn.close()

def print_last_4_weeks():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    four_weeks_ago = (datetime.now() - timedelta(weeks=4)).strftime("%Y-%m-%d")
    c.execute(f"""
        SELECT date, liters, price_per_liter, total_cost, station, weather_info
        FROM {TABLE_NAME}
        WHERE date >= ?
        ORDER BY date DESC
    """, (four_weeks_ago,))
    rows = c.fetchall()
    print("Last 4 Weeks of Fuel Logs:")
    print("-" * 60)
    for row in rows:
        print(f"Date: {row[0]}, Liters: {row[1]}, Price/L: €{row[2]}, Total: €{row[3]}, Station: {row[4]}, Weather: {row[5]}")
    print("-" * 60)
    print(f"Total records: {len(rows)}")
    conn.close()

if __name__ == "__main__":
    setup_db()
    entries = process_input()
    insert_entries(entries)