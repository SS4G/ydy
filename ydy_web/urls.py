from django.conf.urls import url
from . import views
app_name = 'ydy_web'
urlpatterns = [
url(r'^start/$'  , views.start  , name='start_page'),  #起始页面
url(r'^sign_up/$', views.sign_up, name='sign_up_page'),#注册页面
url(r'^sign_in/$', views.sign_in, name='sign_in_page'),#登录页面
#url(r'^$', views.index, name='index'),
#url(r'^$', views.index, name='index'),
#url(r'^$', views.index, name='index'),
]