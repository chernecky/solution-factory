from django.contrib import admin
from django.urls import path, include
from poll.views import *

from solfactRest.poll.views import PollCreateView

app_name = 'poll'
urlpatterns = [
    path('poll/create/', PollCreateView.as_view())
]
