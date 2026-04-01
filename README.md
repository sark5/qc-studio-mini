# 🧠 QC-Studio Mini

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A lightweight **MRI Quality Control (QC)** web application built with **Streamlit** for fast visual inspection, quality analysis, metadata review, and AI-assisted explainability.

QC-Studio Mini is designed as a **simple, modular, and extensible neuroimaging QC tool** for research workflows.

---

## ✨ Features

### 🧠 MRI Visualization

* Upload and inspect **NIfTI MRI scans** (`.nii`, `.nii.gz`)
* View slices in:

  * Sagittal (X)
  * Coronal (Y)
  * Axial (Z)
* Two viewer modes:

  * Matplotlib Viewer (static)
  * Niivue Viewer (interactive)

---

### 📊 QC Dashboard

* Basic MRI quality statistics:

  * Mean intensity
  * Standard deviation
  * Minimum intensity
  * Maximum intensity
* QC heuristics:

  * Low contrast detection
  * Possibly empty / corrupted scan detection
* IQM (Image Quality Metrics) support via `.tsv`

---

### 🧪 Explainability

* AI-generated explanations for MRI quality metrics
* Row-level interpretation of IQM data
* Supports:

  * Groq API
  * Fallback rule-based explanations

---

### 📄 Metadata Viewer

Inspect MRI file metadata:

* Dimensions
* Voxel spacing
* Data type
* Affine matrix

---

### 🆚 Compare Tab

* Compare two IQM rows
* Metric differences
* Quick summary

---

### ⬇️ Export

* Export QC summary as CSV
* Export IQM table

---

## 📁 Project Structure

```bash
qc-studio-mini/
│
├── app.py
├── requirements.txt
├── .env
│
├── components/
│   ├── uploader.py
│   └── iqm_table.py
│
├── loaders/
│   ├── mri_loader.py
│   └── iqm_loader.py
│
├── panels/
│   ├── viewer_panel.py
│   ├── qc_panel.py
│   ├── explainability_panel.py
│   ├── metadata_panel.py
│   ├── compare_panel.py
│   ├── export_panel.py
│   └── niivue_panel.py
│
├── services/
│   └── llm_explainer.py
│
├── utils/
│   └── image_utils.py
│
└── README.md
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/qc-studio-mini.git
cd qc-studio-mini
```

### 2. Create Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_api_key_here
```

If no API key is provided, the app will still run using a fallback explanation system.

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 🧭 How to Use

### Step 1 — Upload MRI File

Upload a `.nii` or `.nii.gz` file.

### Step 2 — Upload IQM File (Optional)

Upload `.tsv` file with metrics:

```
snr, cnr, efc, fwhm, motion
```

### Step 3 — Explore Tabs

#### 🧠 Viewer

* Slice visualization
* Axis selection
* Normalization toggle

#### 📊 QC Dashboard

* Scan statistics
* QC warnings
* IQM table

#### 🧪 Explainability

* Select row
* Generate AI explanation

#### 📄 Metadata

* Header info
* Affine matrix

#### 🆚 Compare

* Compare two rows

#### ⬇️ Export

* Download results

---

## 🧠 Module Breakdown

### app.py

* Main Streamlit app
* Tab navigation
* File handling

### components/

* uploader.py → File upload UI
* iqm_table.py → IQM display

### loaders/

* mri_loader.py → MRI loading
* iqm_loader.py → TSV loading

### panels/

* viewer_panel.py → Visualization
* qc_panel.py → QC stats
* explainability_panel.py → AI explanation
* metadata_panel.py → Metadata
* compare_panel.py → Comparison
* export_panel.py → Export

### services/

* llm_explainer.py → AI logic

### utils/

* image_utils.py → Image processing

---

## 📊 Example IQM TSV Format

```tsv
subject_id	snr	cnr	efc	fwhm	motion
sub-001	12.5	1.8	0.42	3.1	0.12
sub-002	7.2	0.9	0.76	4.5	0.61
```

---

## ⚠️ Notes

* Temporary MRI files are auto-deleted
* Niivue may not work in all environments
* Large MRI files may slow performance
* AI explanations are for research, not diagnosis

---

## 🚧 Future Enhancements

* PASS / WARN / FAIL scoring
* Advanced QC heuristics
* Batch processing
* PDF report export
* Multi-scan comparison
* 3D visualization
* MRIQC metric expansion

---

## 🎯 Why This Project

QC-Studio Mini focuses on:

* Simplicity
* Modularity
* Extensibility
* Research usability

---

## 🤝 Contributing

```bash
git checkout -b feature-name
git commit -m "Add feature"
git push origin feature-name
```

Then open a Pull Request 🚀

---

## 📄 License

MIT License
