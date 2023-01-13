from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import View
from mainapp.forms import AppForm

appform = AppForm()


options = {
    'chk-light': 0.3,
    'chk-shutters': 0.15,
    'chk-ventilation': 0.1,
    'chk-condition': 0.1,
    'chk-warm-floors': 0.1,
    'chk-security': 0.25,
    'chk-outdoor-management': 0.03,
    'chk-voice-helpers': 0.02,
    'chk-flat': 1.0,
    'chk-house': 1.2,
    'chk-office': 0.8,
}


class Calculator(View):
    template_name = 'calcapp/calculate.html'

    def get(self, request):
        context = {
            'title': 'Стоимость',
            'appform': appform

        }
        return render(request, self.template_name, context)

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def get_calculation(request):
    if is_ajax(request=request):
        if not request.POST.dict()['square'] and not request.POST.dict()['checked_type']:
            return JsonResponse({'result': render_to_string('calcapp/calculate_errors.html', {'Error_text': 'Укажите площадь и тип объекта'},
                                                            request=request)})

        if not request.POST.dict()['square']:
            return JsonResponse({'result': render_to_string('calcapp/calculate_errors.html', {'Error_text': 'Укажите площадь объекта'},
                                                            request=request)})

        if not request.POST.dict()['checked_type']:
            return JsonResponse({'result': render_to_string('calcapp/calculate_errors.html', {'Error_text': 'Укажите тип объекта'},
                                                            request=request)})

        if not request.POST.dict()['checked_base']:
            return JsonResponse({'result': render_to_string('calcapp/calculate_errors.html', {'Error_text': 'Укажите хотя бы один базовый фукционал (освещение, шторы, вентиляция, кондиционирование, теплые полы, безопасность)'},
                                                            request=request)})

        project_price_base = 400
        equipment_price_base = 3000
        montage_price_base = 2500

        if request.POST.dict()['checked_base']:
            for item in request.POST.dict()['checked_base'].split('&'):
                item_parse = item.split('=')
                project_price_base += options[item_parse[1]] * 400
                equipment_price_base += options[item_parse[1]] * 5000
                montage_price_base += options[item_parse[1]] * 3500

        if request.POST.dict()['checked_secondary']:
            for item in request.POST.dict()['checked_secondary'].split('&'):
                item_parse = item.split('=')
                equipment_price_base += options[item_parse[1]] * 5000

        if request.POST.dict()['checked_type']:
            for item in request.POST.dict()['checked_type'].split('&'):
                item_parse = item.split('=')
                project_price_base *= options[item_parse[1]]
                equipment_price_base *= options[item_parse[1]]
                montage_price_base *= options[item_parse[1]]

        project_price = project_price_base * int(request.POST.dict()['square'])
        equipment_price = equipment_price_base * int(request.POST.dict()['square'])
        montage_price = montage_price_base * int(request.POST.dict()['square'])
        programming_price = equipment_price * 0.2

        result_price = project_price + equipment_price + montage_price + programming_price
        context = {
            'project_price': round(project_price),
            'equipment_price': round(equipment_price),
            'montage_price': round(montage_price),
            'programming_price': round(programming_price),
            'result_price': round(result_price)
        }

        return JsonResponse({'result': render_to_string('calcapp/calculate_result.html', context, request=request),
                             'flag': 'ok'})
    return HttpResponseRedirect(reverse('mainapp:main'))


def reset_calculation(request):
    if is_ajax(request=request):
        return JsonResponse({'result': '200'})
    return HttpResponseRedirect(reverse('mainapp:main'))

