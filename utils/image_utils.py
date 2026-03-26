import numpy as np

def get_middle_slice(data):
    z = data.shape[2] // 2
    return data[:, :, z]