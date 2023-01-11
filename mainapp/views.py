from django.shortcuts import render
from django.views.generic import View
from .forms import AppForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .utilities import ClientHandler


appform = AppForm()

class Main(View):
    """ CBV Главной страницы """
    template_name = 'mainapp/index.html'

    def get(self, request):
        context = {
            'title': 'Главная',
            'appform': appform
        }
        return render(request, self.template_name, context)

    def post(self, request):
        new_client = ClientHandler(request)
        return HttpResponseRedirect(reverse('mainapp:main'))


class Services(View):
    """ CBV Главной страницы """
    template_name = 'mainapp/services.html'

    def get(self, request):
        context = {
            'title': 'Услуги',
            'appform': appform
        }
        return render(request, self.template_name, context)


class Contacts(View):
    """ CBV Главной страницы """
    template_name = 'mainapp/contacts.html'

    def get(self, request):
        context = {
            'title': 'Контакты',
            'appform': appform
        }
        return render(request, self.template_name, context)


class Command(View):
    """ CBV Главной страницы """
    template_name = 'mainapp/command.html'

    def get(self, request):
        context = {
            'title': 'Команда'
        }
        return render(request, self.template_name, context)


class Privacy(View):
    """ CBV страницы политики конфиденциальности """
    template_name = 'mainapp/privacy.html'

    def get(self, request):
        context = {
            'title': 'Приватность',
            'appform': appform
        }
        return render(request, self.template_name, context)
