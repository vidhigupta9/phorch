import requests
import os
import os.path
import pickle
import torch
from utils import download_model
from extract import extract_url
from model import Net
import numpy as np
import collections
from extract import *

class Detector(object):
    def __init__(self, models_dir = os.getcwd()+'/models'):
        self.model = Net()
        if os.path.isfile(os.path.join(models_dir,'scaler.pkl')):
            self.scaler = pickle.load(open(os.path.join(models_dir,'scaler.pkl'), 'rb'))
        else:
            download_model(models_dir)
            self.scaler = pickle.load(open(os.path.join(models_dir,'scaler.pkl'), 'rb'))
        if os.path.isfile(os.path.join(models_dir,'model.pkl')):
            self.model.load_state_dict(torch.load(os.path.join(models_dir,'model.pt'),map_location=torch.device('cpu')))
        else:
            download_model(models_dir)
            self.model.load_state_dict(torch.load(os.path.join(models_dir,'model.pt'),map_location=torch.device('cpu')))
        #self.model.load_state_dict(torch.load(os.path.join(models_dir,'model.pt'),map_location=torch.device('cpu')))

    def detect(self, url):
        features = extract_url(url)
        features = [w.replace('True', '1').replace('False', '0') for w in np.array(features).astype(str)]
        features = np.array((features)).astype(float)
        features = torch.tensor(self.scaler.transform(features.reshape(1,-1)).ravel())
        output = self.model(features.float().unsqueeze(0))
        _, pred = torch.max(output, 1)
        return pred.item()