import streamlit as st

from loaders.iqm_loader import load_iqm
from services.metric_interpreter import interpret_metric
from services.llm_explainer import generate_explanation

def render_explain_panel(mri_file, iqm_file):
    st.subheader("Explainability")

    st.markdown("### Metric-to-Meaning Translator")

    metric_name = st.selectbox(
        "Choose metric",
        ["snr", "cnr", "efc", "cjv", "fber", "fwhm", "motion"]
    )

    st.info(interpret_metric(metric_name, None))

    if iqm_file:
        st.markdown("---")
        st.markdown("### AI-Assisted QC Interpretation")

        df = load_iqm(iqm_file)
        selected_idx = st.selectbox(
            "Choose IQM row for explanation",
            options=df.index.tolist(),
            format_func=lambda x: f"Row {x}",
            key="explain_row_selector"
        )

        row = df.loc[selected_idx].to_dict()

        if st.button("🧠 Generate Explanation"):
            with st.spinner("Generating explanation..."):
                explanation = generate_explanation(row)

            st.markdown("#### AI Explanation")
            st.write(explanation)
    else:
        st.info("Upload an IQM TSV file to generate AI-assisted explanations.")