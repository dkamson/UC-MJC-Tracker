import streamlit as st
from course_data import ALL_DATA
from firebase_utils import initialize_firebase
from auth import check_authentication, logout, save_progress_to_cloud


st.set_page_config(
    page_title="UC-MJC Transfer Tracker",
    page_icon="🎓",
    layout="wide"
)


def initialize_state():
    
    if 'user_progress' not in st.session_state:
        st.session_state.user_progress = {}

    if "current_uni" not in st.session_state:
        st.session_state.current_uni = 'ucd'
        
    if "current_plan" not in st.session_state:
        st.session_state.current_plan = "cal_getc"
        
    if "initialized" not in st.session_state:
        st.session_state.initialized = True


def calculate_progress(plan_data,user_progress=None):
    all_reqs = (
        plan_data["requirements"]["ge"] +
        plan_data["requirements"]["major_prep"]
    )

    total_count = 0
    completed_count = 0
    
    if user_progress==None:
        user_progress = st.session_state.get("user_progress", {})

    for req in all_reqs:
        if req["type"] == "single":
            if  not req.get("mjc_available", True):
                continue
            total_count+=1           
            
            if user_progress.get(req["id"], False):
                completed_count += 1

        elif req["type"] == "group":
            if not req.get("mjc_available",True):
                continue

            total_count+=1
            options_completed = 0
            for option in req["options"]:
                if user_progress.get(option["id"], False):
                    options_completed += 1
            
            if options_completed >= req["courses_needed"]:
                completed_count += 1

    if total_count > 0:
        progress_percentage = completed_count / total_count
    else:
        progress_percentage = 0
    
    return completed_count, total_count, progress_percentage


def render_requirements(req_list, header):
    with st.sidebar.expander(header, expanded=True):
        for req in req_list:
            if req["type"] == "single":
                if not req.get("mjc_available", True ):

                    st.checkbox(f"⚠️ {req['label']} - NOT offered at MJC (take after transfer)" , value=False, disabled=True,)

                else:
                    req_id = req["id"]
                    current_val = st.session_state.user_progress.get(req_id, False)

                    
                    is_checked = st.checkbox(
                        req["label"],
                        value=current_val,
                        key=f"widget_{req_id}"
                    )
                    
                    if is_checked != current_val:
                        st.session_state.user_progress[req_id] = is_checked
                        st.rerun()

            elif req["type"] == "group":
                if not  req.get("mjc_available", True):
                    st.markdown(f"**{req['label']}** ")
                    for option in req["options"]:
                        st.checkbox(f"⚠️ {option['label']} - NOT offered at MJC (take after transfer)",
                                    disabled=True,
                                    value= False
                                    )

                else:
                    st.markdown(f"**{req['label']}**")
                    for option in req["options"]:
                        opt_id = option["id"]
                        current_val = st.session_state.user_progress.get(opt_id, False)

                        is_checked = st.checkbox(
                            option["label"],
                            value=current_val,
                            key=f"widget_{opt_id}"
                        )
                        
                        if is_checked != current_val:
                            st.session_state.user_progress[opt_id] = is_checked
                            st.rerun()

