import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# 1. PAGE CONFIGURATION & MODERN STYLING INJECTION
st.set_page_config(
    page_title="Yaser Alhusaini | Policy & Data Operations Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed" # Hides the default sidebar layout
)

# Premium Global CSS Injection for Animations and Clean Layouts
st.markdown("""
    <style>
        /* Fade-in animation for pages */
        .fade-in {
            animation: fadeIn ease 0.8s;
            -webkit-animation: fadeIn ease 0.8s;
        }
        @keyframes fadeIn {
            0% {opacity:0; transform: translateY(10px);}
            100% {opacity:1; transform: translateY(0);}
        }
        /* Custom styled containers for a clean professional look */
        .metric-card {
            background-color: #f8f9fa;
            border-left: 4px solid #1f77b4;
            padding: 15px;
            border-radius: 6px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
            margin-bottom: 10px;
        }
        /* Hide default Streamlit decoration elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. TOP HORIZONTAL NAVIGATION BAR
# ==========================================
st.markdown('<div class="fade-in">', unsafe_allow_html=True)

# Title Header Banner
title_col, contact_col = st.columns([2, 1])
with title_col:
    st.title("Yaser Alhusaini")
    st.markdown("**Public Policy & Data Operations Consultant** | Bridging Policy Insights & Scalable Analytics")
with contact_col:
    st.markdown("""
    <div style="text-align: right; padding-top: 10px; color: #555;">
        📍 Maryland, MD &nbsp;|&nbsp; ✉️ <a href="mailto:alhusaini.yaser@gmail.com">alhusaini.yaser@gmail.com</a><br>
        <a href="https://linkedin.com" target="_blank">LinkedIn</a> &nbsp;•&nbsp; <a href="https://github.com" target="_blank">GitHub</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Clean Horizontal Navigation Matrix
nav_col1, nav_col2, nav_col3, nav_spacer = st.columns([1, 1.2, 1, 3])

if 'current_page' not in st.session_state:
    st.session_state.current_page = "🏠 Profile Overview"

with nav_col1:
    if st.button("🏠 Profile Overview", use_container_width=True):
        st.session_state.current_page = "🏠 Profile Overview"
with nav_col2:
    if st.button("📈 Interactive Simulator", use_container_width=True):
        st.session_state.current_page = "📈 Interactive Simulator"
with nav_col3:
    if st.button("💼 Full Experience", use_container_width=True):
        st.session_state.current_page = "💼 Full Experience"

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# PAGE VIEW CONFIGURATIONS
# ==========================================

# --- PAGE: HOME & OVERVIEW ---
if st.session_state.current_page == "🏠 Profile Overview":
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    
    st.subheader("Executive Summary")
    st.markdown("""
    Versatile public-sector and nonprofit professional with deep experience in program operations, 
    data analysis, policy research, and technical documentation. Proven ability to support complex projects, 
    improve internal systems, and translate messy data into clear, executive-ready insights.
    """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.header("🎯 Core Capabilities")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h4>🧠 Policy & Evaluation</h4>
            <ul>
                <li><b>Quantitative & Qualitative Evaluation:</b> Experience with logic models, mixed-methods framework design, and impact assessments.</li>
                <li><b>Stakeholder Management:</b> Coordinating seamlessly across national ministries, regional government agencies (e.g., DOES, OSSE), and community partners.</li>
                <li><b>Strategic Reporting:</b> Drafting comprehensive policy briefs, compliance matrices, and research syntheses for leadership.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h4>💻 Data & Digital Operations</h4>
            <ul>
                <li><b>Advanced Analytics:</b> Statistical modeling, predictive trend forecasting, and data wrangling utilizing <b>R, Python, and STATA</b>.</li>
                <li><b>Internal Systems & Dashboards:</b> Designing operational trackers and interactive analytics layers via <b>Tableau, Qualtrics, and Smartsheet</b>.</li>
                <li><b>Capacity Building:</b> Training, upskilling, and supporting staff members on technical visualization and performance metrics.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.info("💡 **Interactive Element Live:** Click on **'📈 Interactive Simulator'** in the top navigation bar to test a dynamic data simulation tool built natively from scratch.")
    st.markdown('</div>', unsafe_transform=True)

# --- PAGE: INTERACTIVE SIMULATION DASHBOARD ---
elif st.session_state.current_page == "📈 Interactive Simulator":
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    
    st.subheader("📊 DC Metro Youth Workforce Initiative Simulator")
    st.markdown("""
    **Operational Sandbox:** This scenario models outcomes for a regional youth workforce development program based on adjustments to funding profiles, staff allocations, and target baseline enrollment. 
    *Adjust the policy parameters on the left to watch the fiscal year pipeline dynamically animate.*
    """)
    
    st.markdown("---")
    
    # Modern Workspace Grid: Left side Controls, Right side Output Visuals
    control_panel, visual_panel = st.columns([1, 2.2], gap="large")
    
    with control_panel:
        st.markdown("#### 🎛️ Policy Parameters")
        allocated_funding = st.slider("Annual Budget Allocation ($)", min_value=100000, max_value=1500000, value=500000, step=50000)
        mentorship_ratio = st.slider("Staff-to-Participant Ratio (1 : X)", min_value=5, max_value=30, value=15)
        baseline_participants = st.number_input("Enrolled Youth Target (Annual)", min_value=50, max_value=1000, value=200, step=25)
        
        st.markdown("---")
        st.markdown("""
        <small style="color: #666;">
        <b>Methodology Note:</b><br>
        The simulator uses a dynamic response matrix. Scaling down funding below baseline values ($2,500/capita) 
        triggers mathematical operational constraints on retention curves, while optimal staffing density 
        exponentially compounds successful long-term job placements.
        </small>
        """, unsafe_allow_html=True)

    # Backend Algorithmic Calculations
    base_funding_per_capita = 2500  
    actual_funding_per_capita = allocated_funding / baseline_participants
    funding_impact = min(1.2, max(0.5, actual_funding_per_capita / base_funding_per_capita))
    staff_impact = min(1.2, max(0.6, 15 / mentorship_ratio))
    
    completion_rate = min(0.98, max(0.40, 0.75 * funding_impact * (staff_impact ** 0.5)))
    placement_rate = min(0.95, max(0.35, 0.65 * (funding_impact ** 0.5) * staff_impact))
    
    total_completed = int(baseline_participants * completion_rate)
    total_placed = int(total_completed * placement_rate)
    
    with visual_panel:
        # Mini KPI Highlight grid
        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown(f'<div class="metric-card"><strong>Completion Rate</strong><br><span style="font-size:22px; color:#1f77b4; font-weight:bold;">{completion_rate*100:.1f}%</span></div>', unsafe_allow_html=True)
        with m2:
            st.markdown(f'<div class="metric-card"><strong>Placement Rate</strong><br><span style="font-size:22px; color:#ff7f0e; font-weight:bold;">{placement_rate*100:.1f}%</span></div>', unsafe_allow_html=True)
        with m3:
            st.markdown(f'<div class="metric-card"><strong>Total Jobs Secured</strong><br><span style="font-size:22px; color:#2ca02c; font-weight:bold;">{total_placed} / {baseline_participants}</span></div>', unsafe_allow_html=True)
            
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Build Smooth Cumulative Pipeline Arrays
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        distribution = np.array([0.05, 0.08, 0.12, 0.18, 0.25, 0.35, 0.50, 0.65, 0.78, 0.88, 0.95, 1.00])
        
        cum_enrolled = np.round(baseline_participants * distribution).astype(int)
        cum_completed = np.round(total_completed * distribution).astype(int)
        cum_placed = np.round(total_placed * distribution).astype(int)
        
        # ELEGANT ANIMATED PLOTLY IMPLEMENTATION (Using Graph Objects)
        fig = go.Figure()
        
        # Add the data lines
        fig.add_trace(go.Scatter(x=months, y=cum_enrolled, name="Total Enrolled Target", line=dict(color='#1f77b4', width=3), mode='lines+markers'))
        fig.add_trace(go.Scatter(x=months, y=cum_completed, name="Successful Graduations", line=dict(color='#2ca02c', width=3), mode='lines+markers'))
        fig.add_trace(go.Scatter(x=months, y=cum_placed, name="Secured Job Placements", line=dict(color='#ff7f0e', width=3), mode='lines+markers'))
        
        # Inject the frame transitions layout animation script
        fig.update_layout(
            title="Fiscal Year Cumulative Pipeline Performance Tracking",
            xaxis_title="Reporting Period (Fiscal Months)",
            yaxis_title="Cumulative Count of Unique Participants",
            yaxis_range=[0, max(120, int(baseline_participants * 1.15))],
            hovermode="x unified",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            margin=dict(t=30, b=40, l=40, r=20),
            # Transition config triggers smooth canvas slides when inputs recalculate
            transition=dict(
                duration=500,
                easing="cubic-in-out"
            )
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
    st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE: FULL EXPERIENCE (RESUME VIEW) ---
elif st.session_state.current_page == "💼 Full Experience":
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    
    st.subheader("💼 Professional Background & Academic History")
    
    col_ed, col_exp = st.columns([1, 2], gap="large")
    
    with col_ed:
        st.markdown("### 🎓 Education")
        st.markdown("""
        * **The George Washington University** *PhD Courses, Trachtenberg School of Public Policy & Public Administration* Core focus: Advanced Quantitative & Qualitative Research Methods (2021–2022)
          
        * **Georgetown University** *Master of Public Policy (MPP), McCourt School of Public Policy* (2020)
          
        * **University of Manchester (UK)** *BA (Hons) in Politics, Philosophy & Economics (PPE)* (2015)
        """)
        st.markdown("---")
        st.markdown("### 🛠️ Technical Toolkit")
        st.markdown("`STATA` `R Programming` `Python` `Tableau` `Qualtrics` `Smartsheet` `Logic Modeling` `Program Evaluation` `Compliance Tracking`")
        
    with col_exp:
        st.markdown("### 🚀 Professional Experience")
        
        st.markdown("""
        **Employment & Education Specialist** | SAMU First Response  
        *January 2026 – Present | Washington, DC*
        * Provide structured employment and education coaching to transition DC youth experiencing homelessness into high-readiness pathways.
        * Maintain direct mentoring relationships, auditing technical trade school options and higher education configurations.
        
        **Senior Policy Associate** | WE Strategies  
        *April 2024 – April 2025 | Washington, DC*
        * Managed analytical data frameworks and operational pipelines supporting regional workforce initiatives.
        * Spearheaded cross-agency execution and outcome reporting matrices for key entities including **DOES** and **OSSE**.
        * Led technical capacity training for 10+ core staff members focusing on dashboard transparency and metric reporting.
        
        **Data Analysis Intern** | The World Bank  
        *September – December 2019 | Washington, DC*
        * Evaluated complex international business data environments under the *Doing Business 2020* global regulatory benchmarking framework.
        
        **Policy Fellow** | Harvard Kennedy School  
        *October 2016 – July 2018 | Riyadh, Saudi Arabia*
        * Governed multi-method field evaluation operations spanning more than 20 national labor and education portfolios.
        * Interfaced directly with ministerial leadership teams to align monitoring matrices and deployment benchmarks.
        """)
        
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
