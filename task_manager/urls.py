from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/tasks/')),
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('account.urls')),
    url(r'^tasks/', include('task.urls')),
]
