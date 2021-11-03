import numpy as np
import pandas as pd
from tqdm import tqdm
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import MinMaxScaler

def check_sign(phis, legi, feature_no):
    '''
    phis - Phishing Site Data
    legi - Legitimate Site Data
    feature_no - The feature for which sign needs to be checked
    '''
    if (phis.iloc[:,feature_no].mean() - legi.iloc[:,feature_no].mean())>=0:
        return -1
    else:
        return 1

def featureImportance(X, y):
    '''
    X - Data
    y - Labels
    n - The number of features to perturb
    '''
    dtc = DecisionTreeClassifier()
    dtc.fit(X, y)
    importance = dtc.feature_importances_
    df_impor = pd.DataFrame({'Feature':np.arange(0,importance.size), 'Importance':importance},columns=['Feature', 'Importance'])
    df_impor.sort_values(by=['Importance'], ascending=False,inplace=True)
    f = df_impor.iloc[:,0]
    phis = X[y==1]
    legi = X[y==0]
    d = [check_sign(phis, legi, x) for x in f]
    scaler = MinMaxScaler()
    scaler.fit(X)
    return f.to_numpy(), d, scaler
    
def perturbation(f, d, x, scaler, e = 0.05):
    '''
    X - Data
    f - feature_importance; A ranked feature vector
    d - Signed attack direction vector
    x - Sample to be perturbated
    scaler - Scaler used to transform values
    e - The total percentage of the input to modify
    '''
    sample = x
    sample = scaler.transform(sample.reshape(1, -1))
    E = e*np.sum(sample)/f.size
    for i in range(f.size):
        temp = sample[0][f[i]] + (E*d[i])
        if temp<0:
            temp = 0
        sample[0][f[i]] = temp
    sample = scaler.inverse_transform(sample)
    return np.round_(sample)