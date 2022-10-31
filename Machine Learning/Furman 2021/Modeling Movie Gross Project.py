#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 22:06:36 2021

@author: noahjohnson
"""

import pandas as pd
import numpy as np
import ast
import warnings
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler, OrdinalEncoder 
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.feature_selection import f_regression, f_classif, SelectKBest
from xgboost import XGBRegressor, XGBClassifier

df = pd.read_csv("movies_original_with_imdb_2.csv")

# new_list = []

# for i in range(len(df["belongs_to_collection"])):
#     if df["belongs_to_collection"][i] != '1':
#         print((i, df["belongs_to_collection"][i]))
#         temp_dict = ast.literal_eval(df["belongs_to_collection"][i])
#         new_list.append(temp_dict["name"])
#     else:
#         new_list.append("n/a")
    
# df.belongs_to_collection = new_list

# df.to_csv("movies_original.csv", index = False)

# df['belongs_to_collection'] = np.where(df['belongs_to_collection'] == "0", 0, 1)
# df['release_month'] = [int(i.partition('/')[0]) for i in df["release_date"]]
# df['release_day'] = [int(i.partition('/')[2].partition('/')[0]) for i in df["release_date"]]
# df['release_year'] = [int(i.partition('/')[2].partition('/')[2]) for i in df["release_date"]]
# df['release_year'] = np.where(df['year'] >= 91, df['year'] + 1900, df['year'] + 2000)
df = df.drop(['id', 'imdb_id', 'overview', 'tagline', 'title'], axis = 1)

df['budget'] = [int(i[1:].replace(",", "")) for i in df['budget']]
df[' revenue '] = [int(i[1:].replace(",", "")) for i in df[' revenue ']]

imdb_df = pd.read_csv("title_ratings.tsv", sep = '\t')

# df = df.merge(imdb_df, how = 'inner', left_on = df["imdb_id"], right_on = imdb_df['tconst'])

# df = df.drop(['key_0', 'tconst'], axis = 1)

# df = df.rename(columns = {'averageRating': 'imdb_vote_average', 'numVotes': 'imdb_vote_count', 'vote_average':'tmdb_vote_average', 'vote_count':'tmdb_vote_count'})

# df.to_csv("movies_original.csv", index = False)

# df['agg_vote_average'] = [(df['imdb_vote_average'][i] * df['imdb_vote_count'][i] + df['tmdb_vote_average'][i] * df['tmdb_vote_count'][i]) / (df['imdb_vote_count'][i] + df['tmdb_vote_count'][i]) for i in range(len(df['imdb_vote_count']))]

# df['agg_vote_count'] = [(df['imdb_vote_count'][i] + df['tmdb_vote_count'][i]) for i in range(len(df['imdb_vote_count']))]

# df = df.drop(['imdb_vote_average', 'imdb_vote_count', 'tmdb_vote_average', 'tmdb_vote_count'], axis = 1)

# df.to_csv("movies_aggregated.csv", index = False)

# df = pd.read_csv("movies_original_with_imdb.csv")

df.corr()

df_test = pd.read_csv("movies_testing.csv")
df_test = df_test.drop(['title', 'id', 'imdb_id'], axis = 1)

warnings.filterwarnings("ignore")

X = df.iloc[:,:-1]
Y = df[' revenue ']

X_train_current = X
Y_train_current = Y
X_test_current = df_test.iloc[:,:-1]
Y_test_current = df_test[' revenue ']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.33)

def lr(X_train, Y_train, X_test, Y_test):
    lr_model_train = LinearRegression().fit(X_train, Y_train)
    Y_pred_train = lr_model_train.predict(X_test)
    lr_model_mae = '%11.02f'%float(mean_absolute_error(Y_test, Y_pred_train))
    lr_model_rsq = '%07.05f'%float(lr_model_train.score(X_test, Y_test))
    return (lr_model_mae, lr_model_rsq)

def best_knn_reg(X_train, Y_train, X_test, Y_test):
    min_mae = 1000000000000
    mae_n = 0
    max_r2 = 0
    r2_n = 0
    for i in range(2, 31):
        knn_reg_model = KNeighborsRegressor(n_neighbors = i).fit(X_train, Y_train)
        knn_Y_pred = knn_reg_model.predict(X_test)
        if mean_absolute_error(Y_test, knn_Y_pred) < min_mae:
            min_mae = mean_absolute_error(Y_test, knn_Y_pred)
            mae_n = i
        if knn_reg_model.score(X_test, Y_test) > max_r2:
            max_r2 = knn_reg_model.score(X_test, Y_test)
            r2_n = i
    best_knn_reg_mae = (mae_n, '%11.02f'%float(min_mae))
    best_knn_reg_rsq = (r2_n, '%07.05f'%float(max_r2))
    return (best_knn_reg_mae, best_knn_reg_rsq)

def best_reg_tree(X_train, Y_train, X_test, Y_test):
    min_mae_tree = 1000000000000
    mae_n_tree = 0
    max_r2_tree = 0
    r2_n_tree = 0
    for i in range(2, 31):
        tree_model = DecisionTreeRegressor(max_depth = i, random_state = 940687).fit(X_train, Y_train)
        tree_Y_pred = tree_model.predict(X_test)
        if mean_absolute_error(Y_test, tree_Y_pred) < min_mae_tree:
            min_mae_tree = mean_absolute_error(Y_test, tree_Y_pred)
            mae_n_tree = i
        if tree_model.score(X_test, Y_test) > max_r2_tree:
            max_r2_tree = tree_model.score(X_test, Y_test)
            r2_n_tree = i
    best_reg_tree_mae = (mae_n_tree, '%11.02f'%float(min_mae_tree))
    best_reg_tree_rsq = (r2_n_tree, '%07.05f'%float(max_r2_tree))
    return (best_reg_tree_mae, best_reg_tree_rsq)

def scale_svr(X_train, Y_train, X_test, Y_test):
    sc_X = StandardScaler() 
    sc_y = StandardScaler()
    X_scaled = sc_X.fit_transform(X_train) 
    Y_train = np.array(Y_train)
    Y_scaled = sc_y.fit_transform(Y_train.reshape(-1, 1))
    X_scaled_test = sc_X.fit_transform(X_test)
    Y_test = np.array(Y_test)
    Y_scaled_test = sc_y.fit_transform(Y_test.reshape(-1, 1))
    return (X_scaled, Y_scaled, X_scaled_test, Y_scaled_test)
    
def svr_model(X_train, Y_train, X_test, Y_test):
    scaled_svr_tuple = scale_svr(X_train, Y_train, X_test, Y_test)
    svr_model = SVR(kernel = "linear").fit(scaled_svr_tuple[0], scaled_svr_tuple[1].ravel())
    svr_Y_pred = svr_model.predict(X_test)
    svr_mae = '%11.02f'%float(mean_absolute_error(Y_test, svr_Y_pred))
    svr_rsq = '%07.05f'%float(svr_model.score(scaled_svr_tuple[2], scaled_svr_tuple[3]))
    return (svr_mae, svr_rsq)

def xgb_reg(X_train, Y_train, X_test, Y_test):
    xgb_model = XGBRegressor(n_estimators = 1000, max_depth = 15, eta = 0.1, colsample_bytree = 0.8).fit(X_train, Y_train)
    xgb_Y_pred = xgb_model.predict(X_test)
    xgb_mae = '%11.02f'%float(mean_absolute_error(Y_test, xgb_Y_pred))
    xgb_rsq = '%07.05f'%float(xgb_model.score(X_test, Y_test))
    return (xgb_mae, xgb_rsq)
    
###

lr_mae_dict = {}
lr_rsq_dict = {}
knn_reg_mae_dict = {} 
knn_reg_rsq_dict = {} 
reg_tree_mae_dict = {} 
reg_tree_rsq_dict = {} 
svr_mae_dict = {}
svr_rsq_dict = {}
xgb_mae_dict = {}
xgb_rsq_dict = {}

for j in range(28, 0, -1):
       
    fs = SelectKBest(f_regression, k = j).fit(X, Y)
    cols = fs.get_support(indices = True)
    X_train_fs = X_train_current.iloc[:,cols]
    #Y_train_fs = Y_train
    Y_train_fs = Y_train_current
    X_test_fs = X_test_current.iloc[:,cols]
    #Y_test_fs = Y_test
    Y_test_fs = Y_test_current
    
    lr_tuple = lr(X_train_fs, Y_train_fs, X_test_fs, Y_test_fs)
    lr_mae_dict[j] = lr_tuple[0]
    lr_rsq_dict[j] = lr_tuple[1]
    knn_reg_tuple = best_knn_reg(X_train_fs, Y_train_fs, X_test_fs, Y_test_fs)
    knn_reg_mae_dict[j] = knn_reg_tuple[0]
    knn_reg_rsq_dict[j] = knn_reg_tuple[1]
    reg_tree_tuple = best_reg_tree(X_train_fs, Y_train_fs, X_test_fs, Y_test_fs)
    reg_tree_mae_dict[j] = reg_tree_tuple[0]
    reg_tree_rsq_dict[j] = reg_tree_tuple[1]
    svr_tuple = svr_model(X_train_fs, Y_train_fs, X_test_fs, Y_test_fs)
    svr_mae_dict[j] = svr_tuple[0]
    svr_rsq_dict[j] = svr_tuple[1]
    xgb_tuple = xgb_reg(X_train_fs, Y_train_fs, X_test_fs, Y_test_fs)
    xgb_mae_dict[j] = xgb_tuple[0]
    xgb_rsq_dict[j] = xgb_tuple[1]
    
    feature_names = []
    for i in range(len(cols)):
        feature_names.append(df.columns[cols[i]])
    print(feature_names)
    print('\n')

orig_lr_tuple = lr(X_train_current, Y_train_current, X_test_current, Y_test_current) 
orig_knn_reg_tuple = best_knn_reg(X_train_current, Y_train_current, X_test_current, Y_test_current)
orig_reg_tree_tuple = best_reg_tree(X_train_current, Y_train_current, X_test_current, Y_test_current)
orig_svr_tuple = svr_model(X_train_current, Y_train_current, X_test_current, Y_test_current)
orig_xgb_tuple = xgb_reg(X_train_current, Y_train_current, X_test_current, Y_test_current)

mae_result_dict = {"linear regression" : {"original" : orig_lr_tuple[0], "feature selected" : min(lr_mae_dict.values())}, 
                       "KNN regression" : {"original" : orig_knn_reg_tuple[0], "feature selected" : min(knn_reg_mae_dict.values(), key=lambda x:x[1])}, 
                       "regression tree" : {"original" : orig_reg_tree_tuple[0], "feature selected" : min(reg_tree_mae_dict.values(), key=lambda x:x[1])}, 
                       "SVR" : {"original" : orig_svr_tuple[0], "feature selected" : min(svr_mae_dict.values())}, 
                       "XGBoost" : {"original" : orig_xgb_tuple[0], "feature selected" : min(xgb_mae_dict.values())}}
r2_result_dict = {"linear regression" : {"original" : orig_lr_tuple[1], "feature selected" : max(lr_rsq_dict.values())}, 
                       "KNN regression" : {"original" : orig_knn_reg_tuple[1], "feature selected" : max(knn_reg_rsq_dict.values(), key=lambda x:x[1])}, 
                       "regression tree" : {"original" : orig_reg_tree_tuple[1], "feature selected" : max(reg_tree_rsq_dict.values(), key=lambda x:x[1])}, 
                       "SVR" : {"original" : orig_svr_tuple[1], "feature selected" : max(svr_rsq_dict.values())},
                       "XGBoost" : {"original" : orig_xgb_tuple[1], "feature selected" : max(xgb_rsq_dict.values())}}
print(mae_result_dict)
print('\n')
print(r2_result_dict)

###

from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from tensorflow.keras import Sequential
from tensorflow.keras.losses import SparseCategoricalCrossentropy
from tensorflow.keras.metrics import SparseCategoricalAccuracy
from tensorflow.keras.layers import Dense
from sklearn.metrics import accuracy_score, confusion_matrix
from numpy.random import seed
from tensorflow.keras.utils import set_random_seed


p_30 = np.percentile(df[' revenue '], 30)
p_60 = np.percentile(df[' revenue '], 60)
p_90 = np.percentile(df[' revenue '], 90)

df1 = df.copy(deep = True)
df_test1 = df_test.copy(deep = True)

df1[' revenue '] = np.where(df1[' revenue '] <= p_30, -1, df1[' revenue '])
df1[' revenue '] = np.where((df1[' revenue '] > p_30) & (df1[' revenue '] <= p_60), -2, df1[' revenue '])
df1[' revenue '] = np.where((df1[' revenue '] > p_60) & (df1[' revenue '] <= p_90), -3, df1[' revenue '])
df1[' revenue '] = np.where((df1[' revenue '] > p_90), -4, df1[' revenue '])

df_test1[' revenue '] = np.where(df_test1[' revenue '] <= p_30, -1, df_test1[' revenue '])
df_test1[' revenue '] = np.where((df_test1[' revenue '] > p_30) & (df_test1[' revenue '] <= p_60), -2, df_test1[' revenue '])
df_test1[' revenue '] = np.where((df_test1[' revenue '] > p_60) & (df_test1[' revenue '] <= p_90), -3, df_test1[' revenue '])
df_test1[' revenue '] = np.where((df_test1[' revenue '] > p_90), -4, df_test1[' revenue '])

df1[' revenue '] = [np.abs(df1[' revenue '][i]) - 1 for i in range(len(df_test1[' revenue ']))]
df1[' revenue '] = df1[' revenue '].apply(str)

df_test1[' revenue '] = [np.abs(df_test1[' revenue '][i]) - 1 for i in range(len(df_test1[' revenue ']))]
df_test1[' revenue '] = df_test1[' revenue '].apply(str)

df1.to_csv("movies_with_imdb_nominal_rev.csv", index = False)

X_class = X
Y_class = df1[' revenue ']
X_train_class, X_test_class, Y_train_class, Y_test_class = train_test_split(X_class, Y_class, test_size = 0.33)
Y_train_class_nn = Y_train_class.astype('int64')
Y_test_class_nn = Y_test_class.astype('int64')

X_train_class_current = X_class
Y_train_class_current = Y_class
X_test_class_current = df_test1.iloc[:, :-1]
Y_test_class_current = df_test1[" revenue "]
Y_train_class_current_nn = Y_train_class_current.astype('int64')
Y_test_class_current_nn = Y_test_class_current.astype('int64')

def knn_class(X_train, Y_train, X_test, Y_test):
    max_accuracy = 0
    max_acc_n = 0
    max_acc_cm = 0
    for i in range(2, 31):
        knn_class_model = KNeighborsClassifier(n_neighbors = i).fit(X_train, Y_train)
        knn_class_Y_pred = knn_class_model.predict(X_test)
        knn_acc = accuracy_score(Y_test, knn_class_Y_pred)
        if knn_acc > max_accuracy:
            max_accuracy = knn_acc
            max_acc_n = i
            max_acc_cm = confusion_matrix(Y_test, knn_class_Y_pred)
    return tuple((tuple((max_acc_n, max_accuracy)), max_acc_cm))

def naive_bayes(X_train, Y_train, X_test, Y_test):
    nb_model = GaussianNB().fit(X_train, Y_train)
    nb_Y_pred = nb_model.predict(X_test)
    nb_acc = accuracy_score(Y_test, nb_Y_pred)
    nb_cm = confusion_matrix(Y_test, nb_Y_pred)
    return tuple((nb_acc, nb_cm))

def random_forest(X_train, Y_train, X_test, Y_test):
    rf_class = RandomForestClassifier(n_estimators = 250, criterion = 'entropy', max_features = 'sqrt', random_state = 460).fit(X_train, Y_train)
    rf_Y_pred = rf_class.predict(X_test)
    rf_acc = accuracy_score(Y_test, rf_Y_pred)
    rf_cm = confusion_matrix(Y_test, rf_Y_pred)
    return tuple((rf_acc, rf_cm))

def decision_tree_class(X_train, Y_train, X_test, Y_test):
    max_accuracy = 0
    max_acc_n = 0
    max_acc_cm = 0
    for i in range(2, 31):
        dt_class = DecisionTreeClassifier(criterion = 'entropy', max_depth = i, random_state = 242).fit(X_train, Y_train)
        dt_Y_pred = dt_class.predict(X_test)
        dt_acc = accuracy_score(Y_test, dt_Y_pred)
        if dt_acc > max_accuracy:
            max_accuracy = dt_acc
            max_acc_n = i
            max_acc_cm = confusion_matrix(Y_test, dt_Y_pred)
    return tuple((tuple((max_acc_n, max_accuracy)), max_acc_cm))

# def scale_svc(X_train, Y_train, X_test, Y_test):
#     sc_X = StandardScaler() 
#     X_scaled = sc_X.fit_transform(X_train) 
#     X_scaled_test = sc_X.fit_transform(X_test)
#     return (X_scaled, Y_train, X_scaled_test, Y_test)

# def svc_model(X_train, Y_train, X_test, Y_test):
#     scaled_svc_tuple = scale_svc(X_train, Y_train, X_test, Y_test)
#     svc_lin_class = SVC(kernel = "linear", class_weight = {'0' : 1, '1' : '1', '2' : 1, '3' : 3}).fit(scaled_svc_tuple[0], scaled_svc_tuple[1].ravel())
#     svc_lin_Y_pred = svc_lin_class.predict(X_test)
#     svc_lin_acc = accuracy_score(Y_test, svc_lin_Y_pred)
#     svc_lin_cm = confusion_matrix(Y_test, svc_lin_Y_pred)
#     svc_rad_class = SVC(kernel = "rbf", class_weight = {'0' : 1, '1' : 1, '2' : 1, '3' : 3}).fit(scaled_svc_tuple[2], scaled_svc_tuple[3].ravel())
#     svc_rad_Y_pred = svc_rad_class.predict(X_test)
#     svc_rad_acc = accuracy_score(Y_test, svc_rad_Y_pred)
#     svc_rad_cm = confusion_matrix(Y_test, svc_rad_Y_pred)
#     return tuple((tuple((svc_lin_acc, svc_lin_cm)), tuple((svc_rad_acc, svc_rad_cm))))

def xgb_class(X_train, Y_train, X_test, Y_test):
    warnings.filterwarnings("ignore")
    xgb_c = XGBClassifier(n_estimators = 1000, max_depth = 15, eta = 0.1, colsample_bytree = 0.8).fit(X_train, Y_train)
    xgb_c_Y_pred = xgb_c.predict(X_test)
    xgb_c_acc = accuracy_score(Y_test, xgb_c_Y_pred)
    xgb_c_cm = confusion_matrix(Y_test, xgb_c_Y_pred)
    return tuple((xgb_c_acc, xgb_c_cm))

def mlp_model(X_train, Y_train, X_test, Y_test):
    seed(390875)
    set_random_seed(705821)
    n_features = X_train.shape[1]
    model = Sequential()
    model.add(Dense(2000, activation = 'relu', kernel_initializer = 'he_normal', input_shape = (n_features,)))
    model.add(Dense(800, activation = 'relu', kernel_initializer = 'he_normal'))
    model.add(Dense(200, activation = 'relu', kernel_initializer = 'he_normal'))
    model.add(Dense(50, activation = 'relu', kernel_initializer = 'he_normal'))
    model.add(Dense(4, activation = 'softmax'))
    model.compile(optimizer = 'adam', loss = SparseCategoricalCrossentropy(), metrics = SparseCategoricalAccuracy())
    model.fit(X_train, Y_train, epochs = 10, verbose = 0)
    loss, mlp_acc = model.evaluate(X_test, Y_test, verbose = 0)
    mlp_Y_pred = np.argmax(model.predict(X_test), axis = 1)
    mlp_cm = confusion_matrix(Y_test, mlp_Y_pred)
    return tuple((mlp_acc, mlp_cm))

knn_class_accs = {}
knn_class_cms = {}
nb_accs = {}
nb_cms = {}
rf_accs = {}
rf_cms = {}
dt_accs = {}
dt_cms = {}
xgb_class_accs = {}
xgb_class_cms = {}
mlp_accs = {}
mlp_cms = {}


for j in range(28, 0, -1):
    fs_class = SelectKBest(f_classif, k = j).fit(X_train_class_current, Y_train_class_current)
    cols_class = fs_class.get_support(indices = True)
    X_train_fs_class = X_train_class_current.iloc[:, cols_class]
    Y_train_fs_class = Y_train_class_current
    X_test_fs_class = X_test_class_current.iloc[:, cols_class]
    Y_test_fs_class = Y_test_class_current
    Y_train_fs_class_nn = Y_train_class_current_nn
    Y_test_fs_class_nn = Y_test_class_current_nn
    
    knn_class_tuple = knn_class(X_train_fs_class, Y_train_fs_class, X_test_fs_class, Y_test_fs_class)
    knn_class_accs[j] = knn_class_tuple[0][1]
    knn_class_cms[knn_class_tuple[0][1]] = knn_class_tuple[1]
    
    nb_tuple =  naive_bayes(X_train_fs_class, Y_train_fs_class, X_test_fs_class, Y_test_fs_class)
    nb_accs[j] = nb_tuple[0]
    nb_cms[nb_tuple[0]] = nb_tuple[1]
     
    rf_tuple = random_forest(X_train_fs_class, Y_train_fs_class, X_test_fs_class, Y_test_fs_class)
    rf_accs[j] = rf_tuple[0]
    rf_cms[rf_tuple[0]] = rf_tuple[1]
    
    dt_tuple = decision_tree_class(X_train_fs_class, Y_train_fs_class, X_test_fs_class, Y_test_fs_class)
    dt_accs[j] = dt_tuple[0][1]
    dt_cms[dt_tuple[0][1]] = dt_tuple[1]
    
    xgb_class_tuple = xgb_class(X_train_fs_class, Y_train_fs_class, X_test_fs_class, Y_test_fs_class)
    xgb_class_accs[j] = xgb_class_tuple[0]
    xgb_class_cms[xgb_class_tuple[0]] = xgb_class_tuple[1]
    
    mlp_tuple = mlp_model(X_train_fs_class, Y_train_fs_class_nn, X_test_fs_class, Y_test_fs_class_nn)
    mlp_accs[j] = mlp_tuple[0]
    mlp_cms[mlp_tuple[0]] = mlp_tuple[1]
    
    feature_names_class = []
    for i in range(len(cols_class)):
        feature_names_class.append(df1.columns[cols_class[i]])
    print(feature_names_class)
    print('\n')
 
    
orig_knn_class_tuple = knn_class(X_train_class_current, Y_train_class_current, X_test_class_current, Y_test_class_current)
orig_nb_class_tuple = naive_bayes(X_train_class_current, Y_train_class_current, X_test_class_current, Y_test_class_current)
orig_rf_class_tuple = random_forest(X_train_class_current, Y_train_class_current, X_test_class_current, Y_test_class_current)
orig_dt_class_tuple = decision_tree_class(X_train_class_current, Y_train_class_current, X_test_class_current, Y_test_class_current)
orig_xgb_class_tuple = xgb_class(X_train_class, Y_train_class, X_test_class, Y_test_class)
orig_mlp_class_tuple = mlp_model(X_train_class, Y_train_class_nn, X_test_class, Y_test_class_nn)

result_dict = {"KNN classification" : {"original" : orig_knn_class_tuple[0][1], "feature selected" : max(knn_class_cms)}, 
                       "Naive Bayes" : {"original" : orig_nb_class_tuple[0], "feature selected" : max(nb_cms)}, 
                       "Random Forest" : {"original" : orig_rf_class_tuple[0], "feature selected" : max(rf_cms)}, 
                       "Decision Tree" : {"original" : orig_dt_class_tuple[0][1], "feature selected" : max(dt_cms)},
                       "XGBoost Classifier" : {"original" : orig_xgb_class_tuple[0], "feature selected" : max(xgb_class_cms)}, 
                       "MLP Neural Network" : {"original" : orig_mlp_class_tuple[0], "feature selected" : max(mlp_cms)}}  

cm_dict = {"KNN classification" : {"original" : orig_knn_class_tuple[1], "feature selected" : knn_class_cms[max(knn_class_cms)]}, 
                       "Naive Bayes" : {"original" : orig_nb_class_tuple[1], "feature selected" : nb_cms[max(nb_cms)]}, 
                       "Random Forest" : {"original" : orig_rf_class_tuple[1], "feature selected" : rf_cms[max(rf_cms)]}, 
                       "Decision Tree" : {"original" : orig_dt_class_tuple[1], "feature selected" : dt_cms[max(dt_cms)]},
                       "XGBoost Classifier" : {"original" : orig_xgb_class_tuple[1], "feature selected" : xgb_class_cms[max(xgb_class_cms)]}, 
                       "MLP Neural Network" : {"original" : orig_mlp_class_tuple[1], "feature selected" : mlp_cms[max(mlp_cms)]}}  

print('\n')
print('KNN Original Confusion Matrix\n')
print(cm_dict["KNN classification"]["original"])
print('\n')
print('KNN FS Confusion Matrix\n')
print(cm_dict["KNN classification"]["feature selected"])
print('\n')
print('Naive Bayes Original Confusion Matrix\n')
print(cm_dict["Naive Bayes"]["original"])
print('\n')
print('Naive Bayes FS Confusion Matrix\n')
print(cm_dict["Naive Bayes"]["feature selected"])
print('\n')  
print('Random Forest Original Confusion Matrix\n')
print(cm_dict["Random Forest"]["original"])
print('\n')
print('Random Forest FS Confusion Matrix\n')
print(cm_dict["Random Forest"]["feature selected"])
print('\n')
print('Decision Tree Original Confusion Matrix\n')
print(cm_dict["Decision Tree"]["original"])
print('\n')
print('Decision Tree FS Confusion Matrix\n')
print(cm_dict["Decision Tree"]["feature selected"])
print('\n')
print('XGBoost Original Confusion Matrix\n')
print(cm_dict["XGBoost Classifier"]["original"])
print('\n')
print('XGBoostc FS Confusion Matrix\n')
print(cm_dict["XGBoost Classifier"]["feature selected"])
print('\n')
print('MLP Neural Network Original Confusion Matrix\n')
print(cm_dict["MLP Neural Network"]["original"])
print('\n')
print('MLP Neural Network FS Confusion Matrix\n')
print(cm_dict["MLP Neural Network"]["feature selected"])
print('\n')
print('Accuracy Results\n')
print(result_dict)   
    
    