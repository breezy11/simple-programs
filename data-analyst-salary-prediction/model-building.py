# Imports
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


df = pd.read_csv("data/data.csv")

# choose relevant columns
df_model = df[['avg salary', "rating", "Size", 'Type of ownership', 'Industry', 'Sector', 'Revenue', 'comp_num',
               'state', 'age', 'python_yn', "spark_yn" ,"matlab_yn", "excel_yn", "jupyter_yn", "sql_yn", "spss_yn", "desc_len" ,"seniority"]]

# get dummy data
df_dum = pd.get_dummies(df_model)

# train test split
X = df_dum.drop("avg salary", axis=1)
y = df_dum["avg salary"].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# multiple linear regression
lm = LinearRegression()
lm.fit(X_train, y_train)

# print(np.mean(cross_val_score(lm, X_train, y_train, scoring='neg_mean_absolute_error', cv=3)))

# random forest
rf = RandomForestRegressor()

# print(np.mean(cross_val_score(rf, X_train, y_train,scoring='neg_mean_absolute_error', cv=3)))

# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start = 200, stop = 2000, num = 10)]
# Number of features to consider at every split
max_features = ['auto', 'sqrt']
# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(10, 110, num = 11)]
max_depth.append(None)
# Minimum number of samples required to split a node
min_samples_split = [2, 5, 10]
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 4]
# Method of selecting samples for training each tree
bootstrap = [True, False]

# Create the random grid
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}

rf_random = RandomizedSearchCV(estimator = rf, param_distributions = random_grid, n_iter = 10, cv = 3, verbose=2, random_state=42, n_jobs = -1)
rf_random.fit(X_train,y_train)

# test
pred_lm = lm.predict(X_test)
pred_rf = rf_random.predict(X_test)

print(mean_absolute_error(y_test,pred_lm))
print(mean_absolute_error(y_test,pred_rf))
