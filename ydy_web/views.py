from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.utils import timezone
from ydy_web.models import *
import re

# Create your views here.

def get_item_num(item_type=None):
    """
    该函数是获取数据库中各个类型数目的函数
    返回值是 具体要求项目的在数据库中的总数目
    """
    nums_info= Item_id_log.objects.get(id=1)#获取当前已经注册的用户数
    if   item_type=="User":
        return  nums_info.User_num
    elif item_type=="Topic":
        return  nums_info.Topic_num
    elif item_type=="Comment":
        return  nums_info.Comment_num
    elif item_type=="Equipment":
        return  nums_info.Equipment_num
    else :
        raise Http404("The item you want does not exist!")#raise 404 Error alearting user

def set_item_num(item_type="PP",new_val=0):
    """
    该函数是设置数据库中各个类型数目的函数
    返回值是 具体要求项目的在数据库中的总数目
    """
    nums_info= Item_id_log.objects.get(id=1)#获取当前已经注册的用户数 这个表只有一行

    if   item_type=="User":
        nums_info.User_num=new_val
        nums_info.save()
    elif item_type=="Topic":
        nums_info.Topic_num=new_val
        nums_info.save()
    elif item_type=="Comment":
        nums_info.Comment_num=new_val
        nums_info.save()
    elif item_type=="Equipment":
        nums_info.Equipment_num=new_val
        nums_info.save()
    else :
        raise Http404("The item you want does not exist!")#raise 404 Error alearting user
       
def start(req):
    context={}
    return render(req, 'ydy_web/start.html', context)
    #return HttpResponse("<h1>start_page</h1>")

def sign_in(req):
    context={}
    return render(req, 'ydy_web/sign_in.html', context)
    #return HttpResponse("<h1>sing_in_page</h1>")

def sign_up(req):
    context={}
    return render(req, 'ydy_web/sign_up.html', context)
    #return HttpResponse("<h1>sing_up_page</h1>")

def password_format_check(password):
    """
    return True if the string check passed
    """
    return False if len(password)!=6 else True

def user_account_format_check(account):
    """
    return True if the string check passed
    """
    return False if len(account)!=12 else True

def user_nickname_format_check(nickname):
    """
    return True if the string check passed
    """
    return True if (len(nickname)<=12 or len(nickname)<=0) else False

def account_registered_check(account):
    """
    检查这个账号是否已经被注册过
    registered: return False
    hasn' been registered True 
    """
    #try :
    #    registered_user=User.objects.get(user_accont=account)
    #    return False
    #except User.DoesNotExist:#在数据库中没有查找到相关的项
    #    return True
    registered_user=User.objects.filter(user_accont=account)
    print(registered_user)
    if len(registered_user)==0:
        return True
    else :
        return False

def sign_up_result(req):
    """
    该函数根据接收到的表单进行数据的处理 
    果注册信息符合要求则
    将数据存入数据库
    
    测试状态：基本测试已通过

    """
    ctx = {}
    sign_up_success=True
    Failure_reason="****"#empty reason
    #获取当前数据库中已经注册的用户数目
    next_user_id=get_item_num(item_type="User")+1

    #从注册表单中获取数据
    user_account    =req.POST['user_account']
    user_nickname   =req.POST['nick_name' ]
    user_password_0 =req.POST['password_0']
    user_password_1 =req.POST['password_1']

    if user_password_0!=user_password_1:#两次输入的密码不一致
        sign_up_success=False
        Failure_reason="两次输入的密码不一致"
    elif not password_format_check(user_password_1):
        sign_up_success=False
        Failure_reason="密码格式不正确"
    elif not user_account_format_check(user_account):
        sign_up_success=False
        Failure_reason="账号格式不正确"
    elif not user_nickname_format_check(user_nickname):
        sign_up_success=False
        Failure_reason="昵称格式不正确"
    elif not account_registered_check(user_account):
        sign_up_success=False
        Failure_reason="这个账号已经被注册"
    else :
        #account_registered_check(user_account)
        sign_up_success=True
        set_item_num(item_type="User",new_val=next_user_id)#save new user number in database
        user=User(  user_id=next_user_id,
                    user_accont=user_account,
                    user_nick_name=user_nickname,
                    user_password=user_password_0
                  )#创建一个新的用户数据条目
        user.save() #save data to database      
        #print(User.objects.filter(user_nick_name="DF5"))
    ctx["sign_up_success"]=sign_up_success
    ctx["fail_reason"]=Failure_reason
    
    #q = User(user_id=578, pub_date=timezone.now())
    return render(req, "ydy_web/sign_up_result.html", ctx)

