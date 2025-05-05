# Diabetes Prediction App

This is a Streamlit app that predicts the risk of diabetes based on input data. The app uses machine learning models to analyze factors such as age, blood glucose level, HbA1c, height, weight, and more.

## How to Run the App

Follow the steps below to run the app on your computer.

### 1. Clone the Repository

To get started, clone the repository to your local machine:

```bash
git clone https://github.com/silenticc/DiabetesPredictionApp.git
```

Or you can just simply download the project as a .zip file.
### 2. Set Up Virtual Environment

First, ensure you have Python installed. You can check by typing `python --version` in your terminal or command prompt.

#### For Windows:

1. Open **Command Prompt.**
2. Navigate to the project directory (change to the actual path):
```bash
cd DiabetesPredictionApp 
```
3. Create a virtual environment:
```bash
python -m venv venv
```
4. Activate the virtual environment:
```bash
venv\Scripts\activate
```

#### For Mac/Linux:

1. Open **Termial.**
2. Navigate to the project directory (change to the actual path):
```bash
cd DiabetesPredictionApp
```
3. Create a virtual environment:
```bash
python3 -m venv venv
```
4. Activate the virtual environment:
```bash
source venv/bin/activate
```

### 3. Install Dependencies
Make sure you're in the project directory and the virtual environment is activated. Then run:
```bash
pip install -r requirements.txt
```
This will install all the necessary libraries for the app.

### 4. Run the App
To run the app, use the following command:
```bash
streamlit run app.py
```
This will start the app and open it in your browser. If it doesn't open automatically, visit http://localhost:8501 in your web browser.

### 5. Deactivate the Virtual Environment
When you're done, you can deactivate the virtual environment by running:
```bash
deactivate
```

## Dataset

The project utilizes a diabetes prediction dataset, which can be downloaded from Kaggle:

[Diabetes prediction dataset](https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset)