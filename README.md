# UC-MJC Transfer Tracker 🎓

**🚀 [LIVE APP](https://uc-mjc-tracker.streamlit.app) 🚀**

## Demo Video

[![Watch Demo](https://cdn.loom.com/sessions/thumbnails/dcd17bb9ec864f01bb3da41e789caf8c-with-play.gif)](https://www.loom.com/share/dcd17bb9ec864f01bb3da41e789caf8c)

*Click to watch a demo of the app in action*



A full-stack web application to help Modesto Junior College (MJC) students track their Computer Science transfer requirements to any UC campus.

Built by a fellow MJC transfer student to solve the problem of fragmented transfer data across ASSIST.org, UC websites, and college catalogs.

---

## ✨ Features

### Core Functionality
- 📊 **Track all 9 UC campuses**: Davis, Berkeley, LA, Irvine, San Diego, Santa Barbara, Santa Cruz, Riverside, Merced
- ✅ **60+ requirements tracked**: Major Prep + General Education courses
- 🎯 **Real-time progress**: Progress bar and completion metrics update instantly
- 🔄 **Dual plan support**: Toggle between IGETC (pre-2025) and Cal-GETC (post-2025)
- 🧠 **Smart requirements**: Handles complex group logic ("Choose 2 of 3")

### Cloud & Authentication
- 🔐 **Secure login**: Firebase Authentication with email/password
- ☁️ **Cloud sync**: Your progress saves automatically to Firestore
- 📱 **Multi-device**: Access your progress from any device
- 🔑 **Password reset**: Email-based password recovery
- 🔒 **Data privacy**: Firestore security rules ensure users only access their own data

### User Experience
- ⚡ **Instant updates**: Progress recalculates immediately on every click
- 💾 **Manual save**: Sync your progress to the cloud with one button
- 🏫 **University switching**: Switch between UCs without losing progress
- 📋 **Plan switching**: Toggle IGETC ↔ Cal-GETC seamlessly

---

## 🏗️ Tech Stack

**Frontend**: Python + Streamlit  
**Backend**: Firebase (Authentication + Firestore)  
**Deployment**: Streamlit Community Cloud  
**Data**: Manually verified against ASSIST.org articulation agreements

---

## 🚀 Try It Live

👉 **[https://uc-mjc-tracker.streamlit.app](https://uc-mjc-tracker.streamlit.app)**

1. Create an account
2. Select your target UC campus
3. Choose your transfer plan (IGETC or Cal-GETC)
4. Check off completed courses
5. Click "💾 Save Progress" to sync to cloud
6. Track your progress toward transfer!

---

## 💻 Run Locally

### Prerequisites
- Python 3.8+
- Firebase account

### Setup

1. **Clone the repository:**
```bash
   git clone https://github.com/dkamson/UC-MJC-Tracker.git
   cd UC-MJC-Tracker
```

2. **Create virtual environment:**
```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Mac/Linux
   source venv/bin/activate
```

3. **Install dependencies:**
```bash
   pip install -r requirements.txt
```

4. **Set up Firebase:**
   - Create project at [Firebase Console](https://console.firebase.google.com)
   - Enable Authentication (Email/Password)
   - Create Firestore database
   - Download service account key as `firebase_key.json`
   - Create `.streamlit/secrets.toml`:
```toml
     FIREBASE_WEB_API_KEY = "your_web_api_key"
```

5. **Run the app:**
```bash
   streamlit run app.py
```

---

## 📁 Project Structure
```
UC-MJC-Tracker/
├── app.py                  # Main application (UI, progress calculation, state management)
├── auth.py                 # Authentication UI (login, signup, password reset)
├── firebase_utils.py       # Firebase backend (auth, Firestore operations)
├── course_data.py          # UC articulation database (all 9 campuses)
├── requirements.txt        # Python dependencies
├── firebase_key.json       # Service account key (not in repo)
└── .streamlit/
    └── secrets.toml        # API keys (not in repo)
```

---

## 🏛️ Architecture

### Safe Harbor Pattern
All user data lives in a single source of truth: `st.session_state.user_progress`

### Immediate Reactivity
Every checkbox click triggers `st.rerun()` for instant progress updates

### Metadata Persistence
Saves not just what you checked, but which university and plan you were on

### Callback-Based Auth
Uses Streamlit callbacks to prevent login state loops

---

## 🔒 Security

- **Firebase Authentication**: Industry-standard OAuth 2.0
- **Password Hashing**: Bcrypt hashing via Firebase
- **Firestore Security Rules**: Users can only read/write their own data
- **Token-Based Password Reset**: Secure email verification
- **HTTPS**: All data transmitted over secure connections

---

## 📊 Data Accuracy

All course articulation data manually verified using:
- ASSIST.org (official UC articulation agreements)
- UC campus CS major requirement pages
- MJC 2024-2025 course catalogs

**Last updated:** December 2024

---

## 🎯 Roadmap

- [ ] Email notifications for ASSIST.org updates
- [ ] Export progress as PDF
- [ ] Google Sign-In integration
- [ ] Mobile app version
- [ ] Integration with ASSIST.org API (when available)

---

## 👨‍💻 About

Built by a Modesto Junior College CS student navigating the UC transfer process.

This project evolved from a simple checklist (V1) to a full-stack cloud application (V4):
- **V1**: Static checklist (UC Davis only)
- **V2**: Multi-school support (all 9 UCs)
- **V3**: Smart requirement tracking (group requirements)
- **V4**: User authentication + cloud sync ⭐

**Not affiliated with** Modesto Junior College or the University of California system.

---

## 📄 License

MIT License - Feel free to fork and adapt!

---

## 🙏 Acknowledgments

- Course data from [ASSIST.org](https://assist.org)
- Built with [Streamlit](https://streamlit.io)
- Powered by [Firebase](https://firebase.google.com)

---

**Questions or feedback?** Open an issue on GitHub!
