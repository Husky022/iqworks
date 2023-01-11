from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, HttpResponse
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

    def post(self, request):
        print(request.POST)


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def get_calculation(request):
    if is_ajax(request=request):

        if not request.POST.dict()['square'] and not request.POST.dict()['checked_type']:
            page = '<div class="result-container">' \
                       '<div class="result-warning-icon">' \
                       '<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="red" class="bi bi-patch-exclamation" viewBox="0 0 16 16">' \
                       '<path d="M7.001 11a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 4.995a.905.905 0 1 1 1.8 0l-.35 3.507a.553.553 0 0 1-1.1 0L7.1 4.995z"/>' \
                       '<path d="m10.273 2.513-.921-.944.715-.698.622.637.89-.011a2.89 2.89 0 0 1 2.924 2.924l-.01.89.636.622a2.89 2.89 0 0 1 0 4.134l-.637.622.011.89a2.89 2.89 0 0 1-2.924 2.924l-.89-.01-.622.636a2.89 2.89 0 0 1-4.134 0l-.622-.637-.89.011a2.89 2.89 0 0 1-2.924-2.924l.01-.89-.636-.622a2.89 2.89 0 0 1 0-4.134l.637-.622-.011-.89a2.89 2.89 0 0 1 2.924-2.924l.89.01.622-.636a2.89 2.89 0 0 1 4.134 0l-.715.698a1.89 1.89 0 0 0-2.704 0l-.92.944-1.32-.016a1.89 1.89 0 0 0-1.911 1.912l.016 1.318-.944.921a1.89 1.89 0 0 0 0 2.704l.944.92-.016 1.32a1.89 1.89 0 0 0 1.912 1.911l1.318-.016.921.944a1.89 1.89 0 0 0 2.704 0l.92-.944 1.32.016a1.89 1.89 0 0 0 1.911-1.912l-.016-1.318.944-.921a1.89 1.89 0 0 0 0-2.704l-.944-.92.016-1.32a1.89 1.89 0 0 0-1.912-1.911l-1.318.016z"/>' \
                       '</svg>' \
                       '</div>' \
                       '<div class="result-warning-message">Укажите площадь и тип объекта' \
                       '</div>' \
                   '</div>'
            return JsonResponse({'result': page})

        if not request.POST.dict()['square']:
            page = '<div class="result-container">' \
                       '<div class="result-warning-icon">' \
                           '<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="red" class="bi bi-patch-exclamation" viewBox="0 0 16 16">' \
                               '<path d="M7.001 11a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 4.995a.905.905 0 1 1 1.8 0l-.35 3.507a.553.553 0 0 1-1.1 0L7.1 4.995z"/>' \
                               '<path d="m10.273 2.513-.921-.944.715-.698.622.637.89-.011a2.89 2.89 0 0 1 2.924 2.924l-.01.89.636.622a2.89 2.89 0 0 1 0 4.134l-.637.622.011.89a2.89 2.89 0 0 1-2.924 2.924l-.89-.01-.622.636a2.89 2.89 0 0 1-4.134 0l-.622-.637-.89.011a2.89 2.89 0 0 1-2.924-2.924l.01-.89-.636-.622a2.89 2.89 0 0 1 0-4.134l.637-.622-.011-.89a2.89 2.89 0 0 1 2.924-2.924l.89.01.622-.636a2.89 2.89 0 0 1 4.134 0l-.715.698a1.89 1.89 0 0 0-2.704 0l-.92.944-1.32-.016a1.89 1.89 0 0 0-1.911 1.912l.016 1.318-.944.921a1.89 1.89 0 0 0 0 2.704l.944.92-.016 1.32a1.89 1.89 0 0 0 1.912 1.911l1.318-.016.921.944a1.89 1.89 0 0 0 2.704 0l.92-.944 1.32.016a1.89 1.89 0 0 0 1.911-1.912l-.016-1.318.944-.921a1.89 1.89 0 0 0 0-2.704l-.944-.92.016-1.32a1.89 1.89 0 0 0-1.912-1.911l-1.318.016z"/>' \
                           '</svg>' \
                       '</div>' \
                       '<div class="result-warning-message"> Укажите площадь объекта'\
                       '</div>' \
                   '</div>'
            return JsonResponse({'result': page})

        if not request.POST.dict()['checked_type']:
            page = '<div class="result-container">' \
                       '<div class="result-warning-icon">' \
                       '<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="red" class="bi bi-patch-exclamation" viewBox="0 0 16 16">' \
                       '<path d="M7.001 11a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 4.995a.905.905 0 1 1 1.8 0l-.35 3.507a.553.553 0 0 1-1.1 0L7.1 4.995z"/>' \
                       '<path d="m10.273 2.513-.921-.944.715-.698.622.637.89-.011a2.89 2.89 0 0 1 2.924 2.924l-.01.89.636.622a2.89 2.89 0 0 1 0 4.134l-.637.622.011.89a2.89 2.89 0 0 1-2.924 2.924l-.89-.01-.622.636a2.89 2.89 0 0 1-4.134 0l-.622-.637-.89.011a2.89 2.89 0 0 1-2.924-2.924l.01-.89-.636-.622a2.89 2.89 0 0 1 0-4.134l.637-.622-.011-.89a2.89 2.89 0 0 1 2.924-2.924l.89.01.622-.636a2.89 2.89 0 0 1 4.134 0l-.715.698a1.89 1.89 0 0 0-2.704 0l-.92.944-1.32-.016a1.89 1.89 0 0 0-1.911 1.912l.016 1.318-.944.921a1.89 1.89 0 0 0 0 2.704l.944.92-.016 1.32a1.89 1.89 0 0 0 1.912 1.911l1.318-.016.921.944a1.89 1.89 0 0 0 2.704 0l.92-.944 1.32.016a1.89 1.89 0 0 0 1.911-1.912l-.016-1.318.944-.921a1.89 1.89 0 0 0 0-2.704l-.944-.92.016-1.32a1.89 1.89 0 0 0-1.912-1.911l-1.318.016z"/>' \
                       '</svg>' \
                       '</div>' \
                       '<div class="result-warning-message"> Укажите тип объекта' \
                       '</div>' \
                   '</div>'

            return JsonResponse({'result': page})

        if not request.POST.dict()['checked_base']:
            page = '<div class="result-container">' \
                       '<div class="result-warning-icon">' \
                           '<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="red" class="bi bi-patch-exclamation" viewBox="0 0 16 16">'\
                              '<path d="M7.001 11a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 4.995a.905.905 0 1 1 1.8 0l-.35 3.507a.553.553 0 0 1-1.1 0L7.1 4.995z"/>'\
                              '<path d="m10.273 2.513-.921-.944.715-.698.622.637.89-.011a2.89 2.89 0 0 1 2.924 2.924l-.01.89.636.622a2.89 2.89 0 0 1 0 4.134l-.637.622.011.89a2.89 2.89 0 0 1-2.924 2.924l-.89-.01-.622.636a2.89 2.89 0 0 1-4.134 0l-.622-.637-.89.011a2.89 2.89 0 0 1-2.924-2.924l.01-.89-.636-.622a2.89 2.89 0 0 1 0-4.134l.637-.622-.011-.89a2.89 2.89 0 0 1 2.924-2.924l.89.01.622-.636a2.89 2.89 0 0 1 4.134 0l-.715.698a1.89 1.89 0 0 0-2.704 0l-.92.944-1.32-.016a1.89 1.89 0 0 0-1.911 1.912l.016 1.318-.944.921a1.89 1.89 0 0 0 0 2.704l.944.92-.016 1.32a1.89 1.89 0 0 0 1.912 1.911l1.318-.016.921.944a1.89 1.89 0 0 0 2.704 0l.92-.944 1.32.016a1.89 1.89 0 0 0 1.911-1.912l-.016-1.318.944-.921a1.89 1.89 0 0 0 0-2.704l-.944-.92.016-1.32a1.89 1.89 0 0 0-1.912-1.911l-1.318.016z"/>'\
                           '</svg>' \
                       '</div>' \
                       '<div class="result-warning-message"> Укажите хотя бы один базовый фукционал (освещение, шторы, вентиляция, ' \
                       'кондиционирование, теплые полы, безопасность)' \
                       '</div>' \
                   '</div>'
            return JsonResponse({'result': page})

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

        page = '<div class="result-warning-message">' \
                   '<div class="result_prices_wrap">' \
                       '<div>' \
                           f'<p class="price_text">Проект: <span class="price_figure">{round(project_price) } руб</span>' \
                           f'<p class="price_text">Оборудование: <span class="price_figure">{round(equipment_price)} руб</span>' \
                       '</div>' \
                       '<div class="margin-left-25px">' \
                           f'<p class="price_text">Монтаж: <span class="price_figure">{round(montage_price)} руб</span>' \
                           f'<p class="price_text">Настройка: <span class="price_figure">{round(programming_price)} руб</span>'\
                       '</div>' \
                   '</div>' \
                   f'<p class="price_text">Общая стоимость: <span class="price_figure">{round(result_price)} руб</span>' \
               '</div>'

        return JsonResponse({'result': page, 'flag': 'ok'})
    return HttpResponseRedirect(reverse('mainapp:main'))


def reset_calculation(request):
    if is_ajax(request=request):
        return JsonResponse({'result': '200'})
    return HttpResponseRedirect(reverse('mainapp:main'))

