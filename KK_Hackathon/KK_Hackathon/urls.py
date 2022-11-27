"""KK_Hackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('start', views.start, name='start'),
    # path('home_submit', views.home_submit, name='home_submit'),
    path('quest', views.quest, name='quest'),
    path('results', views.results, name='results'),
    path('end', views.end, name='end'),
    path('answer', views.answer, name='answer'),
    path('highscore', views.high_score, name='highscore'),
    # path('quest_submit', views.quest_submit, name='quest_submit'),
]
