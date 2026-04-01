# 📸 MoodCam AI: Real-Time Facial Emotion Recognition

**MoodCam** adalah aplikasi deteksi emosi wajah berbasis kecerdasan buatan (AI) yang menggunakan kamera laptop untuk menganalisis ekspresi pengguna secara real-time. Proyek ini menggunakan model *Convolutional Neural Network* (CNN) yang sudah dilatih sebelumnya (Pre-trained) untuk mengklasifikasikan 7 emosi dasar manusia.



## 🚀 Fitur Utama
- **Real-Time Analysis:** Deteksi emosi instan dengan *frame-per-second* (FPS) monitor.
- **7 Emotion Categories:** Happy, Sad, Angry, Surprise, Fear, Disgust, dan Neutral.
- **Dynamic UI:** Kotak deteksi wajah berubah warna sesuai dengan emosi yang dirasakan.
- **Mood Indicator:** Header bar khusus yang menampilkan emosi dominan saat ini.

## 💻 Spesifikasi Sistem (Tested On)
- **OS:** Windows 11
- **Python Version:** 3.12.x (Sangat disarankan dibanding 3.13)

## 📦 Dependency & Versi Library (WAJIB)
Berdasarkan hasil *debugging*, versi berikut adalah yang paling stabil untuk menghindari konflik `StringDType` dan `pkg_resources`:

| Library | Versi | Fungsi |
| :--- | :--- | :--- |
| **FER** | `22.5.1` | Logika utama deteksi emosi |
| **TensorFlow** | `2.16.x` | Backend Machine Learning (Deep Learning) |
| **NumPy** | `2.0.0+` | Komputasi matriks (Harus v2 untuk TensorFlow terbaru) |
| **Setuptools** | `69.5.1` | Menyediakan `pkg_resources` untuk library FER |
| **OpenCV-Python**| `Terbaru` | Mengambil input kamera dan rendering visual |

## ⚙️ Cara Instalasi
Buka terminal VS Code (jalur Python 3.12) dan jalankan perintah berikut secara berurutan:

```powershell
# 1. Update NumPy ke versi terbaru (v2)
pip install --upgrade numpy

# 2. Instal setuptools versi spesifik (Legacy)
pip install setuptools==69.5.1

# 3. Instal library FER versi stabil
pip install fer==22.5.1

# 4. Instal OpenCV
pip install opencv-python
