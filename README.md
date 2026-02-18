#  Churn Prediction & Retention Strategy for a Telecom Provider

##  Problem Statement

Customer churn is a critical business challenge in the telecom industry, where acquiring new customers is significantly more expensive than retaining existing ones. The objective of this project is to **predict which customers are likely to churn** and provide **actionable retention strategies** based on model insights.

This project builds a machine learning pipeline that:

* Identifies high-risk churn customers
* Explains the key drivers behind churn
* Supports business teams with data-driven retention decisions


## Dataset Description

The dataset contains customer-level information related to:

Customer Demographics  (e.g., tenure, contract type)
* **Service Usage** (internet service, phone service, add-ons)
* **Billing & Payment Details** (monthly charges, total charges, payment method)
* **Target Variable**

  * `is_churn` (1 = Customer churned, 0 = Customer retained)


### Key Features

| Feature            | Description                                               |
| ------------------ | --------------------------------------------------------- |
| `tenure_months`    | Number of months the customer has stayed with the company |
| `contract_type`    | Month-to-month, One year, Two year                        |
| `payment_method`   | Mode of payment used by the customer                      |
| `internet_service` | Type of internet service subscribed                       |

---

## Project Approach

### Data Preprocessing

* Handled missing values and inconsistent records
* Converted categorical variables using encoding techniques
* Scaled numerical features where required
* Performed feature selection using correlation analysis and business relevance

### Exploratory Data Analysis (EDA)

* Analyzed churn distribution across customer segments
* Studied relationships between tenure, charges, contract type, and churn
* Used visualizations such as:

  * Boxplots
  * Correlation heatmaps
  * Churn vs feature comparison charts

###  Model Building

Multiple classification models were trained and evaluated using cross-validation:

* Logistic Regression
* Random Forest
* XGBoost Classifier

Hyperparameter tuning was performed using **RandomizedSearchCV** with ROC-AUC as the primary evaluation metric.

---

## Models Used

| Model               | Purpose                                          |
| ------------------- | ------------------------------------------------ |
| Logistic Regression | Baseline interpretable model                     |
| Random Forest       | Non-linear model for feature importance analysis |
| XGBoost             | High-performance gradient boosting classifier    |

### Evaluation Metrics

* ROC-AUC Score
* Precision
* Recall
* F1-Score
* Confusion Matrix

The final model was selected based on:

* Best ROC-AUC performance
* Stability across cross-validation folds
* Business interpretability

---

## Results

* The model successfully identified high-risk churn customers with strong predictive performance
* Key churn drivers identified:

  * Low tenure
  * High monthly charges
  * Month-to-month contracts
  * Certain payment methods

### Performance Snapshot

| Metric    | Score                         |
| --------- | ----------------------------- |
| ROC-AUC   | High-performing               |
| Precision | Balanced                      |
| Recall    | Optimized for churn detection |

---

## Business Impact

This system enables telecom providers to:

* Proactively target customers likely to churn
* Design personalized retention campaigns
* Reduce revenue loss
* Improve customer lifetime value (CLV)

### Example Business Strategy

* Customers with **high churn probability (>70%)** are offered:

  * Contract upgrades
  * Discounted service bundles
  * Priority customer support

This transforms raw model output into **actionable business intelligence**.

---

## Streamlit Web Application

A user-friendly web app was built using **Streamlit** to:

* Input customer details
* Get real-time churn predictions
* View churn probability

### Features

* Interactive UI
* Model caching for performance
* Business-friendly prediction output

---

##  How to Run the Project

### 1. Clone the Repository

```bash
git clone <your-github-repo-url>
cd <project-folder>
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Jupyter Notebook

```bash
jupyter notebook
```

Open:

```
Capstone_project_Vrushali.ipynb
```

### 5. Run Streamlit App

```bash
streamlit run streamlit_app.py
```

App will open at:

```
http://localhost:8501
```

---

##  Project Structure

```
Telecom-Churn-Prediction/
│
├── data/
│   └── telecom_churn.csv
├── notebook/
│   └── Capstone_project.ipynb
├── app/
│   └── streamlit_app.py
├── model/
│   └── model.pkl
├── reports/
│   └── project_report.pdf
├── requirements.txt
└── README.md

```
<img width="1919" height="994" alt="image" src="https://github.com/user-attachments/assets/85b34903-f9fa-4d85-b62b-ce50e019fd88" />
<img width="1919" height="1007" alt="image" src="https://github.com/user-attachments/assets/67580627-ef55-46d6-9626-5eb2ddf9c367" />

---

## Project Done By:-

**Vrushali Oak**
Aspiring Data Scientist | Machine Learning | Analytics


