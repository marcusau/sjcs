import yaml
from dataclasses import dataclass
import functools


@functools.lru_cache(maxsize=2)
def read_config():
    with open('config.yaml', 'r') as fr:
        return yaml.load(fr, Loader=yaml.FullLoader)


dataclass
class CONFIG:
    model_name: str=read_config()['model']
    base_url: str=read_config()['base_url']
    temperature: int=read_config()['temperature']
    seed: int = read_config()['seed']
    top_p: int = read_config()['top_p']
    num_predict: int =read_config()['num_predict']
   
config=CONFIG()
model_para={"temperature":config.temperature,"seed":config.seed,"top_p":config.top_p,"num_predict":config.num_predict}