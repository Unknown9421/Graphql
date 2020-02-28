from django.urls import path
from . import views


app_name = 'website'

urlpatterns = [
    path('', views.home, name='home'),
    path('api/<str:model_name>/', views.view_api, name='api')
]
