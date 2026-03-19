import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Elite Auto Purchase", page_icon="🏎️")

# Custom CSS for the "Elite" feel
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    .stButton>button { 
        width: 100%; 
        background-color: #1e3a8a; 
        color: white; 
        border-radius: 8px; 
        height: 3.5em; 
        font-weight: bold;
    }
    .fee-box {
        background-color: #f1f5f9;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #1e3a8a;
        margin-bottom: 25px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("ELITE AUTO PURCHASE")
st.subheader("Premium Vehicle Negotiation & Concierge")

# 2. The Elite Value Proposition
st.markdown(f"""
<div class="fee-box">
    <strong>THE ELITE PROMISE:</strong> For a flat <strong>$500 service fee</strong>, we handle 
    everything. We find the exact spec, negotiate the price, and finalize the contract. 
    <br><br>
    <em>Your only job? Sign the papers and take delivery.</em>
</div>
""", unsafe_allow_html=True)

# 3. Service Selection
service_type = st.radio(
    "How can we serve you today?",
    ["I want to negotiate a deal", "Request a 10-min Strategy Call"],
    horizontal=True
)

st.divider()

# 4. Form Logic
with st.form("elite_request_form", clear_on_submit=True):
    
    st.markdown("### **1. Contact Information**")
    col_n, col_p = st.columns(2)
    with col_n:
        name = st.text_input("Full Name *")
    with col_p:
        phone = st.text_input("Phone Number *")
    email = st.text_input("Email Address *")

    if service_type == "I want to negotiate a deal":
        st.markdown("### **2. Vehicle Specifications**")
        col1, col2 = st.columns(2)
        with col1:
            condition = st.selectbox("Condition", ["New", "Pre-Owned", "CPO"])
            make = st.text_input("Make (e.g. Jeep)")
        with col2:
            model = st.text_input("Model (e.g. Gladiator)")
            target_price = st.number_input("Target Out-the-Door Price ($)", value=35000, step=500)

        # --- PAYMENT CALCULATOR SUB-SECTION ---
        st.markdown("#### *Payment Estimator*")
        c1, c2, c3 = st.columns(3)
        with c1:
            down_payment = st.number_input("Down Payment ($)", value=2000, step=500)
        with c2:
            interest = st.slider("Interest Rate (%)", 0.0, 15.0, 6.5)
        with c3:
            term = st.selectbox("Term (Months)", [36, 48, 60, 72, 84])
        
        # Simple Interest Calculation (Monthly)
        loan_amount = target_price - down_payment
        if loan_amount > 0:
            monthly_rate = (interest / 100) / 12
            if interest > 0:
                payment = loan_amount * (monthly_rate * (1 + monthly_rate)**term) / ((1 + monthly_rate)**term - 1)
            else:
                payment = loan_amount / term
            st.metric("Estimated Monthly Payment", f"${payment:,.2f}")
        # ---------------------------------------

        st.markdown("### **3. Preferences & Logistics**")
        warranties = st.multiselect("Warranty Options", ["Powertrain", "Bumper-to-Bumper", "Gap Insurance", "None"])
        
        st.write("Delivery Preference:")
        d_col1, d_col2 = st.columns(2)
        with d_col1:
            delivery_home = st.checkbox("Home Delivery (VIP)")
        with d_col2:
            delivery_dealer = st.checkbox("Sign at Dealership")
        
        notes = st.text_area("Additional Notes")

    else:
        st.markdown("### **2. Strategy Call Goals**")
        goals = st.multiselect("Focus areas:", ["Lease vs Buy", "Credit Coaching", "Budgeting", "Market Trends"])
        best_time = st.selectbox("Best time to call?", ["Morning", "Afternoon", "Evening"])
        notes = st.text_area("Tell us a bit about your current situation")

    submitted = st.form_submit_button("SUBMIT TO ELITE AUTO")

    if submitted:
        if name and (phone or email):
            st.success(f"Success! The Elite team has been notified. We will reach out to begin your {condition} {make} search.")
        else:
            st.error("Please fill out the required name and contact fields.")

st.caption("© 2026 Elite Auto Purchase | Professional Car Negotiation Concierge")
