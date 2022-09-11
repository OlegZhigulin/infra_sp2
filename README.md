## Описание
YaMDb - это новый веб сервис, который собирает отзывы пользователей на различные произведения (книги, фильмы, музыку и т.д.) Через этот интерфейс могут работать мобильное приложение или чат-бот; через него же можно будет передавать данные в любое приложение или на фронтенд.

#### Реализован функционал, дающий возможность:
* Оставлять и редактировать отзывы на произведения.
* Комментировать отзывы и редактировать эти комментарии.
* Добавлять в базу данных новые произведения, категории, жанры (для прользователей с правами доступа Администратора) 
* Ставить оценки произведениям, видеть их рейтинг.

Для выполнения всех запросов существуют различные уровни доступа (автор поста/комментария, авторизованный пользователь, неавторизованный пользователь, модератор, администратор, суперюзер Django).

Механизм авторизации пользователей реализован с помощью JWT-токенов, причем токен пользователь получает после подтверждения своего e-mail 

### Технологии
``` 
Python 3.7
Django 2.2.19
DRF 3.12.4
docker-compose 3.8
```

# Endpoint:
- /auth   : аутентификация.
- /users   : пользователи.
- /genres   : жанры произведений. Одно произведение может быть привязано к нескольким жанрам.
- /titles   : произведения, к которым пишут отзывы (определённый фильм, книга или песенка).
- /categories   : категории (типы) произведений («Фильмы», «Книги», «Музыка»).
- /comments   : комментарии к отзывам. Комментарий привязан к определённому отзыву.
- /reviews   : отзывы на произведения. Отзыв привязан к определённому произведению.



# инструкция по запуску и настройке

## в терминале выполнить команду:
git clone git@github.com:OlegZhigulin/infra_sp2.git


## В переменную окружения .env добавить:
```{
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME= # имя базы данных
POSTGRES_USER= # логин для подключения к базе данных
POSTGRES_PASSWORD= # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД }
```
## Перейти в папку infra и запустить docker-compose.yaml (при установленном и запущенном Docker)

cd infra_sp2/infra

<<<<<<< HEAD
## для запуска контейнера выполнить команду :
### с логами в терминале:
docker-compose up --build
### без логов в терминале:
docker-compose up -d --build
=======
## для запуска контейнера выполнить команду:

docker-compose up -d --build

>>>>>>> 18be7ef5881531982a63dffc8666942815de83c2
## после успешного запуска подготовить миграции

docker-compose exec web python manage.py makemigrations

## и выполнить миграции

docker-compose exec web python manage.py migrate

## создать суперпользователя 

docker-compose exec web python manage.py createsuperuser

## и собрать статику

docker-compose exec web python manage.py collectstatic --no-input 

## Теперь проект доступен по адресу: http://localhost/admin/

<<<<<<< HEAD
# Примеры запросов к API:

### Авторизация пользователя
На эндпоинт http://localhost/api/v1/auth/signup/ передаем POST запрос с параметрами username и email. 
В консоли видим эмуляцию отправки электронного письма:
```
{
    nginx_1  | 192.168.48.1 - - [10/Sep/2022:16:45:42 +0000] "POST /api/v1/auth/signup/ HTTP/1.1" 200 48 "-" "PostmanRuntime/7.29.0" "-"
    web_1    | Content-Type: text/plain; charset="utf-8"
    web_1    | MIME-Version: 1.0
    web_1    | Content-Transfer-Encoding: 7bit
    web_1    | Subject: =?utf-8?b?0JrQvtC0INC/0L7QtNCy0LXRgNC20LTQtdC90LjRjw==?=
    web_1    | From: admin@email.com
    web_1    | To: sthjring@gdfd.ccc
    web_1    | Date: Sat, 10 Sep 2022 16:45:43 -0000
    web_1    | Message-ID: <166282834346.9.14572168642777625108@dbc31c8fcedf>
    web_1    |
    web_1    |**642-1a534c7de4ab349347ce**
}
```
### Получаем JWT-токен
Далее, на эндпоинт http://localhost/api/v1/auth/token/ передаем POST запрос с параметрами username и confirmation_code. В ответ получаем JWT-токен, который используем для выполнения запросов POST, DELETE, PATCH, PUT как авторизованный пользователь.
=======
# Примеры запросов к API Yatube:

