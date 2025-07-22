# 🤖 Real-Time Hand Gesture Recognition

This project is a real-time hand gesture recognition system built using **Python**, **OpenCV**, and **Mediapipe**. It captures hand landmarks from your webcam, allows you to record custom gestures, trains a classifier, and then predicts them live on screen.  

---

## 📦 Features

- 📷 Real-time hand detection with Mediapipe
- ✋ Custom gesture recording (CSV format)
- 🧠 KNN model for gesture classification
- ⚡ Live gesture prediction with FPS counter
- 🧪 Easy to extend with new gestures
- 🧼 Clean modular structure

---

## 🗂️ Project Structure

```
FaceDetectionApp/
│
├── gesture_data/               # Saved CSV data for each gesture
│   ├── peace.csv
│   ├── rock.csv
│   └── ...
│
├── combined_data.csv           # Combined dataset
├── trained_knn_model.pkl       # Saved classifier model
│
├── data_collector.py           # Collects hand gesture data and saves to CSV
├── combine_data.py             # Combines all CSVs into one
├── train_model.py              # Trains the KNN model
├── predict_live.py             # Real-time webcam prediction
│
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Collect gesture data
```bash
python data_collector.py
```
- Follow prompts to record gestures like `peace`, `rock`, `ok`, etc.

### 3. Combine all gesture data
```bash
python combine_data.py
```

### 4. Train the model
```bash
python train_model.py
```

### 5. Run real-time prediction
```bash
python predict_live.py
```

---

## ✋ Supported Gestures (so far)
- 👍 Good job  
- 👎 Dislike  
- 🧘 Peace  
- 🤘 Rock  
- 🤞 Good luck  
- 👌 OK  
- ✋ Stop  

---

## 📌 Notes
- You can easily add more gestures by recording new ones in `data_collector.py` and repeating the steps above.
- This project is beginner-friendly and modular — feel free to customize!

---

## 🔗 Connect With Me

Made with ❤️ by [Shirin](https://github.com/shirin292006)  
Feel free to [connect on LinkedIn](https://www.linkedin.com/in/shirin-bhattacharjee-2819702b6/) and drop a ⭐ if you liked it!

---

## 🛠️ Future Enhancements
- Add CNN model for more accuracy
- Support dual-hand gestures
- Export gesture events as keyboard shortcuts
