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
