import nibabel as nib
import numpy as np
import tempfile
import os

def load_mri(file):
    """
    Load MRI from a file path (str) or Streamlit UploadedFile.
    Returns normalized data and nibabel image object.
    """

    # If it's a Streamlit UploadedFile, write to a temporary file
    if not isinstance(file, str):
        suffix = ".nii.gz" if file.name.lower().endswith(".nii.gz") else ".nii"
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(file.getvalue())
            tmp.flush()
            tmp_path = tmp.name

        try:
            img = nib.load(tmp_path)
            data = img.get_fdata()
        finally:
            # Clean up temp file
            os.remove(tmp_path)
    else:
        # If already a path string
        img = nib.load(file)
        data = img.get_fdata()

    # Normalize to 0–1
    if data.max() > data.min():
        if data.max() > data.min():
           data = (data - data.min()) / (data.max() - data.min())
        else:
          data = np.zeros_like(data)

    return data, img