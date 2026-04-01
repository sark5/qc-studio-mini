import streamlit as st
from services.llm_explainer import generate_explanation


def render_explainability_tab(df):
    st.subheader("🧪 Explainability")

    if df is None or df.empty:
        st.info("Upload an IQM TSV file to generate AI explanations.")
        return

    row_options = [f"Row {i}" for i in df.index]
    selected = st.selectbox("Select IQM Row", row_options)
    idx = int(selected.split()[-1])

    row_data = df.loc[idx].to_dict()

    st.markdown("### Selected Metrics")
    st.json(row_data)

    if st.button("🧠 Generate Explanation"):
        with st.spinner("Generating explanation..."):
            explanation = generate_explanation(row_data)
        st.markdown("### AI QC Interpretation")
        st.success(explanation)