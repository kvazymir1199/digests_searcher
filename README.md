![Header](git_hub/preview.png)
[![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)](https://www.django-rest-framework.org/)
[![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)

![Digests Searcher](https://github.com/kvazymir1199/foodgram-project-react/actions/workflows/foodgram_react_project_workflow.yml/badge.svg)

# Digests Searcher

## Отписание

**«Digests Searcher»** - микросервис, который формирует дайджесты контента
для пользователей на основе их подписок. Дайджест представляет собой выборку
постов из различных источников, на которые подписан пользователь.

### Функионал

1. Получение запроса на формирование дайджеста: Микросервис должен уметь
   принимать запросы от основного приложения на формирование дайджеста для
   пользователя, идентифицируемого по уникальному ID.

2. Определение подписок пользователя: После получения запроса, микросервис
   должен определить источники, на которые подписан пользователь, используя
   информацию о подписках пользователя.

3. Сбор постов из подписок: Зная подписки пользователя, микросервис должен
   собирать посты из этих источников. Подумайте о нём как о "сканере" подписок
   пользователя в поисках нового контента.

4. Фильтрация постов: Из собранных постов отфильтруйте те, которые не
   соответствуют интересам пользователя или недостаточно популярны. Микросервис
   должен использовать определенные критерии для фильтрации.

5. Создание дайджеста: После фильтрации, оставшиеся посты упаковываются в
   дайджест. Дайджест - это совокупность постов, отобранных для пользователя.

6. Отправка дайджеста: Сформированный дайджест возвращается в главное
   приложение, которое предоставит его пользователю.

# Технологии

- [Python 3.10](https://www.python.org/downloads/release/python-388/)
- [Django 3.2](https://www.djangoproject.com/download/)
- [Django Rest Framework 3.12.4](https://www.django-rest-framework.org/)
- [PostgreSQL 13.0](https://www.postgresql.org/download/)
- [gunicorn 20.0.4](https://pypi.org/project/gunicorn/)
- [nginx 1.19.3](https://nginx.org/ru/download.html)
- # Контейнер

- [Docker 20.10.14](https://www.docker.com/)
- [Docker Compose 2.4.1](https://docs.docker.com/compose/)

# URL's

- http://localhost/