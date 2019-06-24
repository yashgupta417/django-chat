from rest_framework import serializers
from app_one.models import Post,UserInfo
from django.contrib.auth import get_user_model

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['image','title','message','posted_by','likes']
        read_only_fields=['pk',]
# class UserInfoDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=UserInfo
#         fields='__all__'
#
# class PostDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Post
#         fields='__all__'
#         read_only_fields=['pk',]
#hello
class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserInfo
        fields=['user','id','following','followers','post_liked']
        read_only_fields=['pk',]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields='__all__'
