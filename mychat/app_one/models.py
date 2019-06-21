
from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
# Create your views here.

from django.contrib import auth
from django.urls import reverse

class UserInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    # friend=models.ManyToManyField(User,related_name='friends',blank=True)
    following=models.ManyToManyField('UserInfo',related_name='followers',blank=True)
    # likes=models.ManyToManyField('Post',related_name='liked_by',blank=True)
    def __str__(self):
        return "@"+self.user.username

    # def get_absolute_url(self):
    #
    #     return reverse('app_one:profile',kwargs={'pk':self.user.id})

# class FriendShip(models.Model):
#     person1=models.ForeignKey(UserInfo,related_name='friendships1',on_delete=models.CASCADE)
#     person2=models.ForeignKey(UserInfo,related_name='friendships2',on_delete=models.CASCADE)
#     date=models.DateTimeField(default=timezone.now)

class Post(models.Model):
    posted_by=models.ForeignKey(UserInfo,related_name='posts',on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=255)
    message=models.TextField()
    likes=models.ManyToManyField(UserInfo,related_name='post_liked',blank=True)
    date_of_posting=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    message=models.TextField()
    commented_by=models.ForeignKey(UserInfo,related_name='user_comments',on_delete=models.CASCADE)
    date_of_commenting=models.DateTimeField(default=timezone.now)
    # Likes=models.IntegerField()

    def __str__(self):
        return self.message

# class ChatRoom(models.Model):
#     chat_room_name=models.CharField(max_length=256,blank=True)
#     persons=models.ManyToManyField(UserInfo,related_name='chat_rooms',blank=True)
# class Message(models.Model):
#     chatRoom=models.ForeignKey(ChatRoom,related_name='messages',on_delete=models.CASCADE)
#     message=models.TextField()
#     sender=models.ForeignKey(UserInfo,related_name='messages_as_sender',on_delete=models.CASCADE)
#     recipient=models.ForeignKey(UserInfo,related_name='messages_as_recipient',on_delete=models.CASCADE)
#     date_of_messaging=models.DateTimeField(timezone.now)
