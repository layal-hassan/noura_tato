from django.urls import include, path
from . import views

app_name='nour'
urlpatterns = [


    path('',views.services_list ,name='service'),
    path('derail/<int:id>/', views.service_detail, name='service_detail'),


]
