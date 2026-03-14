X = df.drop('hired', axis=1)
y = df['hired']
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