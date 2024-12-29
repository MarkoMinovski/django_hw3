from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def home_page_content(request):
    return render(request, 'MSE_Analyzer/home_page_content.html')


def about_us(request):
    return render(request, 'MSE_Analyzer/about-us.html')


def contact(request):
    return render(request, 'MSE_Analyzer/contact.html')


def services(request):
    return render(request, 'MSE_Analyzer/services_intro.html')
