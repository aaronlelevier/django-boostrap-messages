from django.conf.urls import include, url
from django.contrib import admin

from bootstrap_message import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
]
