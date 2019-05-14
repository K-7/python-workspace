from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
import views


urlpatterns = patterns('',
    url(r'^$',views.home , name="home"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^app/',include("app.urls")),
    url(r'^webapp/',views.webapp,name="webapp"),
)
