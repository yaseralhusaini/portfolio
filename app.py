import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import base64
import os

st.set_page_config(
    page_title="Yaser Alhusaini · Policy & Data",
    page_icon="◆",
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
report_b64 = get_file_b64("takafu_report.pdf")
brief_b64  = get_file_b64("early_retirement_brief.pdf")
aspire_b64 = get_file_b64("aspire_report.pdf")

# ── Page routing via session state (avoids Streamlit Cloud routing issues) ──
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Allow HTML links like <a href="?page=takafu"> to trigger navigation
_qp = st.query_params
if _qp.get("page") in ("takafu", "georgetown", "aspire"):
    st.session_state.page = _qp.get("page")
    st.query_params.clear()
    st.rerun()

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

/* ── Experience case study button (HTML anchor styled as outline btn) ── */
.btn-exp-cs {
    display: inline-block;
    margin-top: 1.4rem;
    background: transparent !important;
    color: #6b4718 !important;
    border: 2px solid #9c6f3a !important;
    font-family: 'Jost', sans-serif !important;
    font-size: 0.78rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
    padding: 0.55rem 1.2rem !important;
    text-decoration: none !important;
    transition: background 0.2s, color 0.2s;
    white-space: nowrap;
}
.btn-exp-cs:hover {
    background: #9c6f3a !important;
    color: #f7f5f0 !important;
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
    grid-template-columns: repeat(3, 1fr);
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
    transition: background 0.2s, box-shadow 0.2s;
}
.work-card:hover { background: #efece5; }
a#takafu-work-card {
    text-decoration: none !important;
    color: inherit !important;
    cursor: pointer;
    position: relative;
    border-top: 3px solid transparent;
    transition: background 0.2s, border-top-color 0.2s, box-shadow 0.2s;
    display: flex;
    flex-direction: column;
    gap: 1.1rem;
}
a#takafu-work-card:hover {
    background: #efece5;
    border-top-color: #9c6f3a;
    box-shadow: 0 4px 20px rgba(156,111,58,0.10);
}
a#takafu-work-card::after {
    content: '→';
    position: absolute;
    bottom: 1.5rem;
    right: 1.8rem;
    font-family: 'Jost', sans-serif;
    font-size: 1.1rem;
    color: rgba(156,111,58,0.45);
    transition: color 0.2s, transform 0.2s;
}
a#takafu-work-card:hover::after {
    color: #9c6f3a;
    transform: translateX(4px);
}
a#georgetown-work-card {
    text-decoration: none !important;
    color: inherit !important;
    cursor: pointer;
    position: relative;
    border-top: 3px solid transparent;
    transition: background 0.2s, border-top-color 0.2s, box-shadow 0.2s;
    display: flex;
    flex-direction: column;
    gap: 1.1rem;
}
a#georgetown-work-card:hover {
    background: #efece5;
    border-top-color: #9c6f3a;
    box-shadow: 0 4px 20px rgba(156,111,58,0.10);
}
a#georgetown-work-card::after {
    content: '→';
    position: absolute;
    bottom: 1.5rem;
    right: 1.8rem;
    font-family: 'Jost', sans-serif;
    font-size: 1.1rem;
    color: rgba(156,111,58,0.45);
    transition: color 0.2s, transform 0.2s;
}
a#georgetown-work-card:hover::after {
    color: #9c6f3a;
    transform: translateX(4px);
}
a#georgetown-work-card:hover .work-pill {
    background: #9c6f3a;
    color: #f7f5f0 !important;
}
a#aspire-work-card {
    text-decoration: none !important;
    color: inherit !important;
    cursor: pointer;
    position: relative;
    border-top: 3px solid transparent;
    transition: background 0.2s, border-top-color 0.2s, box-shadow 0.2s;
    display: flex;
    flex-direction: column;
    gap: 1.1rem;
}
a#aspire-work-card:hover {
    background: #efece5;
    border-top-color: #9c6f3a;
    box-shadow: 0 4px 20px rgba(156,111,58,0.10);
}
a#aspire-work-card::after {
    content: '→';
    position: absolute;
    bottom: 1.5rem;
    right: 1.8rem;
    font-family: 'Jost', sans-serif;
    font-size: 1.1rem;
    color: rgba(156,111,58,0.45);
    transition: color 0.2s, transform 0.2s;
}
a#aspire-work-card:hover::after {
    color: #9c6f3a;
    transform: translateX(4px);
}
a#aspire-work-card:hover .work-pill {
    background: #9c6f3a;
    color: #f7f5f0 !important;
}
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

.work-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    margin-top: 0.6rem;
    padding: 0.38rem 0.9rem;
    background: rgba(156,111,58,0.08);
    border: 1.5px solid #9c6f3a;
    color: #6b4718 !important;
    font-family: 'Jost', sans-serif;
    font-size: 0.76rem;
    font-weight: 500;
    letter-spacing: 0.11em;
    text-transform: uppercase;
    transition: background 0.2s, color 0.2s;
}
a#takafu-work-card:hover .work-pill {
    background: #9c6f3a;
    color: #f7f5f0 !important;
}
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

/* ── Streamlit buttons styled as btn-outline ── */
div[data-testid="stButton"] > button {
    background: transparent !important;
    color: #6b4718 !important;
    border: 2px solid #9c6f3a !important;
    border-radius: 0 !important;
    font-family: 'Jost', sans-serif !important;
    font-size: 0.9rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
    padding: 0.7rem 2rem !important;
    box-shadow: none !important;
    transition: border-color 0.2s, background 0.2s !important;
}
div[data-testid="stButton"] > button:hover,
div[data-testid="stButton"] > button:focus {
    border-color: #6b4718 !important;
    background: rgba(107,71,24,0.07) !important;
    color: #6b4718 !important;
    box-shadow: none !important;
}

