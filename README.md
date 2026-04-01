# 🧠 QC-Studio Mini

A lightweight **MRI Quality Control (QC)** web application built with **Streamlit** for fast visual inspection, basic quality analysis, metadata review, and AI-assisted explainability.

QC-Studio Mini is designed as a **simple, modular, and extensible neuroimaging QC tool** for research workflows.

---

## ✨ Features

### 🧠 MRI Visualization
- Upload and inspect **NIfTI MRI scans** (`.nii`, `.nii.gz`)
- View slices in:
  - **Sagittal (X)**
  - **Coronal (Y)**
  - **Axial (Z)**
- Two viewer modes:
  - **Matplotlib Viewer** (static)
  - **Niivue Viewer** (interactive)

### 📊 QC Dashboard
- Basic MRI quality statistics:
  - Mean intensity
  - Standard deviation
  - Minimum intensity
  - Maximum intensity
- Simple QC heuristics:
  - Low contrast detection
  - Possibly empty / corrupted scan detection
- IQM (Image Quality Metrics) review from uploaded `.tsv` files

### 🧪 Explainability
- AI-generated explanations for MRI quality metrics
- Row-level interpretation of uploaded IQM data
- Supports:
  - **Groq API**
  - Fallback local rule-based explanation if API is unavailable

### 📄 Metadata Viewer
Inspect MRI file metadata such as:
- Dimensions
- Voxel spacing
- Data type
- Affine transformation matrix

### 🆚 Compare Tab
Compare two IQM rows / scans side-by-side:
- Numeric metric differences
- Quick metric summary
- Visual trend comparison

### ⬇️ Export
Export:
- QC summary as CSV
- Uploaded IQM table as CSV

---

## 📁 Project Structure
qc-studio-mini/
│
├── app.py
├── requirements.txt
├── .env
│
├── components/
│ ├── uploader.py
│ └── iqm_table.py
│
├── loaders/
│ ├── mri_loader.py
│ └── iqm_loader.py
│
├── panels/
│ ├── viewer_panel.py
│ ├── qc_panel.py
│ ├── explainability_panel.py
│ ├── metadata_panel.py
│ ├── compare_panel.py
│ ├── export_panel.py
│ └── niivue_panel.py
│
├── services/
│ └── llm_explainer.py
│
├── utils/
│ └── image_utils.py
│
└── README.md


---

## 🚀 Installation

1) Clone the repository

```bash
git clone https://github.com/your-username/qc-studio-mini.git
cd qc-studio-mini
Create a virtual environment

Windows

python -m venv venv
venv\Scripts\activate

macOS / Linux

python -m venv venv
source venv/bin/activate
Install dependencies
pip install -r requirements.txt
🔐 Environment Variables

If you want to use AI explanations via Groq, create a .env file in the project root:

GROQ_API_KEY=your_api_key_here

If no valid API key is provided, the app will still run using a fallback rule-based explanation system.

▶️ Run the App
streamlit run app.py

Then open in your browser:

http://localhost:8501

🧭 How to Use
Step 1 — Upload MRI File

Upload a .nii or .nii.gz MRI scan from the sidebar.

Step 2 — (Optional) Upload IQM File

Upload a .tsv file containing image quality metrics such as:

snr, cnr, efc, fwhm, motion
Step 3 — Explore Tabs

🧠 Viewer
Inspect slices using static and interactive viewers. Choose axis and slice index. Enable/disable normalization.

📊 QC Dashboard
Review basic scan statistics, inspect uploaded IQM table, and view simple QC warnings.

🧪 Explainability
Select an IQM row and generate AI-assisted scan quality interpretation.

📄 Metadata
Review MRI header details and affine matrix.

🆚 Compare
Select two IQM rows and compare metric values side-by-side.

⬇️ Export
Download QC summary or IQM table.

🧠 Module Breakdown
app.py – Main Streamlit application: page layout, file loading, tab creation, backend connections.
components/ – Reusable UI components:
uploader.py → file upload interface
iqm_table.py → IQM table rendering + warning flags
loaders/ – Data loading logic:
mri_loader.py → loads MRI scans using NiBabel
iqm_loader.py → reads IQM .tsv files
panels/ – Main app tabs:
viewer_panel.py → MRI slice viewer
qc_panel.py → QC dashboard
explainability_panel.py → AI interpretation
metadata_panel.py → MRI metadata display
compare_panel.py → row/subject comparison
export_panel.py → CSV export tools
niivue_panel.py → interactive Niivue MRI viewer
services/ – Application logic / AI services:
llm_explainer.py → AI or fallback QC explanations
utils/ – Helper functions:
image_utils.py → slice extraction, normalization, best-slice selection
📊 Example IQM TSV Format
subject_id	snr	cnr	efc	fwhm	motion
sub-001	12.5	1.8	0.42	3.1	0.12
sub-002	7.2	0.9	0.76	4.5	0.61

Supported columns may include: snr, cnr, efc, fwhm, motion. Additional numeric columns are also supported.

⚠️ Notes
Temporary MRI files are created during loading and removed automatically.
Niivue may fail in some browser/local environments (handled gracefully).
Very large MRI volumes may impact performance.
AI explanations are intended for research assistance, not diagnosis.
🚧 Future Enhancements
PASS / WARN / FAIL scoring engine
Better QC heuristics
Batch IQM review
PDF report export
Multi-scan comparison
3D volume rendering
Region-aware best-slice selection
Additional MRIQC metric support
🎯 Why This Project

QC-Studio Mini was built to explore how lightweight, interpretable tooling can simplify MRI quality control workflows for neuroimaging datasets. Focus is on:

Usability
Modular design
Extensibility
Practical research workflow support

rather than overcomplicated interfaces or overclaiming clinical capability.

🤝 Contributing

Contributions are welcome. You can contribute by:

Improving QC heuristics
Adding MRIQC metric support
Enhancing visualizations
Improving explainability
Adding export/reporting features

Suggested workflow:

git checkout -b feature-name
git commit -m "Add feature"
git push origin feature-name

Then open a pull request.

📄 License

MIT License

🙏 Acknowledgements

Built using:

Streamlit
NiBabel
Matplotlib
Niivue
Groq
⚠️ Disclaimer

This project is intended for research, educational, and prototyping purposes only.
It is not a medical device and should not be used for clinical diagnosis or treatment decisions without expert review.


---

If you want, I can also create a **version with collapsible sections** for GitHub so it’s easier to navigate without scrolling endlessly.  

Do you want me to make that?
