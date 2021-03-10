# London-Bike-ML

How many bikes will be rented in London on a given day? In this project, I build and optimize scikit-learn regressor models to predict the number of bikes rented from the London bike rental dataset (https://www.kaggle.com/hmavrodiev/london-bike-sharing-dataset). 

final_proj.ipynb details the preprocessing, iterative hyperparameter search, model selection, and final model interpretation. 
app.py is a locally-hosted browser program where users can submit any feature vector of choice to the final fitted model and get back a prediction.
To run app.py:
1. Create the ml conda environment 
  `conda env create -f environment.yml`
2. Active the environment
  `conda activate ml`
3. run app
  `streamlit run app.py`

This project is for MSDS699 - Machine Learning Laboratory, in partial fulfillment of the MS in Data Science degree at the University of San Francisco.
