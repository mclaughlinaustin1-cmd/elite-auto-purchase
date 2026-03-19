import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Elite Auto Purchase | Premium Concierge", page_icon="🏎️", layout="wide")

# 2. Enhanced Professional Styling
st.markdown("""
    <style>
    /* Main background */
    .stApp { background-color: #f8fafc; }
    
    /* Custom Header */
    .main-header {
        font-family: 'Inter', sans-serif;
        color: #1e3a8a;
        font-size: 42px;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0px;
    }
    
    /* Value Box */
    .elite-card {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        border-top: 5px solid #1e3a8a;
    }
    
    /* Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #1e3a8a 0%, #3b82f6 100%);
        color: white;
        border: none;
        padding: 15px;
        border-radius: 10px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Process Info
with st.sidebar:
    st.markdown("### **THE ELITE PROCESS**")
    st.markdown("""
    1. **Consultation:** We define your exact specs.
    2. **The Search:** We scour dealer inventories nationwide.
    3. **Negotiation:** We grind the numbers so you don't have to.
    4. **Finalization:** We review the 'We Owe' and contracts.
    5. **Delivery:** You sign and drive.
    """)
    st.divider()
    st.info("💎 **Flat $500 Service Fee**\n\nNo hidden percentages. No dealer kickbacks. We work for *you*.")

# 4. Hero Section
st.markdown('<p class="main-header">ELITE AUTO PURCHASE</p>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b; font-size: 18px;'>Professional Automotive Negotiation & Concierge</p>", unsafe_allow_html=True)

st.divider()

# 5. Interactive Calculator (Outside the form for instant updates)
st.markdown("### 📊 Live Deal Estimator")
col_calc1, col_calc2 = st.columns([2, 1])

with col_calc1:
    c1, c2, c3, c4 = st.columns(4)
    with c1: t_price = st.number_input("Target Price", value=45000, step=1000)
    with c2: d_pay = st.number_input("Down Payment", value=5000, step=500)
    with c3: i_rate = st.number_input("APR %", value=5.9, step=0.1)
    with c4: t_months = st.selectbox("Term", [36, 48, 60, 72, 84], index=2)

with col_calc2:
    # Monthly Payment Logic
    loan = t_price - d_pay
    if loan > 0 and i_rate > 0:
        m_rate = (i_rate / 100) / 12
        pmt = loan * (m_rate * (1 + m_rate)**t_months) / ((1 + m_rate)**t_months - 1)
    else:
        pmt = loan / t_months if loan > 0 else 0
    
    st.metric("Estimated Monthly", f"${pmt:,.2f}", delta="Interest & Taxes extra")

st.divider()

# 6. The Official Request Form
st.markdown("### 📝 Secure Intake Form")
with st.container():
    with st.form("elite_intake", clear_on_submit=True):
        f_col1, f_col2 = st.columns(2)
        
        with f_col1:
            st.markdown("**Client Details**")
            u_name = st.text_input("Full Name")
            u_email = st.text_input("Email")
            u_phone = st.text_input("Phone Number")
            u_service = st.segmented_control("Service Requested", ["Full Negotiation", "10-min Strategy Call"])

        with f_col2:
            st.markdown("**Vehicle Details**")
            u_make = st.text_input("Year, Make, Model")
            u_warranty = st.multiselect("Protection Interest", ["Powertrain", "Full Wrap", "GAP", "None"])
            st.write("Delivery Preference:")
            d1, d2 = st.columns(2)
            with d1: h_del = st.checkbox("Home Delivery")
            with d2: d_sig = st.checkbox("In-Dealer Signing")
            
        u_notes = st.text_area("Specific Requirements (Trim, Color, etc.)")
        
        submit_btn = st.form_submit_button("LOCK IN MY ELITE SERVICE")
        
        if submit_btn:
            if u_name and u_phone:
                st.balloons()
                st.success(f"Form Securely Submitted. Welcome to the Elite family, {u_name}.")
            else:
                st.error("Please provide at least a name and phone number.")

st.markdown("<p style='text-align: center; color: #94a3b8; margin-top: 50px;'>Elite Auto Purchase is a private concierge service. We are not a dealership.</p>", unsafe_allow_html=True)
