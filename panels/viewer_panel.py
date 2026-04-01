import streamlit as st
import matplotlib.pyplot as plt

from utils.image_utils import get_slice, normalize_slice, find_best_slice
from panels.niivue_panel import show_niivue


def render_matplotlib(slice_data):
    fig, ax = plt.subplots(figsize=(5.5, 5.5))
    ax.imshow(slice_data.T, cmap="gray", origin="lower")
    ax.axis("off")
    plt.tight_layout(pad=0)
    st.pyplot(fig, use_container_width=True)


def render_viewer_tab(data, mri_file):
    st.subheader("🧠 MRI Viewer")

    if data is None or mri_file is None:
        st.info("Upload an MRI file to start viewing slices.")
        return

    axis_name = st.selectbox("Axis", ["Sagittal (X)", "Coronal (Y)", "Axial (Z)"])
    axis_idx = {"Sagittal (X)": 0, "Coronal (Y)": 1, "Axial (Z)": 2}[axis_name]

    max_slice = data.shape[axis_idx] - 1
    default_idx = find_best_slice(data, axis_idx)

    slice_idx = st.slider("Slice Index", 0, max_slice, default_idx)
    normalize = st.checkbox("Normalize slice", True)

    slice_data = get_slice(data, axis_idx, slice_idx)
    if normalize:
        slice_data = normalize_slice(slice_data)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Static Viewer")
        render_matplotlib(slice_data)

    with col2:
        st.markdown("#### Interactive Viewer")
        try:
            show_niivue(mri_file)
        except Exception as e:
            st.warning("Niivue viewer failed.")
            st.text(str(e))