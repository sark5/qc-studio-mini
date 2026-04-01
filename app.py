import streamlit as st

from components.uploader import upload_files
from loaders.mri_loader import load_mri
from loaders.iqm_loader import load_iqm

from panels.viewer_panel import render_viewer_tab
from panels.qc_panel import render_qc_tab
from panels.explainability_panel import render_explainability_tab
from panels.metadata_panel import render_metadata_tab
from panels.compare_panel import render_compare_tab
from panels.export_panel import render_export_tab

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="QC-Studio Mini",
    page_icon="🧠",
    layout="wide"
)

# -------------------------
# SIMPLE CLEAN UI
# -------------------------
st.markdown("""
<style>
.block-container {
    padding-top: 1.8rem;
    padding-bottom: 2rem;
    max-width: 1250px;
}
h1, h2, h3 {
    letter-spacing: -0.02em;
}
[data-testid="stSidebar"] {
    border-right: 1px solid rgba(120,120,120,0.15);
}
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 10px 10px 0 0;
    padding: 10px 18px;
}
div[data-testid="stMetric"] {
    border: 1px solid rgba(120,120,120,0.15);
    border-radius: 14px;
    padding: 12px 14px;
    background: rgba(250,250,250,0.02);
}
</style>
""", unsafe_allow_html=True)

st.title("🧠 QC-Studio Mini")
st.caption("A lightweight MRI Quality Control app for visualization, QC review, explainability, comparison, and export.")

# -------------------------
# FILE UPLOAD
# -------------------------
mri_file, iqm_file = upload_files()

data, img = (None, None)
df = None

if mri_file:
    data, img = load_mri(mri_file)

if iqm_file:
    df = load_iqm(iqm_file)

# -------------------------
# MAIN TABS
# -------------------------
tabs = st.tabs([
    "🧠 Viewer",
    "📊 QC Dashboard",
    "🧪 Explainability",
    "📄 Metadata",
    "🆚 Compare",
    "⬇️ Export"
])

with tabs[0]:
    render_viewer_tab(data, mri_file)

with tabs[1]:
    render_qc_tab(data, df)

with tabs[2]:
    render_explainability_tab(df)

with tabs[3]:
    render_metadata_tab(img)

with tabs[4]:
    render_compare_tab(df)

with tabs[5]:
    render_export_tab(data, df)