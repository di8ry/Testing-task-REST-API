import requests
from tqdm import tqdm

url = 'http://127.0.0.1:5000/'

for i in tqdm(range(600)):
    requests.get(url)
