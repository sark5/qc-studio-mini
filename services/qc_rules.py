import pandas as pd
import numpy as np


def safe_float(val):
    try:
        if pd.isna(val):
            return None
        return float(val)
    except:
        return None


def basic_scan_qc(data):
    mean_intensity = float(np.mean(data))
    std_intensity = float(np.std(data))

    issues = []
    if std_intensity < 0.05:
        issues.append("Low contrast scan")
    if mean_intensity < 0.05:
        issues.append("Possibly empty or corrupted scan")

    return {
        "mean_intensity": mean_intensity,
        "std_intensity": std_intensity,
        "issues": issues
    }


def analyze_iqm_row(row):
    issues = []
    good = []
    score = 0

    snr = safe_float(row.get("snr"))
    cnr = safe_float(row.get("cnr"))
    efc = safe_float(row.get("efc"))
    cjv = safe_float(row.get("cjv"))
    motion = safe_float(row.get("motion"))
    fd_mean = safe_float(row.get("fd_mean"))
    dvars = safe_float(row.get("dvars"))
    tsnr = safe_float(row.get("tsnr"))
    fwhm = safe_float(row.get("fwhm"))

    if snr is not None:
        if snr < 8:
            issues.append("Low SNR")
            score += 2
        elif snr < 10:
            issues.append("Borderline SNR")
            score += 1
        else:
            good.append("Good SNR")

    if cnr is not None:
        if cnr < 1:
            issues.append("Low CNR")
            score += 2
        else:
            good.append("Good CNR")

    if efc is not None:
        if efc > 0.7:
            issues.append("High EFC")
            score += 1
        else:
            good.append("Acceptable EFC")

    if cjv is not None:
        if cjv > 0.8:
            issues.append("High CJV")
            score += 1
        else:
            good.append("Acceptable CJV")

    if fwhm is not None:
        if fwhm > 6:
            issues.append("Blur / High FWHM")
            score += 1
        else:
            good.append("Acceptable sharpness")

    if motion is not None:
        if motion > 0.5:
            issues.append("High Motion")
            score += 2
        else:
            good.append("Low motion")

    if fd_mean is not None:
        if fd_mean > 0.5:
            issues.append("High FD")
            score += 2
        elif fd_mean > 0.3:
            issues.append("Moderate FD")
            score += 1
        else:
            good.append("Low FD")

    if dvars is not None:
        if dvars > 1.5:
            issues.append("High DVARS")
            score += 1
        else:
            good.append("Stable DVARS")

    if tsnr is not None:
        if tsnr < 25:
            issues.append("Low tSNR")
            score += 1
        else:
            good.append("Good tSNR")

    return issues, good, score


def get_qc_status(score):
    if score == 0:
        return "PASS"
    elif score <= 2:
        return "WARN"
    return "FAIL"


def build_qc_table(df):
    qc_df = df.copy()

    statuses = []
    flag_counts = []
    flag_texts = []
    scores = []

    for _, row in qc_df.iterrows():
        issues, _, score = analyze_iqm_row(row)
        statuses.append(get_qc_status(score))
        flag_counts.append(len(issues))
        flag_texts.append(", ".join(issues) if issues else "No major issues")
        scores.append(score)

    qc_df["qc_status"] = statuses
    qc_df["flag_count"] = flag_counts
    qc_df["qc_flags"] = flag_texts
    qc_df["qc_score"] = scores

    return qc_df