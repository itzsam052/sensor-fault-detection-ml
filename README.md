# sensor-fault-detection-ml
# 🔍 Sensor Fault Detection using Machine Learning

## 📌 Overview
This project presents a Machine Learning-based system for detecting faults in sensor data. It focuses on identifying abnormal patterns such as sudden spikes and gradual drift in time-series signals, which are common in industrial systems.

The goal is to build a reliable fault detection system that can assist in predictive maintenance and reduce system failures.


---

## 📊 Results Preview

### Sensor Signal with Faults
![Signal](outputs/plots/signal.png)

### Confusion Matrix
![Confusion](outputs/plots/confusion_matrix.png)
## 🌍 Industrial Importance

Sensor fault detection is critical in modern industrial systems, where incorrect sensor readings can lead to system failures, safety risks, and increased maintenance costs.

Machine learning-based fault detection enables:
- Early detection of anomalies
- Reduction in downtime
- Improved system reliability
- Support for predictive maintenance

## ⚙️ Problem Statement
In industrial environments, sensors are used to monitor parameters like temperature, pressure, and vibration. Faulty sensor readings can lead to incorrect decisions and system failures.

This project aims to:
- Detect abnormal sensor behavior
- Classify signals as **Normal (0)** or **Fault (1)**
- Improve detection using feature engineering and ML models

---

## 🧠 Approach

### 1. Data Simulation
- Generated synthetic sensor signal using sinusoidal function
- Added noise to simulate real-world conditions
- Injected faults:
  - Spike faults (sudden increase)
  - Drift faults (gradual deviation)

---

### 2. Feature Engineering
To improve model performance, the following features were extracted:

- `signal` → raw sensor value  
- `rolling_mean` → short-term trend (window=5)  
- `rolling_std` → local variation  
- `diff` → sudden changes between values  
- `rolling_mean_long` → long-term trend (window=20)  

---

### 3. Model Used
- Random Forest Classifier
- Handled class imbalance using `class_weight='balanced'`

---

### 4. Evaluation Metrics
- Accuracy
- Precision
- Recall (focused on fault detection)
- Confusion Matrix

---

## 📈 Visualization



### Sensor Signal with Faults
![Signal](outputs/plots/signal.png)

### Confusion Matrix
![Confusion](outputs/plots/confusion_matrix.png)
## 📊 Results

- Accuracy: **85%**
- Fault Detection Recall: **68%**

### Confusion Matrix Insights:
- Successfully detected majority of faults
- Some faults missed (trade-off between precision and recall)
- Model prioritizes reducing false alarms while maintaining good detection

---

## 📁 Project Structure
sensor-fault-detection-ml/
│
├── data/
│ ├── sensor_data.csv
│ └── processed_data.csv
│
├── src/
│ ├── data_generation.py
│ ├── feature_engineering.py
│ ├── model.py
│ └── predict.py
│
├── outputs/
│ └── plots/
│
├── model.pkl
├── README.md
└── requirements.txt

---

## 🚀 How to Run

1. Install dependencies:
 pip install numpy pandas matplotlib scikit-learn seaborn joblib  

2. Generate data:
   python src/data_generation.py
   
3. Perform feature engineering:
   python src/feature_engineering.py
   
4. Train model:
python src/model.py

5. Run prediction:
   python src/predict.py
   

---

## 🔮 Future Scope
- Real-time fault detection system
- Integration with IoT sensors
- Use of deep learning models (LSTM for time-series)
- Deployment using Streamlit dashboard

---

## 👨‍💻 Author
**Sambhav Jindal**

---

## 💡 Key Learning
This project demonstrates how feature engineering and machine learning can be applied to solve real-world industrial problems like sensor fault detection.






















