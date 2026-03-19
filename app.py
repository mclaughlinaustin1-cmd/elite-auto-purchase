import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="Elite Auto Purchase", page_icon="🏎️")

# 2. Professional Header
st.title("🏎️ ELITE AUTO PURCHASE")
st.markdown("### *The Premium Vehicle Negotiation Concierge*")
st.info("Define your deal. We handle the dealerships, the paperwork, and the delivery.")

# 3. The Negotiation Form
with st.form("deal_form", clear_on_submit=True):
    st.subheader("Vehicle Specifications")
    
    col1, col2 = st.columns(2)
    with col1:
        condition = st.selectbox("Vehicle Status", ["New", "Pre-Owned", "Certified Pre-Owned"])
        make = st.text_input("Make", placeholder="e.g. Jeep, Ford, BMW")
    with col2:
        model = st.text_input("Model & Trim", placeholder="e.g. Gladiator Mojave, Maverick XLT")
        year = st.number_input("Desired Year", min_value=2015, max_value=2027, value=2025)

    st.subheader("Financials & Protection")
    target_price = st.number_input("What is your target 'Out-the-Door' price?", step=500, format="%d")
    
    warranties = st.multiselect(
        "Warranty Options (Select all that apply)",
        ["Powertrain Protection", "Bumper-to-Bumper", "Gap Insurance", "Appearance/Key Protection", "None"]
    )

    st.subheader("Logistics")
    delivery = st.radio(
        "How would you like to receive the vehicle?",
        ["Home Delivery (VIP Service)", "In-Person Dealership Signing"]
    )

    st.subheader("Your Contact Info")
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")

    # Submit Button
    submitted = st.form_submit_button("SUBMIT NEGOTIATION REQUEST")

    if submitted:
        if name and email and make:
            st.success(f"Request Received! We are starting the search for your {year} {make} {model} at ${target_price:,}.")
            # Logic for data storage goes here
        else:
            st.error("Please fill out your Name, Email, and Vehicle Make to proceed.")
