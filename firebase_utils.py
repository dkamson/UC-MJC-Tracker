import firebase_admin
from firebase_admin import credentials, firestore, auth
import streamlit as st
import requests


def initialize_firebase():
    if not firebase_admin._apps:
        
        if "firebase_service_account" in st.secrets:

            cred=credentials.Certificate(dict(st.secrets["firebase_service_account"]))
        else:
            cred=credentials.Certificate("firebase_key.json")

        
            
        firebase_admin.initialize_app(cred)
        print("Firebase initialized successfully")
    return firestore.client()

def create_user_account(email,password):
    try:
        user=auth.create_user(email=email, password=password)
        return user.uid
    except Exception as e:
        st.error(f"Error creating account: {e}")
        return None
    
def verify_login_with_rest_api(email,password):
    api_key= st.secrets["FIREBASE_WEB_API_KEY"]
    url= f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={api_key}"

    payload={
        "email": email, 
        "password": password,
        "returnSecureToken": True
    }

    try:
        response=requests.post(url, json=payload)

        if response.status_code ==200:
            user_data=response.json()
            return user_data
        else:
            error_message= response.json().get('error', {}).get("message", "Unkown error")
            st.error(f"Login failed: {error_message}")
            return None
    except Exception as e:
        st.error(f"Error during login: {e}")
        return None
    

def save_user_progress(user_id, progress_data):
    try:
        db=firestore.client()

        doc_ref= db.collection("users").document(user_id).collection("progress").document("courses")
        doc_ref.set(progress_data)
        return True
    except Exception as e:
        st.error(f"Error saving progress: {e}")
        return False
    
def load_user_progress(user_id):
    try:
        db=firestore.client()
        doc_ref=db.collection("users").document(user_id).collection("progress").document("courses")
        doc=doc_ref.get()

        if doc.exists:
            return doc.to_dict()
        else:
            return {}
    except Exception as e:
        st.error(f"Error loading progress: {e}")
        return {}
    
def send_password_reset_email(email):
    api_key=st.secrets["FIREBASE_WEB_API_KEY"]
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key={api_key}"
    

    payload={
        "requestType": "PASSWORD_RESET",
        "email": email
    }

    try:
        response=requests.post(url, json=payload)

        if response.status_code == 200:
            return True
        
        else:
            error_message=response.json().get("error", {}).get("message",'Unknown error')
            st.error(f"Error: {error_message}")
            return False
    except Exception as e:
        st.error(f"Error sending reset email: {e}")
        return False