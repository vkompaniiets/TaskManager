from django.conf.urls import url
from account import views

urlpatterns = [
    url(r'^login/', views.account_login, name='login'),
    url(r'^logout/', views.account_logout, name='logout'),
    url(r'^register/', views.account_register, name='register'),
]
