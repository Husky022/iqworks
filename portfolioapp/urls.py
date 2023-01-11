from django.urls import path


from .views import Objects, ObjectPage

app_name = 'portfolioapp'

urlpatterns = [
    path('objects/', Objects.as_view(), name='objects'),
    path('objectpage/<int:pk>/', ObjectPage.as_view(), name='object_page'),
]
