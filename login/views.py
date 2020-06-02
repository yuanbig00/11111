from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from . import forms
from .models import events
import hashlib
from django.shortcuts import render_to_response
from django.core.paginator import Paginator
import json
# Create your views here.


def index(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    events=models.events.objects.all()
    return render(request, 'login/search_form.html',{'events': events})



def login(request):
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            try:
                user = models.User.objects.get(name=username)
            except :
                message = '用户不存在！'
                return render(request, 'login/login.html', locals())

            if user.password == hash_code(password):
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return redirect('/search_form/')
            else:
                message = '密码不正确！'
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    # if request.session.get('is_login', None):
    #     return redirect('/search_form/')

    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            sex = register_form.cleaned_data.get('sex')

            if password1 != password2:
                message = '两次输入的密码不同！'
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:
                    message = '用户名已经存在'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:
                    message = '该邮箱已经被注册了！'
                    return render(request, 'login/register.html', locals())

                new_user = models.User()
                new_user.name = username
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.sex = sex
                new_user.save()

                return redirect('/login/')
        else:
            return render(request, 'login/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'login/register.html', locals())



def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/login/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/login/")
def hash_code(s, salt='disaster'):# 加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()
def table(request,id):
    event = models.events.objects.get(id=id)
    hots = models.past_hours_hot.objects.get(id=id)
    return render(request, 'login/table.html',{'event':event,'hots':hots})


def remark(request,id):
    event = models.events.objects.get(id=id)
    person=models.person_remarks.objects.get(id=id)

    word_cloud=event.word_cloud
    datalist = word_cloud.split('*')
    datalist = [json.loads(j) for j in datalist]
    return render(request, 'login/remark.html', {'word_cloud':datalist,'event': event,'person':person})


def spread(request,id):
    event = models.events.objects.get(id=id)
    return render(request, 'login/spread.html', {'event': event})


def people(request,id):
    user = models.User.objects.name
    event = models.events.objects.get(id=id)
    number = event.famale + event.male
    female = event.famale / number*100
    male = event.male / number*100
    return render(request, 'login/people.html', {'event': event,'female':female,'male':male,'user':user})

def search_form(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    if request.GET.get('order')=='hot':#字段热度，不是事件热度
        articles_list=events.objects.all().order_by('-hot')[:30]
        order='hot'
    else:
        articles_list=events.objects.all()[:30]
        order='normal'
    paginator=Paginator(articles_list,6)
    page=request.GET.get('page')
    articles=paginator.get_page(page)
    context={'articles':articles,'order':order}
    return  render_to_response('login/search_form.html',context)

def search_result(request):
    if 'q' in request.GET or request.GET['q']:
        q=request.GET['q']
        search=events.objects.filter(event_name__icontains=q)
        return render_to_response('login/search_result.html',{'search':search,'query':q})
    else:
        render_to_response('login/search_form.html',{'error':True})
def show(request,id):
    content=events.objects.get(id=id)
    return render_to_response('login/show.html',{"content":content})
def first(request):
    pass
    return render(request, 'login/first.html', locals())