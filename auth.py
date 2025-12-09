import streamlit as st
from firebase_utils import(
    create_user_account, 
    verify_login_with_rest_api, 
    save_user_progress,
      load_user_progress,
      send_password_reset_email
)

import json
from urllib.parse import quote


def show_login_page():
    st.title("UC-MJC Transfer Tracker")
    st.markdown("Track your Computer Science tranfer")
    
    tab1,tab2=st.tabs(["Login", "Sign up"])

    with tab1:
        st.subheader("Login to your account")

        login_email= st.text_input("Email", key="login_email")
        login_password=st.text_input("Password",type="password", key="login_password")

        if st.button(label="Login", type="primary"):
            if not login_email or not login_password:
                st.error("Please fill in both fields")
            else:
                with st.spinner("Loggin in..."):
                    user_data=verify_login_with_rest_api(login_email, login_password)

                    if user_data:
                        st.session_state.logged_in=True
                        st.session_state.user_id=user_data["localId"]
                        st.session_state.user_email=user_data["email"]

                        saved_progress=load_user_progress(user_data["localId"])

                        if saved_progress:
                            for course_id, is_completed in saved_progress.items():
                                st.session_state[course_id]= is_completed

                        
                        st.success("Login successful!")
                        st.rerun()
        with st.expander("🔑 Forgot Password?"):
            st.write("Enter your email to receive a password reset link:")
            reset_email=st.text_input("Email", key='reset_email')


            if st.button("Send Reset Link", key="reset_button"):
                if not reset_email:
                    st.error("Please enter your email adress")
                else:
                    with st.spinner("Sending reset email..."):
                        success=send_password_reset_email(reset_email)

                        if success:
                            st.success("✅  Password reset email sent! Check your inbox")
                            st.info("Click the link in your email to reset your password")


    with tab2:
        
        st.subheader("Create a new account")
        

        signup_email= st.text_input ("Email", key ="signup_email")
        signup_password=st.text_input("Password",type="password", key="signup_password" )
        signup_password_confirm=st.text_input("Confirm Password",type="password", key= "signup_password_confirm")

        
        if st.button(label="Sign Up", type="primary"):
            if not signup_email or not signup_password or not signup_password_confirm:
                st.error("Please fill in all fields")
            elif signup_password!=signup_password_confirm:
                st.error("Passwords do not match")
            elif len(signup_password) < 6:
                st.error("Password must be at least 6 characters")
            else:
                with st.spinner("Creating account..."):
                    user_id=create_user_account(signup_email, signup_password)

                    if user_id:
                        st.success("Account created! Please log in.")


def check_authentication():
    if not st.session_state.get("logged_in",False):
        show_login_page()
        return False
    return True



def logout():
    st.session_state.logged_in=False
    st.session_state.user_id= None
    st.session_state.user_email=None

    st.rerun()


def save_progress_to_cloud():
    if not st.session_state.get("logged_in"):
        return

    progress_data={}
    for key in st.session_state.keys():
        if "_" in key and key not in ["logged_in", "user_id", "user_email", "current_uni", "current_plan"]:
            progress_data[key]=st.session_state[key]

    user_id=st.session_state.get("user_id")
    if user_id and progress_data:
        save_user_progress(user_id, progress_data)
