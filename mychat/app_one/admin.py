from django.contrib import admin
from app_one.models import UserInfo,Comment,Post,Message
# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Comment)
admin.site.register(Post)
# admin.site.register(ChatRoom)
admin.site.register(Message)
