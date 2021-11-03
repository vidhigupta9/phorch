import torch
from torch import nn

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.linear_layers = nn.Sequential(
                        nn.Linear(111,50),
                        nn.ReLU(),
                        nn.Dropout(p=0.2),
                        nn.Linear(50,20),
                        nn.ReLU(),
                        nn.Dropout(p=0.4),
                        nn.Linear(20,10),
                        nn.ReLU(),
                        nn.Dropout(p=0.4),
                        nn.Linear(10,2)
        )

    # Defining the forward pass    
    def forward(self, x):
        x = self.linear_layers(x)
        return x