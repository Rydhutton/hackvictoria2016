from django.conf.urls import url
from main import views

urlpatterns = [
    url(r'^$', views.mainpage, name='mainpage'),
    url(r'login/', views.login_user, name='login_user'),

]