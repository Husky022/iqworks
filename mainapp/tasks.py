from time import sleep
from django.core.mail import send_mail
from django.template.loader import render_to_string
from celery import shared_task

@shared_task()
def send_email_task(name, mail_client, mail_iqw, phone):
    sleep(5)  # Simulate expensive operation(s) that freeze Django
    client = f'Имя: ' + name + 'Почта: ' + mail_client + 'Телефон: ' + phone
    send_mail('Новая заявка', client, mail_iqw, [mail_iqw])
    data = {'name': name, 'mail': mail_client, 'phone': phone}
    msg = render_to_string('mainapp/template_mail.html', {'context': data})
    send_mail('Обратная связь', msg, mail_iqw, [mail_client], html_message=msg)