def sign_in_result(req):
    """    
    该函数根据表单的信息 去查询数据库 如果查找成功则
    返回登录成功 否则返回登录失败
    测试状态：基本测试已通过
    """
    ctx = {}
    sign_in_success=True
    Failure_reason="****"#empty reason
    #获取当前数据库中已经注册的用户数目

    #从注册表单中获取数据
    user_account    =req.POST['user_account']
    user_password   =req.POST['password']
    account_match_list=User.objects.filter(user_accont=user_account)
    if len(account_match_list)==0:
        sign_in_success=False
        Failure_reason="用户不存在"#empty reason
    elif  len(account_match_list)>1:
        sign_in_success=False
        Failure_reason="数据库中存在多个相同账号 数据库错误"#empty reason
    else:
        if account_match_list[0].user_password!=user_password :
            sign_in_success=False
            Failure_reason="你输入的密码有误"#empty reason
        else:
            sign_in_success=True
            #Failure_reason="你输入的密码有误"#empty reason
            
    ctx["sign_in_success"]=sign_in_success
    ctx["fail_reason"]=Failure_reason
    response=render(req, "ydy_web/sign_in_result.html", ctx) #render data with template
    
    response.set_cookie('ydy_user_account',user_account)#set cookie to the HttpResponse
    return response
    
def Equipment_list(req):
    """
    这个借场函数用于罗列所有的借场信息
    """
    ctx={}
    sign_in_success=True
    try :
        user_account=req.COOKIES["ydy_user_account"]
        
        #if get cookie success 
        ctx["user_account"]=user_account
        Equipment_list=Equipment.objects.filter()
        ctx["Equipment_list"]=Equipment_list    
    except KeyError:
        sign_in_success=False
        ctx["user_account"]="***"
        ctx["Equipment_list"]=["***","***"]        
    ctx["sign_in_success"]=sign_in_success

    return render(req,"ydy_web/Equipment_list.html",ctx)
    
def Equipment_item(req,Equip_id):
    """
    这个函数用于显示所有的场地具体信息
    """
    ctx={}
    sign_in_success=True
    try :
        user_account=req.COOKIES["ydy_user_account"]   
        
        #if get cookie success
        ctx["user_account"]=user_account
        Equipment_selected=Equipment.objects.filter(Equipment_id=Equip_id)
        if len(Equipment_selected)==0:
            raise Http404("场地信息数据库有误 TAT 请联系管理员")
            
        content=Equipment_selected[0].Equipment_content
        
        #get user list string from database
        users=Equipment_selected[0].Equipment_user_list
        users=users.split()
        ctx["users"]=users
        ctx["content"]=content
        ctx["endtime"]=str(Equipment_selected[0].Equipment_end_date)
    except KeyError:
        sign_in_success=False    
        ctx["users"]=["***","***"]  
        ctx["user_account"]="****"
        ctx["content"]="*****"
        ctx["endtime"]="*****"
    ctx["sign_in_success"]=sign_in_success
    return render(req,"ydy_web/Equipment_item.html",ctx)
      
def Topic_list(req):
    """
    该函数用于显示 主题列表
    """
    ctx={}
    sign_in_success=True
    try :
        user_account=req.COOKIES["ydy_user_account"]   
        
        #if get cookie success
        ctx["user_account"]=user_account
        Topic_list0=Topic.objects.filter()
        Topic_title_list=[]
        for i in Topic_list0:
            Topic_title_list.append({"title":i.Topic_title,"date":i.Topic_date,"author":i.Topic_author,"topic_id":i.Topic_id})
        ctx["Topic_title_list"]=Topic_title_list
    except KeyError:
        sign_in_success=False    
        ctx["Topic_title_list"]=[("***","***")]
    ctx["sign_in_success"]=sign_in_success
    return render(req,"ydy_web/Topic_list.html",ctx)
    
    
def Topics(req,Topic_id):
    return HttpResponse("<h1> topics </h1>")
    
    
    
    
def Topic_edit(req):
    pass
def Comment_edit(req,Topic_id):  
    pass 
    

    
