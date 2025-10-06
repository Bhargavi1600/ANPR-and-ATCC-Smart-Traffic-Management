import torch
import cv2
import os
from src.utils import create_folder

VEHICLE_MODEL_PATH = "models/yolov5s.pt"

def count_vehicles(video_path, log_path):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    create_folder(os.path.dirname(log_path))

    cap = cv2.VideoCapture(video_path)
    log_file = open(log_path, 'w')
    log_file.write("frame,vehicle_count\n")

    frame_number = 0
    total_vehicles = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        detections = results.xyxy[0]
        vehicles = [x for x in detections if int(x[-1]) in [2, 3, 5, 7]]
        vehicle_count = len(vehicles)
        total_vehicles += vehicle_count
        log_file.write(f"{frame_number},{vehicle_count}\n")

        frame_number += 1

    cap.release()
    log_file.close()
    print(f"[INFO] ATCC done → Total Vehicles: {total_vehicles}")
    return total_vehicles
