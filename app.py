# app.py
import streamlit as st
from datetime import datetime
import pytz
import time

# List of time zones
time_zones = pytz.all_timezones

# Dropdown menu for selecting locations
selected_locations = st.multiselect('Select up to 4 locations', time_zones, default=["UTC"])
selected_locations = selected_locations[:4]  # Limiting to 4 locations

# Function to get current time for a timezone
def get_time(zone):
    tz = pytz.timezone(zone)
    return datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

# Creating a row of columns for the selected locations
cols = st.columns(len(selected_locations))

# Creating placeholders for each column
time_display = [cols[i].empty() for i in range(len(selected_locations))]

# Update time every second
while True:
    for i, location in enumerate(selected_locations):
        time_display[i].markdown(f"Time in **{location}**: `{get_time(location)}`")
    time.sleep(1)
