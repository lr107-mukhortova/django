from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render


def main_view(request):
    return render(request, 'tours/index.html')


def departure_view(request, departure):
    context = {"departure": departure}
    return render(request, 'tours/departure.html', context=context)


def tour_view(request, id):
    context = {"tour_id": id}
    return render(request, 'tours/tour.html', context=context)


# обработка ошибок
def custom_handler404(request, exception):
    return HttpResponseNotFound('Ресурс не найдет!')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')
