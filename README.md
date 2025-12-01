# UC-MJC Transfer Tracker 🚀

## 🚀 [LIVE APP LINK](https://uc-mjc-tracker.streamlit.app/) 🚀

A Streamlit web app to help Modesto Junior College (MJC) students track their course progress toward transferring to **any UC** as a Computer Science major.

This project was born from my own experience as a CS student at MJC, navigating the complex and fragmented data of the California transfer system.

---

## V3 Features (The "Smart" Refactor)

This app has been completely refactored from V2 to V3 to be a "smart," scalable application.

- **Full Multi-School Support:** Tracks all 9 UC campuses (Davis, Berkeley, LA, Irvine, San Diego, Santa Barbara, Santa Cruz, Riverside, Merced).  
- **"Smart" V3 Database:** `course_data.py` is now a "smart" dictionary that understands complex requirements, including `type: 'single'` and `type: 'group'` (e.g., "Choose 2 from this list").  
- **"Smart" V3 Engine:** The `app.py` engine is fully refactored to read the smart database, build a dynamic UI with grouped/indented checkboxes, and "smartly" calculate progress for group requirements.  
- **Dual Plan Support:** A toggle for both IGETC (pre-2025) and Cal-GETC (post-2025) plans.  
- **Persistent Session State:** Uses `st.session_state` to save your checked courses in your browser session.  
- **Verified Data Model:** The course database is manually researched and verified using all 9 UC articulation agreements from ASSIST.org.  

---

## How to Run Locally

1. Clone this repository:

    ```bash
    git clone https://github.com/dkamson/UC-MJC-Tracker.git
    cd UC-MJC-Tracker
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On Mac/Linux
    source venv/bin/activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the app:

    ```bash
    streamlit run app.py
    ```
