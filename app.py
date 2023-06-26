import streamlit as st
import pandas as pd
import os

# Import profiling capability
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

# ML Stuff
from pycaret.classification import setup, compare_models, pull, save_model
from pycaret.regression import setup as setup_regression, compare_models as compare_models_regression
from pycaret.clustering import setup as setup_clustering, create_model

with st.sidebar:
    st.image("mario_coder.gif")
    st.title("AutoStreamMl")
    choice = st.radio("Navigation", ["Upload", "Profiling", "ML", "Download"])
    st.info("This application allows you to build an automated ML pipeline using Streamlit")

if os.path.exists("sourcedata.csv"):
    df = pd.read_csv("sourcedata.csv", index_col=None)

if choice == "Upload":
    st.title("Upload Your Data for modeling!")
    file = st.file_uploader("Upload Your Dataset Here")
    if file:
        df = pd.read_csv(file, index_col=None)
        df.to_csv("sourcedata.csv", index=None)
        st.dataframe(df)

if choice == "Profiling":
    st.title("Automated Exploratory Data Analysis")
    profile_report = df.profile_report()
    st_profile_report(profile_report)

if choice == "ML":
    st.title("Machine Learning Model for your dataset")
    target = st.selectbox("Select Your Target", df.columns)
    problem_type = st.selectbox("Select Problem Type", ["Classification", "Regression", "Clustering"])

    if problem_type == "Classification":
        if st.button("Train model"):
            setup(df, target=target)
            setup_df = pull()
            st.info("This is the ML Experiment settings")
            st.dataframe(setup_df)
            best_model = compare_models()
            compare_df = pull()
            st.info("This is the ML model")
            st.dataframe(compare_df)
            best_model
            save_model(best_model, 'best_model_classification')

    elif problem_type == "Regression":
        if st.button("Train model"):
            setup_regression(df, target=target)
            setup_df = pull()
            st.info("This is the ML Experiment settings")
            st.dataframe(setup_df)
            best_model = compare_models_regression()
            compare_df = pull()
            st.info("This is the ML model")
            st.dataframe(compare_df)
            best_model
            save_model(best_model, 'best_model_regression')

    elif problem_type == "Clustering":
        clustering_algorithm = st.selectbox("Select Clustering Algorithm", ["kmeans", "agglomerative", "dbscan"])
        if st.button("Train model"):
            setup_clustering(df)
            setup_df = pull()
            st.info("This is the ML Experiment settings")
            st.dataframe(setup_df)
            best_model = create_model(clustering_algorithm)
            st.info("This is the ML model")
            st.write("Number of Clusters:", best_model.n_clusters)
            st.write("Cluster Labels:", best_model.labels_)
            save_model(best_model, 'best_model_clustering')

if choice == "Download":
    if problem_type == "Classification":
        with open("best_model_classification.pkl", "rb") as f:
            st.download_button("Download the Model", f, "Trained_Model_classification.pkl")
    elif problem_type == "Regression":
        with open("best_model_regression.pkl", "rb") as f:
            st.download_button("Download the Model", f, "Trained_Model_regression.pkl")
    elif problem_type == "Clustering":
        with open("best_model_clustering.pkl", "rb") as f:
            st.download_button("Download the Model", f, "Trained_Model_clustering.pkl")
