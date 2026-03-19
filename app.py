import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="Elite Auto Purchase", page_icon="🏎️")

# Custom CSS for a clean, professional look
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    .stButton>button { 
        width: 100%; 
        background-color: #1e3a8a; 
        color: white; 
        border-radius: 8px; 
        height: 3em; 
        font-weight: bold;
    }
    .stCheckbox { margin-bottom: -10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("ELITE AUTO PURCHASE")
st.subheader("Premium Vehicle Negotiation & Concierge")

# 2. Service Selection
service_type = st.radio(
    "How can we serve you today?",
    ["I want to negotiate a deal", "Request a 10-min Strategy Call"],
    horizontal=True
)

st.divider()

# 3. Form Logic
with st.form("elite_request_form", clear_on_submit=True):
    
    # Section A: Personal Details (Always visible)
    st.markdown("### **1. Contact Information**")
    col_n, col_p = st.columns(2)
    with col_n:
        name = st.text_input("Full Name *")
    with col_p:
        phone = st.text_input("Phone Number *")
    email = st.text_input("Email Address *")

    if service_type == "I want to negotiate a deal":
        # Section B: Vehicle Details
        st.markdown("### **2. Vehicle Specifications**")
        col1, col2 = st.columns(2)
        with col1:
            condition = st.selectbox("Condition", ["New", "Pre-Owned", "Certified Pre-Owned"])
            make = st.text_input("Make", placeholder="e.g. Jeep")
        with col2:
            model = st.text_input("Model", placeholder="e.g. Gladiator Mojave")
            target_price = st.number_input("Target Out-the-Door Price ($)", step=500)

        st.markdown("### **3. Preferences & Logistics**")
        warranties = st.multiselect("Warranty Options", ["Powertrain", "Bumper-to-Bumper", "Gap Insurance", "None"])
        
        # Checkbox for Delivery
        st.write("Delivery Preference:")
        delivery_home = st.checkbox("Deliver to my house (VIP Service)")
        delivery_dealer = st.checkbox("I prefer to sign at the dealership")
        
        notes = st.text_area("Additional Notes (Color, Trim, or Trade-in Info)")

    else:
        # Section C: Consultation Details
        st.markdown("### **2. Strategy Call Goals**")
        st.write("Unsure about your next move? Let's talk strategy.")
        goals = st.multiselect("What should we focus on?", ["Lease vs Buy", "Credit Coaching", "Budgeting", "Market Trends"])
        best_time = st.selectbox("Best time to call you?", ["Morning", "Afternoon", "Evening"])
        notes = st.text_area("Tell us a bit about your current situation")

    # 4. Submission
    submitted = st.form_submit_button("SUBMIT TO ELITE AUTO")

    if submitted:
        if name and (phone or email):
            # Success Message
            st.success(f"Perfect, {name}! Your request has been logged. The Elite Auto team will reach out shortly.")
            
            # This is where the Google Sheets connection triggers
            # conn = st.connection("gsheets", type=GSheetsConnection)
            # (Requires the secrets setup mentioned in previous step)
        else:
            st.error("Please fill out the required name and contact fields.")

st.caption("© 2026 Elite Auto Purchase | All negotiations are handled with dealership-standard documentation.")
