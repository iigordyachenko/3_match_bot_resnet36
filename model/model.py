from dataclasses import dataclass
from pathlib import Path

import json
import sys
sys.path.append('/workdir/model')
from model_resnet import resnet34

import torch
import yaml


# load config file
config_path = Path(__file__).parent / "config.yaml"
with open(config_path, "r") as file:
    config = yaml.load(file, Loader=yaml.FullLoader)


def data_transform(json_f):
    #with open(json_f, encoding='utf-8-sig') as f:
        #return torch.tensor([json.load(f)['features']]).float()
    return torch.tensor([json_f['features']]).float()


def load_model():
    model = resnet34()
    model.load_state_dict(torch.load(config['modelpath'], map_location="cpu"))
    model.eval()
    def model_predict(json_f):
        state = data_transform(json_f)
        pred = model(state).sort(descending=True)
        return pred.indices[0].tolist()

    return model_predict
