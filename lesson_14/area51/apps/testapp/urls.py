from django.conf.urls import url
from apps.testapp.views import hello
from apps.testapp.views import root
from apps.testapp.views import current_time, time_ahead, devs, create_dev, devs_template


urlpatterns = [
    url(r'^$', root),
    url(r'^hello/$', hello),
    url(r'^time/$', current_time),
    url(r'^time/(\d{1,2})/$', time_ahead),
    url(r'^devs/$', devs),
    url(r'^create-dev/([a-zA-Z]+)/$', create_dev),
    url(r'^devs-template/$', devs_template),
]

