![Header](git_hub/preview.png)
[![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)](https://www.django-rest-framework.org/)
[![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)

# Digests Searcher

## Отписание

**«Digests Searcher»** - микросервис, который формирует дайджесты контента
для пользователей на основе их подписок. Дайджест представляет собой выборку
постов из различных источников, на которые подписан пользователь.

### Функионал

1. Получение запроса на формирование дайджеста: Микросервис принимаeт запрос от основного приложения на формирование дайджеста для
   пользователя, идентифицируемого по уникальному ID.

2. Определение подписок пользователя: После получения запроса, микросервис
   должен определяет источники, на которые подписан пользователь, используя
   информацию о подписках пользователя.

3. Сбор постов из подписок: Зная подписки пользователя, микросервис 
   собираeт посты из этих источников. 

4. Фильтрация постов: Собранные посты фильтруются по рейтингу

5. Создание дайджеста: После фильтрации, оставшиеся посты упаковываются в
   дайджест. Дайджест - это совокупность постов, отобранных для пользователя.

6. Отправка дайджеста: Сформированный дайджест возвращается в главное
   приложение, которое предоставит его пользователю.

# Технологии

- [Python 3.10](https://www.python.org/downloads/release/python-388/)
- [Django 4.2.3](https://www.djangoproject.com/download/)
- [Django Rest Framework 3.14.0](https://www.django-rest-framework.org/)
- [PostgreSQL 13.0](https://www.postgresql.org/download/)
- [gunicorn 20.0.4](https://pypi.org/project/gunicorn/)
- [nginx 1.19.3](https://nginx.org/ru/download.html)
- # Контейнер

- [Docker 20.10.14](https://www.docker.com/)
- [Docker Compose 2.4.1](https://docs.docker.com/compose/)

# URL's

- http://localhost/api/

# Локальная установка

Клонируйте репозиторий и перейдите в него в командной строке:

```sh
git clone https://github.com/kvazymir1199/digests_searcher.git && cd digests_searcher
```

Создайте .env файл командой:

```sh
touch .env
```

и заполните его данными:

```sh
#.env
DB_ENGINE=<django.db.backends.postgresql>
DB_NAME=<имя базы данных postgres>
DB_USER=<пользователь бд>
DB_PASSWORD=<пароль>
DB_HOST=<db>
DB_PORT=<5432>
SECRET_KEY=<секретный ключ проекта django>
```

Выполните команду

```sh
docker-compose up -d
```
Для заполнения базы тестовыми данными воспользуйтесь командой
```sh
docker-compose run backend python manage.py fill_database
```
Для получения доступа к данным можно использовать консоль или воспользуйтесь 
встроенной admin панелью.
Создайте супер пользователя командой:
```sh
docker-compose run backend python manage.py createsuperuser --email
admin@yandex.ru --username admin
```
Перейдите по ссылке и следуйте форме входа
- http://localhost/admin

# Примеры запросов

**GET**: http://127.0.0.1:8000/api/users/
Пример ответа:

```json
[
    {
        "id": 1,
        "name": "Denis"
    },
    {
        "id": 2,
        "name": "Anton"
    },
    {
        "id": 3,
        "name": "Vladimir"
    },
    {
        "id": 4,
        "name": "Kiril"
    }
]
```
**GET**: http://127.0.0.1:8000/api/users/1/
Пример ответа:

```json
[
    {
        "id": 1,
        "name": "Denis"
    }
]
```
**GET**: http://127.0.0.1:8000/api/users/1/digest
Пример ответа:

```json
{
  "posts": [
    "Сенсация: биткоин достиг исторического минимума",
    "В ожидании выхода God of War 3",
    "Рецепт Домашние блинчики с начинкой",
    "Курс рубля показывает 'небывалый успех'"
  ]
}
```
Для фильтрации по рейтингу используйте query_params в запросе
**GET**: http://127.0.0.1:8000/api/users/1/digest?rating=9
Пример ответа:

```json
{
    "posts": [
        "Сенсация: биткоин достиг исторического минимума"
    ]
}
```
## Автор:
* [kvazymir1199](https://github.com/kvazymir1199)