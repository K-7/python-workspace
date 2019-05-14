from django.conf.urls import patterns, url
from app import views


urlpatterns = patterns('',
    
    url(r'^register/$',views.register,name="save_user"),
    url(r'^login/$',views.login,name="login"),
    url(r'^search/$',views.search,name="search"),
    url(r'^change_pass/$',views.change_password,name="change_password"),
    
)
