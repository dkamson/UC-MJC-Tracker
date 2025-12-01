# UC–MJC Transfer Tracker (Computer Science)
**Live App:** https://uc-mjc-tracker.streamlit.app/
A Streamlit web application that helps **Modesto Junior College (MJC)** students track their progress toward transferring to **any University of California (UC)** campus as a Computer Science major.

This project was inspired by my own experience navigating the fragmented and inconsistent structure of the California transfer system. The goal is simple: make transfer preparation **clear, accurate, and stress-free**.

---

## 🚀 Version 3 — The “Smart” Refactor

Version 3 is a complete architectural overhaul focused on scalability, accuracy, and handling complex UC major preparation requirements.

### ✨ New in V3

- **Full Multi-Campus Support**  
  Tracks articulated requirements for all **9 UC campuses**:  
  *UC Davis, UC Berkeley, UCLA, UC Irvine, UC San Diego, UC Santa Barbara, UC Santa Cruz, UC Riverside, UC Merced.*

- **Smart V3 Data Engine (`course_data.py`)**  
  A fully structured, extensible dictionary that supports:  
  - `type: "single"` requirements  
  - `type: "group"` requirements (e.g., “Choose 2 from this list”)  
  - Nested groups and “logical” group combinations for complex ASSIST agreements  

- **Dynamic UI Rendering**  
  The new `app.py` parses the smart database to automatically generate:  
  - Hierarchical checkboxes  
  - Grouped requirement sections  
  - Real-time progress calculations  

- **Dual Plan Support**  
  Toggle between **IGETC (pre-2025)** and **Cal-GETC (2025+)**.

- **Session Persistence**  
  Uses `st.session_state` so your course selections remain saved for the entire session.

- **Verified Data Model**  
  All courses and requirements are manually researched using the official articulation data from **ASSIST.org** for every UC campus.

---

## 🛠️ Tech Stack

- **Python 3**  
- **Streamlit**  
- **Custom structured data engine** (Python dictionaries)  
- **ASSIST.org articulation agreements**

---

## 📦 Running the App Locally

1. **Clone the repository**
    ```bash
    git clone https://github.com/YOUR_USERNAME/uc-mjc-tracker.git
    cd uc-mjc-tracker
    ```

2. **Create and activate a virtual environment**
    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the app**
    ```bash
    streamlit run app.py
    ```

---

## 🗺️ Roadmap (Upcoming Features)

- Add UCSC BA/BS split logic  
- Add CSU transfer support  
- Visual progress bars & completion meters  
- Export progress to PDF  
- User accounts (optional future addition)  

---

## 📌 Status

V3 is fully functional with complete UC coverage.  
Additional polish and features are planned for V4+.

