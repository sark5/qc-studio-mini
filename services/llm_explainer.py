import os
from groq import Groq
from dotenv import load_dotenv

# ✅ Load environment variables from .env
load_dotenv()

# ✅ Get API key safely
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise RuntimeError("❌ GROQ_API_KEY is not set. Add it to your .env file.")

# ✅ Initialize Groq client
client = Groq(api_key=api_key)


def classify_metrics(metrics):
    result = {}

    if "snr" in metrics:
        result["snr"] = "low" if metrics["snr"] < 10 else "good"

    if "motion" in metrics:
        result["motion"] = "high" if metrics["motion"] > 0.5 else "low"

    return result


def generate_explanation(metrics):
    classified = classify_metrics(metrics)

    snr = classified.get("snr", "unknown")
    motion = classified.get("motion", "unknown")

    prompt = f"""
You are an MRI quality control expert.

Metrics:
- Signal-to-Noise Ratio (SNR): {snr}
- Contrast-to-Noise Ratio (CNR): {metrics.get('cnr','unknown')}
- Full Width Half Maximum (FWHM): {metrics.get('fwhm','unknown')}
- Entropy Focus Criterion (EFC): {metrics.get('efc','unknown')}
- Motion Artifacts: {motion}

Explain the scan quality clearly in exactly 2 sentences.
Be concise and clinically meaningful.
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # ✅ Groq-supported model
            messages=[
                {"role": "system", "content": "You are a medical imaging expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"❌ Error generating explanation: {str(e)}"