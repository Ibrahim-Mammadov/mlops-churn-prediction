# mlops-churn-prediction# 🚀 MLOps Churn Prediction Project
# 🚀 MLOps Churn Prediction Project

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![DVC](https://img.shields.io/badge/Data_Version_Control-DVC-brightgreen.svg)
![MLflow](https://img.shields.io/badge/Experiment_Tracking-MLflow-tracking.svg)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-orange.svg)

Welcome to my end-to-end Customer Churn Prediction project. This repository is built using production-grade MLOps practices...

Welcome to my end-to-end Customer Churn Prediction project. This repository is built using production-grade MLOps practices, focusing on reproducibility, data versioning, and automated workflows.

---

## 🏗️ Project Architecture & Components

The repository is structured as a professional MLOps pipeline:
* **`src/` Folder:** Contains the core production code for the machine learning pipeline (Data Ingestion, Model Training, and Inference scripts).
* **`data/` & `models/` (.dvc pointers):** Data and model artifacts are securely versioned and tracked using **DVC (Data Version Control)** to prevent committing massive binary files directly to Git.
* **Experiment Tracking:** Integrated with **MLflow** to track metrics, parameters, and model versions transparently.

---

## 🛠️ Tech Stack & Tools

* **Version Control:** Git & GitHub
* **Data Versioning:** DVC (Data Version Control)
* **Experiment Tracking:** MLflow
* **Machine Learning:** Python (Pandas, Scikit-Learn)
* **Environment Management:** Python Virtual Environments (`venv`)

---

## 🎯 Current Status & Next Steps

### Completed:
* ✅ Set up repository structure and environment constraints.
* ✅ Developed and executed data ingestion pipeline (`src/data_ingestion.py`).
* ✅ Built and tracked the ML model training cycle (`src/train.py`).
* ✅ Successfully linked data and models to DVC and pushed to GitHub.

### 🚀 Next Milestone: Day 4 — CI/CD with GitHub Actions
The next step is implementing a **Continuous Integration (CI)** pipeline using **GitHub Actions**. Every time new code is pushed to the `main` branch, the workflow will automatically trigger in the cloud to run code linting, syntax validation, and verification tests.

---

## ⚙️ How to Setup and Run Locally

```bash
# 1. Clone the repository
git clone [https://github.com/Ibrahim-Mammadov/mlops-churn-prediction.git](https://github.com/Ibrahim-Mammadov/mlops-churn-prediction.git)
cd mlops-churn-prediction

# 2. Create and activate virtual environment
python -m venv venv
# On Windows:
.\venv\Scripts\activate

# 3. Install packages
pip install -r requirements.txt

# 4. Run the pipelines
python src/data_ingestion.py
python src/train.py