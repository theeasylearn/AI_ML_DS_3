# COMPLETE SCIKIT-LEARN EXAMPLE

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, RandomizedSearchCV, cross_val_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

print("Starting Scikit-learn example")

# 1.  SIMPLE DATASET (Dictionary)
data = {
    'age':        [25, 30, np.nan, 35, 40, 28, np.nan, 32, 27, 45, 29, 33, 31, 38, np.nan, 36],
    'salary':     [50000, 60000, 55000, np.nan, 70000, 52000, 65000, 58000,
                   48000, 75000, 51000, 62000, 59000, np.nan, 67000, 61000],
    'experience': [2, 5, 3, 8, 10, 1, np.nan, 4, 3, 12, 2, 6, 5, 9, 7, np.nan],
    'city':       ['NY','LA','NY','SF','LA','NY','SF','LA','NY','SF','LA','NY','SF','LA','NY','SF'],
    'gender':     ['M','F','M','F','M','F','M','F','M','F','M','F','M','F','M','F'],
    'hired':      [0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0]
}

df = pd.DataFrame(data)
print("Dataset created. Shape:", df.shape)
print(df.head(3))

X = df.drop('hired', axis=1)
y = df['hired']

# 2. SELECT NUMERIC AND CATEGORICAL COLUMNS
num_cols = X.select_dtypes(include=['number']).columns.tolist()
cat_cols = X.select_dtypes(include=['object']).columns.tolist()

print("Numeric columns:", num_cols)
print("Categorical columns:", cat_cols)

# 3. BUILD PREPROCESSING PIPELINES
num_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler',  StandardScaler())
])

cat_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot',  OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

# 4. COLUMNTRANSFORMER
preprocessor = ColumnTransformer([
    ('num', num_pipe, num_cols),
    ('cat', cat_pipe, cat_cols)
], remainder='drop')

# 5. FULL PIPELINE
model_pipe = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(
        n_estimators=100,
        max_depth=None,
        min_samples_split=2,
        max_features='sqrt',
        random_state=89,
        n_jobs=1
    ))
])

# 6. SPLIT DATA
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
print("Train set size:", X_train.shape[0], "| Test set size:", X_test.shape[0])
print("Train data")
print(X_train)
print("Test data")
print(X_test)
# print(y_train,y_test)