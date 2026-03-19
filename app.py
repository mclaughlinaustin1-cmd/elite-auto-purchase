import streamlit as st
from datetime import datetime

# 1. Setup & Custom "Black Label" Styling
st.set_page_config(page_title="Elite Auto Purchase", page_icon="🏎️", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    .main-header { color: #1e3a8a; font-size: 44px; font-weight: 800; text-align: center; margin-bottom: 0px; }
    .status-bar { background-color: #f1f5f9; padding: 20px; border-radius: 15px; border-left: 5px solid #3b82f6; }
    .testimonial-card { background-color: #f8fafc; padding: 20px; border-radius: 12px; border: 1px inset #e2e8f0; font-style: italic; }
    .market-badge { background-color: #dcfce7; color: #166534; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 2. Sidebar Navigation (The Hub)
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?auto=format&fit=crop&q=80&w=400", caption="Elite Concierge")
    menu = st.radio("PLATFORM MENU", ["New Request", "Track My Deal", "Success Stories"])
    st.divider()
    st.markdown("### **Elite Support**")
    st.caption("Direct Line: (941) XXX-XXXX")
    st.caption("Location: Sarasota, FL")

# --- PAGE 1: NEW REQUEST (The Intake & Calculator) ---
if menu == "New Request":
    st.markdown('<p class="main-header">ELITE AUTO PURCHASE</p>', unsafe_allow_html=True)
    st.markdown(f'<div style="text-align:center;"><span class="market-badge">● LIVE MARKET UPDATED: {datetime.now().strftime("%B %d, 2026")}</span></div>', unsafe_allow_html=True)
    
    st.divider()
    
    # Hero/Psychology Section
    col_img, col_txt = st.columns([1, 1])
    with col_img:
        st.image("https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?auto=format&fit=crop&q=80&w=800", caption="We find the car. You take the keys.")
    with col_txt:
        st.markdown("## **White-Glove Car Buying**")
        st.write("For a flat **$500 fee**, we handle the stress. No dealership showrooms, no 'Finance Office' pressure, no hidden fees.")
        st.markdown("- **Personalized Sourcing**\n- **Aggressive Negotiation**\n- **Paperwork Audit**\n- **Doorstep Delivery**")

    # Calculator (Live)
    st.markdown("### 📊 Live Payment Estimator")
    c1, c2, c3, c4 = st.columns(4)
    with c1: price = st.number_input("Target Price", 25000, 200000, 45000)
    with c2: down = st.number_input("Down Payment", 0, 50000, 5000)
    with c3: apr = st.number_input("Interest %", 0.0, 15.0, 6.5)
    with c4: term = st.selectbox("Term", [36, 48, 60, 72, 84], index=2)
    
    loan = price - down
    m_apr = (apr/100)/12
    if loan > 0:
        pmt = loan * (m_apr * (1+m_apr)**term) / ((1+m_apr)**term - 1) if apr > 0 else loan/term
        st.metric("Estimated Monthly Payment", f"${pmt:,.2f}")

    # Intake Form
    st.markdown("### 📝 Secure Intake Form")
    with st.form("request"):
        name = st.text_input("Full Name")
        contact = st.text_input("Phone or Email")
        vehicle = st.text_input("What vehicle are we hunting for?")
        notes = st.text_area("Specific goals (e.g., 'Looking for a Gladiator with the Mojave trim under $50k')")
        if st.form_submit_button("LOCK IN MY DEAL"):
            st.balloons()
            st.success("Welcome to Elite Auto. We'll be in touch within 2 hours.")

# --- PAGE 2: TRACK MY DEAL (The Ticket System) ---
elif menu == "Track My Deal":
    st.title("🛰️ Live Deal Tracker")
    deal_id = st.text_input("Enter your 6-digit Deal ID", placeholder="e.g. EA-9921")
    
    if deal_id:
        st.markdown(f"### **Status for Deal: {deal_id}**")
        
        # This is a Mock-up of your ticket system
        status_steps = ["Intake", "Sourcing", "Negotiating", "Contract Review", "Delivery Ready"]
        current_step = 2 # You would update this in your database
        
        st.success(f"Current Phase: **{status_steps[current_step]}**")
        st.progress((current_step + 1) / len(status_steps))
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Latest Updates:**
            - **10:15 AM:** Located 3 matches in the Southeast region.
            - **09:00 AM:** Dealership 'A' rejected initial offer; counter-offering now.
            - **Yesterday:** Lead verified and fee processed.
            """)
        with col2:
            st.info("💡 **Concierge Note:** Dealership B has a model with the upgraded sound system you wanted. I am pushing for an extra $1,000 off the MSRP to offset the cost.")

# --- PAGE 3: SUCCESS STORIES (Social Proof) ---
elif menu == "Success Stories":
    st.title("💎 Elite Experiences")
    st.write("Real clients. Real savings. Zero stress.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.image("https://images.unsplash.com/photo-1542362567-b05500269774?auto=format&fit=crop&q=80&w=400")
        st.markdown('<div class="testimonial-card">"I told Elite I wanted a Jeep Gladiator for $45k OTD. Two days later, they had one delivered to my driveway in Sarasota. I never even had to talk to a salesman." <br><strong>— Michael R.</strong></div>', unsafe_allow_html=True)
    
    with col_b:
        st.image("https://images.unsplash.com/photo-1553440569-bcc63803a83d?auto=format&fit=crop&q=80&w=400")
        st.markdown('<div class="testimonial-card">"As a busy professional, I don\'t have 6 hours to waste at a dealership. Elite Auto Purchase handled the entire trade-in and new lease. Pure class." <br><strong>— Sarah L.</strong></div>', unsafe_allow_html=True)

st.divider()
st.caption("© 2026 Elite Auto Purchase | Sarasota, FL | High-Performance Automotive Concierge")
