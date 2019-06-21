#views
from django.views.generic import (TemplateView,CreateView,ListView,DetailView)
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from app_one.models import  Post,Comment,UserInfo
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from app_one.forms import UserForm,PostForm
from django.contrib.auth.models import User
from .models import UserInfo,Post,Comment

class HomeView(ListView):
    model=Post
    template_name='app_one/home.html'
    context_object_name='post_list'
    def get_queryset(self):
        userinfo=UserInfo.objects.get(user=self.request.user)
        my_query_set=Post.objects.filter(posted_by=userinfo).order_by('-date_of_posting')[:1]
        for people in userinfo.following.all() :
            sub_query=Post.objects.filter(posted_by=people).order_by('-date_of_posting')
            print(sub_query)
            my_query_set=my_query_set | sub_query
        return my_query_set
# class CreatePost(CreateView):
#     # form_class=PostForm
#     model=Post
#     template_name='app_one/post_create.html'

class IndexView(TemplateView):
    template_name='app_one/index.html'

class ProfileDetailView(DetailView):
    model=UserInfo
    template_name='app_one/profile.html'
    context_object_name='userinfo'
    def post(self,request,*args,**kwargs):
        username_to_be_find=request.POST.get('username_to_be_find',default="n")
        message=request.POST.get('message',default="m")
        title=request.POST.get('title')

        if username_to_be_find!="n":
            user_to_be_find=User.objects.get(username=username_to_be_find)
            userinfo_to_be_find=UserInfo.objects.get(user=user_to_be_find)
            return HttpResponseRedirect(reverse('app_one:profile',kwargs={'pk':user_to_be_find.id}))
        else:
            userinfo=UserInfo.objects.get(user=request.user)
            post=Post(message=message,title=title,posted_by=userinfo)
            post.save()
            return HttpResponseRedirect(reverse('app_one:profile',kwargs={'pk':request.user.id}))



class SignUpView(CreateView):
    model=User
    form_class=UserForm
    template_name='app_one/signup.html'
    def form_valid(self, form):
            user_form=form

            user=user_form.save()
            user.set_password(user.password)
            user.save()
            userInfo=UserInfo(user=user,id=user.id)
            userInfo.save()

            return HttpResponseRedirect(reverse('app_one:index'))

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user= authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('app_one:profile',kwargs={'pk':request.user.id}))
            else:
                return HttpResponse("Account Not Active")
        else:
            return HttpResponse("Invalid Details")
    else:
        return render(request,'app_one/login.html',{})
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('app_one:index'))

def comment_view(request,*args,**kwargs):
    message=request.POST.get('comment')
    userinfo=UserInfo.objects.get(user=request.user)
    post=Post.objects.get(id=kwargs['pk'])
    comment=Comment(message=message,commented_by=userinfo,post=post)
    comment.save()
    if kwargs['from']=='profile':
        return HttpResponseRedirect(reverse('app_one:profile',kwargs={'pk':post.posted_by.id}))
    else:
        return HttpResponseRedirect(reverse('app_one:home'))

def like_view(request,*args,**kwargs):
    post=Post.objects.get(id=kwargs['pk'])
    # profile_username=kwargs['profile_username']
    # profile_user=User.objects.get(username=profile_username)
    userinfo=UserInfo.objects.get(user=request.user)
    post.likes.add(userinfo)
    post.save()
    # return HttpResponse(profile_user)
    if kwargs['from']=='profile':
        return HttpResponseRedirect(reverse('app_one:profile',kwargs={'pk':post.posted_by.id}))
    else:
        return HttpResponseRedirect(reverse('app_one:home'))
def follow_view(request,*args,**kwargs):
    user_i_want_to_follow=UserInfo.objects.get(id=kwargs['user_i_want_to_follow_id'])
    me=UserInfo.objects.get(user=request.user)
    me.following.add(user_i_want_to_follow)
    me.save()
    # return HttpResponse(me)
    return HttpResponseRedirect(reverse('app_one:profile',kwargs={'pk':user_i_want_to_follow.id}))

# class ChatBoardView(ListView):
#     model=ChatRoom
#     context_object_name=chat_room_list
#     template_name='chat_board.html'
#     def get_queryset(self):
#         userinfo=UserInfo.objects.get(user=self.request.user)
#         return userinfo.following.all()
