from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
    'december': None
}

# Create your views here.

# index() creates the front page view where we can select a month
def index(request):
    months = list(monthly_challenges.keys())
    
    return render(request, 'challenges/index.html', {
        'months': months
    })

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
        return render(request, 'challenges/challenge.html',{
            'text': challenge_text,
            'month': month
        })
    except:
        return HttpResponseNotFound('<h1>You entered an invalid month</h1>')