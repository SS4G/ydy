from django.db import models

# Create your models here.
class Item_id_log(models.Model):#这个表用来记录所有其他数据库中的数据条目
    User_num        = models.IntegerField(default=0) #整个网站的注册用户数
    Comment_num     = models.IntegerField(default=0) #整个网站的评论数
    Topic_num       = models.IntegerField(default=0) #整个网站的主题数
    Equipment_num   = models.IntegerField(default=0) #整个网站的借场信息数
    
class User(models.Model):#这个数据库用来记录用户的注册信息
    user_id         = models.IntegerField(default=0) #用户在数据库中的唯一编号
    user_accont     = models.CharField(max_length=20)#用户的账号
    user_nick_name  = models.CharField(max_length=20)#用户的昵称
    user_password   = models.CharField(max_length=20)#用户的密码

class Topic(models.Model):#这个表用来记录 
    Topic_id       = models.IntegerField(default=0) #该主题在数据库中的唯一编号
    Topic_date     = models.DateTimeField('date published')#该主题发表的时间
    Topic_content  = models.CharField(max_length=500)#该主题的正文
    Topic_author   = models.CharField(max_length=20) #该主题的作者的账号
    
class Comment(models.Model):
    Comment_id                  = models.IntegerField(default=0)      #该评论在数据库中的唯一编号
    Comment_date                = models.DateTimeField('date published')#该评论发表的时间
    Comment_author              = models.CharField(max_length=20) #该评论的作者的账号
    Comment_topic_belong_to     = models.IntegerField(default=0)  #该评论隶属于的主题
    Comment_content             = models.CharField(max_length=300) #该评论的正文
    
class Equipment(models.Model):
    Equipment_id                = models.IntegerField(default=0)   #器材资源信息的我在数据库中的唯一编号
    Equipment_user_list         = models.CharField(max_length=500) #器材资源信息的申请用户表 以字符形式存放 账号间 
    Equipment_content           = models.CharField(max_length=300) #器材信息的描述正文
    Equipment_begin_date        = models.DateTimeField('date begin') #信息的发布时间
    Equipment_end_date          = models.DateTimeField('date end')   #信息的过期时间(过期后网站将不再显示)
    
    