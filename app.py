import streamlit as st
from course_data import COURSE_REQUIREMENTS, get_all_courses, get_total_course_count
st.set_page_config(
    page_title="UC-MJC TRansfer Tracker",
    page_icon="🎓",
    layout="wide"
)
def initialize_state():
    if 'initialized' not in st.session_state:
        st.session_state.initialized=True
        for course in get_all_courses():
            st.session_state[course['id']]= False
initialize_state()


def calculate_progress():
    completed_count=0
    for course in get_all_courses():
        if course["id"] != "UCD_ECS_036C":
            if st.session_state[course["id"]]:
                completed_count+=1
    total_count=get_total_course_count()
    if total_count>0:
        progress_percentage=completed_count/total_count
    else:
        progress_percentage=0

    return completed_count, total_count, progress_percentage








st.title('UC-MJC Transfer Tracker')
st.info("A tool to track your CS transfer progress from MJC to UC Davis. Check off completed courses in the sidebar! ")


completed,total,percentage= calculate_progress()

st.divider()
st.header("Your Transfer Progress")

st.progress(percentage, text=f"{percentage*100:.0f}% Complete")
st.metric(
    label="Courses Completed",
    value=f"{completed}/{total}"
)
st.write(f"""You have completed **{completed}** of the **{total}** trackable lower-division requirements for the UC Davis Computer Science (B.S) major. 
     """    
    )
st.success("Great Job! Keep making progress")


#Sidebar UI

st.sidebar.header("My Completed Courses")
st.sidebar.write('Check the boxes for the courses you have completed')
with st.sidebar.expander("**UC Davis CS Major Prep**",expanded=True ):
    for course in COURSE_REQUIREMENTS["uc_davis_cs_prep"]:
        if course["id"]=="UCD_ECS_036C":
            st.checkbox(course['label'], value=False, disabled=True)
        else:
            st.checkbox(course["label"],key=course["id"])

with st.sidebar.expander("**Cal-GETC General Ed**", expanded=True):
    for course in COURSE_REQUIREMENTS["cal_getc"]:
        st.checkbox(course["label"], key =course["id"])

st.sidebar.divider()
st.sidebar.markdown("Built by a fellow MJC student")
