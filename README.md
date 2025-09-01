#  Fraud Banking APK Detection using System Call Frequency

This project is a **Machine Learning-powered Flask web app** to detect whether an Android APK is **safe or malicious** based on its **system call frequencies- Perfect analysis at Operation System Level**.  

It allows:  
-  Uploading APK files (planned feature)  
-  Manual entry of system call frequencies via a **beautiful web form**  
-  Predicting results with a trained ML model (`Safe` ✅ or `Malicious` ❌)  
-  Interactive UI with **Flask, HTML, CSS, and JavaScript**

---

## Features
- **Machine Learning Model** trained on system call patterns of Android apps.  
- **Flask Backend** for model inference and API handling.  
- **Attractive UI** with:
  - Manual form for system call frequencies.
  - Animated prediction result page (glassmorphism + gradient design).  
- **Extensible** → Future integration with automatic APK system call extraction.

---

## 🛠️ Tech Stack
- **Backend:** Python, Flask  
- **ML Models:** CatBoost, LightGBM, XGBoost with Optuna hyperparameter tuning  
- **Frontend:** HTML5, CSS3 (modern styling), JavaScript (animations)  
- **Model Deployment:** Pickle (`model_syscalls.pkl`)  

---

## 📂 Project Structure
fraud-banking-apk-detection/  
│  
├── app.py                # Flask backend  
├── model_syscalls.pkl    # Trained ML model (system call classifier)  
│  
├── templates/            # HTML templates  
│   ├── manual_input.html # Input form for syscall frequencies  
│   └── result.html       # Prediction result page  
│  
├── static/               # Static files (CSS & JS)  
│   ├── style.css         # Styling for pages  
│   └── script.js         # Animations & interactivity  
│  
├── requirements.txt      # Python dependencies  
└── README.md             # Project documentation  


---

## ⚙️ Installation & Usage
pip install -r requirements.txt

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/VanshSa017/CyberShield_Hackathon 
cd CyberShield_Hackathon 
