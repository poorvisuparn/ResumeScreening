import pandas as pd
from optbinning import Scorecard, BinningProcess
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load the train dataset
df_application = pd.read_csv('./home-credit-default-risk/application_train.csv', low_memory=True)
df_application.set_index('SK_ID_CURR', inplace=True)

# Split the dataset into train and test
df_application_train, df_application_test, y_train, y_test = train_test_split(
df_application, df_application.TARGET, test_size=0.2, random_state=42)





# Define the feature list from dataset (including categorical and numerical)
list_features = df_application_train.drop(columns=['TARGET']).columns.values

# Define categorical features list
list_categorical = df_application_train.select_dtypes(include=['object', 'category']).columns.values

# Define selection criteria for BinningProcess
selection_criteria = {"iv": {"min": 0.005, 'max':0.5, "strategy": "highest"}}

# Instatiate BinningProcess
binning_process = BinningProcess(
    categorical_variables=list_categorical,
    variable_names=list_features,
    selection_criteria=selection_criteria,
)





# Define scaling method and values
scaling_method = "min_max"
scaling_method_data = {"min": 0, "max": 1000}

# Instatiate and fit Scorecard
scorecard = Scorecard(
    target='TARGET',
    binning_process=binning_process,
    estimator=logreg,
    scaling_method=scaling_method,
    scaling_method_params=scaling_method_data,
    intercept_based=False,
    reverse_scorecard=True,
)

scorecard.fit(df_application_train)




scorecard_summary = scorecard.table(style="detailed").round(3)
scorecard_summary.to_csv('scorecard_table_detailed.csv', index=False)





import pickle

# To pickle a Scorecard object
with open('scorecard_model.pickle', 'wb') as pfile:
   pickle.dump(scorecard, pfile)
    
# To unpickle it
with open("scorecard_model.pickle", 'rb') as scorecard_pickle:
    scorecard_production = pickle.load(scorecard_pickle)
    
# To use the Scorecard model for predictions in production
# For one sample
scorecard_production.score(df_application_test.iloc[0:1, :])

# For a few samples
scorecard_production.score(df_application_test.iloc[0:3, :])