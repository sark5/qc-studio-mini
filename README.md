# 🧠 QC-Studio Mini

### ⚡ AI-Powered MRI Quality Control for Research Workflows

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![AI](https://img.shields.io/badge/AI-Enabled-purple)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🚀 Overview

**QC-Studio Mini** is a lightweight, modular, and AI-assisted **MRI Quality Control platform** designed for fast inspection, explainable metrics analysis, and research-grade workflows.

Unlike heavy clinical systems, it focuses on:

* ⚡ Speed
* 🧠 Explainability
* 🧩 Modularity
* 🔬 Research usability

---

## ✨ Key Highlights

### 🧠 MRI Visualization

* Upload `.nii / .nii.gz` scans
* Multiplanar viewing:

  * Sagittal / Coronal / Axial
* Dual modes:

  * Static (Matplotlib)
  * Interactive (Niivue)

---

### 📊 Intelligent QC Dashboard

* Real-time statistics:

  * Mean, Std, Min, Max
* Automatic issue detection:

  * Low contrast
  * Empty / corrupted scans
* IQM support (`.tsv`)

---

### 🤖 AI Explainability Engine

* AI-generated MRI quality interpretation
* Row-level IQM analysis
* Dual-mode system:

  * Groq API (fast AI)
  * Rule-based fallback (offline safe)

---

### 📄 Metadata Intelligence

* Dimensions & voxel spacing
* Data type & affine matrix
* Quick structural insights

---

### 🆚 Smart Comparison

* Compare scans / IQM rows
* Highlight metric differences
* Fast decision support

---

### ⬇️ Export System

* QC summary (CSV)
* IQM data export
* Research-ready outputs

---

## 🧩 Why QC-Studio Mini?

| Feature           | QC-Studio Mini    | Competitor   |
| ----------------- | ----------------- | ------------ |
| Simplicity        | ✅ Clean & focused | ❌ Overloaded |
| Speed             | ⚡ Fast            | ⚠️ Heavy     |
| AI Explainability | ✅ Built-in        | ✅            |
| Modular Code      | ✅ Clear structure | ⚠️ Complex   |
| Beginner Friendly | ✅ Yes             | ❌ No         |

---

## 📁 Project Structure

```bash
qc-studio-mini/
│
├── app.py
├── components/
├── loaders/
├── panels/
├── services/
├── utils/
└── README.md
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/qc-studio-mini.git
cd qc-studio-mini

python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate (Windows)

pip install -r requirements.txt
```

---

## 🔐 Environment Setup

```env
GROQ_API_KEY=your_api_key_here
```

No API? No problem — fallback mode works ✅

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Open → http://localhost:8501

---

## 🧭 Workflow

### 1️⃣ Upload Data

* MRI (`.nii`)
* IQM (`.tsv`)

### 2️⃣ Analyze

* Visual inspection
* QC dashboard
* AI explanation

### 3️⃣ Decide

* Compare scans
* Review metrics

### 4️⃣ Export

* Download results

---

## 📊 Example IQM Format

```tsv
subject_id	snr	cnr	efc	fwhm	motion
sub-001	    12.5	1.8	0.42	3.1	    0.12
```

---

## ⚠️ Notes

* Large MRI files may slow performance
* Niivue may not work in all environments
* AI output is **not for medical diagnosis**

---

## 🚧 Roadmap

* PASS / WARN / FAIL scoring
* Batch processing
* 3D rendering
* PDF reports
* Advanced QC heuristics

---

## 🎯 Vision

To build a **lightweight, explainable, and developer-friendly MRI QC system** that bridges the gap between:

* Heavy clinical tools ❌
* Simple research tools ❌
* Smart AI-assisted workflows ✅

---

## 🤝 Contributing

```bash
git checkout -b feature-name
git commit -m "Add feature"
git push origin feature-name
```

---

## 📄 License

MIT License

---

## 🧠 Final Note

QC-Studio Mini is built for **learning, research, and innovation in neuroimaging QC** — not as a replacement for clinical expertise.
