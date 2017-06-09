from django.conf.urls import url
from django.views.generic import RedirectView
from account import views

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/account/login/')),
    url(r'^login/', views.account_login, name='login'),
    url(r'^logout/', views.account_logout, name='logout'),
    url(r'^register/', views.account_register, name='register'),
]
