import streamlit as st
from datetime import datetime

# 1. Setup & Force High-Contrast Mobile Styling
st.set_page_config(page_title="Elite Auto Purchase", page_icon="🏎️", layout="wide")

st.markdown("""
    <style>
    /* Force background and text colors for mobile readability */
    .stApp {
        background-color: #f8fafc !important;
    }
    
    /* Standard Text Color Fix */
    p, span, label, .stMarkdown {
        color: #1e293b !important;
        font-family: 'Inter', sans-serif;
    }

    /* Professional Headers */
    .main-header {
        color: #1e3a8a !important;
        font-size: 32px;
        font-weight: 800;
        text-align: center;
        margin-bottom: 5px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Card System for Mobile */
    .elite-card {
        background-color: #ffffff !important;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        border: 1px solid #e2e8f0;
    }

    /* Buttons */
    .stButton>button {
        width: 100%;
        background: #1e3a8a !important;
        color: #ffffff !important;
        border-radius: 10px;
        height: 3.5em;
        font-weight: 700;
        border: none;
        text-transform: uppercase;
    }

    /* Sidebar Fix */
    section[data-testid="stSidebar"] {
        background-color: #1e3a8a !important;
    }
    section[data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Sidebar Navigation
with st.sidebar:
    st.markdown("## ELITE MENU")
    menu = st.radio("Navigate", ["New Request", "Track My Deal", "Success Stories"])
    st.divider()
    st.markdown("### **Elite Support**")
    st.write("📍 Sarasota, FL")
    st.write("📞 (941) XXX-XXXX")

# --- PAGE 1: NEW REQUEST ---
if menu == "New Request":
    st.markdown('<p class="main-header">ELITE AUTO PURCHASE</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="text-align:center; color:#64748b !important;">Market Status: Active | {datetime.now().strftime("%B %d, 2026")}</p>', unsafe_allow_html=True)

    # Hero Card
    st.markdown("""
    <div class="elite-card">
        <h3 style="color:#1e3a8a !important; margin-top:0;">The $500 Concierge</h3>
        <p>We handle the dealerships. We find the spec. We negotiate the contract. 
        <b>Your only job is to sign and drive.</b></p>
    </div>
    """, unsafe_allow_html=True)

    # Payment Estimator (Card 1)
    st.markdown("### 📊 Payment Estimator")
    with st.container():
        st.markdown('<div class="elite-card">', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1: 
            t_price = st.number_input("Target Price ($)", 10000, 200000, 45000)
            d_pay = st.number_input("Down Payment ($)", 0, 50000, 5000)
        with c2:
            i_rate = st.number_input("APR (%)", 0.0, 15.0, 6.5)
            t_months = st.selectbox("Term (Months)", [36, 48, 60, 72, 84], index=2)
        
        # Calculation Logic
        loan = t_price - d_pay
        if loan > 0:
            m_rate = (i_rate/100)/12
            pmt = loan * (m_rate * (1+m_rate)**t_months) / ((1+m_rate)**t_months - 1) if i_rate > 0 else loan/t_months
            st.metric("Estimated Monthly Payment", f"${pmt:,.2f}")
        st.markdown('</div>', unsafe_allow_html=True)

    # Intake Form (Card 2)
    st.markdown("### 📝 Start Your Search")
    with st.form("request_form"):
        st.markdown('<div style="background-color:white; padding:10px; border-radius:10px;">', unsafe_allow_html=True)
        name = st.text_input("Full Name")
        phone = st.text_input("Phone Number")
        vehicle = st.text_input("Desired Vehicle (Year/Make/Model)")
        service = st.radio("Service Level", ["Full Negotiation ($500)", "Strategy Call (Free)"])
        notes = st.text_area("Additional Requirements")
        st.markdown('</div>', unsafe_allow_html=True)
        
        if st.form_submit_button("SUBMIT TO CONCIERGE"):
            if name and phone:
                st.balloons()
                st.success("Elite Intake Complete. We will contact you shortly.")
            else:
                st.error("Please provide your name and phone number.")

# --- PAGE 2: TRACK MY DEAL ---
elif menu == "Track My Deal":
    st.markdown('<p class="main-header">DEAL TRACKER</p>', unsafe_allow_html=True)
    st.markdown('<div class="elite-card">', unsafe_allow_html=True)
    deal_id = st.text_input("Enter 6-Digit Deal ID", placeholder="EA-XXXX")
    if deal_id:
        st.info("Current Phase: **Negotiating with Dealership**")
        st.progress(60)
        st.write("**Recent Activity:**")
        st.write("- Found matching spec in Tampa, FL")
        st.write("- Initial offer sent to Fleet Manager")
    else:
        st.write("Enter your ID to see your live progress.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE 3: SUCCESS STORIES ---
elif menu == "Success Stories":
    st.markdown('<p class="main-header">CLIENT RESULTS</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="elite-card">
        <p>"Saved $4,200 off MSRP on my new Gladiator. Elite handled everything."<br><b>— Jordan K., Sarasota</b></p>
    </div>
    <div class="elite-card">
        <p>"The home delivery was flawless. Best $500 I've ever spent."<br><b>— Amanda L., Venice</b></p>
    </div>
    """, unsafe_allow_html=True)

st.divider()
st.caption("© 2026 Elite Auto Purchase | Sarasota, FL")
