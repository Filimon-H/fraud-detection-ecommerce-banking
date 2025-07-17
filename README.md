# 🔍 Fraud Detection Project – E-commerce & Credit Card

This project analyzes and prepares two datasets — one from an **e-commerce platform** and another from **credit card transactions** — to detect patterns of fraudulent behavior and prepare the data for predictive modeling.

---

## 🎯 Objectives

- Clean and preprocess raw transactional data
- Enrich with geographic and temporal features
- Engineer behavior-based features
- Visualize fraud distribution by user attributes
- Prepare final datasets for machine learning

---

## 📁 Datasets

| File                          | Description                                           |
|-------------------------------|-------------------------------------------------------|
| `Fraud_Data.csv`              | E-commerce transactions with timestamp, IP, device   |
| `IpAddress_to_Country.csv`    | Maps IP ranges to country                            |
| `creditcard.csv`              | Credit card transactions with anonymized features    |

---

## 🧹 Task 1: Data Cleaning

### ✅ E-commerce Data
- Removed duplicates (0 found)
- Converted `signup_time` and `purchase_time` to datetime
- Confirmed: **no missing values**
- Final cleaned file: `fraud_data_clean.csv`

### ✅ Credit Card Data
- Removed 1,081 duplicate rows
- Confirmed: **no missing values**
- Scaled `Amount` and `Time` using MinMaxScaler
- Final cleaned file: `creditcard_ready.csv`

---

## 📊 Task 1: Exploratory Data Analysis (EDA)

### E-commerce Highlights

- **Class distribution**: 90.6% non-fraud, 9.4% fraud → heavy imbalance
- **Age Distribution**: Majority users between 25–40
- **Fraud by Source**: Higher fraud rate via `SEO` and `Ads`
- **Fraud by Browser**: Chrome leads in volume; Safari & Opera show relatively more fraud
- **Fraud by Sex**: More fraud among male users, but both affected
- **Top Countries**: United States dominates transaction volume

### Credit Card Highlights

- **Class distribution**: 0.17% fraud → extreme imbalance
- **Amount by Class**:
  - Fraudulent transactions skew lower in value
  - Outliers exist in both classes
- **Correlation**:
  - No strong linear correlation between `Time`, `Amount`, and `Class`

---

## 🧠 Task 2: Feature Engineering

### Time-Based Features

| Feature             | Description                                    |
|---------------------|------------------------------------------------|
| `hour_of_day`       | Hour the purchase occurred                     |
| `day_of_week`       | Day of the week                                |
| `time_since_signup` | Seconds between signup and transaction         |

### Behavior-Based Features

| Feature                     | Description                                  |
|-----------------------------|----------------------------------------------|
| `user_transaction_count`    | Number of transactions per user              |
| `device_transaction_count`  | Number of transactions per device            |
| `transactions_last_hour`    | IP-based burst activity within 1 hour window |

### Geographic Feature

- `country`: derived from `ip_address` using IP-to-country mapping
- Unknown IPs labeled as `"Other"`

Output saved as: `engineered_fraud_data.csv`

---

## 🧪 Task 3: Encoding, Scaling, Class Analysis

- **Categorical Encoding**:
  - One-hot encoded `browser`, `sex`, `source`, and `country`
  - Resulting shape: `(151112, 204)`
- **Numerical Scaling**:  
  - Used `MinMaxScaler` on `purchase_value`, `time_since_signup`, and frequency features
- **Class Balance**:
  - E-commerce fraud ratio: **9.4%**
  - Credit card fraud ratio: **0.17%**
  - Visualized using countplots

Final modeling-ready dataset: `fraud_data_ready.csv`

---

## 📦 Output Files

| Filename                    | Purpose                          |
|-----------------------------|----------------------------------|
| `fraud_data_clean.csv`      | Cleaned e-commerce fraud dataset |
| `engineered_fraud_data.csv` | With temporal, geo, behavior features |
| `fraud_data_ready.csv`      | Fully encoded and scaled dataset |
| `creditcard_ready.csv`      | Cleaned and scaled credit data   |

---

## 📈 Next Steps

Proceed to:

- Train classification models using `fraud_data_ready.csv`
- Evaluate with ROC-AUC, precision/recall, SHAP/LIME
- Explore strategies for class imbalance (resampling, SMOTE, cost-sensitive models)

