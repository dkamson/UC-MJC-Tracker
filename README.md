# UC-MJC Transfer Tracker 🚀

**🚀 [LIVE APP LINK](https://your-app-url.streamlit.app) 🚀**

A Streamlit web app to help Modesto Junior College (MJC) students track their course progress toward transferring to any UC as a Computer Science major.

This project was born from my own experience as a CS student at MJC, navigating the complex and fragmented data of the California transfer system.

---

## ✨ V4 Features (Firebase Authentication Update)

### **NEW in V4:**
- 🔐 **User Authentication**: Secure login and signup with Firebase Authentication
- ☁️ **Cloud Sync**: Your progress saves automatically to the cloud
- 🔑 **Forgot Password**: Reset your password via email if you forget it
- 👤 **Personal Accounts**: Each user has their own private progress tracker
- 📱 **Multi-Device**: Log in from any device and see your progress

### **From V3:**
- 🎓 **Full Multi-School Support**: Tracks all 9 UC campuses (Davis, Berkeley, LA, Irvine, San Diego, Santa Barbara, Santa Cruz, Riverside, Merced)
- 🧠 **"Smart" Database**: Handles complex requirements including group requirements (e.g., "Choose 2 from this list")
- 📊 **Dynamic Progress Tracking**: Real-time progress bar and completion metrics
- 🔄 **Dual Plan Support**: Toggle between IGETC (pre-2025) and Cal-GETC (post-2025) plans
- ✅ **Verified Data**: Manually researched using all 9 UC articulation agreements from ASSIST.org

---

## 🏗️ Tech Stack

- **Frontend**: Streamlit (Python web framework)
- **Backend**: Firebase (Authentication + Firestore Database)
- **Data**: Custom-built course articulation database
- **Deployment**: Streamlit Community Cloud

---

## 🚀 How to Use (Live App)

1. Visit the [live app](https://your-app-url.streamlit.app)
2. Create an account or log in
3. Select your target UC campus
4. Choose your transfer plan (IGETC or Cal-GETC)
5. Check off completed courses
6. Click "💾 Save Progress" to sync to the cloud
7. Track your progress toward transfer!

---

## 💻 How to Run Locally

### Prerequisites
- Python 3.8+
- Firebase account (for authentication)

### Setup

1. **Clone the repository:**
```bash
   git clone https://github.com/dkamson/UC-MJC-Tracker.git
   cd UC-MJC-Tracker
```

2. **Create and activate virtual environment:**
```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On Mac/Linux
   source venv/bin/activate
```

3. **Install dependencies:**
```bash
   pip install -r requirements.txt
```

4. **Set up Firebase:**
   - Create a Firebase project at https://console.firebase.google.com
   - Enable Authentication (Email/Password)
   - Create a Firestore database
   - Download your service account key as `firebase_key.json`
   - Create `.streamlit/secrets.toml` with:
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
├── app.py                  # Main Streamlit application
├── auth.py                 # Authentication UI (login/signup/forgot password)
├── firebase_utils.py       # Firebase backend functions
├── course_data.py          # UC articulation database
├── requirements.txt        # Python dependencies
├── firebase_key.json       # Firebase credentials (not in repo)
└── .streamlit/
    └── secrets.toml        # API keys (not in repo)
```

---

## 🔒 Security Features

- **Firebase Authentication**: Industry-standard OAuth security
- **Password Hashing**: Passwords are never stored in plain text
- **Firestore Security Rules**: Users can only access their own data
- **Secure Password Reset**: Token-based email verification
- **HTTPS**: All data transmitted over secure connections

---

## 🎯 Future Enhancements

- [ ] Google Sign-In integration
- [ ] Export progress as PDF
- [ ] Mobile app version
- [ ] Email notifications for course updates
- [ ] Integration with ASSIST.org API (when available)

---

## 👨‍💻 About

Built by a fellow MJC transfer student to help navigate the complex UC transfer process. All course data is manually verified using official UC articulation agreements.

**Not affiliated with** Modesto Junior College or the University of California system.

---

## 📄 License

MIT License - Feel free to use and modify!

---

## 🙏 Acknowledgments

- Course data sourced from [ASSIST.org](https://assist.org)
- Built with [Streamlit](https://streamlit.io)
- Powered by [Firebase](https://firebase.google.com)
