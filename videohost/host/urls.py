from django.conf.urls import include, url
from django.views.generic.base import TemplateView
from host import views


urlpatterns = [
    url(r'^$', views.mainpage, name='mainpage'),
    url(r'video/(?P<videoid>[0-9]+)/$', views.video, name='video'),
    url(r'video/embed/(?P<videoid>[0-9]+)/$', views.embed, name='embed'),
    url(r'login/', views.login_user, name='login_user'),
    url(r'logout/', views.logout_user, name='logout_user'),
    url(r'userpage/', views.userpage, name='userpage'),
    url(r'update/', views.update, name='update'),
    url(r'dmca/', views.dmca, name='dmca'),
    url(r'tos/', views.tos, name='tos'),
    url(r'faq/', views.faq, name='faq'),

]