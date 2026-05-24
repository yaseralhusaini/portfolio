import streamlit as st
import base64
import os

st.set_page_config(
    page_title="Takafu Equal Opportunity Index — Yaser Alhusaini",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed",
)

_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_DIR = os.path.dirname(_DIR)

def get_file_b64(filename):
    try:
        with open(os.path.join(_PROJECT_DIR, filename), "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return None

report_b64 = get_file_b64("takafu_report.pdf")
report_href = f'data:application/pdf;base64,{report_b64}' if report_b64 else '#'

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
h1, h2, h3, h4, h5, h6 { color: #1c1c1c !important; }
div[data-testid="stMarkdownContainer"] p { margin: 0; }

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
}
.nav-name {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.5rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    color: #1c1c1c;
    text-decoration: none;
}
.nav-back {
    font-family: 'DM Mono', monospace;
    font-size: 0.88rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: rgba(28,28,28,0.60);
    text-decoration: none;
    transition: color 0.2s;
}
.nav-back:hover { color: #1c1c1c; }

/* ── Case study header ── */
.cs-header {
    padding: 5rem 4rem 4rem;
    border-bottom: 1px solid rgba(26,26,26,0.08);
    max-width: 900px;
}
.cs-overline {
    font-family: 'DM Mono', monospace;
    font-size: 0.82rem;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: #9c6f3a;
    margin-bottom: 1.6rem;
}
.cs-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(2.8rem, 5vw, 4.8rem);
    font-weight: 300;
    line-height: 1.05;
    color: #1c1c1c !important;
    margin-bottom: 1.8rem;
}
.cs-line {
    width: 60px;
    height: 2px;
    background: #9c6f3a;
    margin-bottom: 2rem;
}
.cs-meta-row {
    display: flex;
    gap: 2.5rem;
    flex-wrap: wrap;
}
.cs-meta-item {
    display: flex;
    flex-direction: column;
    gap: 0.3rem;
}
.cs-meta-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: rgba(28,28,28,0.45);
}
.cs-meta-value {
    font-size: 1rem;
    font-weight: 300;
    color: rgba(28,28,28,0.80);
}

/* ── Content layout ── */
.cs-body {
    padding: 0 4rem;
    max-width: 960px;
}
.cs-section {
    padding: 4rem 0;
    border-bottom: 1px solid rgba(26,26,26,0.07);
    display: grid;
    grid-template-columns: 180px 1fr;
    gap: 3.5rem;
}
.cs-section:last-child { border-bottom: none; }
.cs-section-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.78rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: rgba(28,28,28,0.42);
    padding-top: 0.35rem;
    line-height: 1.6;
}
.cs-section-label span {
    display: block;
    font-size: 1.6rem;
    font-family: 'Cormorant Garamond', serif;
    color: rgba(28,28,28,0.12);
    letter-spacing: 0;
    font-weight: 300;
    margin-bottom: 0.4rem;
}
.cs-content h3 {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.7rem;
    font-weight: 400;
    color: #1c1c1c !important;
    margin-bottom: 1.2rem;
    line-height: 1.2;
}
.cs-content p {
    font-size: 1.15rem;
    font-weight: 300;
    line-height: 1.85;
    color: rgba(28,28,28,0.82);
    margin-bottom: 1.2rem;
}
.cs-content p:last-child { margin-bottom: 0; }

/* ── Role bullets ── */
.cs-bullets { list-style: none; padding: 0; margin: 0; }
.cs-bullets li {
    font-size: 1.15rem;
    font-weight: 300;
    color: rgba(28,28,28,0.82);
    line-height: 1.85;
    padding-left: 1.4rem;
    position: relative;
    margin-bottom: 0.9rem;
}
.cs-bullets li::before {
    content: '—';
    position: absolute;
    left: 0;
    color: #9c6f3a;
}

