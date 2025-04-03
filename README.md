🔥 **Gesture-Controlled LED System** – _"Điều khiển ánh sáng bằng sức mạnh của bàn tay"_ ✋💡  
> _Một dự án kết hợp Computer Vision & Arduino khiến **Iron Man** cũng phải gật gù._

---

## 💥 Giới thiệu

Chỉ với **1 chiếc webcam**, **5 ngón tay**, và **1 bảng mạch Arduino UNO**, bạn đã có thể **điều khiển ánh sáng theo từng cử động tay**.  
Không cần chạm. Không cần nút bấm. Chỉ cần **vẫy tay – LED sáng**.  
> Vì chúng ta không điều khiển công tắc nữa. Chúng ta điều khiển **ánh sáng bằng cử chỉ.**

---

## 🎯 Tính năng chính
- ✋ **Nhận diện 5 ngón tay** theo thời gian thực bằng Mediapipe + OpenCV.
- ⚡ **Gửi tín hiệu trực tiếp qua cổng Serial** đến Arduino.
- 💡 **Điều khiển 5 LED tương ứng với 5 ngón tay**.
- 🔁 **Phản hồi cực nhanh** – gần như tức thời.

---

## 🧠 Công nghệ sử dụng
| Thành phần        | Mô tả |
|-------------------|------|
| **Python**        | Xử lý video, nhận diện cử chỉ bàn tay |
| **Mediapipe**     | Nhận diện khung xương bàn tay, theo dõi ngón |
| **OpenCV**        | Giao diện camera, hiển thị real-time |
| **pySerial**      | Giao tiếp Serial với Arduino |
| **Arduino Uno**   | Nhận dữ liệu, điều khiển LED qua các chân số |
| **LED x5 + Breadboard** | Hiển thị trạng thái ngón tay bằng đèn sáng |

---

## ⚙️ Cài đặt

### 🔌 Arduino
1. Nạp đoạn mã sau vào Arduino UNO:
```cpp
int ledPins[] = {8, 9, 10, 11, 12};  // Thumb, Index, Middle, Ring, Pinky

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 5; i++) {
    pinMode(ledPins[i], OUTPUT);
  }
}

void loop() {
  if (Serial.available() >= 5) {
    for (int i = 0; i < 5; i++) {
      int fingerState = Serial.read();
      digitalWrite(ledPins[i], fingerState == 1 ? HIGH : LOW);
    }
  }
}
```

### 🐍 Python
```bash
pip install opencv-python mediapipe pyserial
```

### 📸 Chạy mã Python:
```bash
python hand_control_led.py
```

---

## 🧠 Cách hoạt động (chuẩn xác)
| Ngón tay ✋        | Chân Arduino | LED tương ứng |
|------------------|--------------|----------------|
| 👍 **Ngón cái**     | D8           | LED 1 (bên trái) |
| 👉 **Ngón trỏ**     | D9           | LED 2          |
| 🖕 **Ngón giữa**    | D10          | LED 3          |
| 💍 **Ngón áp út**   | D11          | LED 4          |
| 🤙 **Ngón út**      | D12          | LED 5 (bên phải) |

---

## 🤘 Vì sao nên thử dự án này?

- 🧑‍💻 Học được cách kết hợp giữa phần mềm và phần cứng
- ⚙️ Hiểu cơ bản về xử lý ảnh & giao tiếp Serial
- 🚀 Cảm giác **cực ngầu** khi điều khiển thiết bị chỉ bằng… tay không

> "Bấm nút là chuyện của thế kỷ trước. Bây giờ là thời của **cử chỉ.**"

---

## 💡 Mở rộng tiềm năng

- Điều khiển **quạt**, **rèm cửa**, **âm thanh**...
- Biến bàn tay bạn thành **remote vạn năng**  
- Tích hợp nhận diện cử chỉ nâng cao: 👋, ✌️, 🤘...

---

## 🧙 Tác giả
> Một kẻ đam mê công nghệ và không chấp nhận sống tầm thường.  
> Code như thể ngày mai tận thế.  
> Và LED phải sáng theo cách **ngầu nhất có thể.**  

---

Nếu bạn thấy dự án này thú vị, hãy ⭐️ **Star** nó như một cú "high five" nhé!
