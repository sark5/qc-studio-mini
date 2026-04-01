import numpy as np


def get_slice(data, axis_idx, slice_idx):
    if axis_idx == 0:
        return data[slice_idx, :, :]
    elif axis_idx == 1:
        return data[:, slice_idx, :]
    return data[:, :, slice_idx]


def normalize_slice(slice_data):
    min_val = np.min(slice_data)
    max_val = np.max(slice_data)

    if max_val > min_val:
        return (slice_data - min_val) / (max_val - min_val)

    return np.zeros_like(slice_data)


def get_middle_slice(data, axis_idx=2):
    mid = data.shape[axis_idx] // 2
    return get_slice(data, axis_idx, mid)


def find_best_slice(data, axis_idx=2):
    best_idx = data.shape[axis_idx] // 2
    best_score = -1

    for i in range(data.shape[axis_idx]):
        sl = get_slice(data, axis_idx, i)
        score = np.std(sl)

        if score > best_score:
            best_score = score
            best_idx = i

    return best_idx