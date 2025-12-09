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
    if 'initialized' not in st.session_state:
        st.session_state.initialized=True
        st.session_state.current_plan='cal_getc'
        st.session_state.current_uni='ucd'
    for uni_key,uni_data in ALL_DATA.items():
        for plan_key, plan_data in uni_data['plans'].items():
            all_reqs=(
                plan_data["requirements"]["ge"]+
                plan_data["requirements"]["major_prep"]

            )
            for req in all_reqs:
                if req['type']=="single":
                    if req["id"] not in st.session_state:
                        st.session_state[req["id"]]=False
                elif req['type']=="group":
                    for option in req['options']:
                        if option["id"] not in st.session_state:
                            st.session_state[option["id"]]= False





initialize_state()


try:
    db=initialize_firebase()
    st.sidebar.success('Connected to Cloud Database')
except Exception as e:
    st.sidebar.error(f"Failed to connect: {e}")

if not check_authentication():
    st.stop()




def calculate_progress(plan_data):
    all_reqs=(
        plan_data["requirements"]["ge"]+
        plan_data["requirements"]["major_prep"]
    )

    total_count=len(all_reqs)
    completed_count=0
    

    for req in all_reqs:
        if req["type"]=="single":
            if req.get("id","").startswith("UCD_ECS_036C"):
                total_count-=1
                continue
            if st.session_state.get(req["id"], False):
                completed_count+=1

        elif req["type"]== "group":
            options_completed=0
            for option in req["options"]:
                if st.session_state.get(option["id"], False):
                    options_completed+=1
            
            if options_completed>= req["courses_needed"]:
                completed_count+=1

    if total_count>0:
        progress_percentage=completed_count/total_count
    else:
        progress_percentage=0
    return completed_count,total_count, progress_percentage







def render_requirements(req_list, header):
    with st.sidebar.expander(header,expanded=True):
        for req in req_list:
            if req["type"]== "single":
                if req.get("id","").startswith("UCD_ECS_036C"):
                    st.checkbox(req["label"], value=False,disabled=True)
                else:
                    st.checkbox(req["label"], key=req["id"])
            elif req["type"]== "group":
                st.markdown(f"**{req["label"]}**")

                for option in req["options"]:
                    st.checkbox(option["label"],key=option["id"])

                







st.title('UC-MJC Transfer Tracker')
st.info("A tool to track your CS transfer progress from MJC to any UC. Check off completed courses in the sidebar! ")

current_uni_key=st.session_state.current_uni
current_uni_data=ALL_DATA[current_uni_key]

current_plan_key=st.session_state.current_plan
if current_plan_key not in current_uni_data["plans"]:
    current_plan_key=list(current_uni_data["plans"].keys())[0]
    st.session_state.current_plan=current_plan_key

current_plan_data=current_uni_data["plans"][current_plan_key]



completed,total,percentage=calculate_progress(current_plan_data)


st.divider()
st.header("Your Transfer Progress")


st.progress(percentage, text=f"{percentage*100:.0f}% complete")
st.metric(
    label="Requirements Met",
    value=f"{completed}/{total}"
)

st.write(f""" You have met **{completed}** of the **{total}** trackable lower-division requirements for the **{current_uni_data["name"]}**  Computer Science (B.S) major.
         """)





st.success(f"You are currently viewing: {current_uni_data["name"]} ")
st.info(f"You are on the {current_plan_data["name"]} plan")
#Sidebar UI
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



render_requirements(req_list=current_plan_data["requirements"]["major_prep"],
                     header=f"**{current_plan_data["name"]} CS Major Prep**"
                     )

render_requirements(req_list=current_plan_data["requirements"]["ge"], 
                    header="General Education"

)


st.sidebar.divider()

if st.sidebar.button("💾Save Progress", type="primary"):
    with st.spinner("Saving..."):
        save_progress_to_cloud()
        st.success("Progress saved!")

st.sidebar.divider()
st.sidebar.markdown('Built by a fellow MJC student')