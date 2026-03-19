import streamlit as st
from datetime import datetime

# 1. Page Configuration & Mobile Fixes
st.set_page_config(
    page_title="Elite Auto Purchase | Premium Concierge",
    page_icon="🏎️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Hard-Coded High-Contrast Styling (Fixes White-on-White Mobile Issues)
st.markdown("""
    <style>
    /* Force background and global text color */
    .stApp { background-color: #f8fafc !important; }
    
    /* Ensure all standard text is Deep Slate for readability */
    p, span, label, div, .stMarkdown {
        color: #1e293b !important;
        font-family: 'Inter', -apple-system, sans-serif;
    }

    /* Professional Header Styling */
    .main-header {
        color: #1e3a8a !important;
        font-size: 36px;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0px;
        letter-spacing: -1px;
    }

    /* Elite Card System */
    .elite-card {
        background-color: #ffffff !important;
        padding: 24px;
        border-radius: 16px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
        border: 1px solid #e2e8f0;
    }

    /* High-Contrast Buttons */
    .stButton>button {
        width: 100%;
        background: #1e3a8a !important;
        color: #ffffff !important;
        border-radius: 12px;
        height: 3.5em;
        font-weight: 700;
        border: none;
        text-transform: uppercase;
        box-shadow: 0 10px 15px -3px rgba(30, 58, 138, 0.3);
    }

    /* Market Badge */
    .market-badge {
        background-color: #dcfce7 !important;
        color: #166534 !important;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 700;
    }
    
    /* Force Sidebar Colors */
    section[data-testid="stSidebar"] {
        background-color: #1e3a8a !important;
    }
    section[data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Navigation
with st.sidebar:
    st.markdown("## 🏎️ ELITE HUB")
    menu = st.radio("SELECT VIEW", ["New Deal Request", "Track My Live Deal", "Client Success Stories"])
    st.divider()
    st.markdown("### **Concierge Support**")
    st.write("📍 Sarasota, Florida")
    st.write("📞 Direct Line Available Upon Request")
    st.caption("© 2026 Elite Auto Purchase")

# --- PAGE 1: NEW DEAL REQUEST ---
if menu == "New Deal Request":
    # Header Section
    st.markdown('<p class="main-header">ELITE AUTO PURCHASE</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="text-align:center; color:#64748b !important; font-weight:500;">Market Status: Active | {datetime.now().strftime("%B %d, 2026")}</p>', unsafe_allow_html=True)

    # 1. The "Better Than Delivrd" Value Prop
    st.markdown("""
    <div class="elite-card">
        <h3 style="color:#1e3a8a !important; margin-top:0;">The $500 Performance Guarantee</h3>
        <p style="font-size:16px;">We handle the search, the grind, and the "We Owe" paperwork. 
        <b>We find your exact spec, negotiate the price, and deliver the keys.</b></p>
        <span class="market-badge">✓ ZERO DEALER FEES</span>
        <span class="market-badge" style="margin-left:10px;">✓ CONTRACT AUDIT INCLUDED</span>
    </div>
    """, unsafe_allow_html=True)

    # 2. Live Market Intelligence
    st.markdown("### 📊 Market Intelligence")
    col_v1, col_v2 = st.columns([2, 1])
    with col_v1:
        v_name = st.text_input("What vehicle are you hunting?", placeholder="e.g. 2024 Jeep Gladiator Mojave")
    with col_v2:
        st.markdown('<br><span class="market-badge" style="background-color:#fef9c3 !important; color:#854d0e !important;">● HIGH NEGOTIATION POWER</span>', unsafe_allow_html=True)

    # 3. Payment Estimator (Interactive)
    st.markdown("### 🧮 Deal Calculator")
    with st.container():
        st.markdown('<div class="elite-card">', unsafe_allow_html=True)
        c1, c2, c3, c4 = st.columns(4)
        with c1: t_price = st.number_input("Target Price ($)", value=45000, step=1000)
        with c2: d_pay = st.number_input("Down Payment ($)", value=5000, step=500)
        with c3: i_rate = st.number_input("APR (%)", value=5.9, step=0.1)
        with c4: t_months = st.selectbox("Term (Months)", [36, 48, 60, 72, 84], index=2)
        
        loan = t_price - d_pay
        if loan > 0:
            m_rate = (i_rate/100)/12
            pmt = loan * (m_rate * (1+m_rate)**t_months) / ((1+m_rate)**t_months - 1) if i_rate > 0 else loan/t_months
            st.metric("Estimated Monthly Commitment", f"${pmt:,.2f}")
        st.markdown('</div>', unsafe_allow_html=True)

    # 4. Intake Form
    st.markdown("### 📝 Secure Intake Form")
    with st.form("elite_intake"):
        st.markdown('<div style="background-color:white; padding:5px;">', unsafe_allow_html=True)
        f1, f2 = st.columns(2)
        with f1:
            u_name = st.text_input("Full Name *")
            u_phone = st.text_input("Mobile Number *")
        with f2:
            u_email = st.text_input("Email Address *")
            u_delivery = st.multiselect("Preferences", ["Home Delivery", "Dealership Pickup", "Trade-In Appraisal"])
        
        u_notes = st.text_area("Specific Requirements (Trim, Color, Non-Negotiables)")
        st.markdown('</div>', unsafe_allow_html=True)
        
        if st.form_submit_button("LOCK IN MY ELITE SERVICE"):
            if u_name and u_phone:
                st.balloons()
                st.success("Priority Intake Received. An Elite Concierge will contact you within 2 hours.")
            else:
                st.error("Please provide your name and phone number.")

# --- PAGE 2: DEAL TRACKER ---
elif menu == "Track My Live Deal":
    st.markdown('<p class="main-header">LIVE DEAL TRACKER</p>', unsafe_allow_html=True)
    st.markdown('<div class="elite-card">', unsafe_allow_html=True)
    d_id = st.text_input("Enter your 6-Digit Deal ID", placeholder="EA-XXXX")
    if d_id:
        st.markdown(f"#### Status for {d_id}")
        st.progress(65)
        st.info("Current Phase: **Finalizing Contract Audit**")
        st.write("**Recent Updates:**")
        st.write("✅ Dealer 'A' accepted $3,500 under MSRP")
        st.write("✅ 'We Owe' documentation verified for extra key & floor mats")
        st.write("⏳ Scheduling enclosed transport to Sarasota")
    else:
        st.write("Enter your unique Deal ID to see real-time progress on your negotiation.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE 3: SUCCESS STORIES ---
elif menu == "Client Success Stories":
    st.markdown('<p class="main-header">CLIENT RESULTS</p>', unsafe_allow_html=True)
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.image("https://images.unsplash.com/photo-1552519507-da3b142c6e3d?w=500")
        st.markdown("""
        <div class="elite-card">
            <p>"I never had to set foot in a dealership. Elite found my Maverick, did the paperwork, and had it in my driveway in 48 hours."<br><b>— Michael S., Venice, FL</b></p>
        </div>
        """, unsafe_allow_html=True)
    with col_b:
        st.image("https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?w=500")
        st.markdown("""
        <div class="elite-card">
            <p>"The contract audit found $800 in hidden dealer adds I would have missed. This service pays for itself."<br><b>— Sarah D., Sarasota</b></p>
        </div>
        """, unsafe_allow_html=True)

st.divider()
st.caption("Elite Auto Purchase | Private Automotive Concierge | Sarasota, Florida")
