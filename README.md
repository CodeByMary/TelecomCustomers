Telecom Customer Churn Prediction

Objective

The primary goal of this project is to develop a machine learning model to predict customer churn in a telecom company. The model will identify which customers are likely to stop using the company's services, allowing the business to take proactive measures to retain them.

Overview

In this project, I work with a telecom churn dataset from Kaggle. The focus is to create a model that can predict churn with a good balance of precision and recall. The steps include:
    - data download,
    - exploratory data analysis (EDA)
    - data preprocessing, 
    - feature engineering, 
    - model building, evaluation, and fine-tuning of the classification threshold to optimize the model's performance.


Dataset

The dataset used in this project can be downloaded from Kaggle:

Dataset: https://www.kaggle.com/datasets/tarekmuhammed/telecom-customers
Key Information:

The dataset contains information about telecom customers, including their usage patterns, services subscribed, and whether they churned (left the company).
The target variable is Churn, a binary indicator (0 for non-churners, 1 for churners).

The dataset consists of the following features:

CustomerID: Unique customer identifier.
Gender: Gender of the customer.
SeniorCitizen: Whether the customer is a senior citizen (1) or not (0).
Partner: Whether the customer has a partner (Yes/No).
Dependents: Whether the customer has dependents (Yes/No).
Tenure: Number of months the customer has been with the company.
PhoneService: Whether the customer has phone service (Yes/No).
MultipleLines: Whether the customer has multiple lines (Yes/No/No phone service).
InternetService: Type of internet service (DSL, Fiber optic, No).
OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies: Various service options (Yes/No/No internet service).
Contract: Type of contract (Month-to-month, One year, Two year).
PaperlessBilling: Whether the customer uses paperless billing (Yes/No).
PaymentMethod: Payment method (Electronic check, Mailed check, Bank transfer, Credit card).
MonthlyCharges: The amount charged to the customer monthly.
TotalCharges: Total charges incurred by the customer.
Churn: Target variable indicating whether the customer churned (Yes/No).

Dataset Overview
Rows: 7,043
Columns: 21 (20 features + 1 target)


Requirements

This project includes Jupyter notebooks telecomCustomers.ipynb to explore and analyze the datasets interactively.

To run this project, you need to install the following dependencies:

Python 3.10
Additional Python packages listed in requirements.txt
Install Dependencies

You can install the required dependencies using the following command:

pip install jupyter
pip install -r requirements.txt
