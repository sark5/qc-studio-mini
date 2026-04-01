import nibabel as nib
import numpy as np
import tempfile
import os


def load_mri(file):
    """
    Load MRI from uploaded file or file path.
    Returns (normalized_data, nibabel_img)
    """
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
            os.remove(tmp_path)
    else:
        img = nib.load(file)
        data = img.get_fdata()

    if data.max() > data.min():
        data = (data - data.min()) / (data.max() - data.min())
    else:
        data = np.zeros_like(data)

    return data, img