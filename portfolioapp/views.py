from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from portfolioapp.models import PortfolioObject, PortfolioImage
from mainapp.forms import AppForm

appform = AppForm()


class Objects(ListView):
    """ CBV Страницы с портфолио """
    model = PortfolioObject
    template_name = 'portfolioapp/objects.html'
    context_object_name = 'portfolio'
    extra_context = {
        'title': 'Портфолио',
        'appform': appform
    }


class ObjectPage(DetailView):
    """ CBV Страницы объекта """
    model = PortfolioObject
    template_name = 'portfolioapp/objectpage.html'
    extra_context = {
        'title': 'Объект',
        'appform': appform
    }

    def get(self, request, pk):
        object = PortfolioObject.objects.filter(id=pk).first()
        context = {
            'title': 'Объект',
            'object': object,
            'photos': PortfolioImage.objects.filter(object=object),
            'appform': appform
        }
        return render(request, self.template_name, context)