if __name__== "__main__":

    try:
        db = initialize_firebase()
        st.sidebar.success('Connected to Cloud Database')
    except Exception as e:
        st.sidebar.error(f"Failed to connect: {e}")


    if not check_authentication():
        st.stop()


    initialize_state()


    st.title('UC-MJC Transfer Tracker')
    st.info("A tool to track your CS transfer progress from MJC to any UC. Check off completed courses in the sidebar! ")


    current_uni_key = st.session_state.current_uni
    current_uni_data = ALL_DATA[current_uni_key]


    current_plan_key = st.session_state.current_plan
    if current_plan_key not in current_uni_data["plans"]:
        current_plan_key = list(current_uni_data["plans"].keys())[0]
        st.session_state.current_plan = current_plan_key

    current_plan_data = current_uni_data["plans"][current_plan_key]


    completed, total, percentage = calculate_progress(current_plan_data)

    st.divider()
    st.header("Your Transfer Progress")

    st.progress(percentage, text=f"{percentage*100:.0f}% complete")
    st.metric(
        label="Requirements Met",
        value=f"{completed}/{total}"
    )

    st.write(f""" You have met **{completed}** of the **{total}** trackable lower-division requirements for the **{current_uni_data["name"]}** Computer Science (B.S) major.""")

    st.success(f"You are currently viewing: {current_uni_data['name']} ")
    st.info(f"You are on the {current_plan_data['name']} plan")


    st.sidebar.header("My completed courses")
    st.sidebar.info(f"Logged in as {st.session_state.user_email}")

    if st.sidebar.button("Logout", type="secondary"):
        logout()

    st.sidebar.divider()


    st.sidebar.selectbox(
        'Select your target university:', 
        options=ALL_DATA.keys(),
        key="current_uni",
        format_func=lambda key: ALL_DATA[key]["name"]
    )


    st.sidebar.radio(
        "Select your transfer plan:",
        options=current_uni_data["plans"],
        key="current_plan",
        format_func= lambda key: current_uni_data["plans"][key]["name"]
    )
    st.sidebar.write("Select IGETC if you started before Fall 2025")
    st.sidebar.divider()

    if st.session_state.current_uni=="ucd":
        st.info("""
        📋 **UC Davis Special Requirements:**
        - Calculus series (21A, 21B, 21C) must be completed at same institution
        - ECS 191 and 193 must be taken at same university
        """)

    if st.session_state.current_uni == "ucb":
        st.warning("""
    ⚠️ **UC Berkeley Requirements:**
    
    Several required courses are NOT available at MJC:
    - CS 61A, 61C, 70 (Programming & Theory)
    - EECS 16A (Designing Information Devices)
    
    These must be completed after transfer or at another institution before transfer.
    
    **Linear Algebra + Differential Equations (MATH 54):**
    Both MATH 191 AND MATH 193 are required.
    """)
        
    if st.session_state.current_uni == "uci":
        st.warning("""
    ⚠️ **UC Irvine Requirements:**
    
    Several courses are NOT available at MJC:
    - I&C SCI 6N (Computational Linear Algebra)
    - I&C SCI 46 (Data Structures)
    - IN4MATX 43 (Software Engineering)
    - I&C SCI 53 (System Design)
    - STATS 67 (Statistics)
    
    These must be completed after transfer or at another community college.
    Check ASSIST.org for other CC articulations.
    """)
    
    if st.session_state.current_uni == "ucm":
        st.warning("""
    ⚠️ **Important: UC Merced Does Not Offer Computer Science B.S.**
    
    Merced offers "Applied Mathematical Sciences with Computer Science Emphasis" instead.
    
    **What this means:**
    - Different degree title on your diploma
    - Similar coursework but with more math focus
    - Still prepares you for software engineering careers
    
    **This tracker shows ADMISSION requirements only.**
    Additional courses (Calc 3, Linear Algebra, Discrete Math, Programming) 
    are required for graduation but NOT for admission.
    
    For complete degree requirements, visit: 
    https://assist.org (Modesto JC → UC Merced → Applied Math Sciences)
    """)

    
    if st.session_state.current_uni == "ucsd":
        st.warning("""
    ⚠️ **UCSD Major Requirements:**
    
    Several UCSD CS requirements have NO MJC equivalent:
    - CSE 11 (Intro to Programming - Accelerated)
    - CSE 20 (Discrete Mathematics)
    - CSE 21 (Mathematics for Algorithms)
    - CSE 29 (Systems Programming)
    - CSE 30 (Computer Organization)
    
    These must be completed after transfer or at another institution before transfer.
    
    **Important:** Even though MJC offers programming and discrete math courses,
    UCSD has determined they do not meet their specific requirements.
    """)
        
    
    if st.session_state.current_uni == "ucr":
        st.info("""
    ⚠️ **UC Riverside Requirements:**
    
    You must "Select 3 courses from the following" - some options are NOT available at MJC:
    - CS 11 (Discrete Structures) - NOT available at MJC
    - CS 10C (Data Structures) - NOT available at MJC
    
    Available options at MJC: CS 61, MATH 10A (Calc 3), PHYS 40B, PHYS 40C
    """)
        
    if st.session_state.current_uni == "ucsc":
        st.warning("""
    ⚠️ **UCSC Screening Requirements - CRITICAL:**
    
    **This is a SCREENING MAJOR** with specific timing requirements:
    
    1. **By Fall (before spring transfer):**
       - At least 3 of 5 required courses must be completed
       - Minimum 3.0 GPA in completed CS screening courses
    
    2. **By Spring (before fall transfer):**
       - ALL 5 required courses must be completed
       - Maintain 3.0 GPA in CS screening courses
    
    **Required Courses:**
    - CSE 12 (Assembly Language) → CSCI 273
    - CSE 16 (Discrete Math) → CSCI 204
    - CSE 30 (Python) → CSCI 272
    - MATH 19A (Calc 1+2) → MATH 171 + MATH 172
    - MATH 19B (Calc 1+2) → MATH 171 + MATH 172
    
    **Failure to meet these requirements = automatic rejection.**
    
    Visit UCSC admissions for complete screening policy.
    """)
    if st.session_state.current_uni == "ucsb":
        st.warning("""
    ⚠️ **UCSB Requirements - CRITICAL:**
    
    UCSB requires programming courses that are NOT available at MJC:
    - CMPSC 16 (Problem Solving with Computers I)
    - CMPSC 24 (Problem Solving with Computers II)
    
    These must be completed after transfer or at another institution before transfer.
    
    **Note:** This tracker shows REQUIRED courses only. UCSB also has "Strongly Recommended" 
    courses (Calc 3, additional physics, etc.) that can help your application but are not 
    required for admission.
    """)
        
    if st.session_state.current_uni == "ucla":
       st.error("""
    ⚠️ **UCLA Requirements - CRITICAL:**
    
    ALL major prep must be completed by END OF SPRING before fall transfer.
    
    Several UCLA requirements are NOT available at MJC:
    - COM SCI 31, 32, 35L (Programming series)
    - COM SCI M51A/EC ENGR M16 (Logic Design)
    - C++ programming course
    
    These courses are REQUIRED for admission but must be taken at:
    - Another community college (check ASSIST for articulations)
    - UCLA Extension
    - Summer before transfer
    
    **Without these courses, you may not be admitted to UCLA CS.**
    
    Consult with a UCLA transfer counselor for options.
    """)
    

    render_requirements(
        req_list=current_plan_data["requirements"]["major_prep"],
        header=f"**{current_plan_data['name']} CS Major Prep**"
    )

    render_requirements(
        req_list=current_plan_data["requirements"]["ge"], 
        header="General Education"
    )

    st.sidebar.divider()


    if st.sidebar.button("💾 Save Progress", type="primary"):
        with st.spinner("Saving..."):
            if save_progress_to_cloud():
                st.success("Progress saved!")
            else:
                st.error("Save failed. Please try again")
    st.sidebar.divider()
    st.sidebar.markdown('Built by a fellow MJC student')