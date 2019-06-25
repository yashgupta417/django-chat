from rest_framework import generics
from api.serializers import PostSerializer,UserInfoSerializer,UserSerializer
from app_one.models import Post,UserInfo
from django.contrib.auth import get_user_model
class PostListApiView(generics.ListCreateAPIView):
    # queryset=Post.objects.all()
    serializer_class=PostSerializer

    def get_queryset(self):
        return Post.objects.all()
    # def perform_create(self, serializer):
    #     serializer.save(data=self.request.data) this shit was causing errors


class UserInfoListApiView(generics.ListCreateAPIView):
    serializer_class=UserInfoSerializer

    def get_queryset(self):
        return UserInfo.objects.all()

class UserInfoDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    # queryset=UserInfo.objects.all()
    # lookup_field='pk'
    serializer_class=UserInfoSerializer
    def get_queryset(self):
        print(self.request.query_params.get('name'))#query params
        return UserInfo.objects.all()

    def get_object(self):
        pk=self.kwargs.get('pk')
        return UserInfo.objects.get(pk=pk)

class PostDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=PostSerializer
    # lookup_field='pk'
    # queryset=UserInfo.objects.all()
    def get_queryset(self):
        return Post.objects.all()

    def get_object(self):
        pk=self.kwargs.get('pk')
        return Post.objects.get(pk=pk)

class UserListApiView(generics.ListCreateAPIView):
    serializer_class=UserSerializer

    def get_queryset(self):
        return get_user_model().objects.all()

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=UserSerializer

    def get_queryset(self):
        return get_user_model().objects.all()

    def get_object(self):
        pk=self.kwargs.get('pk')
        return get_user_model().objects.get(pk=pk)
