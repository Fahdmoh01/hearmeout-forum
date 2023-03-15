from django.urls import path
from forum import views

app_name = 'forum'

urlpatterns=[
    path('', views.IndexView.as_view(), name='index'),
]