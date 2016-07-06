#coding=utf-8

from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from JxBlog.login.models import BlogUser


# Create your views here.


#定义表单模型
class UserForm(forms.Form):
    username = forms.CharField(label='用户名：',max_length=100)
    password = forms.CharField(label='密码：',widget=forms.PasswordInput())

#登录
def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = BlogUser.objects.filter(username = username,userpwd = password)
            if user:
                return render_to_response('LoginSuccess.html', {'username':username})
            else:
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html', {'uf':uf})
