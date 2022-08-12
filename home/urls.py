from django.urls import path
from . import views


app_name = 'home'

urlpatterns = [
    path('' , views.home , name='home') , 
    path('single1/', views.single1, name='single1'),
    path('single2/', views.single2, name='single2'),
    path('single3/', views.single3, name='single3'),
    path('single4/', views.single4, name='single4'),
    path('single5/', views.single5, name='single5'),
    path('single6/', views.single6, name='single6'),
    path('single7/', views.single7, name='single7'),
    
    path('single8/', views.single8, name='single8'),
    path('single9/', views.single9, name='single9'),
    path('single10/', views.single10, name='single10'),
    path('single11/', views.single11, name='single11'),
    path('single12/', views.single12, name='single12'),
    path('single13/', views.single13, name='single13'),
    path('single14/', views.single14, name='single14'),
    path('single15/', views.single15, name='single15'), 
    path('single16/', views.single16, name='single16'),
    path('single17/', views.single17, name='single17'),  
           
]
