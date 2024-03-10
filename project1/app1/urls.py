from django.urls import path
from .views import RemindView



urlpatterns=[
    path('remindview/',RemindView)
]