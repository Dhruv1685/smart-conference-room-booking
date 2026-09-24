import cv2
import time
import requests
from pyzbar.pyzbar import decode

PI_IP = "172.20.10.3"
URL = f"http://{PI_IP}:5000/scan"

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open webcam")
    exit()

last_data = ""
last_time = 0
cooldown = 3

print("Scanner started")
print("Press ESC to exit")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        break

    barcodes = decode(frame)

    for barcode in barcodes:
        data = barcode.data.decode("utf-8")
        current_time = time.time()

        x, y, w, h = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(
            frame,
            data,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

        if data != last_data or (current_time - last_time) > cooldown:
            print("Scanned:", data)

            try:
                response = requests.post(URL, json={"barcode": data}, timeout=10)
                print("Pi response:", response.status_code, response.json())
            except Exception as e:
                print("Error sending to Pi:", e)

            last_data = data
            last_time = current_time

    cv2.imshow("Barcode Scanner", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()