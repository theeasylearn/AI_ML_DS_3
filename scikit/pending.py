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
        random_state=42,
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

# 7. HYPERPARAMETER TUNING
param_grid = {
    'classifier__n_estimators': [100, 200, 500],
    'classifier__max_depth': [None, 5, 10],
    'classifier__min_samples_split': [2, 5, 10]
}

search = RandomizedSearchCV(
    estimator=model_pipe,
    param_distributions=param_grid,
    n_iter=10,
    cv=5,
    scoring='f1_macro',
    n_jobs=-1,
    random_state=42
)

# 8. TRAIN THE MODEL
print("Training with hyperparameter tuning...")
search.fit(X_train, y_train)

print("Best parameters:", search.best_params_)
print("Best cross-validation score:", round(search.best_score_, 4))

best_model = search.best_estimator_

# 9. MAKE PREDICTIONS
y_pred = best_model.predict(X_test)

# 10. EVALUATE
print("\nFinal Results")
print("Accuracy:", round(accuracy_score(y_test, y_pred), 4))

print("\nDetailed Report:")
print(classification_report(y_test, y_pred, target_names=['Not Hired (0)', 'Hired (1)']))

# 11. CROSS-VALIDATION
cv_scores = cross_val_score(
    best_model, X, y,
    cv=5,
    scoring='f1_macro',
    n_jobs=-1
)
print("\n5-Fold Cross-Validation F1-macro:", round(cv_scores.mean(), 4), "±", round(cv_scores.std(), 4))

print("\nAll steps completed.")