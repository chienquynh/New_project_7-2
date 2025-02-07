import cv2
from ultralytics import YOLO

# Load mô hình YOLOv8
model = YOLO("yolov8n.pt")

# Mở webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Dự đoán vật thể trong khung hình
    results = model(frame)

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Lấy tọa độ vật thể
            confidence = float(box.conf[0])  # Độ chính xác
            class_id = int(box.cls[0])  # ID của vật thể
            label = model.names[class_id]  # Lấy tên vật thể

            # Vẽ hình chữ nhật quanh vật thể
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # Hiển thị tên vật thể và độ chính xác
            text = f"{label} ({confidence:.2f})"
            cv2.putText(frame, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Hiển thị khung hình
    cv2.imshow("Object Detection", frame)

    # Nhấn 'q' để thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
