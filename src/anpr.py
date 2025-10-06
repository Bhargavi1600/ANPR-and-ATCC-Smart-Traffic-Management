import torch
import cv2
import os
from src.utils import extract_text_from_plate, create_folder

MODEL_PATH = "models/best_model.pt"

def detect_number_plate(video_path, output_path, log_path):
    # Ensure output folder exists
    create_folder(os.path.dirname(output_path))
    
    # Load YOLOv5 model from local path
    model = torch.hub.load('yolov5', 'custom', path=MODEL_PATH, source='local')
    
    # Open video
    cap = cv2.VideoCapture(video_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    # Open log file
    log_file = open(log_path, 'w')
    log_file.write("frame,license_number\n")

    frame_number = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Run YOLOv5
        results = model(frame)
        # Make a writable copy of annotated frame
        annotated_frame = results.render()[0].copy()

        # Iterate over detected plates
        for *xyxy, conf, cls in results.xyxy[0]:
            x1, y1, x2, y2 = map(int, xyxy)
            plate_img = frame[y1:y2, x1:x2]
            license_number = extract_text_from_plate(plate_img)
            log_file.write(f"{frame_number},{license_number}\n")

            # Draw text safely on writable frame
            cv2.putText(annotated_frame, license_number, (x1, max(y1-10,0)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

        out.write(annotated_frame)
        frame_number += 1

    # Release resources
    cap.release()
    out.release()
    log_file.close()
    print(f"[INFO] ANPR done → {output_path}, log → {log_path}")
