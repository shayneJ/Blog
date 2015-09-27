from django.db import models
from django.forms import ModelForm
from ckeditor.fields import RichTextField
#用户
class db_user(models.Model):
    userId = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class userForm(ModelForm):
  class Meta:
    model = db_user
    fields = ('username', 'password')

#栏目表
class db_menu(models.Model):
    typeId = models.IntegerField(primary_key=True)
    userId = models.IntegerField()
    type = models.CharField(max_length=10)

class menuForm(ModelForm):
    count = models.IntegerField()
    class Meta:
        model = db_menu
        fields = ('typeId','userId', 'type',)

#文章主表
class db_article(models.Model):
    id = models.IntegerField(primary_key=True)
    userId = models.IntegerField()
    title = models.CharField(max_length=100)
    tags = models.CharField(max_length=50)
    date = models.DateTimeField()
    typeId = models.IntegerField()
    content = models.TextField()
    copyfrom = models.CharField(max_length=40)
    username = models.CharField(max_length=20)
    hit = models.IntegerField()
    comment = models.IntegerField()

class articleForm(ModelForm):
    type = models.CharField(max_length=10)
    class Meta:
        model = db_article
        fields = ('id','userId', 'title','tags','date','typeId','content','copyfrom','username','hit','comment')

class Article(models.Model):
    content = RichTextField('正文')