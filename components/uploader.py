import streamlit as st


def upload_files():
    st.sidebar.header("📁 Upload Files")

    mri_file = st.sidebar.file_uploader(
        "Upload MRI (.nii / .nii.gz)",
        type=["nii", "gz"]
    )

    iqm_file = st.sidebar.file_uploader(
        "Upload IQM (.tsv)",
        type=["tsv"]
    )

    return mri_file, iqm_file