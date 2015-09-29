# coding=utf-8
from django.http import HttpResponse
from django import template
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from MyBlog import service
from MyBlog import models
import traceback
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
#登录页面
@csrf_exempt
def getLogin(request):
    return render_to_response('login.html',locals())
#登录验证
@csrf_exempt
def login(request):
    try:
        if request.method == 'POST': # 如果表单被提交
            form = models.userForm(request.POST) # 获取Post表单数据
            if form.is_valid():
                form = form.cleaned_data
                if service.loginService(form):
                    request.session['username'] = form["username"]
                    return HttpResponseRedirect('/index')
                else:
                    return render_to_response('login.html',locals())
    except Exception as e:
        return print (e)

#主页数据
@csrf_exempt
def getIndex(request):
    username = request.session.get('username', False)
    menuList = service.getMenu(username)
    article = service.articleList(username)
    paginator = Paginator(article, 2) # 分页，每页3个
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

#文章详细内容
@csrf_exempt
def getContent(request):
    contentId = request.GET.get('id')
    article = models.db_article.objects.get(id=contentId)
    comment = models.db_comment.objects.filter(id=contentId)
    return render_to_response('content.html',locals())


