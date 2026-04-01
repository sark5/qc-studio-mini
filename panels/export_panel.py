import streamlit as st
import pandas as pd
import io
import numpy as np


def render_export_tab(data, df):
    st.subheader("⬇️ Export")

    st.markdown("### Export QC Summary")

    summary = {
        "scan_loaded": data is not None,
        "iqm_loaded": df is not None,
    }

    if data is not None:
        summary["mean_intensity"] = float(np.mean(data))
        summary["std_intensity"] = float(np.std(data))

    export_df = pd.DataFrame([summary])

    st.dataframe(export_df, use_container_width=True)

    csv_buffer = io.StringIO()
    export_df.to_csv(csv_buffer, index=False)

    st.download_button(
        label="⬇️ Download QC Summary CSV",
        data=csv_buffer.getvalue(),
        file_name="qc_summary.csv",
        mime="text/csv"
    )

    if df is not None:
        iqm_csv = io.StringIO()
        df.to_csv(iqm_csv, index=False)

        st.download_button(
            label="⬇️ Download IQM Table CSV",
            data=iqm_csv.getvalue(),
            file_name="iqm_table.csv",
            mime="text/csv"
        )