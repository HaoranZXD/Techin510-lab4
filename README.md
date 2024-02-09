# Techin510-lab4
A world clock that displays time in different locations around the world using Streamlit for TECHIN510 lab4

## How to Run

Open the terminal and run the following commands:

```
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

## What's Included

- `app.py`: The main clock application

## Lessons Learned

- Gained an understanding of how Streamlit makes it easy to create and deploy data applications. Learned how to use widgets like multiselect for timezone selection and columns for layout.
- Learned about the pytz library and how to manage timezones effectively in Python. This was crucial for converting UTC time to local times across various time zones.
- Enhanced understanding of Python virtual environments for project isolation. This helps in managing dependencies efficiently and avoiding conflicts between project libraries.

## Questions

-  How can we implement real-time data updates in Streamlit applications without causing the app to hang or become unresponsive due to continuous looping?
-  How can we leverage advanced Streamlit features, such as session state or custom components, to enhance the functionality of our world clock application?
