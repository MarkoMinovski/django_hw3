import datetime
from datetime import timedelta

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import requests as req_lib


def home_page_content(request):
    return render(request, 'MSE_Analyzer/home_page_content.html')


def about_us(request):
    return render(request, 'MSE_Analyzer/about-us.html')


def contact(request):
    return render(request, 'MSE_Analyzer/contact.html')


def services(request):
    return render(request, 'MSE_Analyzer/services_intro.html')


@csrf_exempt
def analysed(request):
    if request.method == "POST":
        selected_ticker = request.POST.get('ticker')
        selected_interval = request.POST.get('interval')
        interval_start = datetime.MINYEAR

        latest_available_date_resp = req_lib.get('http://127.0.0.1:5000/tickers/latest/str')

        lds_json = latest_available_date_resp.json()

        lds_str = lds_json.strip()

        # Return format: MM/DD/YYYY
        lds_parts = lds_str.split('/')

        lds_datetime = datetime.datetime(int(lds_parts[2]), int(lds_parts[0]), int(lds_parts[1]))

        if selected_interval == 'last-week':
            interval_start = lds_datetime - timedelta(days=7)
        elif selected_interval == 'last-month':
            interval_start = lds_datetime - timedelta(days=30)
        else:
            interval_start = lds_datetime - timedelta(days=364)

        template = loader.get_template('MSE_Analyzer/services_graph.html')

        context = {
            'interval_start': interval_start.strftime("%m/%d/%Y"),
            'interval_end': lds_datetime.strftime("%m/%d/%Y"),
            'ticker_code': selected_ticker,
        }

        return HttpResponse(template.render(context, request))
