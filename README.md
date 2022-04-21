# yatube_api
## API для соц. сети авторов статей

Технологии:

- Python and Django
- Rest Framework
- TokenAuthentication

## Установка

- Создайте и активируйте виртуальное окружение
- Установите все необходимые пакеты из requirements.txt.
- Примените миграции

## Примеры запросов к API:
| Ресурс | Тип | Путь | Передаваемые данные (JSON) |
| ------ | ------ | ------ | ------ |
| Получить API токен | POST | /api/v1/api-token-auth/ | {"username":"","password":""}
| Получить Список постов | GET | /api/v1/posts/ |
| Добавить пост | POST | /api/v1/posts/ | {"text": "","group": ""} 

## Эндпоинты
| Путь | Тип | Описание |
| ------ | ------ | ------ |
| api/v1/api-token-auth/ | (POST) | передаём логин и пароль, получаем токен |
| api/v1/posts/ | (GET, POST) | получаем список всех постов или создаём новый пост |
| api/v1/posts/{post_id}/ | (GET, PUT, PATCH, DELETE) | получаем, редактируем или удаляем пост по i |
| api/v1/groups/ | (GET) | получаем список всех групп |
| api/v1/groups/{group_id}/ | (GET) | получаем информацию о группе по id |
| api/v1/posts/{post_id}/comments/ | (GET, POST) | получаем список всех комментариев поста с id=post_id или создаём новый, указав id поста, который хотим прокомментировать |
| api/v1/posts/{post_id}/comments/{comment_id}/ | (GET, PUT, PATCH, DELETE) | получаем, редактируем или удаляем комментарий по id у поста с id=post_id |

**Free Software, Hell Yeah!**