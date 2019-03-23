from django.conf.urls import url
from apps.repository import views


urlpatterns = [
    url(r'index/$', views.index),
    url(r'index/(\d{1})/$', views.list_repository),
    url(r'find/$', views.sarch_repo),
]

