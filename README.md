# 🔍 Sensor Fault Detection System using Machine Learning

## 🧠 Problem Statement

Modern industrial systems rely heavily on sensors for monitoring and decision-making. However, faulty sensors can lead to incorrect readings, system failures, and increased maintenance costs.

This project aims to detect faulty sensors at an early stage using Machine Learning techniques, helping improve system reliability and reduce operational risks.

---

## ⚙️ Approach

The system follows a complete Machine Learning pipeline:

1. **Data Preprocessing**

   * Handling missing values
   * Data cleaning and transformation

2. **Feature Engineering**

   * Selecting important features
   * Scaling and normalization

3. **Model Training**

   * Training classification models on sensor data
   * Handling class imbalance

4. **Model Evaluation**

   * Performance measured using accuracy and other metrics
   * Confusion matrix analysis

5. **Prediction Pipeline**

   * End-to-end pipeline for real-time fault prediction

---

### 🧠 Model Used

Random Forest Classifier was used due to its robustness and ability to handle non-linear data.

## 📊 Results

* The model successfully identifies faulty sensors with high accuracy
* Efficient in handling large and complex sensor datasets
* Provides reliable predictions for early fault detection

## accuracy chart
      precision    recall  f1-score   support

         0.0       0.87      0.93      0.90       141
         1.0       0.80      0.68      0.73        59

    accuracy                           0.85       200
   macro avg       0.84      0.80      0.82       200
weighted avg       0.85      0.85      0.85       200
## 🖥️ Project Output

### 📊 Model Prediction Output
![Model Output]https://github.com/itzsam052/sensor-fault-detection-ml/blob/5dce1353ac6385290569192d4a63df68963d73a5/predictions.csv

### 📉 Confusion Matrix
![Confusion Matrix]https://github.com/itzsam052/sensor-fault-detection-ml/blob/d6dc6f0f385655adf66b8ad502ceec350112c16c/confusion%20matrix.png
### 📊 Confusion Matrix Explanation

The confusion matrix is used to evaluate the performance of the classification model.

- True Positive (TP): Model correctly predicts a faulty sensor  
- True Negative (TN): Model correctly predicts a normal sensor  
- False Positive (FP): Model incorrectly predicts a fault (false alarm)  
- False Negative (FN): Model fails to detect an actual fault  

In this project, minimizing False Negatives is critical, as undetected sensor faults can lead to system failures.

The confusion matrix helps in understanding not just accuracy, but also the reliability of the model in real-world scenarios.

---

## 🚀 Key Features

* ✅ Automated sensor fault detection
* ✅ End-to-end ML pipeline (training + prediction)
* ✅ Scalable for industrial applications
* ✅ Clean and modular code structure

---

## 💡 Real-World Impact

This system can help industries:

* Reduce maintenance costs
* Prevent unexpected system failures
* Improve operational efficiency
* Enable predictive maintenance

---

## 🖥️ Demo

Below are sample outputs of the system detecting sensor faults:
data on which model is trained:
![model data]https://github.com/itzsam052/sensor-fault-detection-ml/blob/218b3ec919a956d44a90c48a14e3c273b8dacc15/processed_data.csv
### 🔄 Working Flow

1. Upload sensor dataset (CSV)
2. Data is preprocessed
3. Features (rolling mean, std, diff) are calculated
4. Model predicts fault / no fault
---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-learn
* **Concepts:** Machine Learning, Data Preprocessing, Model Evaluation

---

## ▶️ How to Run the Project

```bash
git clone https://github.com/itzsam052/sensor-fault-detection-ml
cd sensor-fault-detection-ml

pip install -r requirements.txt

python app.py
```

---

## 📌 Challenges Faced

* Handling missing and noisy sensor data
* Managing class imbalance in dataset
* Selecting the most effective ML model

---

## 📈 Future Improvements

* Real-time sensor data integration
* Interactive dashboard for monitoring
* Deployment on cloud platforms
* Integration with IoT systems

---

## 🙌 Conclusion

This project demonstrates how Machine Learning can be applied to solve real-world industrial problems like sensor fault detection. It highlights the importance of predictive maintenance in improving system reliability and reducing operational costs.






