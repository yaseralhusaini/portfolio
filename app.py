import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import base64
import os

st.set_page_config(
    page_title="Yaser Alhusaini",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Resolve paths relative to this script file so they work regardless of cwd
_DIR = os.path.dirname(os.path.abspath(__file__))

def get_file_b64(filename):
    try:
        with open(os.path.join(_DIR, filename), "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return None

resume_b64 = get_file_b64("resume.pdf")
photo_b64  = get_file_b64("photo_nobg.png")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400;1,600&family=DM+Mono:wght@300;400;500&family=Jost:wght@200;300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'Jost', sans-serif;
    background-color: #f7f5f0;
    color: #1c1c1c;
}
.stApp { background: #f7f5f0; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stSidebar"] { display: none; }

/* Force all headings dark — overrides Streamlit theme */
h1, h2, h3, h4, h5, h6 { color: #1c1c1c !important; }
.hero-title em { color: #9c6f3a !important; }
.contact-headline em { color: #9c6f3a !important; }

/* ── Nav ── */
.nav-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.4rem 4rem;
    border-bottom: 1px solid rgba(26,26,26,0.1);
    position: sticky;
    top: 0;
    background: rgba(247,245,240,0.97);
    backdrop-filter: blur(12px);
    z-index: 100;
    animation: fadeDown 0.8s ease both;
}
.nav-name {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.5rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    color: #1c1c1c;
}
.nav-links { display: flex; gap: 2.5rem; }
.nav-links a {
    font-size: 0.93rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: rgba(28,28,28,0.65);
    text-decoration: none;
    transition: color 0.2s;
}
.nav-links a:hover { color: #1c1c1c; }

/* ── Hero + Stats side by side ── */
.hero-stats-row {
    display: flex;
    align-items: stretch;
    border-bottom: 1px solid rgba(26,26,26,0.08);
    animation: fadeUp 0.9s ease 0.15s both;
}
.hero-content {
    padding: 3.5rem 4rem 3rem;
    flex: 0 0 56%;
}
.hero-overline {
    font-family: 'DM Mono', monospace;
    font-size: 0.92rem;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: #9c6f3a;
    margin-bottom: 1.8rem;
}
.hero-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(3.2rem, 6vw, 6rem);
    font-weight: 300;
    line-height: 0.95;
    letter-spacing: -0.02em;
    color: #1c1c1c !important;
    margin-bottom: 2rem;
}
.hero-line {
    width: 60px;
    height: 2px;
    background: #9c6f3a;
    margin-bottom: 2rem;
    animation: expandWidth 1s ease 0.8s both;
}
.hero-desc {
    font-size: 1.32rem !important;
    font-weight: 300;
    line-height: 1.85;
    color: rgba(28,28,28,0.80);
    max-width: 580px;
    margin-bottom: 0;
}
.hero-cta-row {
    display: flex;
    gap: 1.2rem;
    flex-wrap: wrap;
    margin-top: 3.5rem;
}
.btn-gold {
    display: inline-block;
    padding: 0.9rem 2.2rem;
    background: #6b4718;
    color: #ffffff !important;
    font-family: 'Jost', sans-serif;
    font-size: 0.9rem;
    font-weight: 500;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    text-decoration: none !important;
    border: none;
    cursor: pointer;
    transition: background 0.2s;
}
.btn-gold:hover,
a.btn-gold:hover { background: #9c6f3a; color: #ffffff !important; }
a.btn-gold,
a.btn-gold:link,
a.btn-gold:visited,
a.btn-gold:active { color: #ffffff !important; text-decoration: none !important; }

.btn-outline {
    display: inline-block;
    padding: 0.9rem 2.2rem;
    background: transparent;
    color: #6b4718 !important;
    font-family: 'Jost', sans-serif;
    font-size: 0.9rem;
    font-weight: 500;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    text-decoration: none !important;
    border: 2px solid #9c6f3a;
    cursor: pointer;
    transition: border-color 0.2s, background 0.2s, color 0.2s;
}
a.btn-outline,
a.btn-outline:link,
a.btn-outline:visited,
a.btn-outline:active { color: #6b4718 !important; text-decoration: none !important; }
.btn-outline:hover,
a.btn-outline:hover {
    border-color: #6b4718;
    background: rgba(107,71,24,0.07);
    color: #6b4718 !important;
}

/* ── Hero right panel (photo + stats) ── */
.hero-right {
    flex: 0 0 44%;
    display: flex;
    flex-direction: column;
    border-left: 1px solid rgba(26,26,26,0.08);
}
.hero-photo-wrap {
    border-bottom: 1px solid rgba(26,26,26,0.08);
    background: #f7f5f0;
    overflow: hidden;
    flex-shrink: 0;
}
.hero-photo {
    width: 100%;
    height: 340px;
    object-fit: cover;
    object-position: 50% 12%;
    display: block;
}

/* ── Stats column (right of hero) ── */
.stats-column {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 2rem 3rem;
}

/* ── MPP credential under hero buttons ── */
.hero-mpp {
    margin-top: 2rem;
    padding: 1.5rem 1.8rem;
    background: #ede9e0;
    border-top: 2px solid #9c6f3a;
}
.hero-mpp-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.55rem;
    font-weight: 400;
    color: #1c1c1c;
    line-height: 1.25;
    margin-bottom: 0.4rem;
}
.hero-mpp-sub {
    font-family: 'DM Mono', monospace;
    font-size: 0.78rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: rgba(28,28,28,0.60);
    line-height: 1.5;
}
.stat-row {
    padding: 1.8rem 0;
    border-bottom: 1px solid rgba(26,26,26,0.08);
}
.stat-row:last-child { border-bottom: none; }
.stat-num {
    font-family: 'Cormorant Garamond', serif;
    font-size: 3rem;
    font-weight: 300;
    color: #1c1c1c;
    line-height: 1;
    margin-bottom: 0.5rem;
}
.stat-num span { color: #9c6f3a; }
.stat-label {
    font-size: 1.02rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: rgba(28,28,28,0.65);
    line-height: 1.5;
}

/* ── Section base ── */
.section {
    padding: 4rem 4rem;
    border-bottom: 1px solid rgba(26,26,26,0.06);
}
.section-alt {
    background: #edeae2;
}
.section-alt .skill-card { background: #edeae2; }
.section-alt .skill-card:hover { background: #e4e0d6; }
.section-header {
    display: flex;
    align-items: baseline;
    gap: 1.5rem;
    margin-bottom: 3.5rem;
    padding-bottom: 1rem;
    border-bottom: 2px solid rgba(156,111,58,0.22);
}
.section-num {
    font-family: 'DM Mono', monospace;
    font-size: 0.82rem;
    color: #9c6f3a;
    letter-spacing: 0.12em;
    border: 1px solid rgba(156,111,58,0.50);
    padding: 0.2rem 0.55rem;
    line-height: 1;
    flex-shrink: 0;
}
.section-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 2.6rem;
    font-weight: 300;
    color: #1c1c1c;
}

/* ── Experience timeline ── */
.exp-item {
    display: grid;
    grid-template-columns: 220px 1fr;
    gap: 3rem;
    padding: 2.8rem 0;
    border-bottom: 1px solid rgba(26,26,26,0.06);
}
.exp-item:last-child { border-bottom: none; }
.exp-date {
    font-family: 'DM Mono', monospace;
    font-size: 0.94rem;
    color: #9c6f3a;
    letter-spacing: 0.08em;
    margin-bottom: 0.5rem;
    line-height: 1.6;
}
.exp-org {
    font-size: 1.02rem;
    color: rgba(28,28,28,0.60);
    letter-spacing: 0.06em;
    text-transform: uppercase;
    margin-top: 0.4rem;
}
.exp-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.85rem;
    font-weight: 400;
    color: #1c1c1c;
    margin-bottom: 0.4rem;
    line-height: 1.2;
}
.exp-loc {
    font-size: 1rem;
    color: rgba(28,28,28,0.55);
    letter-spacing: 0.06em;
    margin-bottom: 1.2rem;
}
.exp-bullets { list-style: none; padding: 0; }
.exp-bullets li {
    font-size: 1.18rem;
    font-weight: 300;
    color: rgba(28,28,28,0.82);
    line-height: 1.85;
    padding-left: 1.2rem;
    position: relative;
    margin-bottom: 0.5rem;
}
.exp-bullets li::before {
    content: '—';
    position: absolute;
    left: 0;
    color: #9c6f3a;
}

/* ── Skills grid ── */
.skills-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1px;
    background: rgba(26,26,26,0.08);
    border: 1px solid rgba(26,26,26,0.08);
}
.skill-card {
    background: #f7f5f0;
    padding: 2.2rem 2rem;
    transition: background 0.2s;
}
.skill-card:hover { background: #efece5; }
.skill-cat {
    font-family: 'DM Mono', monospace;
    font-size: 0.85rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #9c6f3a;
    margin-bottom: 1rem;
}
.skill-items {
    font-size: 1.18rem;
    font-weight: 300;
    color: rgba(28,28,28,0.80);
    line-height: 2;
}

/* ── Dashboard ── */
.dash-intro {
    font-size: 1.25rem !important;
    font-weight: 300;
    line-height: 1.85;
    color: rgba(28,28,28,0.78);
    max-width: 700px;
    margin-bottom: 2.5rem;
}
.live-bar {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1px;
    background: rgba(26,26,26,0.12);
    border: 1px solid rgba(26,26,26,0.12);
    margin-bottom: 2.5rem;
}
.live-cell {
    background: #ffffff;
    padding: 2rem 4.5rem;
}
.live-period {
    font-family: 'DM Mono', monospace;
    font-size: 0.68rem;
    letter-spacing: 0.12em;
    color: rgba(28,28,28,0.65);
    margin-bottom: 0.6rem;
    display: flex;
    align-items: center;
}
.live-val {
    font-family: 'Cormorant Garamond', serif;
    font-size: 2.6rem;
    font-weight: 300;
    color: #1c1c1c;
    line-height: 1;
    margin-bottom: 0.4rem;
}
.live-val.danger { color: #a32020; }
.live-lbl {
    font-size: 0.98rem;
    font-weight: 400;
    color: rgba(28,28,28,0.75);
    margin-bottom: 0.5rem;
}
.live-delta { font-family: 'DM Mono', monospace; font-size: 0.88rem; }
.delta-bad { color: #a32020; }
.delta-ok { color: #2d6e42; }

/* ── Live pulse dot — bigger and more dramatic ── */
.pulse-dot {
    display: inline-block;
    width: 13px;
    height: 13px;
    border-radius: 50%;
    background: #a32020;
    margin-right: 8px;
    flex-shrink: 0;
    animation: pulse-ring 1.4s ease-out infinite;
    box-shadow: 0 0 0 0 rgba(163,32,32,0.5);
}
@keyframes pulse-ring {
    0%   { box-shadow: 0 0 0 0 rgba(163,32,32,0.55); opacity: 1; }
    60%  { box-shadow: 0 0 0 10px rgba(163,32,32,0); opacity: 0.85; }
    100% { box-shadow: 0 0 0 0 rgba(163,32,32,0); opacity: 1; }
}

/* ── Contact ── */
.contact-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6rem;
}
.contact-headline {
    font-family: 'Cormorant Garamond', serif;
    font-size: 3.4rem;
    font-weight: 300;
    line-height: 1.1;
    color: #1c1c1c !important;
    margin-bottom: 1.5rem;
}
.contact-sub {
    font-size: 1.28rem !important;
    font-weight: 300;
    line-height: 1.85;
    color: rgba(28,28,28,0.72);
    margin-bottom: 0;
}
.contact-cta-row {
    display: flex;
    gap: 1.2rem;
    flex-wrap: wrap;
    margin-top: 3.5rem;
}
.contact-item {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 1.2rem 0;
    border-top: 1px solid rgba(26,26,26,0.07);
    font-size: 1.18rem;
    font-weight: 300;
    color: rgba(28,28,28,0.85);
}
.contact-icon {
    font-family: 'DM Mono', monospace;
    font-size: 0.85rem;
    color: #9c6f3a;
    letter-spacing: 0.1em;
    min-width: 80px;
}

/* ── Footer ── */
.site-footer {
    padding: 2rem 4rem;
    border-top: 1px solid rgba(26,26,26,0.07);
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.footer-text {
    font-family: 'DM Mono', monospace;
    font-size: 0.85rem;
    letter-spacing: 0.08em;
    color: rgba(28,28,28,0.55);
}

/* ── Keyframes ── */
@keyframes fadeUp { from{opacity:0;transform:translateY(22px);} to{opacity:1;transform:translateY(0);} }
@keyframes fadeDown { from{opacity:0;transform:translateY(-14px);} to{opacity:1;transform:translateY(0);} }
@keyframes expandWidth { from{width:0;} to{width:60px;} }

/* ── Streamlit overrides ── */
div[data-testid="stMarkdownContainer"] p { margin: 0; }
.stPlotlyChart {
    border: 1px solid rgba(26,26,26,0.10) !important;
    margin: 0 3rem 1.5rem !important;
}

/* Fix invisible white text in Streamlit widgets */
[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] label,
.stSelectbox > label,
.stCheckbox > label,
[data-baseweb="select"] span,
[data-baseweb="menu"] li,
[data-baseweb="menu"] li span,
div[data-testid="stSelectbox"] label,
div[data-testid="stCheckbox"] label {
    color: #1c1c1c !important;
    font-size: 1.06rem !important;
}

/* Experience — secondary section divider */
.exp-section-divider {
    padding: 1.8rem 0 1rem;
    border-top: 1px solid rgba(26,26,26,0.08);
    margin-top: 0.5rem;
    display: flex;
    align-items: center;
    gap: 1.2rem;
}
.exp-section-divider::after {
    content: '';
    flex: 1;
    height: 1px;
    background: rgba(26,26,26,0.06);
}
.exp-section-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.80rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: rgba(28,28,28,0.42);
    white-space: nowrap;
}

/* Dashboard chart container horizontal padding */
div[data-testid="stHorizontalBlock"] {
    padding-left: 1rem !important;
    padding-right: 1rem !important;
}

/* ── Selected Work ── */
.work-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1px;
    background: rgba(26,26,26,0.08);
    border: 1px solid rgba(26,26,26,0.08);
}
.work-card {
    background: #f7f5f0;
    padding: 2.8rem 2.5rem;
    display: flex;
    flex-direction: column;
    gap: 1.1rem;
    transition: background 0.2s;
}
.work-card:hover { background: #efece5; }
.work-overline {
    font-family: 'DM Mono', monospace;
    font-size: 0.80rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #9c6f3a;
}
.work-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 2.1rem;
    font-weight: 400;
    color: #1c1c1c;
    line-height: 1.15;
    margin: 0;
}
.work-meta {
    font-size: 0.95rem;
    color: rgba(28,28,28,0.52);
    letter-spacing: 0.05em;
}
.work-finding {
    border-left: 2px solid #9c6f3a;
    padding-left: 1.2rem;
    margin: 0.4rem 0;
}
.work-finding-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: rgba(28,28,28,0.45);
    display: block;
    margin-bottom: 0.4rem;
}
.work-finding-text {
    font-size: 1.12rem;
    font-weight: 300;
    color: #1c1c1c;
    line-height: 1.55;
}
.work-link { margin-top: 0.8rem; align-self: flex-start; }
.work-placeholder {
    background: #f0ede6;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 2.8rem 2.5rem;
    color: rgba(28,28,28,0.30);
    font-family: 'DM Mono', monospace;
    font-size: 0.85rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
}

/* Featured service card (spans full row) */
.skill-card-featured {
    background: #ede9e0;
    padding: 2.2rem 2.5rem;
    grid-column: span 3;
    display: grid;
    grid-template-columns: 260px 1fr;
    gap: 2.5rem;
    align-items: start;
    border-top: 2px solid #9c6f3a;
    transition: background 0.2s;
}
.skill-card-featured:hover { background: #e5e0d6; }
</style>
""", unsafe_allow_html=True)

# ── Resume b64 ─────────────────────────────────────────────────────────────────
resume_href = f'data:application/pdf;base64,{resume_b64}' if resume_b64 else '#'

# ── Nav ────────────────────────────────────────────────────────────────────────
st.markdown("""
<nav class="nav-bar">
  <div class="nav-name">Yaser Alhusaini</div>
  <div class="nav-links">
    <a href="#experience">Experience</a>
    <a href="#selected-work">Work</a>
    <a href="#dashboard">Dashboard</a>
    <a href="#services">Services</a>
    <a href="#contact">Contact</a>
  </div>
</nav>
""", unsafe_allow_html=True)

# ── Hero + Stats (side by side) ────────────────────────────────────────────────
st.markdown(f"""
<div class="hero-stats-row">
  <section class="hero-content">
    <div class="hero-overline">Policy · Data · Research · Impact</div>
    <h1 class="hero-title">
      Research that<br>moves people<br><em>forward.</em>
    </h1>
    <div class="hero-line"></div>
    <p class="hero-desc">
      Public policy analyst, data strategist, and program evaluator with a decade of experience
      spanning workforce development, education policy, economic research, and direct service —
      from DC's frontlines to the World Bank and Harvard Kennedy School.
    </p>
    <div class="hero-cta-row">
      <a href="#dashboard" class="btn-gold">View Dashboard</a>
      <a href="{resume_href}" download="Yaser_Alhusaini_Resume.pdf" class="btn-outline">Download Resume</a>
      <a href="https://www.linkedin.com/in/yaser-alhusaini-43330b281/" target="_blank" class="btn-outline">LinkedIn</a>
    </div>
    <div class="hero-mpp">
      <div class="hero-mpp-title">Master of Public Policy</div>
      <div class="hero-mpp-sub">Georgetown University · McCourt School of Public Policy · 2020</div>
    </div>
  </section>

  <div class="hero-right">
    <div class="hero-photo-wrap">
      <img src="data:image/png;base64,{photo_b64}" class="hero-photo" alt="Yaser Alhusaini">
    </div>
    <div class="stats-column">
      <div class="stat-row">
        <div class="stat-num">50<span>+</span></div>
        <div class="stat-label">Research projects managed</div>
      </div>
      <div class="stat-row">
        <div class="stat-num">30<span>+</span></div>
        <div class="stat-label">Staff trained in data &amp; evaluation</div>
      </div>
      <div class="stat-row">
        <div class="stat-num">5</div>
        <div class="stat-label">
          Countries<br>
          <span style="font-size:0.87em;color:rgba(28,28,28,0.55);line-height:2;display:block;">Middle East — Saudi Arabia · UAE · Egypt</span>
          <span style="font-size:0.87em;color:rgba(28,28,28,0.55);line-height:1.6;display:block;">North America — United States</span>
          <span style="font-size:0.87em;color:rgba(28,28,28,0.55);line-height:1.6;display:block;">Europe — United Kingdom</span>
        </div>
      </div>
    </div>
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
    <div>
      <div class="exp-date">Jan 2026 — Present</div>
      <div class="exp-org">SAMU First Response</div>
    </div>
    <div>
      <div class="exp-title">Employment &amp; Education Specialist</div>
      <div class="exp-loc">Washington, DC</div>
      <ul class="exp-bullets">
        <li>Provide one-on-one employment and education coaching to DC youth experiencing homelessness at a drop-in center, with a focus on building sustained relationships that support long-term stability.</li>
        <li>Develop and maintain individualized service plans tracking each participant's progress across employment, education, and housing milestones, using outcome data to adjust coaching strategy in real time.</li>
        <li>Advise participants on full spectrum of education pathways — GED completion, trade and vocational programs, community college, and four-year degree options — connecting them to financial aid and enrollment support.</li>
        <li>Build and maintain a network of employer and community resource referrals, matching youth to job opportunities aligned with their skills and readiness level.</li>
        <li>Deliver workplace readiness training covering resume writing, interview preparation, and professional communication, adapting curriculum to meet participants where they are.</li>
      </ul>
    </div>
  </div>

  <div class="exp-item">
    <div>
      <div class="exp-date">Apr 2024 — Apr 2025</div>
      <div class="exp-org">WE Strategies</div>
    </div>
    <div>
      <div class="exp-title">Senior Policy Associate</div>
      <div class="exp-loc">Washington, DC</div>
      <ul class="exp-bullets">
        <li>Built and led company-wide data infrastructure, automating operations and external reporting pipelines — increasing reporting efficiency by 40% and reducing manual data processing across multiple program teams.</li>
        <li>Led performance tracking and analysis for DC's Department of Employment Services (DOES) and Office of the State Superintendent of Education (OSSE), translating administrative data into quarterly strategic reports for agency leadership.</li>
        <li>Designed and implemented mixed-methods data collection tools — including surveys, focus groups, and structured interviews — to assess program effectiveness and surface equity-related findings.</li>
        <li>Managed a data team; led onboarding, training, and adoption of Tableau and Smartsheet tools across programs, building organization-wide analytical capacity through hands-on staff instruction.</li>
        <li>Developed a real-time participant monitoring system with automated red-flag alerts to identify and support struggling youth, seniors, and returning citizens enrolled in training programs.</li>
        <li>Authored analytical memos, policy briefs, and grant compliance reports using survey data, literature reviews, and focus group findings to inform program design and funding priorities.</li>
      </ul>
    </div>
  </div>

  <div class="exp-item">
    <div>
      <div class="exp-date">Feb 2022 — Aug 2022</div>
      <div class="exp-org">Alnahda Society / Alwathba Consultancy</div>
    </div>
    <div>
      <div class="exp-title">Research Analyst — Takafu Equal Opportunity Index</div>
      <div class="exp-loc">Riyadh, Saudi Arabia</div>
      <ul class="exp-bullets">
        <li>Served as a core analyst on the Takafu Equal Opportunity Index — Saudi Arabia's first gender parity index for the private sector — commissioned by Alnahda Society, the Kingdom's oldest and largest women's empowerment nonprofit.</li>
        <li>Analyzed national administrative data from GOSI (General Organization for Social Insurance) covering over 7.8 million private sector employees, running advanced regression models to measure gender gaps in participation, career development, and compensation.</li>
        <li>Conducted Oaxaca-Blinder decomposition analyses to isolate and quantify the unexplained portion of the gender wage gap across industries and firm sizes.</li>
        <li>Designed and analyzed dual survey instruments — one targeting HR managers, one targeting employees — collecting responses from 57 companies and 985 Saudi workers across Riyadh, Makkah, and the Eastern Province.</li>
        <li>Synthesized quantitative findings and qualitative survey data into the published Takafu 2020 Executive Summary, with policy and employer recommendations cited by government stakeholders aligned to Saudi Vision 2030.</li>
      </ul>
    </div>
  </div>

  <div class="exp-item">
    <div>
      <div class="exp-date">Oct 2016 — Jul 2018</div>
      <div class="exp-org">Harvard Kennedy School</div>
    </div>
    <div>
      <div class="exp-title">Policy Fellow — Evidence for Policy Design (EPoD)</div>
      <div class="exp-loc">Riyadh, Saudi Arabia</div>
      <ul class="exp-bullets">
        <li>Embedded within Harvard's Evidence for Policy Design (EPoD) unit in Riyadh, supporting a portfolio of 20+ active research projects at the intersection of education, labor markets, and social protection in Saudi Arabia.</li>
        <li>Managed data acquisition, cleaning, and preparation for field studies conducted in partnership with the Ministry of Labor and Social Development and the Ministry of Education — including panel datasets covering all private sector workers in the Kingdom.</li>
        <li>Oversaw the incubation of 12 new research projects: matched potential researchers with relevant government policymakers, negotiated data access agreements, and managed stakeholder relationships from project inception through delivery.</li>
        <li>Co-developed survey instruments and analytic files for a 500-participant labor market study on early retirement patterns, managing field coordination and STATA-based analysis.</li>
        <li>Designed and delivered capacity-building workshops on evidence-based research design and Randomized Controlled Trials (RCTs) to ministry counterparts and NGO partners.</li>
        <li>Contributed to policy briefs and executive communications shared with senior officials across multiple Saudi ministries and affiliated institutions.</li>
      </ul>
    </div>
  </div>

  <div class="exp-section-divider">
    <span class="exp-section-label">Additional Research &amp; Analysis</span>
  </div>

  <div class="exp-item">
    <div>
      <div class="exp-date">Feb — Jun 2021</div>
      <div class="exp-org">Kugler Economic Associates</div>
    </div>
    <div>
      <div class="exp-title">Economic Analyst</div>
      <div class="exp-loc">Bethesda, MD</div>
      <ul class="exp-bullets">
        <li>Supported Prof. Adriana Kugler (Principal Investigator) in analyzing wage and employment trends among essential workers during COVID-19, running advanced regression models in STATA on large longitudinal datasets.</li>
        <li>Developed reproducible statistical code and codebooks for peer-reviewed research; presented findings in policy memos and presentations to senior leadership.</li>
      </ul>
    </div>
  </div>

  <div class="exp-item">
    <div>
      <div class="exp-date">Jul — Oct 2020<br>May 2017 — Jul 2018</div>
      <div class="exp-org">Georgetown University</div>
    </div>
    <div>
      <div class="exp-title">Research Fellow &amp; Teaching Assistant</div>
      <div class="exp-loc">Washington, DC</div>
      <ul class="exp-bullets">
        <li>Research Fellow: co-managed a 500-participant labor market survey under a Georgetown–Harvard Kennedy School collaboration; synthesized findings into policy briefs for government and academic partners in Saudi Arabia.</li>
        <li>Teaching Assistant: supported instruction in Quantitative Methods III — Advanced Regression and Program Evaluation Methods — advising 46 graduate students on STATA-based econometric analysis and capstone evaluations.</li>
        <li>Georgetown awarded best capstone graduation project for equity-focused program evaluation work.</li>
      </ul>
    </div>
  </div>

  <div class="exp-item">
    <div>
      <div class="exp-date">Sep — Dec 2019</div>
      <div class="exp-org">World Bank</div>
    </div>
    <div>
      <div class="exp-title">Data Analysis Intern — Doing Business 2020</div>
      <div class="exp-loc">Washington, DC</div>
      <ul class="exp-bullets">
        <li>Conducted descriptive and inferential analysis on international business regulation data for 200+ countries using STATA and R, contributing to the World Bank's Doing Business 2020 publication.</li>
        <li>Built outlier detection routines and cross-year validation checks; produced internal memos translating findings into policy-ready insights for project teams.</li>
      </ul>
    </div>
  </div>

</section>
""", unsafe_allow_html=True)

# ── Education ──────────────────────────────────────────────────────────────────
st.markdown("""
<section class="section section-alt">
  <div class="section-header">
    <span class="section-num">02</span>
    <span class="section-title">Education</span>
  </div>

  <div class="exp-item">
    <div>
      <div class="exp-date">2021 — 2022</div>
      <div class="exp-org">George Washington University</div>
    </div>
    <div>
      <div class="exp-title">Doctor of Philosophy — Public Policy and Public Administration</div>
      <div class="exp-loc">Trachtenberg School · Washington, DC</div>
      <ul class="exp-bullets">
        <li>Concentration: Poverty and Inequality. Coursework in quantitative and qualitative research methods.</li>
      </ul>
    </div>
  </div>

  <div class="exp-item">
    <div>
      <div class="exp-date">2018 — 2020</div>
      <div class="exp-org">Georgetown University</div>
    </div>
    <div>
      <div class="exp-title">Master of Public Policy</div>
      <div class="exp-loc">McCourt School of Public Policy · Washington, DC · GPA: 3.60</div>
      <ul class="exp-bullets">
        <li>Awarded best capstone graduation project. Concentration in economic and labor policy.</li>
      </ul>
    </div>
  </div>

  <div class="exp-item">
    <div>
      <div class="exp-date">2012 — 2015</div>
      <div class="exp-org">University of Manchester</div>
    </div>
    <div>
      <div class="exp-title">Bachelor of Arts (Honours) — Politics, Philosophy &amp; Economics</div>
      <div class="exp-loc">Manchester, United Kingdom</div>
    </div>
  </div>

</section>
""", unsafe_allow_html=True)

# ── Skills ─────────────────────────────────────────────────────────────────────
st.markdown("""
<section class="section">
  <div class="section-header">
    <span class="section-num">03</span>
    <span class="section-title">Expertise &amp; Tools</span>
  </div>
  <div class="skills-grid">
    <div class="skill-card">
      <div class="skill-cat">Research Methods</div>
      <div class="skill-items">Quantitative &amp; qualitative design<br>Mixed-methods analysis<br>Regression modeling (OLS, Oaxaca-Blinder)<br>Randomized Controlled Trials<br>Survey &amp; questionnaire design<br>Field research operations</div>
    </div>
    <div class="skill-card">
      <div class="skill-cat">Data &amp; Technology</div>
      <div class="skill-items">STATA · R · Python<br>Tableau · Flourish · Qualtrics<br>Smartsheet · Office Suite<br>Dashboard development<br>Automated reporting pipelines<br>Outcome tracking systems</div>
    </div>
    <div class="skill-card">
      <div class="skill-cat">Policy &amp; Programs</div>
      <div class="skill-items">Workforce development<br>Education policy<br>Labor market analysis<br>Gender equity &amp; inclusion<br>Grant coordination<br>Compliance reporting</div>
    </div>
    <div class="skill-card">
      <div class="skill-cat">Communication</div>
      <div class="skill-items">Policy briefs &amp; memos<br>Executive briefings<br>Analytical reports<br>Stakeholder presentations<br>Staff training &amp; capacity building<br>Cross-agency coordination</div>
    </div>
    <div class="skill-card">
      <div class="skill-cat">Web Development</div>
      <div class="skill-items">Website design &amp; development<br>Wix · Squarespace · WordPress<br>Streamlit application development<br>Interactive dashboards for web<br>Site deployment &amp; management<br>Web-based reporting systems</div>
    </div>
    <div class="skill-card">
      <div class="skill-cat">International &amp; Languages</div>
      <div class="skill-items">United States · United Kingdom · Saudi Arabia<br>English — Fluent<br>Arabic — Native<br>MIT J-PAL Research Methods<br>CFA Level I</div>
    </div>
  </div>
</section>
""", unsafe_allow_html=True)

# ── Selected Work ──────────────────────────────────────────────────────────────
st.markdown('<div id="selected-work"></div>', unsafe_allow_html=True)
st.markdown("""
<section class="section">
  <div class="section-header">
    <span class="section-num">04</span>
    <span class="section-title">Selected Work</span>
  </div>
  <div class="work-grid">
    <div class="work-card">
      <div class="work-overline">01 · Gender Equity Research</div>
      <h3 class="work-title">Takafu Equal Opportunity Index</h3>
      <div class="work-meta">Gender Parity Index &nbsp;·&nbsp; Saudi Arabia &nbsp;·&nbsp; 2022</div>
      <div class="work-finding">
        <span class="work-finding-label">Key finding</span>
        <span class="work-finding-text">46% economic opportunity gap between men and women across Saudi Arabia's private sector, measured across 7.8 million GOSI employees.</span>
      </div>
      <a href="/takafu" target="_self" class="btn-outline work-link">Read case study →</a>
    </div>
    <div class="work-placeholder">More case studies coming soon</div>
  </div>
</section>
""", unsafe_allow_html=True)

# ── Dashboard ──────────────────────────────────────────────────────────────────
st.markdown('<div id="dashboard"></div>', unsafe_allow_html=True)
st.markdown("""
<section class="section">
  <div class="section-header">
    <span class="section-num">05</span>
    <span class="section-title">DMV Federal Workforce Impact — Interactive Dashboard</span>
  </div>
  <p class="dash-intro">
    A data lens on how federal workforce reductions have reshaped the DC–Maryland–Virginia regional economy.
    This dashboard reflects the kind of analytical work I build for agency and nonprofit clients —
    translating labor market and housing data into clear, decision-ready insights. Use the filters to explore each dimension.
  </p>
""", unsafe_allow_html=True)

# Live indicator strip
st.markdown("""
<div class="live-bar">
  <div class="live-cell">
    <div class="live-period"><span class="pulse-dot"></span>Mar 2026 — DC City (seas. adj.)</div>
    <div class="live-val danger">6.3%</div>
    <div class="live-lbl">Unemployment Rate</div>
    <div class="live-delta delta-bad">▲ +1.2 pts vs. Mar 2025</div>
  </div>
  <div class="live-cell">
    <div class="live-period"><span class="pulse-dot"></span>Feb 2025 → Feb 2026</div>
    <div class="live-val danger">−63,100</div>
    <div class="live-lbl">Federal Jobs Lost, DMV Region</div>
    <div class="live-delta delta-bad">▼ −14.2% of DMV federal workforce</div>
  </div>
  <div class="live-cell">
    <div class="live-period"><span class="pulse-dot"></span>2025 Annual Ranking</div>
    <div class="live-val">#1</div>
    <div class="live-lbl">Home Listing Surge, US Metros</div>
    <div class="live-delta" style="color:rgba(28,28,28,0.6);font-family:'DM Mono',monospace;font-size:0.75rem;">Largest inventory jump in the country</div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("</section>", unsafe_allow_html=True)

# ── Chart controls ─────────────────────────────────────────────────────────────
with st.container():
    st.markdown('<div style="padding: 0 4rem 4rem;">', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2, 2, 4])
    with col1:
        panel = st.selectbox(
            "Select Panel",
            ["Unemployment Trend", "Sector Job Losses", "Housing Squeeze"],
            label_visibility="visible"
        )
    with col2:
        if panel == "Unemployment Trend":
            show_nat = st.checkbox("Show national baseline", value=True)
        elif panel == "Sector Job Losses":
            cat_filter = st.selectbox(
                "Filter by category",
                ["All", "Direct — Federal", "Direct — Contracting", "Downstream"],
                label_visibility="visible"
            )
        elif panel == "Housing Squeeze":
            metric = st.selectbox(
                "Show metric",
                ["Both", "Listings only", "Price change only"],
                label_visibility="visible"
            )

    # ── Plotly shared theme ──────────────────────────────────────────────────
    BG      = "#f7f5f0"
    PLOT_BG = "#ffffff"
    GRID    = "rgba(28,28,28,0.10)"
    TICK    = "rgba(28,28,28,0.75)"
    GOLD    = "#9c6f3a"
    CRIMSON = "#a32020"
    NAVY    = "#2a4e7a"
    MUTED   = "rgba(28,28,28,0.55)"
    FONT    = "Jost, sans-serif"

    base_layout = dict(
        paper_bgcolor=BG,
        plot_bgcolor=PLOT_BG,
        font=dict(family=FONT, color=TICK, size=13),
        margin=dict(l=60, r=30, t=110, b=60),
        legend=dict(
            bgcolor="rgba(255,255,255,0.97)",
            bordercolor="rgba(28,28,28,0.20)",
            borderwidth=1,
            font=dict(size=15, color="#1c1c1c", family=FONT),
            orientation="h",
            yanchor="bottom",
            y=1.04,
            xanchor="left",
            x=0,
            itemsizing="constant",
            tracegroupgap=8,
        ),
        xaxis=dict(
            gridcolor=GRID, tickcolor=TICK, linecolor="rgba(28,28,28,0.15)",
            zeroline=False, tickfont=dict(size=13, color=TICK),
        ),
        yaxis=dict(
            gridcolor=GRID, tickcolor=TICK, linecolor="rgba(28,28,28,0.15)",
            zeroline=False, tickfont=dict(size=13, color=TICK),
        ),
        hoverlabel=dict(
            bgcolor="#ffffff",
            bordercolor=GOLD,
            font=dict(family=FONT, color="#1c1c1c", size=14)
        ),
    )

    # ── Panel 1: Unemployment Trend ──────────────────────────────────────────
    if panel == "Unemployment Trend":
        months = ["Jan 24","Feb 24","Mar 24","Apr 24","May 24","Jun 24",
                  "Jul 24","Aug 24","Sep 24","Oct 24","Nov 24","Dec 24",
                  "Jan 25","Feb 25","Mar 25","Apr 25","May 25","Jun 25",
                  "Jul 25","Aug 25","Sep 25","Oct 25","Nov 25","Dec 25",
                  "Jan 26","Feb 26"]
        dc_md   = [4.7,4.4,4.1,3.9,3.7,4.2,4.3,4.1,3.9,3.8,3.9,3.8,
                   4.7,4.9,5.1,5.3,5.5,5.7,5.8,5.6,5.3,5.2,5.1,5.1,5.6,5.7]
        dc_city = [5.9,5.6,5.3,5.0,4.8,5.5,5.7,5.4,5.1,5.0,5.2,5.1,
                   6.0,6.2,6.4,6.5,6.7,6.9,6.0,5.9,5.7,5.8,5.9,6.7,6.7,6.5]
        national= [3.7,3.9,3.8,3.9,4.0,4.1,4.3,4.2,4.1,4.1,4.2,4.2,
                   4.0,4.1,4.2,4.2,4.2,4.1,4.3,4.2,4.1,4.2,4.1,4.2,4.7,4.5]

        fig = go.Figure()
        fig.add_vrect(x0="Jan 25", x1="Feb 26",
                      fillcolor="rgba(163,32,32,0.05)", line_width=0)
        fig.add_annotation(
            xref="x", yref="paper",
            x="Jun 24", y=0.97,
            text="Pre-DOGE period",
            showarrow=False,
            font=dict(size=16, color="rgba(28,28,28,0.55)", family=FONT),
            xanchor="center",
            yanchor="top",
        )
        fig.add_trace(go.Scatter(
            x=months, y=dc_city, name="DC City (seas. adj.)",
            line=dict(color=CRIMSON, width=3),
            mode="lines+markers", marker=dict(size=6),
            hovertemplate="<b>DC City</b>  %{x}: <b>%{y:.1f}%</b><extra></extra>"
        ))
        fig.add_trace(go.Scatter(
            x=months, y=dc_md, name="DC–MD Metro Division",
            line=dict(color=GOLD, width=3),
            mode="lines+markers", marker=dict(size=6),
            hovertemplate="<b>DC–MD Metro</b>  %{x}: <b>%{y:.1f}%</b><extra></extra>"
        ))
        if show_nat:
            fig.add_trace(go.Scatter(
                x=months, y=national, name="National",
                line=dict(color="#555555", width=2, dash="dot"),
                mode="lines",
                hovertemplate="<b>National</b>  %{x}: <b>%{y:.1f}%</b><extra></extra>"
            ))
        fig.add_annotation(
            x="Jul 25", y=6.0,
            text="DC leads US<br>unemployment",
            showarrow=True, arrowhead=2, arrowwidth=1.5, arrowcolor=CRIMSON,
            font=dict(size=12, color=CRIMSON, family=FONT),
            ax=65, ay=-80,
            bgcolor="rgba(255,255,255,0.94)",
            bordercolor=CRIMSON,
            borderwidth=1,
            borderpad=6,
        )

        layout = base_layout.copy()
        layout.update(dict(
            title=dict(text="DMV Unemployment Rate vs. National — Jan 2024 to Feb 2026",
                       font=dict(size=17, color="#1c1c1c", family=FONT), x=0.5, xanchor="center", y=0.97),
            yaxis=dict(**base_layout["yaxis"], ticksuffix="%",
                       title=dict(text="Unemployment Rate", font=dict(size=14, color=TICK))),
            height=520,
            margin=dict(l=60, r=90, t=110, b=60),
        ))
        fig.update_layout(**layout)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('<p style="font-size:0.78rem;color:rgba(28,28,28,0.45);font-family:\'DM Mono\',monospace;letter-spacing:0.05em;padding:0 3.5rem 0.5rem;">Source: Bureau of Labor Statistics, Local Area Unemployment Statistics (LAUS), 2024–2026.</p>', unsafe_allow_html=True)

    # ── Panel 2: Sector Job Losses ───────────────────────────────────────────
    elif panel == "Sector Job Losses":
        sectors = [
            ("Federal government",           53800, "Direct — Federal"),
            ("Federal contracting",           18000, "Direct — Contracting"),
            ("Professional & business svcs",   9400, "Direct — Contracting"),
            ("Nonprofit / grant-funded",        6200, "Downstream"),
            ("Tourism & hospitality",           3600, "Downstream"),
            ("Hospitality & food service",      4800, "Downstream"),
            ("Retail trade",                    3100, "Downstream"),
            ("Transportation & utilities",      2200, "Downstream"),
            ("State & local government",        2400, "Downstream"),
            ("Real estate & rental",            1800, "Downstream"),
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
            x=df["Jobs Lost"], y=df["Sector"],
            orientation="h",
            marker=dict(color=colors, line=dict(width=0)),
            customdata=df["Category"],
            hovertemplate="<b>%{y}</b><br>Jobs lost: <b>%{x:,}</b><br>%{customdata}<extra></extra>",
            text=df["Jobs Lost"].apply(lambda x: f"{x:,}"),
            textposition="outside",
            textfont=dict(color="#1c1c1c", size=13),
            showlegend=False,
        ))
        # Dummy traces so legend appears above chart (always show all 3 categories)
        for cat, color in color_map.items():
            fig.add_trace(go.Bar(
                x=[None], y=[None], name=cat,
                marker=dict(color=color),
                orientation="h", showlegend=True,
            ))
        layout = base_layout.copy()
        layout.update(dict(
            title=dict(text="DMV Job Losses by Sector — 2025 Year-over-Year",
                       font=dict(size=17, color="#1c1c1c", family=FONT), x=0.5, xanchor="center", y=0.97),
            xaxis=dict(**base_layout["xaxis"],
                       title=dict(text="Jobs Lost", font=dict(size=14, color=TICK)),
                       tickformat=",",
                       range=[0, 72000]),
            height=520,
            showlegend=True,
            legend=dict(
                bgcolor="rgba(255,255,255,0.97)",
                bordercolor="rgba(28,28,28,0.20)",
                borderwidth=1,
                font=dict(size=15, color="#1c1c1c", family=FONT),
                orientation="h",
                yanchor="bottom",
                y=1.04,
                xanchor="left",
                x=0.16,
            ),
            margin=dict(l=200, r=90, t=130, b=60),
        ))
        fig.update_layout(**layout)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('<p style="font-size:0.78rem;color:rgba(28,28,28,0.45);font-family:\'DM Mono\',monospace;letter-spacing:0.05em;padding:0 3.5rem 0.5rem;">Source: BLS Quarterly Census of Employment and Wages (QCEW); Moody\'s Analytics regional estimates, 2025.</p>', unsafe_allow_html=True)

    # ── Panel 3: Housing Squeeze ─────────────────────────────────────────────
    elif panel == "Housing Squeeze":
        months = ["Jan 24","Feb 24","Mar 24","Apr 24","May 24","Jun 24",
                  "Jul 24","Aug 24","Sep 24","Oct 24","Nov 24","Dec 24",
                  "Jan 25","Feb 25","Mar 25","Apr 25","May 25","Jun 25",
                  "Jul 25","Aug 25","Sep 25","Oct 25","Nov 25","Dec 25",
                  "Jan 26","Feb 26"]
        listings  = [5820,5640,6100,6890,7420,7810,7650,7200,6540,5980,5510,4980,
                     5230,5640,6820,8100,9350,10200,10800,10400,9800,9200,8100,7200,7600,8100]
        price_chg = [5.1,5.4,5.8,6.2,6.0,5.5,4.8,4.2,3.9,3.5,3.1,2.8,
                     2.5,2.1,1.4,0.8,0.2,-0.5,-1.2,-1.8,-2.1,-2.4,-2.0,-1.6,-1.4,-1.1]

        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_vrect(x0="Jan 25", x1="Feb 26",
                      fillcolor="rgba(163,32,32,0.05)", line_width=0)

        if metric in ["Both", "Listings only"]:
            bar_colors = [GOLD if i >= 12 else "rgba(156,111,58,0.35)" for i in range(len(months))]
            fig.add_trace(go.Bar(
                x=months, y=listings, name="Active Listings",
                marker=dict(color=bar_colors, line=dict(width=0)),
                hovertemplate="<b>Active Listings</b>  %{x}: <b>%{y:,}</b><extra></extra>",
            ), secondary_y=False)

        if metric in ["Both", "Price change only"]:
            pc_colors = [CRIMSON if v < 0 else "#2d6e42" for v in price_chg]
            fig.add_trace(go.Scatter(
                x=months, y=price_chg, name="Median Price Change YoY %",
                line=dict(color=CRIMSON, width=3),
                mode="lines+markers",
                marker=dict(size=7, color=pc_colors),
                hovertemplate="<b>Price Change</b>  %{x}: <b>%{y:+.1f}%</b><extra></extra>",
            ), secondary_y=True)

        fig.add_hline(y=0, secondary_y=True,
                      line=dict(color="rgba(28,28,28,0.30)", width=1.5, dash="dot"))

        # Annotation only makes sense when listings bars are visible
        if metric in ["Both", "Listings only"]:
            fig.add_annotation(x="Jul 25", y=10800,
                               text="Listings peak +41% YoY",
                               showarrow=True, arrowhead=2, arrowwidth=1.5,
                               arrowcolor=GOLD,
                               font=dict(size=12, color="#7a5520", family=FONT),
                               ax=55, ay=-50,
                               bgcolor="rgba(255,255,255,0.92)",
                               bordercolor=GOLD, borderwidth=1, borderpad=5)

        # Primary axis: show for listings, hide when price-change-only
        if metric == "Price change only":
            primary_yaxis = dict(visible=False, showgrid=False)
        else:
            primary_yaxis = dict(**base_layout["yaxis"],
                                 title=dict(text="Active Listings",
                                            font=dict(size=14, color=TICK)),
                                 tickformat=",")

        layout = base_layout.copy()
        layout.update(dict(
            title=dict(text="DMV Housing: Listing Surge vs. Price Pressure — 2024 to 2026",
                       font=dict(size=17, color="#1c1c1c", family=FONT), x=0.5, xanchor="center", y=0.97),
            yaxis=primary_yaxis,
            yaxis2=dict(
                title=dict(text="Price Change YoY %", font=dict(size=14, color=TICK)),
                ticksuffix="%",
                gridcolor=GRID,
                tickfont=dict(size=13, color=TICK),
                zeroline=True,
                zerolinecolor="rgba(28,28,28,0.20)",
                zerolinewidth=1,
                side="right",
                showline=True,
                linecolor="rgba(28,28,28,0.15)",
            ),
            height=520,
            barmode="overlay",
            margin=dict(l=60, r=90, t=110, b=60),
        ))
        fig.update_layout(**layout)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('<p style="font-size:0.78rem;color:rgba(28,28,28,0.45);font-family:\'DM Mono\',monospace;letter-spacing:0.05em;padding:0 3.5rem 0.5rem;">Source: Realtor.com Market Reports; Zillow Research; DC Office of Planning (DMPED), 2024–2026.</p>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ── Services ───────────────────────────────────────────────────────────────────
st.markdown('<div id="services"></div>', unsafe_allow_html=True)
st.markdown("""
<section class="section section-alt">
  <div class="section-header">
    <span class="section-num">06</span>
    <span class="section-title">Services</span>
  </div>
  <div class="skills-grid">
    <div class="skill-card">
      <div class="skill-cat">01</div>
      <div style="font-family:'Cormorant Garamond',serif;font-size:1.2rem;font-weight:400;color:#1c1c1c;margin-bottom:0.8rem;">Program Evaluation &amp; Impact Assessment</div>
      <div class="skill-items">Design and execute mixed-methods evaluations from logic model development through data collection, analysis, and final reporting — for government, nonprofit, and foundation clients.</div>
    </div>
    <div class="skill-card">
      <div class="skill-cat">02</div>
      <div style="font-family:'Cormorant Garamond',serif;font-size:1.2rem;font-weight:400;color:#1c1c1c;margin-bottom:0.8rem;">Data Strategy &amp; Dashboard Design</div>
      <div class="skill-items">Build internal and client-facing dashboards in Tableau, Flourish, and R that translate raw program data into clear performance insights. Includes automated pipelines and staff training.</div>
    </div>
    <div class="skill-card">
      <div class="skill-cat">03</div>
      <div style="font-family:'Cormorant Garamond',serif;font-size:1.2rem;font-weight:400;color:#1c1c1c;margin-bottom:0.8rem;">Policy Research &amp; Strategic Reporting</div>
      <div class="skill-items">Produce analytical memos, policy briefs, and grant reports that synthesize evidence for decision-makers. Experienced with DC DOES, OSSE, and federal workforce program frameworks.</div>
    </div>
    <div class="skill-card">
      <div class="skill-cat">04</div>
      <div style="font-family:'Cormorant Garamond',serif;font-size:1.2rem;font-weight:400;color:#1c1c1c;margin-bottom:0.8rem;">Workforce &amp; Education Program Support</div>
      <div class="skill-items">Support program design and operations for workforce and education initiatives, including participant tracking, employer partnerships, and equity-focused outcome systems.</div>
    </div>
    <div class="skill-card">
      <div class="skill-cat">05</div>
      <div style="font-family:'Cormorant Garamond',serif;font-size:1.2rem;font-weight:400;color:#1c1c1c;margin-bottom:0.8rem;">Grant Coordination &amp; Compliance Reporting</div>
      <div class="skill-items">Manage data collection, performance measurement, and narrative reporting for federally-funded programs including WIOA and Title I workforce grants.</div>
    </div>
    <div class="skill-card">
      <div class="skill-cat">06</div>
      <div style="font-family:'Cormorant Garamond',serif;font-size:1.2rem;font-weight:400;color:#1c1c1c;margin-bottom:0.8rem;">Field Research Operations</div>
      <div class="skill-items">Design and manage large-scale surveys and field data collection across labor market, education, and social protection studies — from Saudi Arabia's private sector to DC youth programs.</div>
    </div>
    <div class="skill-card-featured">
      <div>
        <div class="skill-cat">07</div>
        <div style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;font-weight:400;color:#1c1c1c;margin-bottom:0.5rem;line-height:1.3;">Website Development<br>&amp; Management</div>
      </div>
      <div class="skill-items">Design, build, and maintain professional websites and web-based data tools — from organizational landing pages and portfolio sites to fully interactive dashboards and automated reporting platforms.
        Built using Wix, Squarespace, WordPress, and custom Python/Streamlit applications. Ongoing management includes content updates, performance monitoring, and continuous improvement based on site analytics.</div>
    </div>
  </div>
</section>
""", unsafe_allow_html=True)

# ── Contact ────────────────────────────────────────────────────────────────────
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.markdown(f"""
<section class="section">
  <div class="section-header">
    <span class="section-num">07</span>
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
      <div class="contact-cta-row">
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
           style="color:rgba(28,28,28,0.85);text-decoration:none;">linkedin.com/in/yaser-alhusaini-43330b281</a>
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
  <span class="footer-text">MPP Georgetown · BA Manchester · MIT J-PAL · CFA Level I</span>
</footer>
""", unsafe_allow_html=True)
