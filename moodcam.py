import cv2
from fer import FER
import time
import numpy as np

# --- 1. INISIALISASI ---
# Gunakan mtcnn=True untuk akurasi tinggi, atau False jika ingin FPS lebih kencang
detector = FER(mtcnn=False) 

cap = cv2.VideoCapture(0)
pTime = 0
window_name = "MoodCam"

# Warna untuk tiap emosi (BGR Format)
emotion_colors = {
    "angry": (0, 0, 255),        # Merah
    "disgust": (0, 255, 0),      # Hijau
    "fear": (255, 0, 255),       # Ungu
    "happy": (0, 255, 255),      # Kuning
    "sad": (255, 0, 0),          # Biru
    "surprise": (0, 165, 255),   # Oranye
    "neutral": (200, 200, 200)   # Abu-abu
}

print("📸 MoodCam Berhasil Dijalankan! Tekan 'Q' untuk keluar.")

while True:
    success, img = cap.read()
    if not success: break
    img = cv2.flip(img, 1) # Mirroring
    
    # --- 2. PROSES DETEKSI ---
    # Model CNN bekerja di sini untuk menganalisis ekspresi wajah
    results = detector.detect_emotions(img)

    # Iterasi setiap wajah yang tertangkap kamera
    for face in results:
        (x, y, w, h) = face["box"]
        emotions = face["emotions"]

        # Ambil emosi dengan nilai probabilitas tertinggi
        top_emotion = max(emotions, key=emotions.get)
        confidence = emotions[top_emotion]
        
        # Ambil warna sesuai emosi
        color = emotion_colors.get(top_emotion, (255, 255, 255))

        # Tampilkan Efek Visual
        # Kotak Wajah
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        
        # Label Emosi di atas kotak
        label = f"{top_emotion.upper()} ({int(confidence*100)}%)"
        cv2.putText(img, label, (x, y - 10), cv2.FONT_HERSHEY_DUPLEX, 0.7, color, 2)
        
        # Mood Indicator Besar di Tengah Atas
        cv2.rectangle(img, (0, 0), (800, 50), (0, 0, 0), -1) # Header bar
        cv2.putText(img, f"CURRENT MOOD: {top_emotion.upper()}", (250, 35), 
                    cv2.FONT_HERSHEY_TRIPLEX, 0.8, color, 2)

    # --- 3. PERFORMANCE MONITOR ---
    cTime = time.time()
    fps = 1 / (cTime - pTime) if (cTime - pTime) > 0 else 0
    pTime = cTime
    
    cv2.putText(img, f'FPS: {int(fps)}', (20, 80), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 255, 255), 2)

    cv2.imshow(window_name, img)

    # Keluar dengan tombol 'q' atau klik tombol silang (X)
    if cv2.waitKey(1) & 0xFF == ord('q') or cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()