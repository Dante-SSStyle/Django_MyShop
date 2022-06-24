# MyShop

## Онлайн магазин на Django
### Start
#### Локально, сервер разработчика

<code>python manage.py runserver</code>

Также используются RabbitMQ, Celery и Redis

<code>rabbitmq-server</code>

<code>celery -A Django_MyShop worker -l info</code> - внутри проекта

Адрес: http://localhost:8000/


#### Необходимо создать .py файл с данными для  использования Braintree и SMTP (В данном проекте использовался mail.ru).

Смотри data_dict_example.py.


#### Cайт администрирования:

<code>python manage.py createsuperuser</code>

http://localhost:8000/admin/