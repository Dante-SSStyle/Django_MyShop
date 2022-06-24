# from celery.app import task
from django.core.mail import send_mail

from Django_MyShop.celery import app
from Django_MyShop.data_dict import email_data
from .models import Order


@app.task
def order_created(order_id):
    '''Задача отправки email-уведомлений при успешном оформлении заказа.'''
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order_id)
    message = 'Дорогой {}, \n\nВы успешно оформили заказ. Номер вашего заказа: {}.'\
        .format(order.first_name, order_id)
    mail_sent = send_mail(subject, message, email_data.get('Email'), [order.email])
    return mail_sent
