import cv2
import mediapipe as mp
import csv
import os

# Setup MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1)
mp_drawing = mp.solutions.drawing_utils

# Directory to save gesture data
DATA_DIR = "gesture_data"
os.makedirs(DATA_DIR, exist_ok=True)

# Get label input
label = input("Enter the label for this gesture (e.g., A, Hello): ").strip()
file_path = os.path.join(DATA_DIR, f"data_{label}.csv")

# Create CSV with header if it doesn't exist
if not os.path.exists(file_path):
    with open(file_path, mode='w', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['label'] + [f'{i}_{coord}' for i in range(21) for coord in ['x', 'y', 'z']])

# Open webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("[!] Could not access the webcam.")
    exit()

print("[INFO] Press 's' to save a frame. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("[!] Failed to grab frame.")
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            landmarks = []
            for lm in hand_landmarks.landmark:
                landmarks.extend([lm.x, lm.y, lm.z])

            key = cv2.waitKey(1)
            if key == ord('s'):
                with open(file_path, mode='a', newline='') as f:
                    csv_writer = csv.writer(f)
                    csv_writer.writerow([label] + landmarks)
                print(f"[+] Saved frame for gesture: {label}")

    # Display frame
    cv2.imshow("Collecting Gesture Data", frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        print("[INFO] Exiting...")
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
