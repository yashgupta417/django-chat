from django.conf.urls import url
from app_one import views

app_name='app_one'
urlpatterns=[
    # url(r'^create_post/$',views.CreatePost.as_view(),name="post_create"),
    url(r'^home/$',views.HomeView.as_view(),name="home"),
    url(r'^logout/$',views.user_logout,name="logout"),
    url(r'^login/$',views.user_login,name="login"),
    url(r'^signup/$',views.SignUpView.as_view(),name="signup"),
    url(r'^$',views.IndexView.as_view(),name="index"),
    url(r'^profile/(?P<pk>\d+)/$',views.ProfileDetailView.as_view(),name="profile"),
    url(r'^follow/(?P<user_i_want_to_follow_id>\d+)/$',views.follow_view,name="follow"),
    url(r'^add_comment/(?P<pk>\d+)/(?P<from>\w+)/$',views.comment_view,name="comment"),
    url(r'^like/(?P<pk>\d+)/(?P<from>\w+)/$',views.like_view,name="like"),
    # url(r'^chat_board/$',views.ChatBoardView.as_view(),name="chat_board")
]
