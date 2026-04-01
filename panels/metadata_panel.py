import streamlit as st


def render_metadata_tab(img):
    st.subheader("📄 MRI Metadata")

    if img is None:
        st.info("Upload an MRI file to inspect metadata.")
        return

    header = img.header

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Core Information")
        st.write("**Dimensions:**", header.get_data_shape())
        st.write("**Voxel Size:**", header.get_zooms())
        st.write("**Data Type:**", header.get_data_dtype())

    with col2:
        st.markdown("### Affine Matrix")
        st.write(img.affine)