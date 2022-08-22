# Проект Foodgram
![Build Status](https://github.com/xjt85/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/)

Сервис Foodgram предназначен для публикации рецептов. Авторизованные пользователи
могут подписываться на понравившихся авторов, добавлять рецепты в избранное,
в покупки, скачивать список покупок ингредиентов для добавленных в покупки
рецептов.

## Подготовка и запуск проекта
### Склонировать репозиторий на локальную машину:
```
git clone https://github.com/xjt85/foodgram-project-react
```
## Для работы с удаленным сервером (на Ubuntu):
* Выполните вход на свой удаленный сервер
```
ssh <login>@<IP>
```
* Установите docker на сервер:
```
sudo apt install docker.io 
```
* Установите docker-compose на сервер:
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
* Локально откройте файл infra/nginx.conf и в строке server_name впишите IP вашего удаленного сервера

* Скопируйте файлы docker-compose.yml и nginx.conf из директории infra на сервер:
```
cd infra
scp docker-compose.yml <username>@<host>:/home/<username>/docker-compose.yml
scp nginx.conf <username>@<host>:/home/<username>/nginx.conf
```

* Cоздайте .env файл и впишите:
    ```
    DB_ENGINE = <django.db.backends.postgresql>
    DB_NAME = <имя базы данных postgres>
    DB_USER = <пользователь бд>
    DB_PASSWORD = <пароль>
    DB_HOST = <db>
    DB_PORT = <5432>
    SECRET_KEY = <секретный ключ проекта django>
    ```
* Для работы с Workflow добавьте переменные окружения в раздел "Secrets" настроек репозитория:
    ```
    DB_ENGINE = <django.db.backends.postgresql>
    DB_NAME = <имя базы данных postgres>
    DB_USER = <пользователь бд>
    DB_PASSWORD = <пароль>
    DB_HOST = <db>
    DB_PORT = <5432>
    
    DOCKER_PASSWORD = <пароль от DockerHub>
    DOCKER_USERNAME = <имя пользователя>
    
    SECRET_KEY = <секретный ключ проекта django>

    USER = <username для подключения к серверу>
    HOST = <IP сервера>
    PASSPHRASE = <пароль для сервера, если он установлен>
    SSH_KEY = <ваш SSH ключ (для получения используйте команду: cat ~/.ssh/id_rsa)>

    TELEGRAM_TO = <ID чата, в который придет сообщение>
    TELEGRAM_TOKEN = <токен вашего бота>
    ```
    Workflow состоит из 4 шагов:
     - Проверка кода на соответствие PEP8
     - Сборка и публикация образа бекенда на DockerHub.
     - Автоматический деплой на удаленный сервер.
     - Отправка уведомления в телеграм-чат.  
  
* На удаленном сервере соберите docker-compose:
```
sudo docker-compose up -d --build
```
* После успешной сборки на удаленном сервере выполните команды (только после первого деплоя):
    - Соберите статические файлы:
    ```
    sudo docker-compose exec backend python manage.py collectstatic --noinput
    ```
    - Примените миграции:
    ```
    sudo docker-compose exec backend python manage.py migrate --noinput
    ```
    - Загрузите ингредиенты  в базу данных (не обязательно):  
    *Если файл не указывать, по умолчанию выберется ingredients.json*
    ```
    sudo docker-compose exec backend python manage.py load_ingredients <Название файла из директории data>
    ```
    - Создайте суперпользователя Django:
    ```
    sudo docker-compose exec backend python manage.py createsuperuser
    ```
    - Проект будет доступен по заданому IP-адресу

## Проект в интернете
Проект запущен и доступен по [адресу](http://51.250.30.21)

### Автор: Роман Чуклинов (xjavue).