from django.conf.urls import url
from main import views

urlpatterns = [
    url(r'^$', views.mainpage, name='mainpage'),
    url(r'login/', views.login_user, name='login_user'),
    url(r'logout/', views.logout_user, name='logout_user'),
    url(r'userpage/', views.userpage, name='userpage'),
    url(r'addtrip/', views.addtrip, name='addtrip'),
     url(r'editprofile/(.*)', views.editprofile, name='editprofile'),

]