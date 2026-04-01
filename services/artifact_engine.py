import numpy as np

def estimate_artifact_risk(data):
    issues = []
    scores = {}

    mean_val = float(np.mean(data))
    std_val = float(np.std(data))

    # Empty / corrupted suspicion
    empty_score = max(0, 1 - (mean_val / 50))
    scores["empty_scan_risk"] = round(min(empty_score, 1.0), 2)
    if mean_val < 5:
        issues.append("Very low overall signal suggests an empty or corrupted scan.")

    # Low contrast suspicion
    contrast_score = max(0, 1 - (std_val / 30))
    scores["low_contrast_risk"] = round(min(contrast_score, 1.0), 2)
    if std_val < 10:
        issues.append("Low intensity variation suggests poor contrast.")

    # Noise suspicion (rough heuristic)
    slice_diffs = np.abs(np.diff(data, axis=2)) if data.shape[2] > 1 else np.array([0])
    noise_proxy = float(np.mean(slice_diffs))
    noise_score = min(noise_proxy / 50, 1.0)
    scores["noise_risk"] = round(noise_score, 2)
    if noise_proxy > 20:
        issues.append("High inter-slice intensity change may indicate noise or instability.")

    return {
        "scores": scores,
        "issues": issues
    }