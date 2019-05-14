from django.conf.urls import url
from core import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^login$', views.login, name="login"),
    url(r'^register$', views.register, name="register"),
    url(r'^logout$', views.logout, name="logout"),
]