from django.conf.urls import url
from . import views
app_name = 'ydy_web'
urlpatterns = [
    url(r'^start/$'  ,                                  views.start  ,          name='start_page'               ),#起始页面
    url(r'^sign_up/$',                                  views.sign_up,          name='sign_up_page'             ),#注册页面
    url(r'^sign_in/$',                                  views.sign_in,          name='sign_in_page'             ),#登录页面
    url(r'^sign_in_result/$',                           views.sign_in_result,   name='sign_in_result_page'      ),#登录结果页面
    url(r'^sign_up_result/$',                           views.sign_up_result,   name='sign_up_result_page'      ),#注册结果页面
    url(r'^Equipment/list/$',                           views.Equipment_list,   name='Equipment_list_page'      ),#借场信息页面
    url(r'^Equipment/item/(?P<Equip_id>[0-9]+)/$',      views.Equipment_item,   name='Equipment_item_page'      ),#借场结果页面
    url(r'^Forum/Topic_list/$',                         views.Topic_list,       name='Forum_Topic_list_page'    ),#论坛主题列表页面
    url(r'^Forum/Topics/(?P<Topic_id>[0-9]+)/$',        views.Topics,           name='Forum_Topics_page'        ),#论坛主题页面
    url(r'^Forum/Topic_edit/$',                         views.Topic_edit,       name='Forum_Topic_edit_page'    ),#论坛主题编辑页面
    url(r'^Forum/Comment_edit/(?P<Topic_id>[0-9]+)$',   views.Comment_edit,     name='Forum_Comment_edit_page'  ),#论坛评论编辑页面
    #url(r'^$', views.index, name='index'),
    #url(r'^$', views.index, name='index'),
    #url(r'^$', views.index, name='index'),
]
