# 🚗✨ ANPR + ATCC Smart Traffic Management

## 🎀 Project Overview
This project implements an intelligent traffic management system using **Automatic Number Plate Recognition (ANPR)** and **Automatic Traffic Counting & Classification (ATCC)**.  
Leveraging Deep Learning and Object Detection (YOLOv5), the system automates traffic monitoring for smart city environments.

---

## 🌟 Key Features
- 📋 **ANPR** – Detects and reads vehicle number plates from videos.  
- 🚥 **ATCC** – Counts vehicles per frame and logs traffic data.  
- 📉 **CSV Logging** – Generate structured logs for analysis.  
- 🎬 **Visualization** – Annotated videos of traffic with detected plates and vehicle counts.  

---

## 🎬 Results
- Annotated video: `output/annotated_video.mp4`  
- ANPR CSV: `output/anpr_log.csv` (frame, license_number)  
- ATCC CSV: `output/atcc_log.csv` (frame, vehicle_count)  

---

## 🚀 Workflow
1. **Run Streamlit interface**
```bash
streamlit run ui.py

2.Upload a traffic video in the interface.

3.Run ANPR → annotated video + license plate CSV generated.

4.Run ATCC → vehicle count CSV generated.

5.Repeat with new videos; use timestamps in output filenames to keep logs separate.



🛠️ Setup and Installation

1. Clone the repository

git clone <your-repo-url>
cd ANPR_ATCC

2. Create & activate virtual environment

python -m venv .venv
# Windows
.venv\Scripts\Activate.ps1
# Mac/Linux
source .venv/bin/activate


3.Install dependencies

pip install --upgrade pip
pip install -r requirements.txt


4. Place YOLOv5 model

models/best_model.pt

-----------------------------------------------------------------

📁 Folder Structure

ANPR_ATCC/
├─ .venv/               # Python virtual environment
├─ models/
│   └─ best_model.pt    # YOLOv5 weights
├─ src/
│   ├─ anpr.py          # ANPR detection
│   ├─ atcc.py          # Vehicle counting
│   └─ utils.py         # Helper functions
├─ videos/              # Uploaded videos
├─ output/              # Annotated videos & CSV logs
├─ ui.py                # Streamlit interface
├─ requirements.txt     # Python dependencies
└─ README.md            # Documentation


⚡ Tips

Use unique filenames or timestamps for multiple runs:

annotated_video = os.path.join(output_folder, f"annotated_{uploaded_file.name}")
anpr_log = os.path.join(output_folder, f"anpr_log_{uploaded_file.name}.csv")
atcc_log = os.path.join(output_folder, f"atcc_log_{uploaded_file.name}.csv")


**Ensure the virtual environment is activated before running Streamlit.

**Videos >200MB may take longer to process.