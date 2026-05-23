import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="Yaser Alhusaini | Policy & Data Operations",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. SIDEBAR NAVIGATION & CONTACT
with st.sidebar:
    st.title("Yaser Alhusaini")
    st.caption("Maryland, MD | alhusaini.yaser@gmail.com")
    st.markdown("---")
    st.markdown("### 🌐 Navigation")
    page = st.radio("Go to:", ["Home & Portfolio", "Interactive Simulation Dashboard", "Full Experience"])
    st.markdown("---")
    st.markdown("### ✉️ Let's Collaborate")
    st.markdown("[LinkedIn](https://linkedin.com) | [GitHub](https://github.com)")
    st.write("Available for public-sector and nonprofit consulting contracts.")

# ==========================================
# PAGE: HOME & PORTFOLIO
# ==========================================
if page == "Home & Portfolio":
    st.title("Yaser Alhusaini")
    st.subheader("Bridging the Gap Between Complex Public Policy & Data Operations")
    
    st.markdown("""
    Versatile public-sector and nonprofit professional with deep experience in program operations, 
    data analysis, policy research, and technical documentation. Proven ability to support complex projects, 
    improve internal systems, and translate messy data into clear, executive-ready insights.
    """)
    
    st.markdown("---")
    
    # Core Competencies Columns
    st.header("🎯 Core Capabilities")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🧠 Policy & Evaluation")
        st.markdown("""
        * **Quantitative & Qualitative Evaluation:** Experience in logic models, mixed-methods design, and impact assessments.
        * **Stakeholder Management:** Coordinating seamlessly across national ministries, government agencies, and community partners.
        * **Strategic Reporting:** Drafting comprehensive policy briefs, compliance reports, and briefs for leadership.
        """)
        
    with col2:
        st.markdown("#### 💻 Data & Digital Operations")
        st.markdown("""
        * **Advanced Analytics:** Statistical modeling and trend extraction using **R, Python, and STATA**.
        * **Internal Systems & Dashboards:** Designing tracking frameworks and internal tools using **Tableau, Qualtrics, and Smartsheet**.
        * **Capacity Building:** Training and upskilling team members on data visualization and performance tracking.
        """)
        
    st.markdown("---")
    st.header("🚀 Featured Project Showcase")
    st.info("💡 **How to view:** Select **'Interactive Simulation Dashboard'** from the sidebar to test a live data product.")

