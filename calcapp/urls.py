from django.urls import path

from .views import Calculator, get_calculation, reset_calculation

app_name = 'calcapp'

urlpatterns = [
    path('calculate/', Calculator.as_view(), name='calculate'),
    path('get_calculation/', get_calculation, name='get_calculation'),
    path('reset_calculation/', reset_calculation, name='reset_calculation'),
]
