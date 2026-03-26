import streamlit as st

def show_iqm_table(df):
    st.dataframe(df)

    # Highlight simple QC issues
    for idx, row in df.iterrows():
     if "snr" in row and row["snr"] < 10:
        st.warning(f"⚠️ Low SNR detected in row {idx}")
     if "motion" in row and row["motion"] > 0.5:
        st.warning(f"⚠️ High motion detected in row {idx}")