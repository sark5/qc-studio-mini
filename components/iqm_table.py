import streamlit as st
import pandas as pd


def show_iqm_table(df: pd.DataFrame):
    if df is None or df.empty:
        st.info("No IQM table available.")
        return

    st.dataframe(df, use_container_width=True)

    warnings = []

    for idx, row in df.iterrows():
        if "snr" in df.columns and pd.notna(row.get("snr")) and row["snr"] < 10:
            warnings.append(f"⚠️ Row {idx}: Low SNR")
        if "motion" in df.columns and pd.notna(row.get("motion")) and row["motion"] > 0.5:
            warnings.append(f"⚠️ Row {idx}: High motion")
        if "efc" in df.columns and pd.notna(row.get("efc")) and row["efc"] > 0.7:
            warnings.append(f"⚠️ Row {idx}: Elevated EFC")
        if "cnr" in df.columns and pd.notna(row.get("cnr")) and row["cnr"] < 1:
            warnings.append(f"⚠️ Row {idx}: Low CNR")

    if warnings:
        st.markdown("### QC Flags")
        for w in warnings[:10]:
            st.warning(w)