import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import base64
import time

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Yaser Alhusaini",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Load resume for download ───────────────────────────────────────────────────
def get_resume_b64():
    try:
        with open("resume.pdf", "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return None

resume_b64 = get_resume_b64()

# ── CSS ────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400;1,600&family=DM+Mono:wght@300;400;500&family=Jost:wght@200;300;400;500&display=swap');

/* ── Reset & base ── */
html, body, [class*="css"] {
    font-family: 'Jost', sans-serif;
    background-color: #0a0a0a;
    color: #e8e4dc;
}
.stApp { background: #0a0a0a; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stSidebar"] { display: none; }

/* ── Noise grain overlay ── */
.stApp::before {
    content: '';
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.03'/%3E%3C/svg%3E");
    pointer-events: none;
    z-index: 0;
    opacity: 0.4;
}

/* ── Nav ── */
.nav-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.6rem 4rem;
    border-bottom: 1px solid rgba(232,228,220,0.08);
    position: sticky;
    top: 0;
    background: rgba(10,10,10,0.92);
    backdrop-filter: blur(12px);
    z-index: 100;
    animation: fadeDown 0.8s ease both;
}
.nav-name {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.25rem;
    font-weight: 600;
    letter-spacing: 0.05em;
    color: #e8e4dc;
}
.nav-links {
    display: flex;
    gap: 2.5rem;
    list-style: none;
}
.nav-links a {
    font-size: 0.72rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: rgba(232,228,220,0.5);
    text-decoration: none;
    transition: color 0.2s;
}
.nav-links a:hover { color: #e8e4dc; }

/* ── Hero ── */
.hero-section {
    min-height: 92vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 6rem 4rem 4rem;
    position: relative;
    overflow: hidden;
    animation: fadeUp 1s ease 0.2s both;
}
.hero-overline {
    font-family: 'DM Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: #b5936b;
    margin-bottom: 2rem;
    animation: fadeUp 0.8s ease 0.4s both;
}
.hero-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(3.5rem, 7vw, 7rem);
    font-weight: 300;
    line-height: 0.95;
    letter-spacing: -0.02em;
    color: #e8e4dc;
    margin-bottom: 2.5rem;
    animation: fadeUp 0.8s ease 0.5s both;
}
.hero-title em {
    font-style: italic;
    color: #b5936b;
}
.hero-desc {
    font-size: 1rem;
    font-weight: 300;
    line-height: 1.85;
    color: rgba(232,228,220,0.6);
    max-width: 520px;
    margin-bottom: 3rem;
    animation: fadeUp 0.8s ease 0.6s both;
}
.hero-line {
    width: 60px;
    height: 1px;
    background: #b5936b;
    margin-bottom: 3rem;
    animation: expandWidth 1s ease 0.8s both;
}
.hero-cta-row {
    display: flex;
    gap: 1.2rem;
    flex-wrap: wrap;
    animation: fadeUp 0.8s ease 0.7s both;
}
.btn-gold {
    display: inline-block;
    padding: 0.75rem 2rem;
    background: #b5936b;
    color: #0a0a0a;
    font-family: 'Jost', sans-serif;
    font-size: 0.75rem;
    font-weight: 500;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    text-decoration: none;
    border: none;
    cursor: pointer;
    transition: background 0.2s, color 0.2s;
}
.btn-gold:hover { background: #c8a880; }
.btn-outline {
    display: inline-block;
    padding: 0.75rem 2rem;
    background: transparent;
    color: #e8e4dc;
    font-family: 'Jost', sans-serif;
    font-size: 0.75rem;
    font-weight: 400;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    text-decoration: none;
    border: 1px solid rgba(232,228,220,0.25);
    cursor: pointer;
    transition: border-color 0.2s, color 0.2s;
}
.btn-outline:hover { border-color: #e8e4dc; }

/* ── Stats strip ── */
.stats-strip {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    border-top: 1px solid rgba(232,228,220,0.08);
    border-bottom: 1px solid rgba(232,228,220,0.08);
    margin: 0 4rem;
    animation: fadeUp 0.8s ease 0.9s both;
}
.stat-item {
    padding: 2.5rem 2rem;
    border-right: 1px solid rgba(232,228,220,0.08);
}
.stat-item:last-child { border-right: none; }
.stat-num {
    font-family: 'Cormorant Garamond', serif;
    font-size: 3rem;
    font-weight: 300;
    color: #e8e4dc;
    line-height: 1;
    margin-bottom: 0.4rem;
}
.stat-num span { color: #b5936b; }
.stat-label {
    font-size: 0.72rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: rgba(232,228,220,0.4);
}

/* ── Section base ── */
.section {
    padding: 6rem 4rem;
    border-bottom: 1px solid rgba(232,228,220,0.06);
}
.section-header {
    display: flex;
    align-items: baseline;
    gap: 1.5rem;
    margin-bottom: 4rem;
    padding-bottom: 1.2rem;
    border-bottom: 1px solid rgba(232,228,220,0.08);
}
.section-num {
    font-family: 'DM Mono', monospace;
    font-size: 0.68rem;
    color: #b5936b;
    letter-spacing: 0.15em;
}
.section-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 2rem;
    font-weight: 300;
    color: #e8e4dc;
    letter-spacing: 0.02em;
}

/* ── Experience timeline ── */
.exp-item {
    display: grid;
    grid-template-columns: 200px 1fr;
    gap: 3rem;
    padding: 2.5rem 0;
    border-bottom: 1px solid rgba(232,228,220,0.05);
    animation: fadeUp 0.6s ease both;
}
.exp-item:last-child { border-bottom: none; }
.exp-meta { padding-top: 0.15rem; }
.exp-date {
    font-family: 'DM Mono', monospace;
    font-size: 0.68rem;
    color: #b5936b;
    letter-spacing: 0.1em;
    margin-bottom: 0.5rem;
}
.exp-org {
    font-size: 0.78rem;
    color: rgba(232,228,220,0.45);
    letter-spacing: 0.06em;
    text-transform: uppercase;
}
.exp-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.35rem;
    font-weight: 400;
    color: #e8e4dc;
    margin-bottom: 1rem;
    line-height: 1.2;
}
.exp-loc {
    font-size: 0.75rem;
    color: rgba(232,228,220,0.35);
    letter-spacing: 0.06em;
    margin-bottom: 1rem;
}
.exp-bullets { list-style: none; padding: 0; }
.exp-bullets li {
    font-size: 0.88rem;
    font-weight: 300;
    color: rgba(232,228,220,0.65);
    line-height: 1.75;
    padding-left: 1rem;
    position: relative;
    margin-bottom: 0.4rem;
}
.exp-bullets li::before {
    content: '—';
    position: absolute;
    left: 0;
    color: #b5936b;
    font-size: 0.8rem;
}

/* ── Skills ── */
.skills-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1px;
    background: rgba(232,228,220,0.06);
}
.skill-card {
    background: #0a0a0a;
    padding: 2rem 1.8rem;
    transition: background 0.2s;
}
.skill-card:hover { background: #111; }
.skill-cat {
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #b5936b;
    margin-bottom: 1rem;
}
.skill-items {
    font-size: 0.88rem;
    font-weight: 300;
    color: rgba(232,228,220,0.65);
    line-height: 1.9;
}

/* ── Dashboard section ── */
.dash-intro {
    font-size: 0.9rem;
    font-weight: 300;
    line-height: 1.8;
    color: rgba(232,228,220,0.55);
    max-width: 680px;
    margin-bottom: 2.5rem;
}
.filter-strip {
    display: flex;
    gap: 0.5rem;
    margin-bottom: 2rem;
    flex-wrap: wrap;
}

/* ── Live indicator ── */
.live-bar {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1px;
    background: rgba(232,228,220,0.06);
    margin-bottom: 3rem;
    border: 1px solid rgba(232,228,220,0.06);
}
.live-cell {
    background: #0f0f0f;
    padding: 1.5rem 2rem;
}
.live-period {
    font-family: 'DM Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: 0.15em;
    color: rgba(232,228,220,0.3);
    margin-bottom: 0.6rem;
}
.live-val {
    font-family: 'Cormorant Garamond', serif;
    font-size: 2.4rem;
    font-weight: 300;
    color: #e8e4dc;
    line-height: 1;
    margin-bottom: 0.4rem;
}
.live-val.danger { color: #c8402a; }
.live-lbl {
    font-size: 0.75rem;
    font-weight: 300;
    color: rgba(232,228,220,0.45);
    margin-bottom: 0.5rem;
}
.live-delta { font-family: 'DM Mono', monospace; font-size: 0.72rem; }
.delta-bad { color: #c8402a; }
.delta-ok { color: #4a9e72; }
.pulse-dot {
    display: inline-block;
    width: 6px; height: 6px;
    border-radius: 50%;
    background: #c8402a;
    margin-right: 6px;
    animation: pulse 2s infinite;
    vertical-align: middle;
}
@keyframes pulse {
    0%,100%{opacity:1;} 50%{opacity:0.3;}
}

/* ── Contact ── */
.contact-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6rem;
}
.contact-headline {
    font-family: 'Cormorant Garamond', serif;
    font-size: 3rem;
    font-weight: 300;
    line-height: 1.1;
    color: #e8e4dc;
    margin-bottom: 1.5rem;
}
.contact-headline em { font-style: italic; color: #b5936b; }
.contact-sub {
    font-size: 0.9rem;
    font-weight: 300;
    line-height: 1.85;
    color: rgba(232,228,220,0.5);
    margin-bottom: 2.5rem;
}
.contact-item {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 1.2rem 0;
    border-top: 1px solid rgba(232,228,220,0.06);
    font-size: 0.9rem;
    font-weight: 300;
    color: rgba(232,228,220,0.7);
}
.contact-icon {
    font-family: 'DM Mono', monospace;
    font-size: 0.7rem;
    color: #b5936b;
    letter-spacing: 0.1em;
    min-width: 60px;
}

/* ── Footer ── */
.site-footer {
    padding: 2rem 4rem;
    border-top: 1px solid rgba(232,228,220,0.06);
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.footer-text {
    font-family: 'DM Mono', monospace;
    font-size: 0.68rem;
    letter-spacing: 0.1em;
    color: rgba(232,228,220,0.25);
}

/* ── Keyframes ── */
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(24px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes fadeDown {
    from { opacity: 0; transform: translateY(-16px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes expandWidth {
    from { width: 0; }
    to   { width: 60px; }
}

/* ── Streamlit overrides ── */
div[data-testid="stMarkdownContainer"] p { margin: 0; }
.stPlotlyChart { border: 1px solid rgba(232,228,220,0.07) !important; }
div[data-testid="stHorizontalBlock"] > div { padding: 0 !important; }
button[kind="secondary"] {
    background: transparent !important;
    border: 1px solid rgba(232,228,220,0.2) !important;
    color: rgba(232,228,220,0.7) !important;
    border-radius: 0 !important;
    font-family: 'Jost', sans-serif !important;
    font-size: 0.72rem !important;
    letter-spacing: 0.15em !important;
    text-transform: uppercase !important;
}
button[kind="secondary"]:hover {
    border-color: #b5936b !important;
    color: #b5936b !important;
}
</style>
""", unsafe_allow_html=True)

# ── Nav ────────────────────────────────────────────────────────────────────────
st.markdown("""
<nav class="nav-bar">
  <div class="nav-name">Yaser Alhusaini</div>
  <div class="nav-links">
    <a href="#experience">Experience</a>
    <a href="#dashboard">Dashboard</a>
    <a href="#services">Services</a>
    <a href="#contact">Contact</a>
  </div>
</nav>
""", unsafe_allow_html=True)

# ── Hero ───────────────────────────────────────────────────────────────────────
resume_href = f'data:application/pdf;base64,{resume_b64}' if resume_b64 else '#'

st.markdown(f"""
<section class="hero-section">
  <div class="hero-overline">Policy · Data · Research · Impact</div>
  <h1 class="hero-title">
    Research that<br>moves people<br><em>forward.</em>
  </h1>
  <div class="hero-line"></div>
  <p class="hero-desc">
    Public policy analyst, data strategist, and program evaluator with a decade of experience
    spanning workforce development, education policy, economic research, and direct service —
    from DC's frontlines to the World Bank.
  </p>
  <div class="hero-cta-row">
    <a href="#dashboard" class="btn-gold">View Dashboard</a>
    <a href="{resume_href}" download="Yaser_Alhusaini_Resume.pdf" class="btn-outline">Download Resume</a>
    <a href="https://www.linkedin.com/in/yaser-alhusaini-43330b281/" target="_blank" class="btn-outline">LinkedIn</a>
  </div>
</section>
""", unsafe_allow_html=True)

# ── Stats strip ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="stats-strip">
  <div class="stat-item">
    <div class="stat-num">500<span>+</span></div>
    <div class="stat-label">Research participants managed</div>
  </div>
  <div class="stat-item">
    <div class="stat-num">10<span>+</span></div>
    <div class="stat-label">Staff trained in data & evaluation</div>
  </div>
  <div class="stat-item">
    <div class="stat-num">5</div>
    <div class="stat-label">Cities — DC · Bethesda · London · Riyadh · Manchester</div>
  </div>
  <div class="stat-item">
    <div class="stat-num">MPP</div>
    <div class="stat-label">Georgetown McCourt School of Public Policy</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Experience ─────────────────────────────────────────────────────────────────
st.markdown('<div id="experience"></div>', unsafe_allow_html=True)
st.markdown("""
<section class="section">
  <div class="section-header">
    <span class="section-num">01</span>
    <span class="section-title">Experience</span>
  </div>

  <div class="exp-item">
    <div class="exp-meta">
      <div class="exp-date">Jan 2026 — Present</div>
      <div class="exp-org">SAMU First Response</div>
    </div>
    <div>
      <div class="exp-title">Employment &amp; Education Specialist</div>
      <div class="exp-loc">Washington, DC</div>
      <ul class="exp-bullets">
        <li>Provide employment and education coaching to DC youth experiencing homelessness at a drop-in center</li>
        <li>Build ongoing mentorship as participants transition into new employment and develop workplace readiness</li>
        <li>Advise on education pathways including high school completion, trade school, and college options</li>
        <li>Connect youth with individualized employment, education, and community resources</li>
      </ul>
    </div>
  </div>

  <div class="exp-item">
    <div class="exp-meta">
      <div class="exp-date">Apr 2024 — Apr 2025</div>
      <div class="exp-org">WE Strategies</div>
    </div>
    <div>
      <div class="exp-title">Senior Policy Associate</div>
      <div class="exp-loc">Washington, DC</div>
      <ul class="exp-bullets">
        <li>Managed data strategy and program operations across workforce development and education initiatives</li>
        <li>Led analysis and performance tracking for DOES and OSSE</li>
        <li>Authored analytical and strategic reports to inform program design and funding priorities</li>
        <li>Trained and supported 10+ staff on data visualization, reporting, and evaluation methods</li>
      </ul>
    </div>
  </div>

  <div class="exp-item">
    <div class="exp-meta">
      <div class="exp-date">Feb — Jun 2021</div>
      <div class="exp-org">Kugler Economic Associates</div>
    </div>
    <div>
      <div class="exp-title">Economic Analyst</div>
      <div class="exp-loc">Bethesda, MD</div>
      <ul class="exp-bullets">
        <li>Analyzed wage and employment data to identify trends among essential workers during COVID-19</li>
        <li>Presented findings in policy memos and presentations to senior leadership</li>
        <li>Collaborated with senior researchers to validate data and align with project deliverables</li>
      </ul>
    </div>
  </div>

  <div class="exp-item">
    <div class="exp-meta">
      <div class="exp-date">Oct 2016 — Jul 2018</div>
      <div class="exp-org">Harvard Kennedy School</div>
    </div>
    <div>
      <div class="exp-title">Policy Fellow</div>
      <div class="exp-loc">Riyadh, Saudi Arabia</div>
      <ul class="exp-bullets">
        <li>Oversaw field research operations across 20+ education and labor programs</li>
        <li>Coordinated data collection, analysis, and reporting with national ministry teams</li>
        <li>Designed evaluation frameworks and provided technical support for monitoring and performance tracking</li>
      </ul>
    </div>
  </div>

  <div class="exp-item">
    <div class="exp-meta">
      <div class="exp-date">Sep — Dec 2019</div>
      <div class="exp-org">World Bank</div>
    </div>
    <div>
      <div class="exp-title">Data Analysis Intern</div>
      <div class="exp-loc">Washington, DC</div>
      <ul class="exp-bullets">
        <li>Conducted data analysis for regulatory reform projects under the Doing Business 2020 initiative</li>
        <li>Prepared internal reports summarizing progress and policy implications for education and workforce sectors</li>
      </ul>
    </div>
  </div>

  <div class="exp-item">
    <div class="exp-meta">
      <div class="exp-date">Jul 2020 — Oct 2020<br>May 2017 — Jul 2018</div>
      <div class="exp-org">Georgetown University</div>
    </div>
    <div>
      <div class="exp-title">Research Fellow &amp; Teaching Assistant</div>
      <div class="exp-loc">Washington, DC</div>
      <ul class="exp-bullets">
        <li>Managed coordination for a 500-participant labor market survey</li>
        <li>Synthesized findings into policy briefs for government and academic partners</li>
        <li>Supported instruction in quantitative program evaluation; guided 46 graduate students</li>
      </ul>
    </div>
  </div>
</section>
""", unsafe_allow_html=True)

# ── Skills ─────────────────────────────────────────────────────────────────────
st.markdown("""
<section class="section">
  <div class="section-header">
    <span class="section-num">02</span>
    <span class="section-title">Expertise &amp; Tools</span>
  </div>
  <div class="skills-grid">
    <div class="skill-card">
      <div class="skill-cat">Research Methods</div>
      <div class="skill-items">Quantitative &amp; qualitative design<br>Mixed-methods analysis<br>Logic models<br>Impact assessment<br>Field research operations<br>Survey design (Qualtrics)</div>
    </div>
    <div class="skill-card">
      <div class="skill-cat">Data &amp; Technology</div>
      <div class="skill-items">STATA · R · Python<br>Tableau · Flourish<br>Smartsheet · Office Suite<br>Dashboard development<br>Data visualization<br>Performance tracking systems</div>
    </div>
    <div class="skill-card">
      <div class="skill-cat">Policy &amp; Programs</div>
      <div class="skill-items">Workforce development<br>Education policy<br>Grant coordination<br>Compliance reporting<br>Stakeholder engagement<br>Cross-agency coordination</div>
    </div>
    <div class="skill-card">
      <div class="skill-cat">Communication</div>
      <div class="skill-items">Policy briefs &amp; memos<br>Executive briefings<br>Analytical reports<br>Presentations<br>Staff training<br>Partner relations</div>
    </div>
    <div class="skill-card">
      <div class="skill-cat">Education</div>
      <div class="skill-items">MPP — Georgetown University<br>BA PPE — Univ. of Manchester<br>PhD coursework — GWU<br>MIT J-PAL Research Methods<br>CFA Level I</div>
    </div>
    <div class="skill-card">
      <div class="skill-cat">Languages</div>
      <div class="skill-items">English — Fluent<br>Arabic — Native</div>
    </div>
  </div>
</section>
""", unsafe_allow_html=True)

# ── Dashboard ──────────────────────────────────────────────────────────────────
st.markdown('<div id="dashboard"></div>', unsafe_allow_html=True)
st.markdown("""
<section class="section">
  <div class="section-header">
    <span class="section-num">03</span>
    <span class="section-title">DMV Federal Workforce Impact — Interactive Dashboard</span>
  </div>
  <p class="dash-intro">
    A live analytical lens on how federal workforce reductions have reshaped the DC–Maryland–Virginia
    regional economy. This dashboard reflects the kind of data work I build for agency and nonprofit
    clients — translating administrative and labor market data into clear, decision-ready insights.
  </p>
""", unsafe_allow_html=True)

# Live indicator strip
st.markdown("""
<div class="live-bar">
  <div class="live-cell">
    <div class="live-period"><span class="pulse-dot"></span>Mar 2026 — DC City (seas. adj.)</div>
    <div class="live-val danger">6.3%</div>
    <div class="live-lbl">Unemployment rate</div>
    <div class="live-delta delta-bad">▲ +0.4 pts since Feb 2026</div>
  </div>
  <div class="live-cell">
    <div class="live-period"><span class="pulse-dot"></span>Feb 2025 → Feb 2026</div>
    <div class="live-val danger">−63,100</div>
    <div class="live-lbl">Federal jobs lost, DMV region</div>
    <div class="live-delta delta-bad">▼ −14.2% of DMV federal workforce</div>
  </div>
  <div class="live-cell">
    <div class="live-period"><span class="pulse-dot"></span>2025 annual ranking</div>
    <div class="live-val">#1</div>
    <div class="live-lbl">Home listing surge, US metros</div>
    <div class="live-delta" style="color:rgba(232,228,220,0.35);">Largest inventory jump in the country</div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("</section>", unsafe_allow_html=True)

# ── Dashboard controls ─────────────────────────────────────────────────────────
with st.container():
    st.markdown('<div style="padding: 0 4rem 2rem;">', unsafe_allow_html=True)

    col_filters = st.columns([1, 1, 1, 3])
    with col_filters[0]:
        panel = st.selectbox(
            "Panel",
            ["Unemployment Trend", "Sector Job Losses", "Housing Squeeze"],
            label_visibility="collapsed"
        )
    with col_filters[1]:
        if panel == "Unemployment Trend":
            show_nat = st.checkbox("Show national baseline", value=True)
        elif panel == "Sector Job Losses":
            cat_filter = st.selectbox("Category", ["All", "Direct — Federal", "Direct — Contracting", "Downstream"], label_visibility="collapsed")
        elif panel == "Housing Squeeze":
            metric = st.selectbox("Metric", ["Both", "Listings only", "Price change only"], label_visibility="collapsed")

    # ── Plotly theme ──
    PLOT_BG     = "#0a0a0a"
    PAPER_BG    = "#0a0a0a"
    GRID_COLOR  = "rgba(232,228,220,0.05)"
    TICK_COLOR  = "rgba(232,228,220,0.3)"
    GOLD        = "#b5936b"
    CRIMSON     = "#c8402a"
    NAVY        = "#2a5080"
    MUTED       = "rgba(232,228,220,0.4)"
    FONT_FAMILY = "Jost, sans-serif"

    base_layout = dict(
        paper_bgcolor=PAPER_BG,
        plot_bgcolor=PLOT_BG,
        font=dict(family=FONT_FAMILY, color=TICK_COLOR, size=11),
        margin=dict(l=20, r=20, t=40, b=20),
        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            bordercolor="rgba(232,228,220,0.1)",
            borderwidth=1,
            font=dict(size=11, color=TICK_COLOR)
        ),
        xaxis=dict(gridcolor=GRID_COLOR, tickcolor=TICK_COLOR, linecolor=GRID_COLOR, zeroline=False),
        yaxis=dict(gridcolor=GRID_COLOR, tickcolor=TICK_COLOR, linecolor=GRID_COLOR, zeroline=False),
        hoverlabel=dict(
            bgcolor="#1a1a1a",
            bordercolor=GOLD,
            font=dict(family=FONT_FAMILY, color="#e8e4dc", size=12)
        ),
    )

    # ── PANEL 1: Unemployment Trend ──
    if panel == "Unemployment Trend":
        months = [
            "Jan 24","Feb 24","Mar 24","Apr 24","May 24","Jun 24",
            "Jul 24","Aug 24","Sep 24","Oct 24","Nov 24","Dec 24",
            "Jan 25","Feb 25","Mar 25","Apr 25","May 25","Jun 25",
            "Jul 25","Aug 25","Sep 25","Oct 25","Nov 25","Dec 25",
            "Jan 26","Feb 26",
        ]
        dc_md = [4.7,4.4,4.1,3.9,3.7,4.2,4.3,4.1,3.9,3.8,3.9,3.8,
                 4.7,4.9,5.1,5.3,5.5,5.7,5.8,5.6,5.3,5.2,5.1,5.1,5.6,5.7]
        dc_city = [5.9,5.6,5.3,5.0,4.8,5.5,5.7,5.4,5.1,5.0,5.2,5.1,
                   6.0,6.2,6.4,6.5,6.7,6.9,6.0,5.9,5.7,5.8,5.9,6.7,6.7,6.5]
        national = [3.7,3.9,3.8,3.9,4.0,4.1,4.3,4.2,4.1,4.1,4.2,4.2,
                    4.0,4.1,4.2,4.2,4.2,4.1,4.3,4.2,4.1,4.2,4.1,4.2,4.7,4.5]

        annotations = [
            dict(x="Jan 25", y=4.7, text="DOGE launches", showarrow=True, arrowhead=0,
                 arrowcolor=GOLD, font=dict(size=10, color=GOLD), ax=40, ay=-30),
            dict(x="Jul 25", y=5.8, text="DC leads US unemployment<br>(3rd consecutive month)", showarrow=True,
                 arrowhead=0, arrowcolor=CRIMSON, font=dict(size=10, color=CRIMSON), ax=-80, ay=-40),
            dict(x="Feb 26", y=5.7, text="63,100 jobs lost YoY", showarrow=True,
                 arrowhead=0, arrowcolor=MUTED, font=dict(size=10, color=MUTED), ax=40, ay=30),
        ]

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=months, y=dc_city,
            name="DC City (seas. adj.)",
            line=dict(color=CRIMSON, width=2.5),
            mode="lines+markers",
            marker=dict(size=4, color=CRIMSON),
            hovertemplate="<b>DC City</b><br>%{x}: %{y:.1f}%<extra></extra>"
        ))
        fig.add_trace(go.Scatter(
            x=months, y=dc_md,
            name="DC–MD Metro Division",
            line=dict(color=GOLD, width=2.5),
            mode="lines+markers",
            marker=dict(size=4, color=GOLD),
            hovertemplate="<b>DC–MD Metro</b><br>%{x}: %{y:.1f}%<extra></extra>"
        ))
        if show_nat:
            fig.add_trace(go.Scatter(
                x=months, y=national,
                name="National",
                line=dict(color=MUTED, width=1.5, dash="dot"),
                mode="lines",
                hovertemplate="<b>National</b><br>%{x}: %{y:.1f}%<extra></extra>"
            ))
        # Shade post-inauguration
        fig.add_vrect(x0="Jan 25", x1="Feb 26",
                      fillcolor="rgba(200,64,42,0.04)", line_width=0,
                      annotation_text="Post-DOGE period", annotation_position="top left",
                      annotation_font_color=MUTED, annotation_font_size=10)

        layout = base_layout.copy()
        layout.update(dict(
            title=dict(text="DMV Unemployment Rate vs. National — Jan 2024 to Feb 2026",
                       font=dict(size=14, color="#e8e4dc"), x=0.02),
            yaxis=dict(**base_layout["yaxis"], ticksuffix="%", title="Unemployment Rate"),
            annotations=annotations,
            height=480,
        ))
        fig.update_layout(**layout)
        st.plotly_chart(fig, use_container_width=True)

    # ── PANEL 2: Sector Job Losses ──
    elif panel == "Sector Job Losses":
        sectors = [
            ("Federal government",           53800, "Direct — Federal"),
            ("Professional & business svcs",  9400, "Direct — Contracting"),
            ("Federal contracting",           18000, "Direct — Contracting"),
            ("Nonprofit / grant-funded",       6200, "Downstream"),
            ("Tourism & hospitality",          3600, "Downstream"),
            ("Hospitality & food service",     4800, "Downstream"),
            ("Retail trade",                   3100, "Downstream"),
            ("Transportation & utilities",     2200, "Downstream"),
            ("Real estate & rental",           1800, "Downstream"),
            ("State & local government",       2400, "Downstream"),
        ]
        df = pd.DataFrame(sectors, columns=["Sector", "Jobs Lost", "Category"])
        df = df.sort_values("Jobs Lost", ascending=True)

        if cat_filter != "All":
            df = df[df["Category"] == cat_filter]

        color_map = {
            "Direct — Federal":      CRIMSON,
            "Direct — Contracting":  GOLD,
            "Downstream":            NAVY,
        }
        colors = [color_map[c] for c in df["Category"]]

        fig = go.Figure(go.Bar(
            x=df["Jobs Lost"],
            y=df["Sector"],
            orientation="h",
            marker=dict(color=colors, line=dict(width=0)),
            customdata=df["Category"],
            hovertemplate="<b>%{y}</b><br>Jobs lost: %{x:,}<br>Category: %{customdata}<extra></extra>",
            text=df["Jobs Lost"].apply(lambda x: f"{x:,}"),
            textposition="outside",
            textfont=dict(color=TICK_COLOR, size=11),
        ))
        layout = base_layout.copy()
        layout.update(dict(
            title=dict(text="DMV Job Losses by Sector — 2025 Year-over-Year",
                       font=dict(size=14, color="#e8e4dc"), x=0.02),
            xaxis=dict(**base_layout["xaxis"], title="Jobs Lost", tickformat=","),
            height=420,
            showlegend=False,
        ))
        fig.update_layout(**layout)

        # Legend annotation
        for cat, col in color_map.items():
            fig.add_annotation(
                x=1, y=0, xref="paper", yref="paper",
                text="", showarrow=False
            )

        st.plotly_chart(fig, use_container_width=True)
        st.markdown(f"""
        <div style="display:flex;gap:1.5rem;padding:0.5rem 0 1.5rem;font-size:0.75rem;color:{TICK_COLOR};">
          <span><span style="color:{CRIMSON};">■</span> Direct — Federal</span>
          <span><span style="color:{GOLD};">■</span> Direct — Contracting</span>
          <span><span style="color:{NAVY};">■</span> Downstream</span>
        </div>
        """, unsafe_allow_html=True)

    # ── PANEL 3: Housing Squeeze ──
    elif panel == "Housing Squeeze":
        months = [
            "Jan 24","Feb 24","Mar 24","Apr 24","May 24","Jun 24",
            "Jul 24","Aug 24","Sep 24","Oct 24","Nov 24","Dec 24",
            "Jan 25","Feb 25","Mar 25","Apr 25","May 25","Jun 25",
            "Jul 25","Aug 25","Sep 25","Oct 25","Nov 25","Dec 25",
            "Jan 26","Feb 26",
        ]
        listings = [5820,5640,6100,6890,7420,7810,7650,7200,6540,5980,5510,4980,
                    5230,5640,6820,8100,9350,10200,10800,10400,9800,9200,8100,7200,7600,8100]
        price_chg = [5.1,5.4,5.8,6.2,6.0,5.5,4.8,4.2,3.9,3.5,3.1,2.8,
                     2.5,2.1,1.4,0.8,0.2,-0.5,-1.2,-1.8,-2.1,-2.4,-2.0,-1.6,-1.4,-1.1]

        fig = make_subplots(specs=[[{"secondary_y": True}]])

        if metric in ["Both", "Listings only"]:
            fig.add_trace(go.Bar(
                x=months, y=listings,
                name="Active Listings",
                marker=dict(color=[GOLD if i >= 12 else "rgba(181,147,107,0.25)" for i in range(len(months))],
                            line=dict(width=0)),
                hovertemplate="<b>Active Listings</b><br>%{x}: %{y:,}<extra></extra>",
            ), secondary_y=False)

        if metric in ["Both", "Price change only"]:
            pc_colors = [CRIMSON if v < 0 else "#4a9e72" for v in price_chg]
            fig.add_trace(go.Scatter(
                x=months, y=price_chg,
                name="Median Price Change YoY %",
                line=dict(color=CRIMSON, width=2),
                mode="lines+markers",
                marker=dict(size=5, color=pc_colors),
                hovertemplate="<b>Price Change</b><br>%{x}: %{y:+.1f}%<extra></extra>",
            ), secondary_y=True)

        fig.add_vrect(x0="Jan 25", x1="Feb 26",
                      fillcolor="rgba(200,64,42,0.04)", line_width=0)
        fig.add_annotation(x="Jul 25", y=10800, text="Listings peak<br>+41% YoY",
                           showarrow=True, arrowhead=0, arrowcolor=GOLD,
                           font=dict(size=10, color=GOLD), ay=-40)
        fig.add_hline(y=0, secondary_y=True,
                      line=dict(color="rgba(232,228,220,0.15)", width=1, dash="dot"))

        layout = base_layout.copy()
        layout.update(dict(
            title=dict(text="DMV Housing: Listing Surge vs. Price Pressure — 2024 to 2026",
                       font=dict(size=14, color="#e8e4dc"), x=0.02),
            yaxis=dict(**base_layout["yaxis"], title="Active Listings", tickformat=","),
            yaxis2=dict(title="Median Price Change YoY %", ticksuffix="%",
                        gridcolor=GRID_COLOR, tickcolor=TICK_COLOR),
            height=480,
            barmode="overlay",
        ))
        fig.update_layout(**layout)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ── Services ───────────────────────────────────────────────────────────────────
st.markdown('<div id="services"></div>', unsafe_allow_html=True)
st.markdown("""
<section class="section">
  <div class="section-header">
    <span class="section-num">04</span>
    <span class="section-title">Services</span>
  </div>
  <div class="skills-grid">
    <div class="skill-card">
      <div class="skill-cat">01</div>
      <div class="exp-title" style="font-size:1.1rem;margin-bottom:0.8rem;">Program Evaluation &amp; Impact Assessment</div>
      <div class="skill-items">Design and execute mixed-methods evaluations from logic model development through data collection, analysis, and final reporting — for government, nonprofit, and foundation clients.</div>
    </div>
    <div class="skill-card">
      <div class="skill-cat">02</div>
      <div class="exp-title" style="font-size:1.1rem;margin-bottom:0.8rem;">Data Strategy &amp; Dashboard Design</div>
      <div class="skill-items">Build internal and client-facing dashboards in Tableau, Flourish, and R that translate raw program data into clear performance insights. Includes staff training and documentation.</div>
    </div>
    <div class="skill-card">
      <div class="skill-cat">03</div>
      <div class="exp-title" style="font-size:1.1rem;margin-bottom:0.8rem;">Policy Research &amp; Strategic Reporting</div>
      <div class="skill-items">Produce analytical memos, policy briefs, and grant reports that synthesize evidence for decision-makers. Experienced with DOES, OSSE, and federal workforce program frameworks.</div>
    </div>
    <div class="skill-card">
      <div class="skill-cat">04</div>
      <div class="exp-title" style="font-size:1.1rem;margin-bottom:0.8rem;">Workforce &amp; Education Program Support</div>
      <div class="skill-items">Support program design and operations for workforce and education initiatives, including participant engagement, employer partnerships, and outcome tracking systems.</div>
    </div>
    <div class="skill-card">
      <div class="skill-cat">05</div>
      <div class="exp-title" style="font-size:1.1rem;margin-bottom:0.8rem;">Grant Coordination &amp; Compliance Reporting</div>
      <div class="skill-items">Manage data collection, performance measurement, and narrative reporting for federally-funded programs, including WIOA and Title I workforce grants.</div>
    </div>
    <div class="skill-card">
      <div class="skill-cat">06</div>
      <div class="exp-title" style="font-size:1.1rem;margin-bottom:0.8rem;">Field Research Operations</div>
      <div class="skill-items">Design and manage large-scale surveys and field data collection. Proven across 500+ participant labor market studies, ministry-level monitoring systems, and World Bank initiatives.</div>
    </div>
  </div>
</section>
""", unsafe_allow_html=True)

# ── Contact ────────────────────────────────────────────────────────────────────
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
resume_href = f'data:application/pdf;base64,{resume_b64}' if resume_b64 else '#'
st.markdown(f"""
<section class="section">
  <div class="section-header">
    <span class="section-num">05</span>
    <span class="section-title">Work Together</span>
  </div>
  <div class="contact-grid">
    <div>
      <h2 class="contact-headline">Let's turn your data<br>into <em>decisions.</em></h2>
      <p class="contact-sub">
        Available for consulting engagements, research contracts, program evaluation projects,
        and embedded analyst roles with government agencies, nonprofits, and mission-driven
        firms in the DC metro area and beyond.
      </p>
      <div class="hero-cta-row">
        <a href="mailto:alhusaini.yaser@gmail.com" class="btn-gold">Send an Email</a>
        <a href="{resume_href}" download="Yaser_Alhusaini_Resume.pdf" class="btn-outline">Download Resume</a>
      </div>
    </div>
    <div>
      <div class="contact-item">
        <span class="contact-icon">EMAIL</span>
        <span>alhusaini.yaser@gmail.com</span>
      </div>
      <div class="contact-item">
        <span class="contact-icon">PHONE</span>
        <span>(571) 326–8979</span>
      </div>
      <div class="contact-item">
        <span class="contact-icon">LOCATION</span>
        <span>Maryland · DC Metro Area</span>
      </div>
      <div class="contact-item">
        <span class="contact-icon">LINKEDIN</span>
        <a href="https://www.linkedin.com/in/yaser-alhusaini-43330b281/" target="_blank"
           style="color:rgba(232,228,220,0.7);text-decoration:none;">linkedin.com/in/yaser-alhusaini-43330b281</a>
      </div>
      <div class="contact-item">
        <span class="contact-icon">STATUS</span>
        <span>Open to contracts &amp; consulting</span>
      </div>
    </div>
  </div>
</section>
""", unsafe_allow_html=True)

# ── Footer ─────────────────────────────────────────────────────────────────────
st.markdown("""
<footer class="site-footer">
  <span class="footer-text">© 2025 Yaser Alhusaini — Policy · Data · Research</span>
  <span class="footer-text">MPP Georgetown · BA Manchester · MIT J-PAL</span>
</footer>
""", unsafe_allow_html=True)
