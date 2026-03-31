#  QC-Studio Mini

A lightweight **MRI Quality Control (QC) web app** built with Streamlit.
It allows users to upload MRI scans, visualize slices interactively, analyze quality metrics, and generate AI-powered explanations.

---

##  Project Structure

```bash
qc-studio-mini/
│
├── app.py                    # Main Streamlit app
├── requirements.txt         # Dependencies
├── .env                     # Environment variables (API keys, etc.)
│
├── components/              # UI components
│   ├── uploader.py          # File upload UI
│   ├── iqm_table.py         # IQM table display
│
├── loaders/                 # Data loading logic
│   ├── mri_loader.py        # MRI loading (nibabel wrapper)
│   ├── iqm_loader.py        # IQM file parsing
│
├── panels/                  # Visualization panels
│   ├── niivue_panel.py      # Niivue viewer integration
│
├── services/                # Business logic / AI services
│   ├── llm_explainer.py     # AI explanation generator
│
├── utils/                   # Utility/helper functions
│   ├── image_utils.py       # Image processing helpers
│
├── venv/                    # Virtual environment (ignored in git)
└── __pycache__/             # Python cache (auto-generated)
```

---

##  Features

###  MRI Visualization

* Supports `.nii` and `.nii.gz` files
* Multi-axis viewing:

  * Sagittal (X)
  * Coronal (Y)
  * Axial (Z)
* Interactive slice navigation
* Optional normalization
* Two viewers:

  *  Matplotlib (static)
  *  Niivue (interactive)

---

###  Quality Control

* Computes:

  * Mean intensity
  * Standard deviation
* Detects:

  * Low contrast scans
  * Possibly corrupted or empty scans

---

###  IQM Support

* Upload `.tsv` IQM files
* Display structured table
* AI-generated explanations per row

---

###  Metadata Viewer

* Dimensions
* Voxel spacing
* Data type
* Affine matrix

---

##  Installation

### 1. Clone the repo

```bash
git clone https://github.com/sark5/qc-studio-mini.git
cd qc-studio-mini
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

##  Requirements

Typical dependencies:

```txt
streamlit
nibabel
numpy
matplotlib
pandas
python-dotenv
```

---

##  Run the App

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

##  Module Breakdown

###  `app.py`

Main entry point:

* Handles UI layout
* Manages tabs (Viewer, QC, Metadata)
* Connects all modules

---

###  `components/`

Reusable UI pieces:

* **uploader.py** → File upload logic
* **iqm_table.py** → Displays IQM data in table form

---

###  `loaders/`

Data ingestion layer:

* **mri_loader.py** → Loads MRI using nibabel
* **iqm_loader.py** → Reads IQM `.tsv` files

---

###  `panels/`

Visualization modules:

* **niivue_panel.py** → Web-based MRI viewer

---

###  `services/`

Core logic / AI:

* **llm_explainer.py** → Generates explanations for IQMs

---

###  `utils/`

Helper utilities:

* **image_utils.py**:

  * Slice extraction
  * Normalization
  * Image transformations

---

##  Environment Variables

Create a `.env` file if using LLM APIs:

```env
OPENAI_API_KEY=your_api_key_here
```

---

##  Workflow

1. Upload MRI file
2. (Optional) Upload IQM file
3. Adjust viewer settings
4. Explore:

   * Viewer tab → visualize scan
   * QC tab → analyze quality
   * Metadata tab → inspect scan details
5. Generate AI explanations

---

##  Notes

* Temporary MRI files are created during runtime and deleted automatically
* Niivue viewer may fail in some environments (handled gracefully)
* Large MRI files may impact performance

---

##  Future Enhancements

* 3D volume rendering
* Advanced QC metrics (SNR, motion artifacts)
* Batch uploads
* Export reports (PDF/CSV)
* Drag-and-drop UI improvements

---

## Community Interaction

- Shared prototype in discussion group
- Reached out to mentors via email
- Documented development challenges and learnings

##  Contributing

Feel free to:

* Fork the repo
* Create feature branches
* Submit pull requests

---

##  License

MIT License

---

##  Acknowledgements

* Streamlit
* NiBabel
* Matplotlib
* Niivue

---

##  Pro Tip

For best results:

* Use high-resolution MRI scans
* Provide well-formatted IQM `.tsv` files

---

Happy QC’ing! 🧠✨
