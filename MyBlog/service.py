import MyBlog
from django.db import connection
import json
#验证登录
def loginService(form):
    raw_sql = "select username,password,userId from db_user WHERE username='%s' and password='%s'"% \
            (form["username"],form["password"] )
    result = MyBlog.models.db_user.objects.raw(raw_sql); #xx.objects.raw()执行原始sql
    if len(list(result))==1:
        flag = True
    else:
        flag = False
    return flag

#得到用户基本数据
def getMenu(username):
    sql = "SELECT b.typeId,b.type,count(c.title) AS count FROM db_user a LEFT JOIN db_menu b ON a.userId = b.userId LEFT JOIN db_article c ON b.typeId=c.typeId WHERE a.username='%s' GROUP BY b.type"% \
            (username)
    result = MyBlog.models.db_menu.objects.raw(sql); #xx.objects.raw()执行原始sql
    # sql = "SELECT b.type,count(b.type) AS count FROM db_user a LEFT JOIN db_menu b ON a.userId = b.userId LEFT JOIN db_article c ON b.typeId=c.typeId WHERE a.username='%s' GROUP BY b.type"% \
    #         (form["username"] )
    # cursor = connection.cursor()
    # cursor.execute(sql)
    # result = cursor.fetchall()
    # print (dict(result))
    return list(result)


#主页文章列表
def articleList(username):
    sql = "SELECT id,a.userId,title,tags,date,a.typeId,type,content,copyfrom,username,hit,comment,url FROM db_article a LEFT JOIN db_menu b ON a.userId = b.userId and a.typeId = b.typeId WHERE a.username='%s' "% \
            (username)
    result = MyBlog.models.db_article.objects.raw(sql); #xx.objects.raw()执行原始sql
    return list(result)

