from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    'january':'month 1',
    'february':'month 2',
    'march':'month 3',
    'april':'month 4',
    'may':'month 5',
    'june':'month 6',
    'july':'month 7',
    'august':'month 8',
    'september':'month 9',
    'october':'month 10',
    'november':'month 11',
    'december':'month 12'
}

# Create your views here.

def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())
    
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse('month-challenge', args=[month])
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'
    
    response_text = f'<ul>{list_items}</ul>'
    
    return HttpResponse(response_text)

def monthly_challenge_by_number(request, month):
    months_list = list(monthly_challenges.keys())
    
    if month > len(months_list):
        return HttpResponseNotFound('<h1>You entered an invalid month</h1>')
    
    redirect_month = months_list[month-1]
    #dynamically creates path according to month-challenge in urls.py
    redirect_path = reverse('month-challenge', args=[redirect_month]) 
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_text = f'<h1>{challenge_text}</h1>'
        return HttpResponse(response_text)
    except:
        return HttpResponseNotFound('<h1>You entered an invalid month</h1>')