from django.urls import path,include
from . import views

app_name = 'users'


urlpatterns = [
    path('login/', views.login_req,name='login'),
    path('signup/',views.signup_req,name='signup'),
    path('logout/',views.logout_req,name='logout'),
    ]