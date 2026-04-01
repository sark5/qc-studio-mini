import streamlit as st

def render_sidebar():
    st.sidebar.title("QC Inputs")

    mri_file = st.sidebar.file_uploader(
        "Upload MRI Scan",
        type=["nii", "gz"],
        help="Supported: .nii, .nii.gz"
    )

    iqm_file = st.sidebar.file_uploader(
        "Upload IQM Table",
        type=["tsv"],
        help="Optional MRIQC-style TSV file"
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown("### Review Focus")
    st.sidebar.caption(
        "This workbench is designed to support explainable MRI quality control, "
        "especially for student researchers and neuroimaging workflows."
    )

    return {
        "mri": mri_file,
        "iqm": iqm_file
    }