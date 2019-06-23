from django.contrib import admin
from rest_framework.authtoken.models import Token
from app_one.models import UserInfo,Comment,Post
# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Comment)
admin.site.register(Post)
# admin.site.register(ChatRoom)
# admin.site.register(Message)
# admin.site.register(Token)
