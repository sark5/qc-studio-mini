import streamlit as st
import numpy as np

from components.iqm_table import show_iqm_table


def render_qc_tab(data, df):
    st.subheader("📊 QC Dashboard")

    if data is None:
        st.info("Upload an MRI file to compute QC metrics.")
    else:
        mean_intensity = float(np.mean(data))
        std_intensity = float(np.std(data))
        min_intensity = float(np.min(data))
        max_intensity = float(np.max(data))

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Mean Intensity", f"{mean_intensity:.3f}")
        c2.metric("Std Intensity", f"{std_intensity:.3f}")
        c3.metric("Min", f"{min_intensity:.3f}")
        c4.metric("Max", f"{max_intensity:.3f}")

        st.markdown("### Automated Scan Flags")
        if std_intensity < 0.05:
            st.warning("⚠️ Low contrast image detected")
        else:
            st.success("✅ Contrast appears acceptable")

        if mean_intensity < 0.01:
            st.warning("⚠️ Possibly empty or corrupted scan")
        else:
            st.success("✅ Scan intensity distribution looks usable")

    st.markdown("---")
    st.markdown("### IQM Review")

    if df is not None:
        show_iqm_table(df)

        numeric_cols = df.select_dtypes(include="number").columns.tolist()
        if numeric_cols:
            selected_metric = st.selectbox("Plot IQM Metric", numeric_cols)
            st.line_chart(df[selected_metric])
    else:
        st.info("Upload an IQM TSV file to view structured quality metrics.")