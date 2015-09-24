# coding=utf-8
from django.http import HttpResponse
from django import template
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from MyBlog import service
import traceback
import MyBlog
# Create your views here.
@csrf_exempt
def getLogin(request):
    return render_to_response('login.html',locals())

@csrf_exempt
def login(request):
    try:
        if request.method == 'POST': # 如果表单被提交
            form = MyBlog.models.userForm(request.POST) # 获取Post表单数据
            if form.is_valid():
                form = form.cleaned_data
                if service.loginService(form):
                    request.session['username'] = form["username"]
                    menuList = service.getMenu(form)
                    articleList = service.articleList(request.session.get('username', False))
                    print(menuList)
                    print(articleList)
                    return render_to_response('index.html',locals())
                else:
                    return render_to_response('login.html',locals())
    except Exception as e:
        return print (e)

    #return HttpResponse(service.loginService(request))

@csrf_exempt
def getIndex(request):
    return render_to_response('index.html',locals())


