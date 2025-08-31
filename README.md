# 🚨 Fraud Banking App Detection

A Machine Learning project to detect **fraudulent banking APKs** (applications) using advanced ensemble learning techniques.  
This system leverages **stacked models (XGBoost, LightGBM, CatBoost, RandomForest, Logistic Regression)** with **SMOTE balancing, log-transformation, scaling, and hyperparameter tuning** to achieve high accuracy in fraud detection.

---

## 📌 Features
- End-to-End ML pipeline with:
  - Data preprocessing (skewness handling with log1p transform, scaling, encoding)
  - Imbalanced dataset handling via **SMOTE**
  - Hyperparameter tuning for multiple models
  - **Stacked Ensemble** for best performance
- High accuracy (**98%+**) and AUC (**0.99+**)
- Supports **direct prediction on raw new data** (log-transform & scaling handled automatically via pipeline)
- Easily deployable with Flask / FastAPI for real-world use
- Saved pipeline with preprocessing + model (`stacking_pipeline.pkl`)