from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

data = load_iris()
X = data.data
y = data.target

model = RandomForestClassifier(random_state=42)

params = {
    "max_depth": [3, 5, 7],
    "n_estimators": [50, 100]
}

grid_search = GridSearchCV(
    estimator=model,
    param_grid=params,
    cv=5,
    scoring="accuracy"
)

grid_search.fit(X, y)

print("Best Parameters:", grid_search.best_params_)
print("Best Score:", grid_search.best_score_)