# BOT 3match
## Быстрый старт
### Клонируем репозитарий
```
git clone https://github.com/iigordyachenko/3_match_bot_resnet36.git
cd 3_match_bot_resnet36
```
### Docker build
```
docker build -t default-service-fastpai:latest . 
```
### Docker run
Здесь инициализируется REST API
```
docker container run --publish 80:80 --name demo-app-container default-service-fastpai:latest  
```
К какому хосту и порту обращаться 
```
http://0.0.0.0:80/
```
### Отправка json для инференса модели осуществляется через метод predict
```
http://0.0.0.0:80/predict
```
На выходе будет строка с номерами граней ходов
```
'[103, 102, 2, ..., 1]'
```
Грани отсортированы по вероятности. Выбираем первый элемент в массиве, если этот ход оказывается невалидным, то берем следующий элемент.
### Как выглядит инференс на python
3_match_bot_resnet36/json_predict/predict.py

Отправленный пример json был с encoding='utf-8-sig', поэтому здесь указана такая кодирвока. 
```
import requests
import argparse
import json
import ast


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='inference script')
    parser.add_argument('--json_path', type=str)
    args = parser.parse_args()
    
    with open(args.json_path, encoding='utf-8-sig') as f:
        data = json.load(f)
    url = 'http://0.0.0.0:80/predict'
    
    x = requests.post(url, json=data)
    #Преобразование строки в list
    res = ast.literal_eval(x.text)
    print(type(res))

```
