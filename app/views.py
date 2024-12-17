from django.shortcuts import render


def index_page(request):
    return render(request, 'index.html')


def stats_page(request):
    return render(request, 'stats.html')


def relevance_page(request):
    return render(request, 'relevance.html')


def geography_page(request):
    return render(request, 'geography.html')


def skills_page(request):
    return render(request, 'skills.html')


def last_vacancies_page(request):
    return render(request, 'last_vacancies.html')


def index_page(request):
    return render(request, 'index.html')
