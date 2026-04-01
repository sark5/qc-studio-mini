# 🧠 QC-Studio Mini

### ⚡ AI-Powered MRI Quality Control for Research Workflows

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![AI](https://img.shields.io/badge/AI-Enabled-purple)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🚀 Overview

**QC-Studio Mini** is a lightweight, modular, and AI-assisted **MRI Quality Control (QC) platform** designed for fast visual inspection, quantitative analysis, and explainable decision-making.

It is built specifically for:

* 🧠 Neuroimaging researchers
* 📊 MRIQC-based workflows
* 🧪 Experimental AI-assisted QC pipelines

Unlike heavy clinical systems, QC-Studio Mini emphasizes:

* ⚡ Fast interaction
* 🧩 Modular architecture
* 🧠 Explainable AI outputs
* 🔬 Research-first design

---

## ✨ Core Features

### 🧠 MRI Visualization Engine

* Upload **NIfTI MRI scans** (`.nii`, `.nii.gz`)
* Multi-planar slice visualization:

  * Sagittal (X-axis)
  * Coronal (Y-axis)
  * Axial (Z-axis)
* Dual viewing modes:

  * **Matplotlib Viewer** → lightweight & stable
  * **Niivue Viewer** → interactive & responsive
* Slice navigation with index control
* Optional intensity normalization

---

### 📊 Quality Control Dashboard

Perform quick, interpretable QC checks:

#### 📈 Basic Statistics

* Mean intensity
* Standard deviation
* Minimum / Maximum values

#### ⚠️ Heuristic Checks

* Low contrast detection
* Near-empty scan detection
* Abnormal intensity distribution

#### 📂 IQM Integration

* Upload `.tsv` MRIQC files
* Supports metrics such as:

  * SNR (Signal-to-Noise Ratio)
  * CNR (Contrast-to-Noise Ratio)
  * EFC (Entropy Focus Criterion)
  * FWHM (Smoothness)
  * Motion parameters

---

### 🤖 AI Explainability Engine

Transform raw metrics into **human-readable insights**:

* AI-generated explanations for MRI quality
* Row-level interpretation of IQM data
* Context-aware reasoning based on metrics

#### Modes:

* ⚡ **Groq API (LLM-based)** → fast inference
* 🧠 **Rule-based fallback** → offline reliability

#### Output includes:

* Quality interpretation
* Potential issues
* Suggested actions

---

### 📄 Metadata Intelligence

Extract and display MRI header information:

* Image dimensions
* Voxel spacing
* Data type
* Affine transformation matrix

Useful for:

* Debugging pipelines
* Understanding acquisition parameters

---

### 🆚 Comparison Module

Compare two scans or IQM rows:

* Side-by-side metric comparison
* Difference highlighting
* Quick evaluation support

---

### ⬇️ Export & Reporting

* Export QC summary as CSV
* Export IQM tables
* Lightweight reporting for research workflows

---

## 🧩 System Architecture

QC-Studio Mini follows a **modular, layered design**:

```text
UI Layer (Streamlit)
   ↓
Panels (Feature Modules)
   ↓
Loaders (Data Processing)
   ↓
Services (AI / Logic)
   ↓
Utils (Helpers)
```

### Key Principles:

* Separation of concerns
* Easy extensibility
* Replaceable AI backend
* Lightweight execution

---

## 📁 Project Structure

```bash id="gq1l9n"
qc-studio-mini/
│
├── app.py                  # Main Streamlit app
├── requirements.txt
├── .env
│
├── components/             # UI components
│   ├── uploader.py
│   └── iqm_table.py
│
├── loaders/                # Data loading logic
│   ├── mri_loader.py
│   └── iqm_loader.py
│
├── panels/                 # Feature modules
│   ├── viewer_panel.py
│   ├── qc_panel.py
│   ├── explainability_panel.py
│   ├── metadata_panel.py
│   ├── compare_panel.py
│   ├── export_panel.py
│   └── niivue_panel.py
│
├── services/               # AI / business logic
│   └── llm_explainer.py
│
├── utils/                  # Helper functions
│   └── image_utils.py
│
└── README.md
```

---

## ⚙️ Installation

```bash id="7dn2k5"
git clone https://github.com/your-username/qc-studio-mini.git
cd qc-studio-mini

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

---

## 🔐 Environment Configuration

Create a `.env` file:

```env id="9xj2sl"
GROQ_API_KEY=your_api_key_here
```

If no API key is provided:

* The system automatically switches to fallback mode ✅

---

## ▶️ Running the Application

```bash id="d5ytg0"
streamlit run app.py
```

Access:

```
http://localhost:8501
```

---

## 🧭 Usage Workflow

### Step 1 — Upload Data

* MRI scan (`.nii / .nii.gz`)
* Optional IQM file (`.tsv`)

### Step 2 — Explore

* Visual inspection (Viewer tab)
* QC metrics (Dashboard tab)

### Step 3 — Analyze

* Generate AI explanations
* Identify potential issues

### Step 4 — Compare

* Compare scans or subjects

### Step 5 — Export

* Download QC summaries

---

## 📊 Example IQM Format

```tsv id="kq5w6k"
subject_id	snr	cnr	efc	fwhm	motion
sub-001	12.5	1.8	0.42	3.1	0.12
sub-002	7.2	0.9	0.76	4.5	0.61
```

---

## ⚠️ Limitations

* Not intended for clinical diagnosis
* Performance depends on MRI size
* Niivue may not work in all environments
* AI outputs may require human validation

---

## 🚧 Future Enhancements

* PASS / WARN / FAIL scoring system
* Batch processing pipeline
* 3D volume rendering
* Advanced QC heuristics
* PDF report generation
* Integration with MRIQC / BIDS pipelines

---

## 🎯 Design Goals

QC-Studio Mini is built with the following principles:

* **Simplicity over complexity**
* **Explainability over black-box AI**
* **Modularity over monolithic design**
* **Research usability over clinical rigidity**

---

## 🤝 Contributing

Contributions are welcome!

```bash id="v1wq2m"
git checkout -b feature-name
git commit -m "Add feature"
git push origin feature-name
```

---

## 📄 License

MIT License

---

## 🧠 Disclaimer

This tool is intended for **research and educational purposes only**.
It should not be used as a substitute for professional medical diagnosis or clinical decision-making.
