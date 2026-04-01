import os
from dotenv import load_dotenv

load_dotenv()

try:
    from groq import Groq
except ImportError:
    Groq = None

api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key) if (Groq and api_key) else None


def classify_metrics(metrics):
    result = {}

    if "snr" in metrics and metrics["snr"] is not None:
        result["snr"] = "low" if metrics["snr"] < 10 else "good"

    if "motion" in metrics and metrics["motion"] is not None:
        result["motion"] = "high" if metrics["motion"] > 0.5 else "low"

    return result


def fallback_explanation(metrics):
    notes = []

    snr = metrics.get("snr")
    cnr = metrics.get("cnr")
    efc = metrics.get("efc")
    motion = metrics.get("motion")

    if snr is not None:
        notes.append("SNR is low, suggesting weaker signal quality." if snr < 10 else "SNR appears acceptable.")
    if cnr is not None:
        notes.append("CNR is low, which may reduce tissue contrast." if cnr < 1 else "CNR appears acceptable.")
    if efc is not None:
        notes.append("EFC is elevated, which may indicate artifact or blur." if efc > 0.7 else "EFC appears within a reasonable range.")
    if motion is not None:
        notes.append("Motion appears high and may affect scan usability." if motion > 0.5 else "Motion appears low.")

    if not notes:
        return "No strong QC abnormalities were detected from the available metrics."

    return " ".join(notes[:2])


def generate_explanation(metrics):
    classified = classify_metrics(metrics)

    snr = classified.get("snr", "unknown")
    motion = classified.get("motion", "unknown")

    prompt = f"""
You are an MRI quality control expert.

Metrics:
- Signal-to-Noise Ratio (SNR): {snr}
- Contrast-to-Noise Ratio (CNR): {metrics.get('cnr', 'unknown')}
- Full Width Half Maximum (FWHM): {metrics.get('fwhm', 'unknown')}
- Entropy Focus Criterion (EFC): {metrics.get('efc', 'unknown')}
- Motion Artifacts: {motion}

Explain the scan quality clearly in exactly 2 sentences.
Be concise and clinically meaningful.
"""

    if client is None:
        return fallback_explanation(metrics)

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a medical imaging expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content.strip()
    except Exception:
        return fallback_explanation(metrics)