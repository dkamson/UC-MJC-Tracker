# UC-MJC Transfer Tracker 🚀

A Streamlit web app to help Modesto Junior College (MJC) students track their course progress toward transferring to a UC as a Computer Science major.

This project was born from my own experience as an 18-year-old immigrant and CS student at MJC, navigating the complex and fragmented data of the California transfer system.

## The Problem
The requirements for transferring are spread across multiple, disconnected sources:
1.  The official UC major requirement pages (e.g., UC Davis).
2.  The MJC general education catalogs (which are in flux from IGETC to Cal-GETC).
3.  The ASSIST.org articulation database.

This tool solves this problem by curating and verifying this data into a single, simple, and interactive dashboard.

## V1 MVP Features
* **Progress Tracking:** A main dashboard with a progress bar and summary metric (`X / Y courses completed`).
* **Persistent State:** Uses `st.session_state` to save your checked courses in your browser session.
* **Verified Data Model:** The course database (`course_data.py`) is manually verified using the 2024-2025 MJC IGETC pattern and the official UC Davis CS major-prep articulation agreements.
* **Clean UI:** All courses are organized into expandable sections in a clean sidebar.

## How to Run Locally
1.  Clone this repository:
    ```bash
    git clone https://github.com/dkamson/UC-MJC-Tracker/tree/main
    cd uc-mjc-tracker
    ```
2.  Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4.  Run the app:
    ```bash
    streamlit run app.py
    ```