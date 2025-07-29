# 🕵️‍♂️ Fraud Detection in E-Commerce & Banking

A machine learning project to detect fraudulent transactions in both e-commerce and credit card payment systems. This project compares multiple models, applies advanced feature engineering, and leverages SHAP for model explainability.

---

## 🧠 Project Summary

This repository showcases a complete fraud detection pipeline—from data preprocessing to model explainability—applied to two distinct domains:

- **E-Commerce Fraud Detection** using behavioral and geolocation features.
- **Credit Card Fraud Detection** using anonymized PCA-transformed features.

---

## 👥 Target Audience

This project is designed for:

- Data scientists and ML engineers building fraud detection systems.
- FinTech analysts evaluating fraud signals.
- Recruiters or instructors reviewing project-based ML competency.

---

## 📁 Repo Structure Overview

```
fraud-detection-ecommerce-banking/
│
├── data/
│   ├── Fraud_Data.csv
│   ├── IpAddress_to_Country.csv
│   ├── creditcard.csv
│   └── [processed CSVs]
│
├── notebooks/
│   ├── eda_fraud_data.ipynb
│   ├── eda_credit_card.ipynb
│   ├── modeling_fraud.ipynb
│   ├── modeling_credit.ipynb
│   └── shap_explainer.ipynb
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   └── model_utils.py
│
├── models/
│   ├── rf_fraud_model.pkl
│   ├── rf_credit_model.pkl
│   └── xgb_credit_model.pkl
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🧱 Setup Instructions

### 🔧 Prerequisites

- Python 3.10+
- pip or conda
- Git

### 🛠 Installation

```bash
# Clone the repo
git clone https://github.com/Filimon-H/fraud-detection-ecommerce-bankinggit
cd fraud-detection-ecommerce-banking

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```

---

## 🚀 Usage Instructions

### 📊 Run Notebooks

Open Jupyter Lab or VSCode and run the following notebooks in order:

1. `eda_fraud_data.ipynb` – Exploratory analysis of e-commerce data.
2. `eda_credit_card.ipynb` – Analysis of anonymized credit card data.
3. `modeling_fraud.ipynb` – Train, evaluate, and save models for e-commerce fraud.
4. `modeling_credit.ipynb` – Do the same for credit card fraud.
5. `shap_explainer.ipynb` – Visualize model explanations using SHAP.

---

## 📌 Key Features

- 🧹 Cleaned and preprocessed complex real-world datasets
- 🌍 Geo-enriched e-commerce data via IP-to-country mapping
- 📈 Advanced feature engineering (time since signup, frequency features)
- ⚖️ SMOTE for class imbalance handling
- 🤖 Model comparison: Logistic Regression, Random Forest, XGBoost
- 🔍 SHAP visualizations for interpretability

---

## 📊 Model Insights

| Dataset        | Best Model       | F1 Score | AUC-PR | Strengths                         |
|----------------|------------------|----------|--------|----------------------------------|
| Credit Card    | XGBoost          | 0.676    | 0.8016 | High precision, effective ranking |
| E-Commerce     | Random Forest    | 0.6784   | 0.7779 | Balanced performance, fast train |

> 🏆 Final Recommendation: Use **Random Forest** for deployment due to better interpretability and performance consistency.

---

## 📜 License

MIT License – see [LICENSE](LICENSE) for details.

---

## 👤 Maintainer

**Filimon Hailemariam**  
GitHub: https://github.com/Filimon-H/fraud-detection-ecommerce-banking
