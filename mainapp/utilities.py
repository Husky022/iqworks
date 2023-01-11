from .models import Client
from django.core.mail import send_mail
from django.template.loader import render_to_string
from iqworks.secrets_local import mail_user


class ClientHandler:
	def __init__(self, request):
		self.name = request.POST.get('name')
		self.mail = request.POST.get('mail')
		self.phone = request.POST.get('phone')
		self.add_to_db()
		self.send_mail()

	def add_to_db(self):
		new_client = Client.objects.create(name=self.name, mail=self.mail, phone=self.phone)
		new_client.save()

	def send_mail(self):
		client = f'Имя: ' + self.name + 'Почта: ' + self.mail + 'Телефон: ' + self.phone
		send_mail('Новая заявка', client, mail_user, [mail_user])
		data = {'name': self.name, 'mail': self.mail, 'phone': self.phone}
		msg = render_to_string('mainapp/template_mail.html', {'context': data})
		send_mail('Обратная связь', msg, mail_user, [self.mail], html_message=msg)
