def interpret_metric(name, value):
    explanations = {
        "snr": "Signal-to-Noise Ratio: higher is usually better and indicates cleaner signal.",
        "cnr": "Contrast-to-Noise Ratio: reflects how well tissues are visually separable.",
        "efc": "Entropy Focus Criterion: higher values may suggest ghosting, blur, or motion-related disorder.",
        "cjv": "Coefficient of Joint Variation: may reflect poor gray-white matter separation when elevated.",
        "fber": "Foreground-Background Energy Ratio: low values can indicate poor foreground signal quality.",
        "fwhm": "Full Width Half Maximum: relates to image smoothness or blurring.",
        "motion": "Motion estimate: higher values suggest subject movement during acquisition."
    }

    return explanations.get(name.lower(), f"{name}: No explanation available yet.")