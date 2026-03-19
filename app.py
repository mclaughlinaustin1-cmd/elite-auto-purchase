import streamlit as st
from datetime import datetime

# 1. Page Configuration & Professional Branding
st.set_page_config(
    page_title="Elite Auto Purchase | Premium Concierge",
    page_icon="🏎️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Hard-Coded High-Contrast Styling (Mobile Visibility Fix)
st.markdown("""
    <style>
    /* Force background and global text color to prevent blending */
    .stApp { background-color: #f8fafc !important; }
    
    /* Ensure all standard text is Deep Slate/Black for readability */
    p, span, label, div, .stMarkdown, .stSelectbox, .stTextInput, .stNumberInput {
        color: #1e293b !important;
        font-family: 'Inter', -apple-system, sans-serif;
    }

    /* Professional Header Styling */
    .main-header {
        color: #1e3a8a !important;
        font-size: 38px;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0px;
        letter-spacing: -1.5px;
    }

    /* Elite Card System - Used to group information professionally */
    .elite-card {
        background-color: #ffffff !important;
        padding: 24px;
        border-radius: 16px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
        border: 1px solid #e2e8f0;
    }

    /* High-Contrast Primary Buttons */
    .stButton>button {
        width: 100%;
        background: #1e3a8a !important;
        color: #ffffff !important;
        border-radius: 12px;
        height: 3.8em;
        font-weight: 700;
        border: none;
        text-transform: uppercase;
        box-shadow: 0 10px 15px -3px rgba(30, 58, 138, 0.3);
        transition: all 0.2s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 15px 20px -5px rgba(30, 58, 138, 0.4);
    }

    /* Status Badges */
    .market-badge {
        background-color: #dcfce7 !important;
        color: #166534 !important;
        padding: 6px 14px;
        border-radius: 30px;
        font-size: 13px;
        font-weight: 700;
        display: inline-block;
    }
    
    /* Force Sidebar Colors to Elite Navy */
    section[data-testid="stSidebar"] {
        background-color: #1e3a8a !important;
    }
    section[data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Navigation Hub
with st.sidebar:
    st.markdown("## 🏎️ ELITE PORTAL")
    menu = st.radio("SERVICE MENU", ["Start New Request", "Track Live Deal", "Elite Success Stories"])
    st.divider()
    st.markdown("### **Concierge Desk**")
    st.write("📍 Headquarters: Sarasota, FL")
    st.write("📞 Direct Line: Request via Intake")
    st.caption(f"System Time: {datetime.now().strftime('%H:%M EST')}")

# --- PAGE 1: NEW DEAL REQUEST (Intake & Value Prop) ---
if menu == "Start New Request":
    st.markdown('<p class="main-header">ELITE AUTO PURCHASE</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="text-align:center; color:#64748b !important; font-weight:600; font-size:18px;">Automotive Concierge | {datetime.now().strftime("%B %d, 2026")}</p>', unsafe_allow_html=True)

    # Psychological Hook & Value Prop
    st.markdown("""
    <div class="elite-card">
        <h2 style="color:#1e3a8a !important; margin-top:0; font-size:24px;">Skip the Dealership. Save Thousands.</h2>
        <p style="font-size:16px; line-height:1.6;">For a flat <b>$500 fee</b>, we provide the ultimate advantage. 
        We hunt the inventory, grind the negotiation, audit the 'We Owe' paperwork, and coordinate delivery. 
        <b>You simply sign the contract and take the keys.</b></p>
        <div style="margin-top:15px;">
            <span class="market-badge">✓ NO HIDDEN FEES</span>
            <span class="market-badge" style="margin-left:10px;">✓ DOCUMENT AUDIT</span>
            <span class="market-badge" style="margin-left:10px;">✓ NATIONWIDE SOURCING</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Live Market Intelligence Section
    st.markdown("### 📊 Market Intelligence")
    col_v1, col_v2 = st.columns([2, 1])
    with col_v1:
        v_search = st.text_input("Which vehicle are we hunting?", placeholder="e.g. 2024 Jeep Gladiator Mojave")
    with col_v2:
        st.markdown('<br><span class="market-badge" style="background-color:#fef9c3 !important; color:#854d0e !important;">● HIGH NEGOTIATION POWER</span>', unsafe_allow_html=True)
        st.caption("High supply detected in SE Region.")

    # Payment Estimator (Instant Interactivity)
    st.markdown("### 🧮 Elite Deal Calculator")
    with st.container():
        st.markdown('<div class="elite-card">', unsafe_allow_html=True)
        c1, c2, c3, c4 = st.columns(4)
        with c1: t_price = st.number_input("Target OTD Price ($)", value=45000, step=1000)
        with c2: d_pay = st.number_input("Down Payment ($)", value=5000, step=500)
        with c3: i_rate = st.number_input("Est. APR (%)", value=5.9, step=0.1)
        with c4: t_months = st.selectbox("Term (Months)", [36, 48, 60, 72, 84], index=2)
        
        loan_amt = t_price - d_pay
        if loan_amt > 0:
            m_rate = (i_rate/100)/12
            pmt = loan_amt * (m_rate * (1+m_rate)**t_months) / ((1+m_rate)**t_months - 1) if i_rate > 0 else loan_amt/t_months
            st.metric("Estimated Monthly Commitment", f"${pmt:,.2f}")
        st.markdown('</div>', unsafe_allow_html=True)

    # Secure Form Intake
    st.markdown("### 📝 Secure Intake & Service Agreement")
    with st.form("elite_intake"):
        f1, f2 = st.columns(2)
        with f1:
            u_name = st.text_input("Legal Name *")
            u_phone = st.text_input("Mobile Number *")
        with f2:
            u_email = st.text_input("Email Address *")
            u_pref = st.multiselect("Preferences", ["Home Delivery", "Dealership Pickup", "Trade-In Appraisal"])
        
        u_goals = st.text_area("Specific Goals (Preferred Trim, Color, or Financing Limits)")
        
        if st.form_submit_button("LOCK IN MY ELITE SERVICE"):
            if u_name and u_phone:
                st.balloons()
                st.success("Your deal has been prioritized. An Elite agent will contact you within 2 hours.")
            else:
                st.error("Please provide a name and phone number to continue.")

# --- PAGE 2: TRACK LIVE DEAL (The Ticket System) ---
elif menu == "Track Live Deal":
    st.markdown('<p class="main-header">LIVE DEAL TRACKER</p>', unsafe_allow_html=True)
    st.markdown('<div class="elite-card">', unsafe_allow_html=True)
    d_id = st.text_input("Enter your 6-Digit Deal ID", placeholder="EA-XXXX")
    
    if d_id:
        st.markdown(f"#### STATUS: {d_id}")
        st.progress(65)
        st.info("Current Phase: **Phase 3 - Contract Review & Document Audit**")
        
        col_t1, col_t2 = st.columns(2)
        with col_t1:
            st.markdown("**Real-Time Activity Log:**")
            st.write("✅ Dealer 'A' counter-offer rejected by Elite.")
            st.write("✅ Dealer 'B' matching Target Price of $44,500.")
            st.write("✅ Enclosed Transport quote secured ($450).")
        with col_t2:
            st.markdown("**Concierge Documents:**")
            if st.button("📄 Generate Deal Summary PDF"):
                st.success("PDF Summary Generated. Check your email/downloads.")
                st.download_button("Download Summary", "Deal ID: EA-XXXX\nPrice: $44,500\nStatus: Pending Final Signature", file_name="Elite_Deal_Summary.txt")
    else:
        st.write("Please enter your unique Deal ID provided during your strategy call.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE 3: ELITE SUCCESS STORIES (Social Proof) ---
elif menu == "Elite Success Stories":
    st.markdown('<p class="main-header">CLIENT RESULTS</p>', unsafe_allow_html=True)
    
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        st.image("https://images.unsplash.com/photo-1552519507-da3b142c6e3d?w=600", caption="The Elite Handover")
        st.markdown("""
        <div class="elite-card">
            <p>"Elite Auto Purchase found me a Maverick XLT that three other dealerships said didn't exist. They negotiated $1,500 under MSRP and delivered it to my office."<br><b>— Michael R., Sarasota, FL</b></p>
        </div>
        """, unsafe_allow_html=True)
    with col_s2:
        st.image("https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?w=600", caption="Bypassing the Dealership Grind")
        st.markdown("""
        <div class="elite-card">
            <p>"I paid the $500 fee and saved $3,200 in hidden dealer adds. The paperwork audit alone was worth it. Truly a white-glove experience."<br><b>— Sarah G., Tampa, FL</b></p>
        </div>
        """, unsafe_allow_html=True)

st.divider()
st.caption("© 2026 Elite Auto Purchase | Private Concierge Group | Sarasota, Florida")
