# CosmoAI

Datasets:
-Pantheon+SH0ES_ml_nodup: Includes Pantheon+SH0ES cropped dataset with duplicates eliminated
-quasar_00_10: Raw Quasar data, that includes SDSS DR18 quasar dataset within range of redshift 0.0-1.0
-quasar_10_20: Raw Quasar data, that includes SDSS DR18 quasar dataset within the range of   redshift 1.0-2.0
-quasar_20_100: Raw Quasar data, that includes SDSS DR18 quasar dataset within the range of redshift 2.0-10.0
-supernova_quasar_output: The combined dataset, that has been used to train the model

ML Models:
-Neural Network:
  ~feature_order: Order of features (Input) to maintain reusability 
  ~nn_model: Trained Model
  ~nn_prediction: The code that has been used to make prediction from raw quasar data
  ~nn_train: The code that has been used to train the model from the combined dataset
  ~standardscaler: Standardscaler save file to maintain possible
-Other Models:
  ~optimized_random_forest
  ~other_models: random forest, k-Nearest-Neighbour and decision tree
-XGBoost:
  ~xgboost_supernova_quasar_model: Supernova quasar training model that uses extreme gradient boosting
  ~scaler_xgboost: Standardscaler save file to maintain reusability

data_preprocessing: Data preprocessing code to combine two different datasets
parameter_analyse: Ugriz and mu_sh0es parameter analysing codes
