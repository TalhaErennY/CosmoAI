# CosmoAI Project Files
Title: Machine Learning for the Analysis of the Expansion Dynamics of the Universe Using SN Ia and Quasar Data

This study investigates whether there is a relationship between the photometric properties of quasars near Type Ia supernovae and the distance information of these supernovas. Supernovas, which are fundamental tools for understanding the expansion rate and history of the Universe, can be observed up to a certain distance. Direct measurements are not possible in more distant regions due to observational limitations. 
Therefore, the aim of this study is to estimate the distance using quasars that can be detected at significantly larger distances in the universe based on their brightness properties. The dataset of quasar samples matching the supernova data was analyzed using various machine learning algorithms. The best results were obtained by using a neural network model. 
The results show that the bulk properties of quasars can establish an indirect but statistically significant relationship with the expansion structure of the Universe. This suggests that quasars can be used as an alternative cosmological tool in distant regions where classical methods are inadequate in the future.

Below is a guide to the project files

Project Files Overview--------------------------------------------------------------------------------------------------
Datasets:
-Pantheon+SH0ES_ml_nodup: Includes Pantheon+SH0ES cropped dataset with duplicates eliminated
-quasar_00_10: SDSS DR18 quasar dataset with a redshift range of 0.0-1.0
-quasar_10_20: SDSS DR18 quasar dataset with a redshift range of 1.0-2.0
-quasar_20_100: SDSS DR18 quasar dataset with a redshift range of 2.0-10.0
-supernova_quasar_output: The combined dataset, that has been used to train the model

ML Models:
-Neural Network:
  ~feature_order: Order of features (Input) to preserve consistency
  ~nn_model: Trained Model
  ~nn_prediction: The code that has been used to make prediction from raw quasar data
  ~nn_train: The code that has been used to train the model from the combined dataset
  ~standardscaler: Standardscaler save file to preserve consistency
-Other Models:
  ~optimized_random_forest
  ~other_models: random forest, k-Nearest-Neighbour and decision tree
-XGBoost:
  ~xgboost_supernova_quasar_model: Supernova quasar training model that uses extreme gradient boosting
  ~scaler_xgboost: Standardscaler save file to preserve consistency

data_preprocessing: Data preprocessing code to combine two different datasets
parameter_analyse: Ugriz and mu_sh0es parameter analysing codes

(Parameter explanations: coming soon...)
