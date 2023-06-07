import requests
import argparse
import json
import ast

url = 'http://0.0.0.0:80/predict'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='inference script')
    parser.add_argument('--json_path', type=str)
    args = parser.parse_args()
    with open(args.json_path, encoding='utf-8-sig') as f:
        data = json.load(f)

    url = 'http://0.0.0.0:80/predict'
    x = requests.post(url, json=data)
    res = ast.literal_eval(x.text)
    print(type(res))

