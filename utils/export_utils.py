import json

def build_qc_report_json(scan_qc, iqm_qc, selected_metrics):
    report = {
        "scan_qc": scan_qc,
        "iqm_qc": iqm_qc,
        "selected_metrics": selected_metrics
    }

    return json.dumps(report, indent=2, default=str)