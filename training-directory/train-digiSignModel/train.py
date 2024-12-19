from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO("yolov8n.pt")  # 'yolov8n.pt' is a lightweight model; you can try others like 'yolov8m.pt' for better accuracy

# Train the model on the signature detection dataset
results = model.train(data="signature.yaml", epochs=100, imgsz=640)
