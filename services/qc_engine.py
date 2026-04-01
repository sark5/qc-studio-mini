import numpy as np

def evaluate_scan_qc(data):
    mean_intensity = float(np.mean(data))
    std_intensity = float(np.std(data))
    dynamic_range = float(np.max(data) - np.min(data))

    issues = []
    reasons = []

    if std_intensity < 10:
        issues.append("Low contrast")
        reasons.append("Low standard deviation suggests weak tissue contrast.")

    if mean_intensity < 5:
        issues.append("Very low signal")
        reasons.append("Mean intensity is unusually low and may indicate corruption or empty volume.")

    if dynamic_range < 25:
        issues.append("Compressed intensity range")
        reasons.append("Limited dynamic range may reduce visual interpretability.")

    if len(issues) == 0:
        verdict = "PASS"
    elif len(issues) == 1:
        verdict = "WARN"
    else:
        verdict = "FAIL"

    return {
        "mean_intensity": mean_intensity,
        "std_intensity": std_intensity,
        "dynamic_range": dynamic_range,
        "issues": issues,
        "reasons": reasons,
        "verdict": verdict
    }

def evaluate_iqm_row(metrics):
    issues = []
    evidence = []

    def safe_float(x):
        try:
            return float(x)
        except:
            return None

    snr = safe_float(metrics.get("snr"))
    cnr = safe_float(metrics.get("cnr"))
    efc = safe_float(metrics.get("efc"))
    cjv = safe_float(metrics.get("cjv"))
    motion = safe_float(metrics.get("motion"))
    fd_mean = safe_float(metrics.get("fd_mean"))

    if snr is not None and snr < 10:
        issues.append("Low SNR")
        evidence.append("Signal may be noisy.")

    if cnr is not None and cnr < 1:
        issues.append("Low CNR")
        evidence.append("Tissue contrast may be weak.")

    if efc is not None and efc > 0.7:
        issues.append("High EFC")
        evidence.append("Possible ghosting or disorder in intensity structure.")

    if cjv is not None and cjv > 0.8:
        issues.append("High CJV")
        evidence.append("Gray/white matter separation may be poor.")

    if motion is not None and motion > 0.5:
        issues.append("High motion")
        evidence.append("Motion-related artifact may affect analysis.")

    if fd_mean is not None and fd_mean > 0.5:
        issues.append("High framewise displacement")
        evidence.append("Excessive subject movement is likely.")

    if len(issues) == 0:
        verdict = "PASS"
    elif len(issues) <= 2:
        verdict = "WARN"
    else:
        verdict = "FAIL"

    return {
        "verdict": verdict,
        "issues": issues,
        "evidence": evidence
    }