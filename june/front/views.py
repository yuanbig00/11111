from django.shortcuts import render,redirect
#from .models import User,Admin,Event,Word
from django.http import HttpResponse
from django.db import models
from django.db import connection#数据库操作


# Create your views here.
def index(request):
    context={}
    context['hello']='helloworld'
   # return HttpResponse("success")
    return render(request,'index.html',context)






# #查看事件（用户 & 管理员）
# def check_event(request):
#     pass
# #搜索事件（用户 & 管理员）
# def select_event(request):
#     pass
#
# #管理员查看用户信息,用户管理
# def manage_user(request):
#     # 取出所有用户信息
#     user_list=models.User.objects.all()
#     # render渲染前端页面，locals将当前函数所有变量都发送至前端
#     return render(request, 'manage_user.html', locals())
#
#
# #管理员删除用户信息
# # 删除用户信息视图函数
# def delete_user(request):
#     user_id = request.GET.get('user_id')
#     models.User.objects.filter(id=user_id).delete()
#     return redirect('/manage_user/')
#
# #管理员修改用户信息
# def edit_user(request):
#     user_id=request.GET.get('user_id')
#     user_obj=models.User.objects.filter(id=user_id).first()
#     if request.method=='POST':
#         name=request.POST.get('name')
#         password=request.POST.get('password')
#         models.User.objects.filter(id=user_id).update(name=name,password=password)
#         return redirect('/manage_user/')
#     # return render(request,'edit_user.html',locals())
#