/* ── Case study page ── */
.cs-header { padding: 4rem 4rem 3rem; border-bottom: 1px solid rgba(26,26,26,0.08); max-width: 960px; }
.cs-overline { font-family:'DM Mono',monospace; font-size:0.82rem; letter-spacing:0.22em; text-transform:uppercase; color:#9c6f3a; margin-bottom:1.6rem; }
.cs-title { font-family:'Cormorant Garamond',serif; font-size:clamp(2.8rem,5vw,4.8rem); font-weight:300; line-height:1.05; color:#1c1c1c !important; margin-bottom:1.8rem; }
.cs-line { width:60px; height:2px; background:#9c6f3a; margin-bottom:2rem; }
.cs-meta-row { display:flex; gap:2.5rem; flex-wrap:wrap; }
.cs-meta-item { display:flex; flex-direction:column; gap:0.3rem; }
.cs-meta-label { font-family:'DM Mono',monospace; font-size:0.72rem; letter-spacing:0.18em; text-transform:uppercase; color:rgba(28,28,28,0.45); }
.cs-meta-value { font-size:1rem; font-weight:300; color:rgba(28,28,28,0.80); }
.cs-body { padding: 0 4rem; max-width: 960px; }
.cs-section { padding:4rem 0; border-bottom:1px solid rgba(26,26,26,0.07); display:grid; grid-template-columns:180px 1fr; gap:3.5rem; }
.cs-section:last-child { border-bottom:none; }
.cs-section-label { font-family:'DM Mono',monospace; font-size:0.78rem; letter-spacing:0.18em; text-transform:uppercase; color:rgba(28,28,28,0.42); padding-top:0.35rem; line-height:1.6; }
.cs-section-label span { display:block; font-size:1.6rem; font-family:'Cormorant Garamond',serif; color:rgba(28,28,28,0.12); letter-spacing:0; font-weight:300; margin-bottom:0.4rem; }
.cs-content h3 { font-family:'Cormorant Garamond',serif; font-size:1.7rem; font-weight:400; color:#1c1c1c !important; margin-bottom:1.2rem; line-height:1.2; }
.cs-content p { font-size:1.15rem; font-weight:300; line-height:1.85; color:rgba(28,28,28,0.82); margin-bottom:1.2rem; }
.cs-content p:last-child { margin-bottom:0; }
.cs-bullets { list-style:none; padding:0; margin:0; }
.cs-bullets li { font-size:1.15rem; font-weight:300; color:rgba(28,28,28,0.82); line-height:1.85; padding-left:1.4rem; position:relative; margin-bottom:0.9rem; }
.cs-bullets li::before { content:'—'; position:absolute; left:0; color:#9c6f3a; }
.cs-bullets li strong { font-weight:500; color:#1c1c1c; }
.findings-grid { display:grid; grid-template-columns:repeat(2,1fr); gap:1px; background:rgba(26,26,26,0.08); border:1px solid rgba(26,26,26,0.08); margin-top:0.5rem; }
.finding-card { background:#f7f5f0; padding:2rem 1.8rem; }
.finding-num { font-family:'Cormorant Garamond',serif; font-size:2.6rem; font-weight:300; color:#9c6f3a; line-height:1; margin-bottom:0.5rem; }
.finding-desc { font-size:1rem; font-weight:300; color:rgba(28,28,28,0.78); line-height:1.6; }
.cs-callout { background:#ede9e0; border-top:2px solid #9c6f3a; padding:2rem 2.2rem; margin-top:0.5rem; }
.cs-callout p { font-size:1.15rem; font-weight:300; line-height:1.85; color:rgba(28,28,28,0.82); margin:0; }
.cs-btn-row { padding: 2.5rem 4rem; display:flex; gap:1.2rem; flex-wrap:wrap; align-items:center; border-top:1px solid rgba(26,26,26,0.07); }

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

/* ── Mobile ────────────────────────────────────────────────────────────────── */
@media (max-width: 768px) {

  /* Nav */
  .nav-bar {
    padding: 1rem 1.4rem;
    flex-wrap: wrap;
    gap: 0.6rem;
  }
  .nav-links { display: none; }
  .nav-name { font-size: 1rem; }

  /* Hero */
  .hero-stats-row {
    flex-direction: column !important;
    padding: 2rem 1.4rem !important;
    gap: 2rem !important;
  }
  .hero-content { max-width: 100% !important; }
  .hero-title { font-size: clamp(2.4rem, 10vw, 3.5rem) !important; }
  .hero-desc { font-size: 1.05rem !important; }
  .hero-cta-row {
    flex-direction: column !important;
    align-items: flex-start !important;
    gap: 0.7rem !important;
  }
  .hero-cta-row a { width: 100%; text-align: center; }
  .stat-row { flex-direction: row; gap: 1rem; }
  .stats-col {
    flex-direction: row !important;
    flex-wrap: wrap !important;
    gap: 1.2rem 2rem !important;
    border-left: none !important;
    border-top: 1px solid rgba(26,26,26,0.10) !important;
    padding-left: 0 !important;
    padding-top: 1.8rem !important;
  }
  .stat-num { font-size: 2.4rem !important; }

  /* Sections */
  .section, .section-alt { padding: 2.5rem 1.4rem !important; }
  .section-title { font-size: 1.5rem !important; }
  .cs-header { padding: 2rem 1.4rem 1.8rem !important; }
  .cs-body { padding: 0 1.4rem !important; }
  .cs-title { font-size: clamp(2rem, 8vw, 3rem) !important; }
  .cs-section {
    grid-template-columns: 1fr !important;
    gap: 1rem !important;
    padding: 2.5rem 0 !important;
  }
  .cs-btn-row { padding: 2rem 1.4rem !important; flex-direction: column; }

  /* Experience */
  .exp-item {
    grid-template-columns: 1fr !important;
    gap: 0.4rem !important;
    padding: 2rem 0 !important;
  }
  .exp-date { font-size: 0.82rem !important; }
  .exp-org { font-size: 1.1rem !important; }
  .exp-title { font-size: 1.15rem !important; margin-top: 0.2rem !important; }
  .exp-bullets li { font-size: 1rem !important; }
  .btn-exp-cs { margin-top: 0.8rem !important; }

  /* Work grid */
  .work-grid { grid-template-columns: 1fr !important; }
  .work-title { font-size: 1.3rem !important; }

  /* Skills / services grid */
  .skills-grid { grid-template-columns: 1fr !important; }
  .skill-card-featured {
    grid-column: span 1 !important;
    grid-template-columns: 1fr !important;
  }

  /* Findings grid */
  .findings-grid { grid-template-columns: 1fr !important; }

  /* Contact */
  .contact-grid { grid-template-columns: 1fr !important; gap: 2rem !important; }
  .contact-headline { font-size: clamp(2rem, 8vw, 3rem) !important; }
  .contact-sub { font-size: 1.05rem !important; }
  .contact-cta-row { flex-direction: column !important; }
  .contact-cta-row a { width: 100% !important; text-align: center !important; }

  /* Dashboard — hide everything except header and mobile note */
  div[data-testid="stPlotlyChart"] { display: none !important; }
  div[data-testid="stHorizontalBlock"] { display: none !important; }
  div[data-testid="stColumn"] { display: none !important; }
  .live-bar { display: none !important; }
  .dash-desktop-only { display: none !important; }
  .dash-mobile-note { display: block !important; }
  .section-dashboard { padding-bottom: 2rem !important; }

  /* Prevent any element from causing horizontal scroll */
  body, .stApp, .block-container { overflow-x: hidden !important; }

  /* Footer */
  .site-footer {
    flex-direction: column !important;
    gap: 0.4rem !important;
    padding: 1.5rem 1.4rem !important;
    text-align: center !important;
  }

  /* Streamlit block container mobile padding */
  .block-container { padding: 0 !important; }
}
</style>
""", unsafe_allow_html=True)

# ── Takafu case study (session-state routed) ───────────────────────────────────
if st.session_state.page == 'takafu':
    st.iframe("""<script>
        function scrollUp() {
            var targets = [
                window.parent.document.querySelector('[data-testid="stAppViewContainer"]'),
                window.parent.document.querySelector('[data-testid="stMain"]'),
                window.parent.document.querySelector('.main'),
                window.parent.document.documentElement,
                window.parent.document.body
            ];
            targets.forEach(function(el) { if (el) { el.scrollTop = 0; } });
            window.parent.scrollTo(0, 0);
        }
        // Fire immediately, then again after Streamlit finishes re-rendering
        scrollUp();
        setTimeout(scrollUp, 150);
        setTimeout(scrollUp, 500);
    </script>""", height=1)
    report_href = f'data:application/pdf;base64,{report_b64}' if report_b64 else '#'
    st.markdown("""
<nav class="nav-bar">
  <div class="nav-name">Yaser Alhusaini</div>
  <div class="nav-links"><span style="font-family:'DM Mono',monospace;font-size:0.82rem;letter-spacing:0.14em;text-transform:uppercase;color:rgba(28,28,28,0.45);">Case Study — Takafu</span></div>
</nav>""", unsafe_allow_html=True)

    if st.button("← Back to Portfolio", key="cs_back_top"):
        st.session_state.page = 'home'
        st.rerun()

    st.markdown("""
<div class="cs-header">
  <div class="cs-overline">Case Study · 01</div>
  <h1 class="cs-title">Takafu Equal<br>Opportunity Index</h1>
  <div class="cs-line"></div>
  <div class="cs-meta-row">
    <div class="cs-meta-item"><span class="cs-meta-label">Client</span><span class="cs-meta-value">Alnahda Society · Alwathba Consultancy</span></div>
    <div class="cs-meta-item"><span class="cs-meta-label">Geography</span><span class="cs-meta-value">Saudi Arabia</span></div>
    <div class="cs-meta-item"><span class="cs-meta-label">Year</span><span class="cs-meta-value">2022</span></div>
    <div class="cs-meta-item"><span class="cs-meta-label">Domain</span><span class="cs-meta-value">Gender Equity · Labor Economics · Policy Research</span></div>
  </div>
</div>

<div class="cs-body">
  <div class="cs-section">
    <div class="cs-section-label"><span>01</span>Context</div>
    <div class="cs-content">
      <h3>Saudi Arabia's first private-sector gender parity index</h3>
      <p>Alnahda Society — founded in 1962, Saudi Arabia's oldest and largest women's empowerment nonprofit — commissioned the Takafu Equal Opportunity Index as part of a broader push to create a measurable, evidence-based framework for tracking gender parity in the Kingdom's private sector.</p>
      <p>The project arrived at a pivotal moment. Saudi Vision 2030 had set an ambitious target: raise women's labor force participation from 17% to 30% by the decade's end. Yet there was no systematic, data-driven benchmark against which companies or policymakers could assess progress. Takafu was designed to fill that gap — producing the first index of its kind in the Kingdom, with findings intended to inform both employer practice and national policy.</p>
      <p>The index measured gender equality across three dimensions: economic opportunity (hiring and participation), career development (advancement and retention), and compensation equity — drawing on both national administrative data and primary survey research.</p>
    </div>
  </div>
  <div class="cs-section">
    <div class="cs-section-label"><span>02</span>My Role</div>
    <div class="cs-content">
      <h3>End-to-end quantitative research, from administrative data to published findings</h3>
      <ul class="cs-bullets">
        <li><strong>Administrative data analysis</strong> — Analyzed a national GOSI (General Organization for Social Insurance) dataset covering over 7.8 million private sector employees. Ran advanced regression models to measure gender gaps in labor force participation, career progression, and compensation across industries and firm sizes.</li>
        <li><strong>Oaxaca-Blinder decomposition</strong> — Applied decomposition analysis to isolate the portion of the gender wage gap that could not be explained by observable factors such as education, tenure, industry, or firm size — a methodologically rigorous approach for quantifying structural discrimination in labor markets.</li>
        <li><strong>Dual survey design and analysis</strong> — Co-designed two complementary survey instruments: one targeting HR managers (firm-level practices), one targeting employees (individual-level experience). Collected and analyzed responses from 57 companies and 985 Saudi workers across Riyadh, Makkah, and the Eastern Province.</li>
        <li><strong>Policy synthesis</strong> — Synthesized quantitative findings and qualitative survey data into the published Takafu 2020 Executive Summary, with policy and employer recommendations cited by government stakeholders aligned to Saudi Vision 2030.</li>
      </ul>
    </div>
  </div>
  <div class="cs-section">
    <div class="cs-section-label"><span>03</span>Key Findings</div>
    <div class="cs-content">
      <h3>Four numbers that tell the story</h3>
      <div class="findings-grid">
        <div class="finding-card"><div class="finding-num">46%</div><div class="finding-desc">Overall economic opportunity gap between men and women across Saudi Arabia's private sector — capturing disparities in hiring, advancement, and pay.</div></div>
        <div class="finding-card"><div class="finding-num">7.8M</div><div class="finding-desc">Private sector employees in the GOSI administrative dataset analyzed — the most comprehensive labor market dataset available in the Kingdom.</div></div>
        <div class="finding-card"><div class="finding-num">57</div><div class="finding-desc">Companies surveyed alongside 985 individual workers across Riyadh, Makkah, and the Eastern Province — providing firm-level and worker-level perspectives on workplace equity.</div></div>
        <div class="finding-card"><div class="finding-num">∆</div><div class="finding-desc">Significant unexplained wage gap remained after controlling for education, industry, and firm size — pointing to structural barriers beyond human capital differences.</div></div>
      </div>
    </div>
  </div>
  <div class="cs-section">
    <div class="cs-section-label"><span>04</span>Relevance</div>
    <div class="cs-content">
      <h3>What this means for your project</h3>
      <div class="cs-callout">
        <p>Takafu represents the kind of work I bring to complex policy research engagements: the technical depth to handle large administrative datasets, the methodological precision to apply labor economics techniques like Oaxaca-Blinder decomposition, and the end-to-end capacity to move from survey design through published, decision-ready findings.</p>
        <p style="margin-top:1rem;">For clients working on gender equity, workforce analytics, program evaluation, or any initiative that requires translating raw data into credible, actionable policy insight — I bring the same combination of analytical rigor and stakeholder-facing clarity that shaped this project.</p>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

    st.markdown(f"""
<div class="cs-btn-row">
  <a href="{report_href}" download="Takafu_Executive_Summary.pdf" class="btn-gold">Download Executive Summary (PDF)</a>
</div>""", unsafe_allow_html=True)

    if st.button("← Back to Portfolio", key="cs_back_bottom"):
        st.session_state.page = 'home'
        st.rerun()

    st.markdown("""
<footer class="site-footer">
  <span class="footer-text">© 2025 Yaser Alhusaini — Policy · Data · Research</span>
  <span class="footer-text">Case Study · Takafu Equal Opportunity Index · Saudi Arabia</span>
</footer>""", unsafe_allow_html=True)
    st.stop()

# ── Georgetown / Early Retirement case study ───────────────────────────────────
if st.session_state.page == 'georgetown':
    st.iframe("""<script>
        function scrollUp() {
            var targets = [
                window.parent.document.querySelector('[data-testid="stAppViewContainer"]'),
                window.parent.document.querySelector('[data-testid="stMain"]'),
                window.parent.document.querySelector('.main'),
                window.parent.document.documentElement,
                window.parent.document.body
            ];
            targets.forEach(function(el) { if (el) { el.scrollTop = 0; } });
            window.parent.scrollTo(0, 0);
        }
        scrollUp();
        setTimeout(scrollUp, 150);
        setTimeout(scrollUp, 500);
    </script>""", height=1)
    brief_href = f'data:application/pdf;base64,{brief_b64}' if brief_b64 else '#'
    st.markdown("""
<nav class="nav-bar">
  <div class="nav-name">Yaser Alhusaini</div>
  <div class="nav-links"><span style="font-family:'DM Mono',monospace;font-size:0.82rem;letter-spacing:0.14em;text-transform:uppercase;color:rgba(28,28,28,0.45);">Case Study — Early Retirement</span></div>
</nav>""", unsafe_allow_html=True)

    if st.button("← Back to Portfolio", key="gr_back_top"):
        st.session_state.page = 'home'
        st.rerun()

    st.markdown("""
<div class="cs-header">
  <div class="cs-overline">Case Study · 02</div>
  <h1 class="cs-title">Early Retirement<br>in the Private Sector</h1>
  <div class="cs-line"></div>
  <div class="cs-meta-row">
    <div class="cs-meta-item"><span class="cs-meta-label">Partners</span><span class="cs-meta-value">Georgetown University · Harvard Kennedy School EPoD</span></div>
    <div class="cs-meta-item"><span class="cs-meta-label">Geography</span><span class="cs-meta-value">Saudi Arabia</span></div>
    <div class="cs-meta-item"><span class="cs-meta-label">Years</span><span class="cs-meta-value">2017 – 2018 · 2020</span></div>
    <div class="cs-meta-item"><span class="cs-meta-label">Domain</span><span class="cs-meta-value">Labor Economics · Pension Policy · Behavioral Economics</span></div>
  </div>
</div>

<div class="cs-body">
  <div class="cs-section">
    <div class="cs-section-label"><span>01</span>Context</div>
    <div class="cs-content">
      <h3>Why are so many Saudi private sector workers retiring too early?</h3>
      <p>Over a five-year period, more than 57% of all private sector retirees in Saudi Arabia retired early — and among workers who were eligible for early retirement, the rate climbed to 80%. The economic stakes were significant: workers were leaving lifetime pension wealth on the table, and the Kingdom's labor market was losing experienced workers years before a financially optimal exit.</p>
      <p>This research — conducted jointly by Georgetown University's McCourt School of Public Policy under Prof. Nada Eissa and Harvard Kennedy School's Evidence for Policy Design (EPoD) unit — set out to answer a foundational question: were Saudi private sector workers responding rationally to the incentive structure embedded in the pension system, or were uninformed decisions costing them long-term financial security?</p>
      <p>The answer turned out to be both: the pension system was structurally incentivizing early exit, and many workers lacked full information about how their lifetime benefits would change with additional years of work.</p>
    </div>
  </div>
  <div class="cs-section">
    <div class="cs-section-label"><span>02</span>My Role</div>
    <div class="cs-content">
      <h3>Survey design, econometric modeling, and policy synthesis</h3>
      <ul class="cs-bullets">
        <li><strong>Survey design and administration</strong> — Co-designed and administered a 500-participant labor market survey on early retirement decision-making, covering worker demographics, wage histories, retirement intentions, and awareness of pension rules. Managed field coordination and ensured data quality across the full collection cycle.</li>
        <li><strong>GOSI administrative data analysis</strong> — Analyzed national administrative data from Saudi Arabia's General Organization for Social Insurance (GOSI), covering multiple years of private sector retirement patterns across hundreds of thousands of workers.</li>
        <li><strong>Implicit tax modeling</strong> — Modeled the implicit tax structure embedded in the Saudi pension system — calculating at each retirement age how an additional year of work would change a worker's lifetime pension wealth, and identifying the age at which total benefits are maximized.</li>
        <li><strong>Econometric analysis</strong> — Applied regression models to estimate the behavioral drivers of early retirement, controlling for education, wage trajectories, sector, and predicted lifetime pension wealth. Classified retirees into four behavioral groups based on wage patterns and retirement timing.</li>
        <li><strong>Policy brief synthesis</strong> — Synthesized findings into a published policy brief under the Harvard Kennedy School EPoD banner, with recommendations submitted to the Saudi Ministry of Labor and Social Development.</li>
      </ul>
    </div>
  </div>
  <div class="cs-section">
    <div class="cs-section-label"><span>03</span>Key Findings</div>
    <div class="cs-content">
      <h3>Incentives shape behavior — but information gaps make it worse</h3>
      <div class="findings-grid">
        <div class="finding-card"><div class="finding-num">57%</div><div class="finding-desc">Of all private sector retirees over a five-year period retired before the normal retirement age — a strikingly high early retirement rate.</div></div>
        <div class="finding-card"><div class="finding-num">80%</div><div class="finding-desc">Of workers eligible for early retirement took the early retirement option, suggesting strong responsiveness to the incentive structure.</div></div>
        <div class="finding-card"><div class="finding-num">+20%</div><div class="finding-desc">Increase in the probability of retiring in a given year for every 50% increase in the implicit tax rate — confirming that workers respond to pension incentives.</div></div>
        <div class="finding-card"><div class="finding-num">Age 55</div><div class="finding-desc">The age at which lifetime pension wealth is maximized for the average worker entering the private sector at 20 — yet most retire years before reaching it.</div></div>
      </div>
      <p style="margin-top:1.8rem;">Higher-educated workers were found to be <strong>46% more likely to retire early</strong>, holding all other factors constant. Workers with higher predicted lifetime pensions were also significantly more likely to retire early — suggesting the system's incentive structure penalized continued work most sharply for its highest-earning participants. Many workers appeared to lack complete information about how an additional year of work would affect their lifetime benefits, pointing to the value of a targeted information intervention.</p>
    </div>
  </div>
  <div class="cs-section">
    <div class="cs-section-label"><span>04</span>Policy Impact</div>
    <div class="cs-content">
      <h3>Recommendations adopted as national policy five years later</h3>
      <div class="cs-callout">
        <p>The research recommended two reforms: restructuring pension accrual rates at older ages to reduce the implicit tax on continued work — making delayed retirement more financially attractive — and implementing a targeted information intervention to help workers understand how each additional year of work would change their lifetime pension wealth.</p>
        <p style="margin-top:1rem;">Five years after publication, the core recommendation was adopted as national policy across Saudi Arabia. The pension incentive structure for the Kingdom's private sector workforce was restructured — a direct translation of evidence-based research into government action at national scale.</p>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

    st.markdown(f"""
<div class="cs-btn-row">
  <a href="{brief_href}" download="Early_Retirement_Policy_Brief.pdf" class="btn-gold">Download Policy Brief (PDF)</a>
</div>""", unsafe_allow_html=True)

    if st.button("← Back to Portfolio", key="gr_back_bottom"):
        st.session_state.page = 'home'
        st.rerun()

    st.markdown("""
<footer class="site-footer">
  <span class="footer-text">© 2025 Yaser Alhusaini — Policy · Data · Research</span>
  <span class="footer-text">Case Study · Early Retirement in the Private Sector · Saudi Arabia</span>
</footer>""", unsafe_allow_html=True)
    st.stop()

# ── Aspire case study ──────────────────────────────────────────────────────────
if st.session_state.page == 'aspire':
    components.html("""<script>
        function scrollUp() {
            var targets = [
                window.parent.document.querySelector('[data-testid="stAppViewContainer"]'),
                window.parent.document.querySelector('[data-testid="stMain"]'),
                window.parent.document.querySelector('.main'),
                window.parent.document.documentElement,
                window.parent.document.body
            ];
            targets.forEach(function(el) { if (el) { el.scrollTop = 0; } });
            window.parent.scrollTo(0, 0);
        }
        scrollUp();
        setTimeout(scrollUp, 150);
        setTimeout(scrollUp, 500);
    </script>""", height=1)
    aspire_href = f'data:application/pdf;base64,{aspire_b64}' if aspire_b64 else '#'
    st.markdown("""
<nav class="nav-bar">
  <div class="nav-name">Yaser Alhusaini</div>
  <div class="nav-links"><span style="font-family:'DM Mono',monospace;font-size:0.82rem;letter-spacing:0.14em;text-transform:uppercase;color:rgba(28,28,28,0.45);">Case Study — Aspire</span></div>
</nav>""", unsafe_allow_html=True)

    if st.button("← Back to Portfolio", key="asp_back_top"):
        st.session_state.page = 'home'
        st.rerun()

    st.markdown("""
<div class="cs-header">
  <div class="cs-overline">Case Study · 03</div>
  <h1 class="cs-title">Aspire! Afterschool<br>Program Evaluation</h1>
  <div class="cs-line"></div>
  <div class="cs-meta-row">
    <div class="cs-meta-item"><span class="cs-meta-label">Client</span><span class="cs-meta-value">Aspire! Afterschool Learning</span></div>
    <div class="cs-meta-item"><span class="cs-meta-label">Partners</span><span class="cs-meta-value">Georgetown University · McCourt School of Public Policy</span></div>
    <div class="cs-meta-item"><span class="cs-meta-label">Geography</span><span class="cs-meta-value">Arlington, VA</span></div>
    <div class="cs-meta-item"><span class="cs-meta-label">Year</span><span class="cs-meta-value">2019 – 2020</span></div>
    <div class="cs-meta-item"><span class="cs-meta-label">Domain</span><span class="cs-meta-value">Program Evaluation · Education Equity · SEL</span></div>
  </div>
</div>

<div class="cs-body">
  <div class="cs-section">
    <div class="cs-section-label"><span>01</span>Context</div>
    <div class="cs-content">
      <h3>Closing the achievement gap in one of America's wealthiest counties</h3>
      <p>Arlington County, Virginia ranks among the most affluent counties in the United States — yet an entrenched achievement gap divides economically disadvantaged students, predominantly Hispanic and non-English speaking, from their more affluent peers. Aspire! Afterschool Learning has worked for 25 years to narrow that gap, delivering 15 hours of weekly academic and socio-emotional support to 100 low-income 3rd–5th grade students through its Learning ROCKS! program in the Columbia Pike corridor. Over five years, program participants achieved over 90% improvement in reading instructional levels.</p>
      <p>Georgetown University's McCourt School of Public Policy engaged our research team to evaluate the program's impact and provide a concrete roadmap for building stronger evaluation capabilities. The engagement combined quantitative program evaluation, descriptive statistical analysis of three years of student data, a comprehensive evidence-based SEL literature review, and four tracks of actionable recommendations.</p>
      <p>This report was submitted as a Georgetown McCourt capstone project and was awarded best capstone graduation project in the cohort.</p>
    </div>
  </div>
  <div class="cs-section">
    <div class="cs-section-label"><span>02</span>My Role</div>
    <div class="cs-content">
      <h3>Evaluation design, data analysis, and SEL framework review</h3>
      <ul class="cs-bullets">
        <li><strong>Evaluation methodology design</strong> — Led the design of a propensity score matching (PSM) framework to create a comparison group of similar non-Aspire students for causal impact estimation. When individual-level data from Arlington Public Schools was unavailable, pivoted to rigorous descriptive analysis — documenting the methodology gap and providing a clear roadmap for conducting PSM once data access is secured.</li>
        <li><strong>Data construction and analysis</strong> — Built new analytical variables (startread, endread, readchange, hwchange) to standardize reading level and homework tracking across a sample of 82 students from 2016–2019, enabling consistent across-year comparisons of new vs. returning students.</li>
        <li><strong>SEL framework evaluation</strong> — Conducted a comprehensive review of evidence-based socio-emotional learning (SEL) frameworks, assessing each for effectiveness, implementation fit, and relevance to Aspire's low-income, predominantly Hispanic student population. Synthesized the evidence base into ranked recommendations for adoption.</li>
        <li><strong>Consulting report delivery</strong> — Synthesized all findings into a 50+ page consulting report with four actionable recommendation tracks: impact evaluation design, implementation evaluation, SEL framework adoption, and longitudinal study architecture — providing Aspire with a structured path toward rigorous, data-driven self-assessment.</li>
      </ul>
    </div>
  </div>
  <div class="cs-section">
    <div class="cs-section-label"><span>03</span>Key Findings</div>
    <div class="cs-content">
      <h3>Consistent reading gains across new and returning students</h3>
      <div class="findings-grid">
        <div class="finding-card"><div class="finding-num">0.82</div><div class="finding-desc">Average reading category improvement per student during one year in the Aspire program — nearly a full reading level in a single academic year.</div></div>
        <div class="finding-card"><div class="finding-num">70%</div><div class="finding-desc">Of first-year Aspire students made substantial reading progress — improving by one or two full reading categories over the course of the year.</div></div>
        <div class="finding-card"><div class="finding-num">68%</div><div class="finding-desc">Of third-year students continued showing improvement, challenging the "plateau theory" of diminishing returns from extended program participation.</div></div>
        <div class="finding-card"><div class="finding-num">85%</div><div class="finding-desc">Of students maintained or improved their homework scores despite assignments growing more challenging across quarters — a meaningful measure of sustained engagement.</div></div>
      </div>
    </div>
  </div>
  <div class="cs-section">
    <div class="cs-section-label"><span>04</span>Recommendations</div>
    <div class="cs-content">
      <h3>A four-track roadmap for rigorous future evaluation</h3>
      <ul class="cs-bullets">
        <li><strong>Impact evaluation design</strong> — Delivered a propensity score matching blueprint with a detailed list of variables Aspire should begin collecting (gender, race/ethnicity, standardized reading scores, school FRPL rate) to enable future causal analysis comparing Aspire students to similar non-participants.</li>
        <li><strong>SEL framework adoption</strong> — Recommended a suite of evidence-based SEL frameworks ranked by fit with Aspire's student population, delivery model, and resource constraints — with integration pathways and measurement indices for tracking socio-emotional outcomes alongside academic ones.</li>
        <li><strong>Implementation evaluation</strong> — Outlined a process evaluation framework to assess how consistently the program is delivered across Aspire's four sites, identifying implementation variables that may explain variation in student outcomes.</li>
        <li><strong>Longitudinal study design</strong> — Designed a multi-year data architecture for tracking student outcomes across grade transitions, with guidance on sample size, attrition management, and outcome variables needed for statistically sound long-term impact assessment.</li>
      </ul>
      <div class="cs-callout" style="margin-top:1.5rem;">
        <p>This evaluation represents the kind of rigorous, honest program evaluation I bring to nonprofit and government clients: methodologically transparent about what the data can and cannot support, practically focused on what the client can act on now, and forward-looking in building the infrastructure for stronger evidence over time.</p>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

    st.markdown(f"""
<div class="cs-btn-row">
  <a href="{aspire_href}" download="Aspire_Consulting_Report.pdf" class="btn-gold">Download Full Report (PDF)</a>
</div>""", unsafe_allow_html=True)

    if st.button("← Back to Portfolio", key="asp_back_bottom"):
        st.session_state.page = 'home'
        st.rerun()

    st.markdown("""
<footer class="site-footer">
  <span class="footer-text">© 2025 Yaser Alhusaini — Policy · Data · Research</span>
  <span class="footer-text">Case Study · Aspire! Afterschool Program Evaluation · Arlington, VA</span>
</footer>""", unsafe_allow_html=True)
    st.stop()

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
      Policy grounded<br>in evidence.<br><em>Built to deliver.</em>
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
<div class="section" style="padding-bottom:0;border-bottom:none;">
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

  <div class="exp-item" style="border-bottom:none;">
    <div>
      <div class="exp-date">Feb 2022 — Aug 2022</div>
      <div class="exp-org">Alnahda Society / Alwathba Consultancy</div>
      <a href="?page=takafu" target="_self" class="btn-exp-cs">Read case study →</a>
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
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section" style="padding-top:2rem;">
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
      <div class="exp-date">Aug — Dec 2020</div>
      <div class="exp-org">Georgetown University</div>
    </div>
    <div>
      <div class="exp-title">Teaching Assistant — Quantitative Methods III</div>
      <div class="exp-loc">Washington, DC</div>
      <ul class="exp-bullets">
        <li>Supported instruction in Quantitative Methods III — Advanced Regression and Program Evaluation Methods — at Georgetown's McCourt School of Public Policy.</li>
        <li>Provided guidance to 46 graduate students on interpreting econometric output, applying STATA for regression analysis, and designing rigorous program evaluations.</li>
        <li>Contributed to course materials emphasizing data-driven policy analysis and impact assessment methodologies.</li>
      </ul>
    </div>
  </div>

  <div class="exp-item">
    <div>
      <div class="exp-date">Jul — Oct 2020<br>May 2017 — Jul 2018</div>
      <div class="exp-org">Georgetown University</div>
      <a href="?page=georgetown" target="_self" class="btn-exp-cs">Read case study →</a>
    </div>
    <div>
      <div class="exp-title">Research Fellow — Evidence for Policy Design</div>
      <div class="exp-loc">Washington, DC</div>
      <ul class="exp-bullets">
        <li>Co-investigator under Prof. Nada Eissa on a study of early retirement behavior in Saudi Arabia's private sector, analyzing national GOSI administrative data covering multiple years of private sector retirement patterns across hundreds of thousands of workers.</li>
        <li>Co-designed and administered a 500-participant labor market survey on retirement decision-making, managing field coordination and STATA-based econometric analysis across worker demographics, wage histories, and pension awareness.</li>
        <li>Modeled the implicit tax structure embedded in the Saudi pension system, finding that a 50% increase in the implicit tax rate raises the probability of early retirement in a given year by 20%.</li>
        <li>Synthesized findings into a published policy brief under the Harvard Kennedy School Evidence for Policy Design (EPoD) banner, with recommendations submitted to the Saudi Ministry of Labor and Social Development.</li>
        <li>Research recommendations on pension incentive restructuring were adopted as national policy across Saudi Arabia five years after publication, affecting retirement incentive structures for the Kingdom's entire private sector workforce.</li>
      </ul>
    </div>
  </div>

  <div class="exp-item">
    <div>
      <div class="exp-date">Aug 2019 — May 2020</div>
      <div class="exp-org">Aspire After-school Learning</div>
      <a href="?page=aspire" target="_self" class="btn-exp-cs">Read case study →</a>
    </div>
    <div>
      <div class="exp-title">Pro-Bono Consultant</div>
      <div class="exp-loc">Washington, DC</div>
      <ul class="exp-bullets">
        <li>Led quantitative program evaluation for Aspire! Afterschool Learning, analyzing reading and homework outcomes for 82 low-income, predominantly Hispanic students across three school years (2016–2019) using descriptive statistical analysis.</li>
        <li>Designed a propensity score matching (PSM) evaluation framework to estimate causal program impact against similar non-participating students; when individual-level comparison data was unavailable, pivoted to rigorous descriptive analysis and documented a clear methodology roadmap for future causal evaluation.</li>
        <li>Conducted a comprehensive review and comparative evaluation of evidence-based socio-emotional learning (SEL) frameworks, ranking each by effectiveness, implementation fit, and relevance to Aspire's student population — synthesizing findings into prioritized adoption recommendations.</li>
        <li>Delivered a 50+ page consulting report with four recommendation tracks: impact evaluation design, SEL framework adoption, implementation evaluation, and longitudinal study architecture.</li>
        <li>Engagement served as the Georgetown McCourt capstone project, awarded best capstone graduation project in the cohort.</li>
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
    <a href="?page=takafu" target="_self" class="work-card" id="takafu-work-card">
      <div class="work-overline">01 · Gender Equity Research</div>
      <div class="work-title">Takafu Equal Opportunity Index</div>
      <div class="work-meta">Gender Parity Index &nbsp;·&nbsp; Saudi Arabia &nbsp;·&nbsp; 2022</div>
      <div class="work-finding">
        <span class="work-finding-label">Key finding</span>
        <span class="work-finding-text">46% economic opportunity gap between men and women across Saudi Arabia's private sector, measured across 7.8 million GOSI employees.</span>
      </div>
      <div><span class="work-pill">Read case study →</span></div>
    </a>
    <a href="?page=georgetown" target="_self" class="work-card" id="georgetown-work-card">
      <div class="work-overline">02 · Labor Economics</div>
      <div class="work-title">Early Retirement in the Private Sector</div>
      <div class="work-meta">Pension Policy Research &nbsp;·&nbsp; Saudi Arabia &nbsp;·&nbsp; 2017–2018</div>
      <div class="work-finding">
        <span class="work-finding-label">Key finding</span>
        <span class="work-finding-text">A 50% increase in the implicit tax rate raises early retirement probability by 20%. Research recommendations adopted as national pension policy across Saudi Arabia five years after publication.</span>
      </div>
      <div><span class="work-pill">Read case study →</span></div>
    </a>
    <a href="?page=aspire" target="_self" class="work-card" id="aspire-work-card">
      <div class="work-overline">03 · Education Equity</div>
      <div class="work-title">Aspire! Afterschool Program Evaluation</div>
      <div class="work-meta">Program Evaluation &nbsp;·&nbsp; Arlington, VA &nbsp;·&nbsp; 2019–2020</div>
      <div class="work-finding">
        <span class="work-finding-label">Key finding</span>
        <span class="work-finding-text">70% of first-year students improved by 1–2 reading categories in a single year. Delivered SEL framework evaluation and four-track impact roadmap — awarded Georgetown McCourt best capstone project.</span>
      </div>
      <div><span class="work-pill">Read case study →</span></div>
    </a>
  </div>
</section>
""", unsafe_allow_html=True)


# ── Dashboard ──────────────────────────────────────────────────────────────────
st.markdown('<div id="dashboard"></div>', unsafe_allow_html=True)
st.markdown("""
<section class="section section-dashboard">
  <div class="section-header">
    <span class="section-num">05</span>
    <span class="section-title">DMV Federal Workforce Impact — Interactive Dashboard</span>
  </div>
  <p class="dash-intro dash-desktop-only">
    A data lens on how federal workforce reductions have reshaped the DC–Maryland–Virginia regional economy.
    This dashboard reflects the kind of analytical work I build for agency and nonprofit clients —
    translating labor market and housing data into clear, decision-ready insights. Use the filters to explore each dimension.
  </p>
  <p class="dash-mobile-note" style="display:none;font-size:1rem;font-weight:300;color:rgba(28,28,28,0.55);font-family:'Jost',sans-serif;padding:1rem 0;border-top:1px solid rgba(26,26,26,0.08);">
    Interactive charts are best viewed on desktop. Visit yaseralhusaini.com on a larger screen to explore the DMV federal workforce dashboard.
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
    st.markdown('<div style="padding: 0 4rem 2rem;">', unsafe_allow_html=True)

    panel = st.segmented_control(
        "Panel",
        ["Unemployment Trend", "Sector Job Losses", "Housing Squeeze"],
        default="Unemployment Trend",
        label_visibility="collapsed"
    )

    # Defaults — overridden below if the panel needs a secondary filter
    show_nat   = True
    cat_filter = "All"
    metric     = "Both"

    # Secondary filter only for panels that need it
    if panel == "Sector Job Losses":
        col_f, _ = st.columns([3, 5])
        with col_f:
            cat_filter = st.selectbox(
                "Filter by category",
                ["All", "Direct — Federal", "Direct — Contracting", "Downstream"],
                label_visibility="visible"
            )
    elif panel == "Housing Squeeze":
        col_f, _ = st.columns([2, 6])
        with col_f:
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
        st.plotly_chart(fig, width='stretch')
        st.markdown('<div class="dash-desktop-only"><p style="font-size:0.78rem;color:rgba(28,28,28,0.45);font-family:\'DM Mono\',monospace;letter-spacing:0.05em;padding:0 3.5rem 0.5rem;">Source: Bureau of Labor Statistics, Local Area Unemployment Statistics (LAUS), 2024–2026.</p></div>', unsafe_allow_html=True)

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
        st.plotly_chart(fig, width='stretch')
        st.markdown('<div class="dash-desktop-only"><p style="font-size:0.78rem;color:rgba(28,28,28,0.45);font-family:\'DM Mono\',monospace;letter-spacing:0.05em;padding:0 3.5rem 0.5rem;">Source: BLS Quarterly Census of Employment and Wages (QCEW); Moody\'s Analytics regional estimates, 2025.</p></div>', unsafe_allow_html=True)

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
        st.plotly_chart(fig, width='stretch')
        st.markdown('<div class="dash-desktop-only"><p style="font-size:0.78rem;color:rgba(28,28,28,0.45);font-family:\'DM Mono\',monospace;letter-spacing:0.05em;padding:0 3.5rem 0.5rem;">Source: Realtor.com Market Reports; Zillow Research; DC Office of Planning (DMPED), 2024–2026.</p></div>', unsafe_allow_html=True)

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
