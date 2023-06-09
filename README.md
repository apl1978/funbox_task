# Квалификационное задание для разработчиков Python FUNBOX.

Приложение предназначено для учета посещенных ссылок. Приложение удовлетворяет следующим требованиям.

* Приложение написаное на языке Python версии 3.10
* Приложение предоставляет JSON API по HTTP
* Приложение предоставляет два HTTP ресурса
    - Ресурс загрузки посещений: POST /visited_links
    - Ресурс получения статистики: GET /visited_domains?from=...&to=...

**Установка:**

1. Запустить проект:

```bash
docker-compose up
```
2. Запустить тесты:

```bash
python manage.py test --verbosity 2
```

**Технологии:**
- Python 3
- Django
- Django Rest Framework
- Redis
- Docker
- Docker-compose.