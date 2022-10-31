#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 08:26:12 2022

@author: noahjohnson
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report,confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from imblearn.combine import SMOTETomek, SMOTEENN

train_df = pd.read_excel("Mather Project Overview - Spring 2022 UPDATED/mather_retention_1621_with_dd1.xlsx")
test_df = pd.read_excel("Mather Project Overview - Spring 2022 UPDATED/mather_retention_testing_2022_with_dd.xlsx")

# le_train = LabelEncoder()
# le_train.fit(train_df["mail_county"])
# train_df["mail_county"] = le_train.transform(train_df["mail_county"])
# le_test = LabelEncoder()
# le_test.fit(test_df["mail_county"])
# test_df["mail_county"] = le_test.transform(test_df["mail_county"])

X = train_df[["days", "wp", "delivery_cost", "avg_age", "tenure", "miles_from_base"]]
y = train_df["ny_status"]

X, y = SMOTETomek(random_state = 1950641).fit_resample(X, y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)

rfc = RandomForestClassifier(n_estimators=100,criterion="entropy",max_features="sqrt")
rfc.fit(X_train, y_train.values.ravel()) 
rfc_pred = rfc.predict(X_test)
print(confusion_matrix(y_test,rfc_pred))
print(classification_report(y_test,rfc_pred))
print(accuracy_score(y_test,rfc_pred))

X_train = X
y_train = y
X_test = test_df[["days", "wp", "delivery_cost", "tenure", "avg_age", "miles_from_base", "mail_county"]]
rfc.fit(X_train, y_train.values.ravel())
rfc_pred_1 = rfc.predict(X_test)
test_df["probs_2022"] = rfc_pred_1

test_df.to_excel("Mather Project Overview - Spring 2022 UPDATED/predicted_ny_status_rf_2022.xlsx")


