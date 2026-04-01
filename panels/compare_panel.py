import streamlit as st
import pandas as pd


def render_compare_tab(df):
    st.subheader("🆚 Compare Subjects / Rows")

    if df is None or df.empty:
        st.info("Upload an IQM TSV file to compare rows.")
        return

    if len(df) < 2:
        st.info("Need at least 2 rows in IQM file for comparison.")
        return

    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    if not numeric_cols:
        st.warning("No numeric IQM columns found for comparison.")
        return

    row_labels = [f"Row {i}" for i in df.index]

    col1, col2 = st.columns(2)

    with col1:
        row_a = st.selectbox("Select First Row", row_labels, index=0)

    with col2:
        row_b = st.selectbox("Select Second Row", row_labels, index=1 if len(row_labels) > 1 else 0)

    idx_a = int(row_a.split()[-1])
    idx_b = int(row_b.split()[-1])

    series_a = df.loc[idx_a, numeric_cols]
    series_b = df.loc[idx_b, numeric_cols]

    compare_df = pd.DataFrame({
        "Metric": numeric_cols,
        "Row A": series_a.values,
        "Row B": series_b.values,
        "Difference": series_a.values - series_b.values
    })

    st.markdown("### Comparison Table")
    st.dataframe(compare_df, use_container_width=True)

    st.markdown("### Quick Summary")
    higher_a = (compare_df["Difference"] > 0).sum()
    higher_b = (compare_df["Difference"] < 0).sum()

    c1, c2 = st.columns(2)
    c1.metric("Metrics Higher in Row A", int(higher_a))
    c2.metric("Metrics Higher in Row B", int(higher_b))

    st.markdown("### Metric Trends")
    chart_df = compare_df.set_index("Metric")[["Row A", "Row B"]]
    st.line_chart(chart_df)