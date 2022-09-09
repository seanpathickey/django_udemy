from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    #creates a dynamic url: (type:variable, file.function, name)
    path('<int:month>', views.monthly_challenge_by_number), 
    path('<str:month>', views.monthly_challenge, name='month-challenge') 
]