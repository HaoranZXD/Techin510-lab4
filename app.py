import streamlit as st
import pytz
from datetime import datetime
import time
import yfinance as yf


# Function to display world clock
def world_clock_page():
    st.title('World Clock')

    # List of time zones
    time_zones = pytz.all_timezones

    # Dropdown menu for selecting locations
    selected_locations = st.multiselect('Select up to 4 locations', time_zones, default=["UTC"])
    selected_locations = selected_locations[:4]  # Limiting to 4 locations

    # Function to get current time for a timezone
    def get_time(zone):
        tz = pytz.timezone(zone)
        now = datetime.now(tz)
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_time
    
    def get_unix(zone):
        tz = pytz.timezone(zone)
        now = datetime.now(tz)
        unix_timestamp = int(now.timestamp())
        return unix_timestamp
    
    # Creating a row of columns for the selected locations
    if selected_locations:
        cols = st.columns(len(selected_locations))
    else:
        st.write("Please select at least one location.")

    # Creating placeholders for each column
    time_display = [cols[i].empty() for i in range(len(selected_locations))]

    # Update time every second
    while True:
        for i, location in enumerate(selected_locations):
            time_display[i].markdown(f"Time in <br>**{location}**: <br>`{get_time(location)}`<br>`{get_unix(location)}`<br>", unsafe_allow_html=True)
        time.sleep(1)

def unix_converter_page():
    st.title('UNIX Timestamp Converter')
    unix_input = st.number_input('Enter UNIX timestamp', min_value=0, value=int(time.time()), format='%d')

    # Convert to human-readable
    dt_object = datetime.fromtimestamp(unix_input)
    st.write('Human-readable time:', dt_object.strftime('%Y-%m-%d %H:%M:%S'))


def finance_data_page():
    st.title('Finance Data')

    # Example: Fetching Apple stock data
    ticker_symbol = st.text_input('Enter ticker symbol', value='AAPL')
    ticker_data = yf.Ticker(ticker_symbol)
    ticker_df = ticker_data.history(period='1d', start='2020-1-1')

    st.line_chart(ticker_df.Close)



# Main app structure
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ('World Clock', 'UNIX Timestamp Converter', 'Finance Data'))

    if page == 'World Clock':
        world_clock_page()
    elif page == 'UNIX Timestamp Converter':
        unix_converter_page()
    elif page == 'Finance Data':
        finance_data_page()

if __name__ == "__main__":
    main()
