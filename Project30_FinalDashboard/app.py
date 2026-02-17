import streamlit as st
import psutil
import pandas as pd
import time
from datetime import datetime

# Page Configuration
st.set_page_config(page_title="Sentinel Executive Dashboard", page_icon="🚀", layout="wide")

# Sidebar Navigation
st.sidebar.title("🛠️ Sentinel Control")
menu = st.sidebar.radio("Navigation", ["Overview", "System Metrics", "Business Analytics"])

st.sidebar.markdown("---")
st.sidebar.write(f"**User:** Alex Teye Ametepey")
st.sidebar.write(f"**Role:** IT Specialist / TA")

# --- MENU: OVERVIEW ---
if menu == "Overview":
    st.title("🚀 30-Day Python Challenge: Final Showcase")
    st.write("Welcome to the final project. This dashboard represents the culmination of 30 specialized Python projects.")
    
    st.balloons()
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Projects Completed", "30 / 30", "100%")
    col2.metric("Coding Streak", "30 Days", "🔥")
    col3.metric("Status", "Portfolio Ready", "✅")

# --- MENU: SYSTEM METRICS ---
elif menu == "System Metrics":
    st.title("🖥️ Real-Time Resource Monitor")
    st.write("Monitoring local server performance...")

    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    col1, col2, col3 = st.columns(3)
    col1.progress(cpu / 100)
    col1.write(f"**CPU Usage:** {cpu}%")
    
    col2.progress(ram / 100)
    col2.write(f"**RAM Usage:** {ram}%")
    
    col3.progress(disk / 100)
    col3.write(f"**Disk Usage:** {disk}%")

# --- MENU: BUSINESS ANALYTICS ---
elif menu == "Business Analytics":
    st.title("📈 Dominion Tech Solutions: Sales Insights")
    
    # Sample data mimicking your laptop business
    data = {
        'Laptop Model': ['MacBook Air M1', 'HP EliteBook 840', 'Dell Latitude', 'Lenovo ThinkPad'],
        'Units Sold': [12, 25, 18, 10],
        'Revenue (GHS)': [96000, 112500, 72000, 45000]
    }
    df = pd.DataFrame(data)
    
    st.table(df)
    st.bar_chart(df.set_index('Laptop Model')['Units Sold'])