### Получаем JWT-токен
На эндпоинт http://127.0.0.1:8000/api/v1/auth/signup/ передаем POST запрос с параметрами username и email. 
В ответ на указанный email получаем confirmation_code.
Далее, на эндпоинт http://127.0.0.1:8000/api/v1/auth/token/ передаем POST запрос с параметрами username и confirmation_code. В ответ получаем JWT-токен, который используем для выполнения запросов POST, DELETE, PATCH, PUT как авторизованный пользователь.
>>>>>>> 18be7ef5881531982a63dffc8666942815de83c2

При отправке запроса передавайте токен в заголовке Authorization: Bearer <<токен>>

### Создаем новoe произведение 
<<<<<<< HEAD
Передаем POST-запрос на адрес http://localhost/api/v1/titles/ 
=======
Передаем POST-запрос на адрес http://127.0.0.1:8000/api/v1/titles/ 
>>>>>>> 18be7ef5881531982a63dffc8666942815de83c2
Обязательные поля:   
```
{ 
    "name": "Красная шапочка",  
    "year": 1697,  
    "description": "Старинное произведение Ш.Перро",  
    "genre": [  
    "сказка"  
    ],  
    "category": "книга"  
}  
```
Ответ будет выглядеть следующим образом:   

```
{  
    "id": 1,  
    "name": "Красная шапочка",  
    "year": 1697,  
    "rating": 0,  
    "description": "Старинное произведение Ш.Перро",  
    "genre": [  
        "name": "сказка",  
        "slug": "tale"  
    ],  
    "category": {  
        "name": "книга",  
        "slug": "book"  
    } 
} 
```

### Получаем отзыв по id для указанного произведения.
<<<<<<< HEAD
Передаем GET-запрос на адрес http://localhost/api/v1/titles/{title_id}/reviews/{review_id}/
=======
Передаем GET-запрос на адрес http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/
>>>>>>> 18be7ef5881531982a63dffc8666942815de83c2

Ответ будет выглядеть следующим образом:

```
{  
    "id": review_id,  
    "text": "string",  
    "author": "string",  
    "score": 1,  
    "pub_date": "2019-08-24T14:15:22Z"   
} 
```

### Частично обновляем комментарий к отзыву по id.
Для этого действия вы должны быть автором комментария, модератором или администратором. 
<<<<<<< HEAD
Передаем PATCH запрос на эндпоинт http://localhost/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/ с параметром "text": "Измененный текст комментария". 
=======
Передаем PATCH запрос на эндпоинт http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/ с параметром "text": "Измененный текст комментария". 
>>>>>>> 18be7ef5881531982a63dffc8666942815de83c2

Ответ будет выглядеть следующим образом:  

```
{ 
    "id": title_id,  
    "text": "Измененный текст комментария",  
    "author": "string",  
    "pub_date": "2019-08-24T14:15:22Z"  
}   
```
### Добавляем новый жанр
Для этого действия необходимо обладать правами администратора.  
<<<<<<< HEAD
Передаем POST запрос на эндпоинт http://localhost/api/v1/genres/  
=======
Передаем POST запрос на эндпоинт http://127.0.0.1:8000/api/v1/genres/  
>>>>>>> 18be7ef5881531982a63dffc8666942815de83c2
Заполняем поля:

```
{
  "name": "ужасы",
  "slug": "horror"
}
```
Ответ будет выглядеть следующим образом:

```
{
  "name": "ужасы",
  "slug": "horror"
}
```


# Документация (запросы для работы с API): http://localhost/redoc/


# для завершения работы нажмите Ctrl+C

### автор Жигулин Олег телеграм @Oleg_Zhigulin
