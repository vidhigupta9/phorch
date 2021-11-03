import posixpath
import csv
import os
import requests
import os.path
import pickle
from figa import featureImportance, perturbation
from tqdm import tqdm

def download_model(save_dir = os.getcwd()+'/models/'):
    if not os.path.isfile(os.path.join(save_dir,'scaler.pkl')):
        print(os.path.join(save_dir,'scaler.pkl'))
        url = 'https://github.com/vidhigupta9/pytorch/raw/main/model/scaler.pkl'
        scaler = requests.get(url, allow_redirects=True)
        open(os.path.join(save_dir,'scaler.pkl'), 'wb').write(scaler.content)
    if not os.path.isfile(os.path.join(save_dir,'model.pkl')):
        url = 'https://github.com/vidhigupta9/pytorch/raw/main/model/model_FIGA_Trained.pkl'
        modelfile = requests.get(url, allow_redirects=True)
        open(os.path.join(save_dir,'model.pkl'), 'wb').write(modelfile.content)

def perturbate_data(data, percent = 0.3, n_combinations= 3, n_e_combinations = None):
    print("This might take few minutes depending on your machine's computing power.")
    total_data = data
    f, d, scaler = featureImportance(data.iloc[:,:-1], data.iloc[:,-1])
    if n_e_combinations is None:
        n_e_combinations = []
        for i in range(n_combinations):
            n_e_combinations.append((int((i+1)*len(f)/(n_combinations+1)),1-((i+1)*1/(n_combinations+1))))

    for n_f, e in n_e_combinations:
        data_to_perturb = data
        data_to_perturb = data_to_perturb.sample(frac=1).reset_index(drop=True)
        data_to_perturb = data_to_perturb.iloc[:int(data_to_perturb.shape[0]*0.3),:]
        X, y = data_to_perturb.iloc[:,:-1], data_to_perturb.iloc[:,-1]
        for i in tqdm(range(X.shape[0])):
            if y.iloc[i] == 1:
                X.iloc[i,:] = perturbation( f[:n_f], d[:n_f], X.iloc[i,:].to_numpy(), scaler, e).ravel()
        X[data.columns[-1]] = y
        total_data = total_data.append(X)
        del data_to_perturb
    total_data = total_data.sample(frac=1).reset_index(drop=True)
    return total_data