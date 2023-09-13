### Yatube API

Автор проекта - Константин Мельник.

## Tecnhologies

- Python 3.10
- Django 3.2.16
- Django REST framework 3.12.4


Проект имитирует работу реальной соц. сети через API сервис. Аутентификация по JWT-token. С помощью API-сервисов можно оставлять публикации в различные группы, комментировать их и подписываться на других пользователей.

Документация по API:
http://127.0.0.1:8000/redoc/

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:abyxez/api_final_yatube.git
```

```
cd api_final_yatube/
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:
```
cd yatube_api/
```

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

Этот проект имитирует работу социальной сети без front-end части с использованием API cервисов.

Возможные запросы к серверу:

http://127.0.0.1:8000/posts/ - GET/POST
Получить список всех постов всех пользователей/ Написать свой в JSON формате

http://127.0.0.1:8000/posts/5 - GET
Просмотреть детали выбранного поста

