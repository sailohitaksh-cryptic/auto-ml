# AutoStreamML Documentation

This documentation provides an overview of the AutoStreamML application and guides you on how to install, run, and use it effectively.

## Installation

To install AutoStreamML and its dependencies, follow these steps:

1. Clone the repository:

   `git clone https://github.com/sailohitaksh-cryptic/auto-ml`

2. Install the required dependencies: `pip install -r requirements.txt`

3. Run the application: `streamlit run app.py`

4. Access the AutoStreamML application in your web browser at `http://localhost:8501`.

# Usage

## Upload Data

In the "Upload" section of the application, you can upload your dataset by clicking on the "Upload Your Dataset Here" button. Once the dataset is uploaded, it will be displayed in a table format.

## Automated Exploratory Data Analysis

The "Profiling" section of AutoStreamML allows you to perform automated exploratory data analysis on your dataset. It generates a comprehensive report using the `pandas_profiling` library, providing insights and visualizations about the dataset.

## Machine Learning Model Training

In the "ML" section of the application, you can train machine learning models for your dataset based on the problem type.

### Classification

For classification problems, select the target variable from the dropdown menu and click the "Train model" button. AutoStreamML will set up the machine learning experiment, compare different models, and display the best model along with its performance metrics. You can download the trained model as a pickle file.

### Regression

For regression problems, select the target variable from the dropdown menu and click the "Train model" button. AutoStreamML will set up the machine learning experiment for regression, compare different models, and display the best model along with its performance metrics. You can download the trained model as a pickle file.

### Clustering

For clustering problems, select the desired clustering algorithm (e.g., k-means, agglomerative, DBSCAN) from the dropdown menu and click the "Train model" button. AutoStreamML will set up the machine learning experiment for clustering and display the resulting clusters along with the cluster labels. You can download the trained model as a pickle file.

## Download Trained Model

In the "Download" section of the application, you can download the trained machine learning model based on the selected problem type. The downloaded file will be saved with a specific filename corresponding to the problem type.

## Customization

You can customize the AutoStreamML application to suit your specific needs. Feel free to explore the code in the `app.py` file and modify it according to your requirements. You can add new functionalities, change the layout, or enhance the existing features.

---

For detailed information and examples, refer to the source code and comments in the `app.py` file. Enjoy using AutoStreamML for your machine learning projects!