/* ── Findings grid ── */
.findings-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1px;
    background: rgba(26,26,26,0.08);
    border: 1px solid rgba(26,26,26,0.08);
    margin-top: 0.5rem;
}
.finding-card {
    background: #f7f5f0;
    padding: 2rem 1.8rem;
}
.finding-num {
    font-family: 'Cormorant Garamond', serif;
    font-size: 2.6rem;
    font-weight: 300;
    color: #9c6f3a;
    line-height: 1;
    margin-bottom: 0.5rem;
}
.finding-desc {
    font-size: 1rem;
    font-weight: 300;
    color: rgba(28,28,28,0.78);
    line-height: 1.6;
}

/* ── Client callout box ── */
.cs-callout {
    background: #ede9e0;
    border-top: 2px solid #9c6f3a;
    padding: 2rem 2.2rem;
    margin-top: 0.5rem;
}
.cs-callout p {
    font-size: 1.15rem;
    font-weight: 300;
    line-height: 1.85;
    color: rgba(28,28,28,0.82);
    margin: 0;
}

/* ── Buttons ── */
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
    transition: border-color 0.2s, background 0.2s;
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

/* ── CTA section ── */
.cs-cta {
    padding: 4rem;
    display: flex;
    gap: 1.2rem;
    flex-wrap: wrap;
    align-items: center;
    border-top: 1px solid rgba(26,26,26,0.07);
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
</style>
""", unsafe_allow_html=True)

# ── Nav ────────────────────────────────────────────────────────────────────────
st.markdown("""
<nav class="nav-bar">
  <a href="/" target="_self" class="nav-name">Yaser Alhusaini</a>
  <a href="/" target="_self" class="nav-back">← Back to Portfolio</a>
</nav>
""", unsafe_allow_html=True)

# ── Case study header ──────────────────────────────────────────────────────────
st.markdown("""
<div class="cs-header">
  <div class="cs-overline">Case Study · 01</div>
  <h1 class="cs-title">Takafu Equal<br>Opportunity Index</h1>
  <div class="cs-line"></div>
  <div class="cs-meta-row">
    <div class="cs-meta-item">
      <span class="cs-meta-label">Client</span>
      <span class="cs-meta-value">Alnahda Society · Alwathba Consultancy</span>
    </div>
    <div class="cs-meta-item">
      <span class="cs-meta-label">Geography</span>
      <span class="cs-meta-value">Saudi Arabia</span>
    </div>
    <div class="cs-meta-item">
      <span class="cs-meta-label">Year</span>
      <span class="cs-meta-value">2022</span>
    </div>
    <div class="cs-meta-item">
      <span class="cs-meta-label">Domain</span>
      <span class="cs-meta-value">Gender Equity · Labor Economics · Policy Research</span>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Body ───────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="cs-body">

  <!-- 01 Context -->
  <div class="cs-section">
    <div class="cs-section-label">
      <span>01</span>
      Context
    </div>
    <div class="cs-content">
      <h3>Saudi Arabia's first private-sector gender parity index</h3>
      <p>
        Alnahda Society — founded in 1962, Saudi Arabia's oldest and largest women's
        empowerment nonprofit — commissioned the Takafu Equal Opportunity Index as part of
        a broader push to create a measurable, evidence-based framework for tracking gender
        parity in the Kingdom's private sector.
      </p>
      <p>
        The project arrived at a pivotal moment. Saudi Vision 2030 had set an ambitious
        target: raise women's labor force participation from 17% to 30% by the decade's end.
        Yet there was no systematic, data-driven benchmark against which companies or
        policymakers could assess progress. Takafu was designed to fill that gap — producing
        the first index of its kind in the Kingdom, with findings intended to inform both
        employer practice and national policy.
      </p>
      <p>
        The index measured gender equality across three dimensions: economic opportunity
        (hiring and participation), career development (advancement and retention), and
        compensation equity — drawing on both national administrative data and primary
        survey research.
      </p>
    </div>
  </div>

  <!-- 02 Role -->
  <div class="cs-section">
    <div class="cs-section-label">
      <span>02</span>
      My Role
    </div>
    <div class="cs-content">
      <h3>End-to-end quantitative research, from administrative data to published findings</h3>
      <ul class="cs-bullets">
        <li>
          <strong>Administrative data analysis</strong> — Analyzed a national GOSI (General
          Organization for Social Insurance) dataset covering over 7.8 million private sector
          employees. Ran advanced regression models to measure gender gaps in labor force
          participation, career progression, and compensation across industries and firm sizes.
        </li>
        <li>
          <strong>Oaxaca-Blinder decomposition</strong> — Applied decomposition analysis to
          isolate the portion of the gender wage gap that could not be explained by observable
          factors such as education, tenure, industry, or firm size — a methodologically
          rigorous approach for quantifying structural discrimination in labor markets.
        </li>
        <li>
          <strong>Dual survey design and analysis</strong> — Co-designed two complementary
          survey instruments: one targeting HR managers (firm-level practices and policies),
          one targeting employees (individual-level experience). Collected and analyzed
          responses from 57 companies and 985 Saudi workers across Riyadh, Makkah, and
          the Eastern Province.
        </li>
        <li>
          <strong>Policy synthesis</strong> — Synthesized quantitative findings and qualitative
          survey data into the published Takafu 2020 Executive Summary, with policy and employer
          recommendations cited by government stakeholders aligned to Saudi Vision 2030.
        </li>
      </ul>
    </div>
  </div>

  <!-- 03 Key findings -->
  <div class="cs-section">
    <div class="cs-section-label">
      <span>03</span>
      Key Findings
    </div>
    <div class="cs-content">
      <h3>Four numbers that tell the story</h3>
      <div class="findings-grid">
        <div class="finding-card">
          <div class="finding-num">46%</div>
          <div class="finding-desc">
            Overall economic opportunity gap between men and women across
            Saudi Arabia's private sector — the headline index score capturing
            disparities in hiring, advancement, and pay.
          </div>
        </div>
        <div class="finding-card">
          <div class="finding-num">7.8M</div>
          <div class="finding-desc">
            Private sector employees in the GOSI administrative dataset analyzed
            — the most comprehensive labor market dataset available in the Kingdom,
            covering all registered private sector workers.
          </div>
        </div>
        <div class="finding-card">
          <div class="finding-num">57</div>
          <div class="finding-desc">
            Companies surveyed across Riyadh, Makkah, and the Eastern Province,
            alongside 985 individual workers — providing firm-level and
            worker-level perspectives on workplace equity.
          </div>
        </div>
        <div class="finding-card">
          <div class="finding-num">∆</div>
          <div class="finding-desc">
            Significant unexplained wage gap remained after controlling for
            education, industry, and firm size — Oaxaca-Blinder decomposition
            pointed to structural barriers beyond human capital differences.
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- 04 What this demonstrates -->
  <div class="cs-section">
    <div class="cs-section-label">
      <span>04</span>
      Relevance
    </div>
    <div class="cs-content">
      <h3>What this means for your project</h3>
      <div class="cs-callout">
        <p>
          Takafu represents the kind of work I bring to complex policy research engagements:
          the technical depth to handle large administrative datasets, the methodological
          precision to apply labor economics techniques like Oaxaca-Blinder decomposition,
          and the end-to-end capacity to move from survey design through published,
          decision-ready findings.
        </p>
        <p style="margin-top:1rem;">
          For clients working on gender equity, workforce analytics, program evaluation,
          or any initiative that requires translating raw data into credible, actionable
          policy insight — I bring the same combination of analytical rigor and
          stakeholder-facing clarity that shaped this project.
        </p>
      </div>
    </div>
  </div>

</div>
""", unsafe_allow_html=True)

# ── CTA ────────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="cs-cta">
  <a href="{report_href}" download="Takafu_Executive_Summary.pdf" class="btn-gold">
    Download Executive Summary (PDF)
  </a>
  <a href="/" target="_self" class="btn-outline">← Back to Portfolio</a>
</div>
""", unsafe_allow_html=True)

# ── Footer ─────────────────────────────────────────────────────────────────────
st.markdown("""
<footer class="site-footer">
  <span class="footer-text">© 2025 Yaser Alhusaini — Policy · Data · Research</span>
  <span class="footer-text">Case Study · Takafu Equal Opportunity Index · Saudi Arabia</span>
</footer>
""", unsafe_allow_html=True)
