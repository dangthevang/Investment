from django.shortcuts import render
from .models import income_balance
from .forms import CODE_companyForm
from django.http import HttpResponseRedirect
import json
import requests
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
def createUrl(s, key):
    global url_information, url_income, url_balance,url_history
    url_information = 'https://financialmodelingprep.com/api/v3/profile/'+s+'?apikey='+key
    url_income = "https://financialmodelingprep.com/api/v3/income-statement/" + s + "?apikey=" + key
    url_balance = "https://financialmodelingprep.com/api/v3/balance-sheet-statement/" + s + "?apikey=" + key
    url_history = 'https://financialmodelingprep.com/api/v3/historical-chart/1min/'+s+'?apikey='+key

def get_jsonparsed_data(url):
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)
def Main(request):
    form = CODE_companyForm(request.GET)
    Data_Main = {'form':form}
    return render(request, 'main.html',Data_Main)

def Profile_company(request):
    global company, form
    form = CODE_companyForm(request.GET)
    if form['CODE'].value() != None:
        company = form['CODE'].value()
    createUrl(company, 'a0f0ba371748881cc097f74c860278f5')
    Data_Profile = {'infor': get_jsonparsed_data(url_information),
                    'company': company,
                    'form':form
                    }
    return render(request, 'profile.html', Data_Profile)


def Income_balance(request):
    global company, form
    form = CODE_companyForm(request.GET)
    if form['CODE'].value() != None:
        company = form['CODE'].value()
    createUrl(company, 'a0f0ba371748881cc097f74c860278f5')
    Data_IB = { 'Income': get_jsonparsed_data(url_income),
            'Balance': get_jsonparsed_data(url_balance),
            'company': company,'form':form}
    return render(request, 'IB.html', Data_IB)

def History(request):
    global company, form
    form = CODE_companyForm(request.GET)
    if form['CODE'].value() != None:
        company = form['CODE'].value()
    createUrl(company, 'a0f0ba371748881cc097f74c860278f5')
    Data_history = {'history': get_jsonparsed_data(url_history),
                    'company': company,'form':form}
    return render(request, 'history.html', Data_history)
