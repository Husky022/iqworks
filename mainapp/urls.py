from django.urls import path
import mainapp.views as mainapp

from .views import Main, Contacts, Command, Services, Privacy

app_name = 'mainapp'

urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('contacts/', Contacts.as_view(), name='contacts'),
    path('command/', Command.as_view(), name='command'),
    path('services/', Services.as_view(), name='services'),
    path('privacy/', Privacy.as_view(), name='privacy')
]
