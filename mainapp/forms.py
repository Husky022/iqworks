from django import forms


class AppForm(forms.Form):
    name = forms.CharField(label='Имя')
    mail = forms.EmailField(label='Почта')
    phone = forms.IntegerField(label='Телефон')
