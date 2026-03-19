import streamlit as st
from datetime import datetime

# 1. Page Configuration
st.set_page_config(page_title="Elite Auto Purchase | Premium Concierge", page_icon="🏎️", layout="wide")

# 2. Advanced Professional Styling
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    .main-header {
        color: #1e3a8a;
        font-size: 48px;
        font-weight: 800;
        text-align: center;
        letter-spacing: -1px;
        margin-bottom: 0px;
    }
    .hero-text {
        text-align: center;
        color: #64748b;
        font-size: 20px;
        margin-bottom: 30px;
    }
    .value-prop {
        background-color: #f8fafc;
        padding: 30px;
        border-radius: 20px;
        border: 1px solid #e2e8f0;
        text-align: center;
    }
    .stButton>button {
        background: #1e3a8a;
        color: white;
        border-radius: 12px;
        height: 3.5em;
        font-weight: bold;
        border: none;
    }
    .market-badge {
        background-color: #dcfce7;
        color: #166534;
        padding: 5px 15px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: bold;
        display: inline-block;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar: Trust Signals
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1560179707-f14e90ef3623?auto=format&fit=crop&q=80&w=300", caption="Elite Headquarters")
    st.markdown("### **Why Elite?**")
    st.write("✅ **Expert Documentation:** We review every 'We Owe' and Sales Agreement.")
    st.write("✅ **Market Intelligence:** We know the dealer holdbacks and true invoice costs.")
    st.write("✅ **Time Recovery:** You spend 0 minutes at the dealership until it's time to sign.")
    st.divider()
    st.markdown("### **Current Fee: $500**")
    st.caption("Flat rate. No hidden commissions.")

# 4. Header & Live Market Status
current_date = datetime.now().strftime("%B %d, %2026")
st.markdown(f'<p class="main-header">ELITE AUTO PURCHASE</p>', unsafe_allow_html=True)
st.markdown(f'<p class="hero-text">Your Private Liaison for Luxury & Performance Vehicles</p>', unsafe_allow_html=True)

col_status1, col_status2, col_status3 = st.columns([1,2,1])
with col_status2:
    st.markdown(f'<div style="text-align:center;"><span class="market-badge">● LIVE MARKET UPDATED: {current_date}</span></div>', unsafe_allow_html=True)

st.divider()

# 5. The "Reward" Section (Psychological Hook)
col_img, col_txt = st.columns([1.2, 1])

with col_img:
    # This represents the moment of delivery
    st.image("https://images.unsplash.com/photo-1552519507-da3b142c6e3d?auto=format&fit=crop&q=80&w=800", 
             caption="The Elite Handover: Fast, simple, and exactly what you asked for.")

with col_txt:
    st.markdown("## **Skip the Grind.**")
    st.markdown("""
    Negotiating with dealerships is a full-time job. **Make it ours.** We handle the entire lifecycle of your purchase:
    * **Spec Sourcing:** Finding the exact trim and color.
    * **Price Grinding:** We fight for every dollar of the OTD price.
    * **Contract Auditing:** Ensuring no hidden 'dealer adds' or fees.
    
    **Your only job is to take the keys.**
    """)
    if st.button("GET STARTED NOW"):
        st.markdown("---") # Visual jump to form

st.divider()

# 6. Interactive Calculator
st.markdown("### 📊 Real-Time Payment Estimator")
c_1, c_2, c_3, c_4 = st.columns(4)
with c_1: t_price = st.number_input("Target Price", value=45000, step=1000)
with c_2: d_pay = st.number_input("Down Payment", value=5000, step=500)
with c_3: i_rate = st.number_input("Est. APR %", value=5.9, step=0.1)
with c_4: t_months = st.selectbox("Term", [36, 48, 60, 72, 84], index=2)

loan = t_price - d_pay
if loan > 0:
    m_rate = (i_rate / 100) / 12
    pmt = loan * (m_rate * (1 + m_rate)**t_months) / ((1 + m_rate)**t_months - 1) if i_rate > 0 else loan/t_months
    st.metric("Estimated Monthly Commitment", f"${pmt:,.2f}")

st.divider()

# 7. Secure Intake Form
st.markdown("### 📝 Secure Intake & Consultation Request")
with st.form("elite_final_form"):
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        name = st.text_input("Full Name")
        phone = st.text_input("Phone Number")
        service = st.radio("Request Type", ["Full Negotiation ($500 Fee)", "10-Min Strategy Call (Free)"])
    with col_f2:
        vehicle = st.text_input("Desired Vehicle (Year/Make/Model)")
        delivery = st.multiselect("Preferences", ["Home Delivery", "Dealership Pickup", "Trade-In Appraisal Needed"])
        notes = st.text_area("Tell us about your specific goals")

    if st.form_submit_button("SUBMIT TO CONCIERGE"):
        if name and phone:
            st.balloons()
            st.success("Your request has been prioritized. An Elite agent will contact you shortly.")
        else:
            st.error("Please provide a name and phone number to continue.")

st.markdown("<p style='text-align: center; color: #94a3b8; margin-top: 50px;'>Elite Auto Purchase | Sarasota, FL & Nationwide Delivery</p>", unsafe_allow_html=True)
