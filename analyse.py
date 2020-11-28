import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import xgboost
from sklearn.model_selection import GridSearchCV


df = pd.read_csv('dataset.csv', sep=';')
df = df.drop(['date', 'title', 'model'], axis=1)

cat_columns = df.columns[df.dtypes == object].tolist()
# print(cat_columns)
enc = OneHotEncoder(handle_unknown='ignore')
end_df = pd.DataFrame(enc.fit_transform(df[cat_columns]).toarray())
df = df.drop(cat_columns, axis=1)
df = df.join(end_df)

X = df.drop('price', axis=1)
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


model = xgboost.XGBRegressor()
parameters_for_testing = {
   'colsample_bytree':[0.4,0.6,0.8],
   'gamma':[0,0.03,0.1,0.3],
   'min_child_weight':[1.5,6,10],
   'learning_rate':[0.1,0.07],
   'max_depth':[3,5],
#    'n_estimators':[10000],
#    'reg_alpha':[1e-5, 1e-2,  0.75],
#    'reg_lambda':[1e-5, 1e-2, 0.45],
   'subsample':[0.6,0.95]  
}

gsearch1 = GridSearchCV(estimator=model, param_grid=parameters_for_testing, n_jobs=-1, iid=False, verbose=10, scoring='neg_mean_squared_error')
gsearch1.fit(X_train, y_train)
print('Grid scores: {}'.format(gsearch1.grid_scores_))
print('Best params: {}'.format(gsearch1.best_params_))
print('Best score: {}'.format(gsearch1.best_score_))

y_pred = gsearch1.best_estimator_.predict(X_test)
print(mean_absolute_error(y_test, y_pred))
