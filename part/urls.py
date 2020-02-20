from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('controls/', views.controls, name='controls'),
    path('electrics/', views.electrics, name='electrics'),
    path('art/', views.art, name='art'),
    path('dedicated/', views.dedicated, name='dedicated'),
]