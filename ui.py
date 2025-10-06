import streamlit as st
import os
import pandas as pd
from src.utils import create_folder
from src.anpr import detect_number_plate
from src.atcc import count_vehicles

st.set_page_config(page_title="Smart Traffic Management", layout="wide")
st.title("🚦 ANPR + ATCC Smart Traffic Management System")

# Folders for saving videos and outputs
output_folder = "output"
video_folder = "videos"
create_folder(output_folder)
create_folder(video_folder)

# Upload video
uploaded_file = st.file_uploader("Upload a traffic video", type=["mp4", "avi"])
if uploaded_file:
    video_path = os.path.join(video_folder, uploaded_file.name)
    with open(video_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("✅ Video uploaded successfully!")

    # Run ANPR
    if st.button("Run ANPR"):
        st.info("🚀 Running ANPR...")
        anpr_log = os.path.join(output_folder, "anpr_log.csv")
        annotated_video = os.path.join(output_folder, "annotated_video.mp4")

        detect_number_plate(video_path, annotated_video, anpr_log)
        st.video(annotated_video)
        st.success("✅ ANPR Completed!")

        # Clean and read ANPR CSV
        cleaned_lines = []
        with open(anpr_log, 'r', encoding='latin1') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) >= 2:
                    cleaned_lines.append(','.join(parts[:2]))

        with open(anpr_log, 'w', encoding='latin1') as f:
            f.write('\n'.join(cleaned_lines))

        df_anpr = pd.read_csv(anpr_log, encoding='latin1')
        st.dataframe(df_anpr)

    # Run ATCC
    if st.button("Run ATCC"):
        st.info("🚀 Running ATCC...")
        atcc_log = os.path.join(output_folder, "atcc_log.csv")
        total = count_vehicles(video_path, atcc_log)
        st.success(f"✅ ATCC Completed! Total Vehicles Detected: {total}")

        # Clean and read ATCC CSV
        cleaned_lines = []
        with open(atcc_log, 'r', encoding='latin1') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) >= 2:
                    cleaned_lines.append(','.join(parts[:2]))

        with open(atcc_log, 'w', encoding='latin1') as f:
            f.write('\n'.join(cleaned_lines))

        df_atcc = pd.read_csv(atcc_log, encoding='latin1')
        st.dataframe(df_atcc)
