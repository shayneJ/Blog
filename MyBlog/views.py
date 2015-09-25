# coding=utf-8
from django.http import HttpResponse
from django import template
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from MyBlog import service
import traceback
import MyBlog
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect

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
                    return HttpResponseRedirect('/index/')
                else:
                    return render_to_response('login.html',locals())
    except Exception as e:
        return print (e)


@csrf_exempt
def getIndex(request):
    username = request.session.get('username', False)
    menuList = service.getMenu(username)
    article = service.articleList(username)
    paginator = Paginator(article, 3) # 分页，每页3个
    page = request.GET.get('page')
    try:
        articleList = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articleList = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articleList = paginator.page(paginator.num_pages)
    return render_to_response('index.html',locals())


