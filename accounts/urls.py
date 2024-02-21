from django.urls import path
from accounts import views

urlpatterns = [
    path('registration',views.registration,name='register'),
    path('Login',views.userlogin,name='Login'),
   

]