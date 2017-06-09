from django.conf.urls import url

from task import views

urlpatterns = [
    url(r'^$', views.show_all_tasks, name='show_all_tasks'),
    url(r'^add/$', views.add, name='add'),
    url(r'^mark-done/(?P<task_id>[\w+:-]+)/$', views.mark_done, name='mark_done'),
    url(r'^edit/(?P<task_id>[\w+:-]+)/$', views.edit, name='edit'),
    url(r'^delete/(?P<task_id>[\w+:-]+)/$', views.delete, name='delete'),
]
