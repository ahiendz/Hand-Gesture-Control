import cv2  # Thư viện OpenCV để xử lý video
import mediapipe as mp  # Thư viện Mediapipe để nhận diện bàn tay
import serial  # Thư viện giao tiếp với cổng nối tiếp (Arduino)
import time  # Thư viện để điều khiển thời gian chờ

# Khởi tạo kết nối Serial với Arduino
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)
time.sleep(2)  # Đợi 2 giây để kết nối Serial ổn định

# Khởi tạo Mediapipe Hand Tracking
mp_hands = mp.solutions.hands  # Module phát hiện bàn tay
hands = mp_hands.Hands()  # Đối tượng để nhận diện bàn tay
mp_drawing = mp.solutions.drawing_utils  # Công cụ vẽ khung bàn tay

# Hàm phát hiện ngón tay giơ lên (1: lên, 0: xuống)
def detect_fingers(image, hand_landmarks):
    finger_tips = [8, 12, 16, 20]  # ID các đầu ngón: trỏ, giữa, áp út, út
    thumb_tip = 4  # ID đầu ngón cái
    finger_states = [0, 0, 0, 0, 0]  # Trạng thái 5 ngón: cái, trỏ, giữa, áp út, út

    # Kiểm tra ngón cái (dựa trên vị trí x)
    if hand_landmarks.landmark[thumb_tip].x < hand_landmarks.landmark[thumb_tip - 1].x:
        finger_states[0] = 1  # Ngón cái giơ lên

    # Kiểm tra các ngón còn lại (dựa trên vị trí y)
    for idx, tip in enumerate(finger_tips):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            finger_states[idx + 1] = 1  # Ngón trỏ, giữa, áp út, út giơ lên

    return finger_states

# Bắt đầu thu video từ webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()  # Đọc khung hình từ webcam
    if not success:
        break  # Dừng nếu không nhận được hình ảnh

    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)  # Lật hình và chuyển màu
    results = hands.process(image)  # Xử lý để tìm bàn tay
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # Đổi lại màu để hiển thị

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)  # Vẽ khung tay
            fingers_state = detect_fingers(image, hand_landmarks)  # Phát hiện trạng thái ngón
            arduino.write(bytes(fingers_state))  # Gửi trạng thái ngón tay qua cổng Serial
            print(f"Fingers State: {fingers_state}")  # In trạng thái ra màn hình

    cv2.imshow('Hand Tracking', image)  # Hiển thị hình ảnh
    if cv2.waitKey(5) & 0xFF == 27:  # Nhấn phím ESC để thoát
        break

cap.release()  # Giải phóng camera
cv2.destroyAllWindows()  # Đóng tất cả cửa sổ OpenCV
arduino.close()  # Đóng kết nối Serial