from django.urls import path
from . import views

app_name = 'election'

urlpatterns = [
    path('', views.index, name='home'),
    path('pu_results', views.get_pu_results, name='pu_results'),
    path('lga_results', views.get_total_results, name='lga_results')
]