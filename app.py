import streamlit as st
import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tempfile
import os

from components.uploader import upload_files
from components.iqm_table import show_iqm_table
from services.llm_explainer import generate_explanation
from panels.niivue_panel import show_niivue

st.set_page_config(layout="wide")
st.title("🧠 QC-Studio Mini")

# -------------------------
# 📁 UPLOAD FILES
# -------------------------
mri_file, iqm_file = upload_files()

# -------------------------
# 🔧 HELPER FUNCTIONS
# -------------------------
def get_slice(data, axis_idx, slice_idx):
    if axis_idx == 0:
        return data[slice_idx, :, :]
    elif axis_idx == 1:
        return data[:, slice_idx, :]
    else:
        return data[:, :, slice_idx]

def normalize_slice(slice_data):
    min_val = np.min(slice_data)
    max_val = np.max(slice_data)
    if max_val > min_val:
        return (slice_data - min_val) / (max_val - min_val)
    return slice_data

def render_matplotlib(slice_data):
    fig, ax = plt.subplots(figsize=(5.5, 5.5))
    ax.imshow(np.rot90(slice_data), cmap="gray")
    ax.axis("off")
    plt.tight_layout(pad=0)

    st.pyplot(fig, width="stretch")

def qc_checks(data):
    mean_intensity = np.mean(data)
    std_intensity = np.std(data)

    st.write("Mean Intensity:", mean_intensity)
    st.write("Std Intensity:", std_intensity)

    if std_intensity < 10:
        st.warning("⚠️ Low contrast image detected")
    if mean_intensity < 5:
        st.warning("⚠️ Possibly empty or corrupted scan")

# -------------------------
# 🚀 HANDLE MRI FILE
# -------------------------
if mri_file:
    # Save uploaded MRI temporarily (ONLY for nibabel usage)
    suffix = ".nii.gz" if mri_file.name.lower().endswith(".gz") else ".nii"
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(mri_file.getvalue())
        tmp.flush()
        tmp_path = tmp.name

    # Load with nibabel
    img = nib.load(tmp_path)
    data = img.get_fdata()

    st.success("MRI file loaded successfully!")

    # -------------------------
    # 🎛 SIDEBAR CONTROLS
    # -------------------------
    st.sidebar.header("Viewer Controls")
    axis_name = st.sidebar.selectbox("Axis", ["Sagittal (X)", "Coronal (Y)", "Axial (Z)"])
    axis_idx = {"Sagittal (X)":0, "Coronal (Y)":1, "Axial (Z)":2}[axis_name]
    max_slice = data.shape[axis_idx] - 1
    slice_idx = st.sidebar.slider("Slice Index", 0, max_slice, max_slice // 2)
    normalize = st.sidebar.checkbox("Normalize", True)

    slice_data = get_slice(data, axis_idx, slice_idx)
    if normalize:
        slice_data = normalize_slice(slice_data)

    # -------------------------
    # 🗂️ TABS
    # -------------------------
    tab1, tab2, tab3 = st.tabs(["🧠 Viewer", "📊 QC Metrics", "📄 Metadata"])

    # -------------------------
    # 🧠 VIEWER TAB
    # -------------------------
    with tab1:
        col1, col2 = st.columns(2)

        # Matplotlib Viewer
        with col1:
            st.subheader("Matplotlib Viewer")
            render_matplotlib(slice_data)

        # Niivue Viewer (FIXED ✅)
        with col2:
            st.subheader("Niivue Viewer")
            try:
                show_niivue(mri_file)
            except Exception as e:
                st.warning("Niivue failed")
                st.text(str(e))

    # -------------------------
    # 📊 QC METRICS TAB
    # -------------------------
    with tab2:
        st.subheader("🚨 Basic QC Checks")
        qc_checks(data)

        if iqm_file:
            df = pd.read_csv(iqm_file, sep="\t")
            st.subheader("IQM Table")
            show_iqm_table(df)

            if st.button("🧠 Explain Quality"):
                for idx, row in df.iterrows():
                    explanation = generate_explanation(row.to_dict())
                    st.markdown(f"**Row {idx} explanation:** {explanation}")

    # -------------------------
    # 📄 METADATA TAB
    # -------------------------
    with tab3:
        header = img.header
        col1, col2 = st.columns(2)

        with col1:
            st.write("Dimensions:", header.get_data_shape())
            st.write("Voxel Size:", header.get_zooms())

        with col2:
            st.write("Data Type:", header.get_data_dtype())
            st.write("Affine Matrix:")
            st.write(img.affine)

    # Cleanup temp file
    os.remove(tmp_path)

else:
    st.info("👆 Upload an MRI file to begin")