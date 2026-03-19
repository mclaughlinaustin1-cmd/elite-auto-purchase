import streamlit as st
from streamlit_gsheets import GSheetsConnection

# 1. Page Configuration & Style
st.set_page_config(page_title="Elite Auto Purchase", page_icon="🏎️")

st.markdown("""
    <style>
    .stApp { background-color: #fcfcfc; }
    .stButton>button { background-color: #1e3a8a; color: white; border-radius: 10px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("ELITE AUTO PURCHASE")
st.caption("The Premium Vehicle Negotiation Concierge")

# 2. Service Selection (Toggle between Deal or Consultation)
service_type = st.radio(
    "How can we help you today?",
    ["I have a specific vehicle in mind", "I want a 5-10 min Consultation"],
    horizontal=True
)

st.divider()

# 3. The Dynamic Form
with st.form("elite_form", clear_on_submit=True):
    
    if service_type == "I have a specific vehicle in mind":
        st.subheader("Vehicle & Deal Details")
        col1, col2 = st.columns(2)
        with col1:
            condition = st.selectbox("Status", ["New", "Pre-Owned", "CPO"])
            make = st.text_input("Make (e.g. Jeep)")
        with col2:
            model = st.text_input("Model (e.g. Gladiator)")
            target = st.number_input("Target Out-the-Door Price ($)", step=500)
        
        logistics = st.select_slider("Delivery Preference", options=["Dealership Pickup", "Home Delivery"])
        notes = st.text_area("Additional Requirements (Trim, Color, Options)")

    else:
        st.subheader("Book a Strategy Call")
        st.write("Unsure of your budget or goals? Let's talk for 10 minutes to map out a plan.")
        goals = st.multiselect("What should we discuss?", 
                              ["Budgeting", "Lease vs Buy", "Trade-In Value", "Credit Concerns"])
        notes = st.text_area("Briefly describe your financial goals")

    st.subheader("Contact Information")
    c1, c2 = st.columns(2)
    with c1:
        name = st.text_input("Full Name *")
        phone = st.text_input("Phone Number *")
    with c2:
        email = st.text_input("Email Address *")
        best_time = st.selectbox("Best time to call", ["Morning", "Afternoon", "Evening"])

    submitted = st.form_submit_button("SUBMIT TO ELITE AUTO")

    if submitted:
        if name and (phone or email):
            st.success(f"Thank you, {name}. Your request has been sent to the Elite team.")
            # Data would be sent to Google Sheets here
        else:
            st.error("Please provide a name and contact method.")
