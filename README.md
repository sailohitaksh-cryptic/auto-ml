# AutoStreamML

AutoStreamML is a Streamlit application that allows you to build an automated machine learning pipeline. With AutoStreamML, you can upload your dataset, perform automated exploratory data analysis, and train machine learning models for your data.

## Getting Started

To run the AutoStreamML application, follow these steps:

1. Install the required dependencies by running the following command:
`pip install streamlit pandas pandas-profiling streamlit-pandas-profiling pycaret`


2. Create a new Python file and copy the provided code in app.py into it.

3. Run the Python file using the following command:
`streamlit run app.py`


4. The AutoStreamML application will open in your browser.

## Usage

### Upload

In the "Upload" section, you can upload your dataset by clicking on the "Upload Your Dataset Here" button. Once the dataset is uploaded, it will be displayed in a table format.

### Profiling

The "Profiling" section allows you to perform automated exploratory data analysis on your dataset. It generates a comprehensive report using the `pandas_profiling` library, providing insights and visualizations about the dataset.

### ML

In the "ML" section, you can train a machine learning model for your dataset. First, select the target variable from the dropdown menu. Clicking the "Train model" button will initiate the training process. AutoStreamML uses the `pycaret` library to set up the machine learning experiment, compare different models, and display the best model along with its performance metrics.

### Download

The "Download" section provides a download button to save the trained machine learning model as a pickle file (`Trained_Model.pkl`).

## Sidebar

The sidebar on the left side of the application interface provides navigation options and displays an animated image.

## Acknowledgments

- AutoStreamML utilizes the following libraries: `streamlit`, `pandas`, `pandas_profiling`, `streamlit_pandas_profiling`, and `pycaret`.
- The animated image used in the sidebar is sourced from "mario_coder.gif".

---

Feel free to customize and enhance the AutoStreamML application to suit your specific needs. Happy machine learning!
