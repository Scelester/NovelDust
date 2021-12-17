from django.urls import path
from . import views


app_name = 'dustmain'

urlpatterns = [
    path('',views.index,name='index'),
    path('GG/<str:tbnameurl>/',views.topbookpage,name='topbookpage')
]