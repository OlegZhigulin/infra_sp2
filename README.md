# Учебный проект по работе с докером
### Описание
Содержит апи сервис в котором можно оставлять отзывы на произведения 
### Технологии
Python 3.7
Django 2.2.19
DRF 3.12.4
docker-compose 3.8

# Endpoint:
- /auth   : аутентификация.
- /users   : пользователи.
- /genres   : жанры произведений. Одно произведение может быть привязано к нескольким жанрам.
- /titles   : произведения, к которым пишут отзывы (определённый фильм, книга или песенка).
- /categories   : категории (типы) произведений («Фильмы», «Книги», «Музыка»).
- /comments   : комментарии к отзывам. Комментарий привязан к определённому отзыву.
- /reviews   : отзывы на произведения. Отзыв привязан к определённому произведению.



# инструкция по запуску и настройке

# в терминале выполнить команду:
git@github.com:OlegZhigulin/infra_sp2.git


В переменную окружения .env добавить:

DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME= # имя базы данных
POSTGRES_USER= # логин для подключения к базе данных
POSTGRES_PASSWORD= # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД 


# для запуска контейнера выполнить команду:

docker-compose up -d --build

# после успешного запуска подготовить миграции

docker-compose exec web python manage.py makemigrations

# и выполнить миграции

docker-compose exec web python manage.py migrate

# создать суперпользователя 

docker-compose exec web python manage.py createsuperuser

# и собрать статику

docker-compose exec web python manage.py collectstatic --no-input 

# Теперь проект доступен по адресу: http://localhost/admin/

# Документация (запросы для работа с API): http://localhost/redoc/


# для завершения работы нажмите Ctrl+C

# автор Жигулин Олег телеграм @Oleg_Zhigulin