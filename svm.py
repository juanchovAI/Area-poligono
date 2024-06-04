from auto_crear_poli import array_support_df
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score, mean_absolute_error
from sklearn.metrics import classification_report, confusion_matrix,mean_squared_error, r2_score
from sklearn import datasets
from sklearn.cluster import KMeans


def support_vm(array_support):

    y = array_support['convexo']
    X = array_support.drop(columns = ['convexo'])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    svm_classifier= SVC(kernel='poly',degree=3, C=5)
    svm_classifier.fit(X_train_scaled, y_train)

    y_pred = svm_classifier.predict(X_test_scaled)

    report = classification_report(y_test, y_pred)
    print(report)

    return svm_classifier, X_train

