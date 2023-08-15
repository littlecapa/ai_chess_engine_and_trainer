import torch, hashlib
import torch.nn as nn
from libs.eval_lib import MATE_IN_ONE_VALUE
import logging

class Eval_Net_KRk(nn.Module):
    def __init__(self):
        super(Eval_Net_KRk, self).__init__()
        
        # Input layer: 832xboolean values
        self.input_layer = nn.Linear(832, 832)
        
        # Hidden layers (4 layers): 1664xfloat values each
        self.hidden_layers = nn.Sequential(
            nn.Linear(832, 1664),
            nn.ReLU(),
            nn.Linear(1664, 256),
            nn.ReLU(),
            nn.Linear(256, 64),
            nn.ReLU(),
            nn.Linear(64, 8),
            nn.ReLU()
        )
        
        self.output_layer = nn.Linear(8, 1)
        self.first_output = True

    def forward(self, x):
        x = self.input_layer(x)
        x = self.hidden_layers(x)
        x = self.output_layer(x)
        x = torch.tanh(x) * MATE_IN_ONE_VALUE
        if self.first_output == True:
            self.first_output = False
            logging.info(f"Net Output: {x} {x.size}")
        return x.squeeze(-1)

    def get_name(self):
        return "KRk_Beginner"
    
    def get_hash_value(self):
        # Serialize the model's state_dict into a string
        state_dict_str = str(self.state_dict()) + str(self.named_parameters)
        # Compute the SHA-256 hash of the state_dict string
        sha256_hash = hashlib.sha256(state_dict_str.encode()).hexdigest()
        # Convert the hexadecimal hash to an integer
        hash_value = abs(int(sha256_hash, 16))
        return hash_value