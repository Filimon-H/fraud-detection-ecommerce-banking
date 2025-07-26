
# 🔍 Fraud Detection for E-commerce & Credit Card Transactions  
**10 Academy – Week 8 & 9 Challenge | Adey Innovations Inc.**

This project develops accurate and explainable machine learning models to detect fraud in both **e-commerce** and **credit card** transaction data. It addresses challenges such as **class imbalance**, **feature engineering**, **geolocation enrichment**, and **model interpretability** using SHAP.

---

## 🎯 Business Objective

Fraudulent transactions can cause serious financial damage. Our goal is to:
- Detect fraud without causing friction for real customers
- Use behavior, time, and location patterns to signal fraud
- Provide explainable model outputs for transparency and trust

---

## 📁 Datasets Used

| Dataset                    | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| `Fraud_Data.csv`           | E-commerce transactions with timestamps, devices, IPs, and labels           |
| `IpAddress_to_Country.csv` | Maps IP address ranges to countries                                          |
| `creditcard.csv`           | Credit card transactions with anonymized features (`V1`–`V28`)              |

---

## 📊 Task 1: Data Cleaning & EDA

### ✅ E-commerce Data
- Removed duplicates and missing values
- Converted `signup_time` and `purchase_time` to datetime
- Found: 9.4% fraud → **moderate class imbalance**
- Visual trends: higher fraud in `SEO` and `Ads` traffic, and in `Safari`/`Opera` browsers

### ✅ Credit Card Data
- Removed 1,081 duplicates
- No missing values
- Found: 0.17% fraud → **extreme class imbalance**
- Fraud transactions are generally lower in amount

---

## 🛠️ Task 2: Feature Engineering & Transformation

### E-commerce Feature Highlights
- Time-based: `hour_of_day`, `day_of_week`, `time_since_signup`
- Behavior-based: `user_transaction_count`, `device_transaction_count`, `transactions_last_hour`
- Geolocation: `country` derived from `ip_address`
- One-hot encoding: applied to `browser`, `sex`, `source`, and `country`
- Scaling: used MinMaxScaler for key numerical features

---

## 🤖 Task 3: Model Training & Evaluation

### ⚙️ Models Trained (on both datasets)
- **Logistic Regression** (baseline)
- **Random Forest**
- **XGBoost**

### ⚠️ Class Imbalance Strategy
- Used **SMOTE** only on the training set
- Preserved original imbalance in the test set for realistic evaluation

### 📈 Evaluation Metrics
- F1 Score
- AUC-PR (Precision-Recall)
- Confusion Matrix
- Precision & Recall

---

## 📊 Model Comparison Results

### E-commerce Dataset (`fraud_data_ready.csv`)
| Model              | F1 Score | Precision | Recall | AUC-PR |
|--------------------|----------|-----------|--------|--------|
| Logistic Regression | 0.49     | 0.34      | 0.89   | 0.51   |
| Random Forest       | 0.67     | 0.60      | 0.77   | 0.73   |
| **XGBoost**         | **0.69** | **0.61**  | **0.80** | **0.76** ✅

📝 **Best Model**: **XGBoost** — highest F1 and AUC-PR, balancing precision and recall well.

---

### Credit Card Dataset (`creditcard_ready.csv`)
| Model              | F1 Score | Precision | Recall | AUC-PR |
|--------------------|----------|-----------|--------|--------|
| Logistic Regression | 0.11     | 0.07      | 0.69   | 0.12   |
| Random Forest       | 0.62     | 0.60      | 0.65   | 0.64   |
| **XGBoost**         | **0.66** | **0.62**  | **0.71** | **0.68** ✅

📝 **Best Model**: **XGBoost** again — best F1, recall, and overall balance.

---

## 🔍 Task 4: SHAP Explainability

### SHAP Visualizations
- **Summary Plot**: Showed top global drivers (e.g., `time_since_signup`, `device_transaction_count`)
- **Force Plot**: Explained individual fraud decisions by showing how features increased/decreased the fraud score

### Key Insights
- Fast signups followed by purchases were a major fraud signal
- High transaction volume from the same device or IP = suspicious behavior
- Some browsers and countries had stronger fraud associations

---

## 📦 Output Files

| File Name                  | Description                                        |
|---------------------------|----------------------------------------------------|
| `fraud_data_clean.csv`    | Cleaned raw e-commerce dataset                     |
| `engineered_fraud_data.csv` | With temporal, geo, and behavioral features     |
| `fraud_data_ready.csv`    | Final ML-ready e-commerce data (encoded & scaled) |
| `creditcard_ready.csv`    | Cleaned and scaled credit card dataset             |

---

## 📂 Project Structure

├── data/ # Input and processed data files
├── notebooks/
│ ├── eda_fraud_data.ipynb
│ ├── eda_credit_card.ipynb
│ ├── preprocessing_fraud_data.ipynb
│ ├── modeling_fraud_data.ipynb
│ ├── modeling_credit_card.ipynb
│ └── shap_fraud_random_forest.ipynb
├── src/
│ ├── data_loader.py
│ ├── preprocessing.py
│ ├── feature_engineering.py
│ └── model_utils.py
├── README.md
└── requirements.txt

## 🧠 Summary

- ✅ Built and explained fraud models for two different transaction domains
- ✅ Engineered useful behavioral and temporal fraud features
- ✅ Achieved strong results with XGBoost + SHAP explanations
- ✅ Maintained clean, modular, and reproducible code structure