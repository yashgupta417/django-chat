from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^post_list/$',views.PostListApiView.as_view(),name="post_list_api"),
    url(r'^userinfo_detail/(?P<pk>\w+)/$',views.UserInfoDetailApiView.as_view(),name="userinfo_detail_api"),
    url(r'post_detail/(?P<pk>\w+)/$',views.PostDetailApiView.as_view(),name="post_detail_api"),
    url(r'userinfo_list/$',views.UserInfoListApiView.as_view(),name="userinfo_list_api"),
    url(r'user_list/$',views.UserListApiView.as_view(),name="user_list_api")
]
