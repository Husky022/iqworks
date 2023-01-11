from django.db import models


# Create your models here.

class Client(models.Model):
    class Meta:
        ordering = ['-id']

    name = models.CharField(verbose_name='Имя клиента', max_length=168)
    mail = models.CharField(verbose_name='Почта клиента', max_length=168)
    phone = models.CharField(verbose_name='Телефон клиента', max_length=168)

    def __str__(self):
        return self.name
