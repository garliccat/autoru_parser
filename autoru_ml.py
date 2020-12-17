import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor
import xgboost
from sklearn.model_selection import GridSearchCV


df = pd.read_csv('autoru.csv', sep=';')
df = df.drop(['title', 'model'], axis=1)

cat_columns = df.columns[df.dtypes == object].tolist()
# print(cat_columns)
enc = OneHotEncoder(handle_unknown='ignore')
enc_df = pd.DataFrame(enc.fit_transform(df[cat_columns]).toarray())
df_2 = df.drop(cat_columns, axis=1)
df_2 = df.join(enc_df)

X = df_2.drop('price', axis=1)
y = df_2['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

model = RandomForestRegressor()

parameters_for_testing = {
   'max_depth':range(1, 10),
   'n_estimators':range(100, 500, 100),
   'min_samples_split': [5],
   'max_depth': [6],
   }

gsearch = GridSearchCV(estimator=model, param_grid=parameters_for_testing, n_jobs=-1, verbose=10)
gsearch.fit(X_train, y_train)

# print('Grid scores: {}'.format(gsearch.grid_scores_))
print('Best params: {}'.format(gsearch.best_params_))
print('Best score: {}'.format(gsearch.best_score_))

y_pred = gsearch.best_estimator_.predict(X_test)
print(r2_score(y_test, y_pred))
print()
print(gsearch.best_estimator_.predict(X_verify))

df_valid = pd.DataFrame.from_dict({'brand': ['mitsubishi'], 
    'gear': ['автомат'], 
    'drive': ['передний'], 
    'color': ['красный'], 
    'year': [2006], 
    'mileage': [230000], 
    'price': [250000], 
    'eng_vol': [1.6], 
    'hps': [60], 
    'gas_type': ['Бензин']})
enc_df_valid = pd.DataFrame(enc.transform(df_valid[cat_columns]).toarray())
df_valid = df_valid.drop(cat_columns, axis=1)
df_valid = df_valid.join(enc_df_valid)

X_valid = df_valid.drop('price', axis=1)
y_valid = df_valid['price']

print('Predicted car price: {}'.format(gsearch.best_estimator_.predict(X_valid)))
print('Actual car price: {}'.format(y_valid))

# model.fit(X_train, y_train)
# predictions = model.predict(X_test)

# model = xgboost.XGBRegressor()
# parameters_for_testing = {
#    'colsample_bytree':[0.4,0.6,0.8],
#    'gamma':[0,0.03,0.1,0.3],
#    'min_child_weight':[1.5,6,10],
#    'learning_rate':[0.1,0.07],
#    'max_depth':[3,5],
# #    'n_estimators':[10000],
# #    'reg_alpha':[1e-5, 1e-2,  0.75],
# #    'reg_lambda':[1e-5, 1e-2, 0.45],
#    'subsample':[0.6,0.95]  
# }

# gsearch1 = GridSearchCV(estimator=model, param_grid=parameters_for_testing, n_jobs=-1, iid=False, verbose=10, scoring='neg_mean_squared_error')
# gsearch1.fit(X_train, y_train)
# print('Grid scores: {}'.format(gsearch1.grid_scores_))
# print('Best params: {}'.format(gsearch1.best_params_))
# print('Best score: {}'.format(gsearch1.best_score_))

# y_pred = gsearch1.best_estimator_.predict(X_test)
# print(mean_absolute_error(y_test, y_pred))