# ==========================================
# PAGE: INTERACTIVE SIMULATION DASHBOARD
# ==========================================
elif page == "Interactive Simulation Dashboard":
    st.title("📊 DC Metro Youth Workforce Initiative Simulator")
    st.caption("A Mock Project Demonstrating Program Evaluation Modeling & Strategic Operations")
    
    st.markdown("""
    **The Scenario:** A local agency (e.g., DOES or OSSE) wants to project outcomes for a youth workforce training and mentorship program based on changes to funding allocation, staff capacities, and participant enrollment.
    
    *Adjust the inputs below to see how changes to resource metrics shift program completion and job placement outcomes.*
    """)
    
    st.markdown("---")
    
    # Interactive Input Widgets (The Controls)
    st.sidebar.markdown("### 🎛️ Simulation Parameters")
    allocated_funding = st.sidebar.slider("Annual Budget Allocation ($)", min_value=100000, max_value=1500000, value=500000, step=50000)
    mentorship_ratio = st.sidebar.slider("Target Staff-to-Participant Ratio (1 : X)", min_value=5, max_value=30, value=15)
    baseline_participants = st.sidebar.number_input("Enrolled Youth Target", min_value=50, max_value=500, value=200)
    
    # 🧠 BACKEND LOGIC: Simulating real-time policy impact math
    # Funding changes baseline success curves
    funding_factor = allocated_funding / 500000
    # Higher student/teacher ratio reduces success due to lower individual attention
    staff_factor = 15 / mentorship_ratio 
    
    # Calculate simulated outcomes
    completion_rate = min(0.95, 0.70 * (funding_factor ** 0.15) * (staff_factor ** 0.1))
    placement_rate = min(0.90, 0.60 * (funding_factor ** 0.2) * (staff_factor ** 0.15))
    
    total_completed = int(baseline_participants * completion_rate)
    total_placed = int(total_completed * placement_rate)
    
    # DISPLAY METRICS (KPI Cards)
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric(label="Predicted Program Completion Rate", value=f"{completion_rate*100:.1f}%")
    kpi2.metric(label="Predicted Post-Program Job Placement", value=f"{placement_rate*100:.1f}%")
    kpi3.metric(label="Total Youth Employed via Simulation", value=f"{total_placed} Pax")
    
    st.markdown("### 📈 Visualizing the Trends")
    
    # Create simulated monthly tracking data for a mock interactive chart
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    np.random.seed(42)
    
    # Generate interactive time-series chart data responsive to inputs
    monthly_enrollment = np.round(np.linspace(baseline_participants/12, (baseline_participants/12)*1.3, 12)).astype(int)
    monthly_placements = np.round(monthly_enrollment * completion_rate * placement_rate).astype(int)
    
    df_chart = pd.DataFrame({
        "Month": months,
        "Target Enrolled": monthly_enrollment,
        "Simulated Job Placements": monthly_placements
    })
    
  # Plotly Chart Generation
    fig = px.bar(
        df_chart, 
        x="Month", 
        y=["Target Enrolled", "Simulated Job Placements"],
        barmode="group",  # <-- FIXED HERE
        title="Simulated Operational Performance Tracking over 12 Months",
        labels={"value": "Count of Participants", "variable": "Metric"},
        color_discrete_sequence=["#1f77b4", "#ff7f0e"]
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Behind the Scenes Context Box
    st.markdown("---")
    with st.expander("🔍 Behind the Scenes: How this answers real-world operational challenges"):
        st.markdown("""
        **Why this tool wins contracts:**
        1. **Data-Driven Evaluation:** Instead of reading static PDFs, decision-makers can stress-test financial choices instantly to optimize program design.
        2. **Technical Mastery without Frontend Bottlenecks:** Built natively in Python, meaning your data pipelines connect directly to your user interface seamlessly.
        3. **Scalability:** This logic can easily ingest live programmatic feeds from PostgreSQL databases, AWS storage, or manual CSV uploads.
        """)

# ==========================================
# PAGE: FULL EXPERIENCE
# ==========================================
elif page == "Full Experience":
    st.title("💼 Professional Background & Timeline")
    
    # Quick Summary Checklist
    st.markdown("#### 🎓 Education")
    st.markdown("""
    * **The George Washington University** | PhD Courses, Public Policy & Public Administration (Research Methods Focus)
    * **Georgetown University** | Master of Public Policy (McCourt School)
    * **University of Manchester** | BA (Hons) Politics, Philosophy & Economics
    """)
    
    st.markdown("---")
    
    st.markdown("#### 🛠️ Professional History Snapshot")
    
    with st.container():
        st.subheader("Senior Policy Associate | WE Strategies")
        st.caption("April 2024 - April 2025 | Washington, DC")
        st.markdown("""
        * Managed data strategy and program operations across workforce development and education initiatives.
        * Led analysis and performance tracking for critical regional agencies including **DOES** and **OSSE**.
        * Trained and supported 10+ staff members on data visualization, reporting, and evaluation methods.
        """)

    with st.container():
        st.subheader("Employment & Education Specialist | SAMU First Response")
        st.caption("January 2026 - Present | Washington, DC")
        st.markdown("""
        * Provide employment and education coaching to DC youth experiencing homelessness.
        * Advise participants on structural pathway completions including trade schools, certifications, and higher degree options.
        """)
        
    with st.container():
        st.subheader("Policy Fellow | Harvard Kennedy School")
        st.caption("October 2016 - July 2018 | Riyadh, Saudi Arabia")
        st.markdown("""
        * Oversaw complex field research operations across more than 20 education and labor programs.
        * Coordinated data collection, analysis, and execution matrices directly with national ministry teams.
        """)
