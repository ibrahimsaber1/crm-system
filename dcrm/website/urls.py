from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout_user'),
    path('regester/', views.regester, name='regester'),
    path('record/<int:id>/', views.home, name='record'),

]
