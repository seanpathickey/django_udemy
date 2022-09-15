from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #use name to reference in other places
    #creates a dynamic url: (type:variable, file.function, name)
    path('<int:month>', views.monthly_challenge_by_number), 
    path('<str:month>', views.monthly_challenge, name='month-challenge') 
]