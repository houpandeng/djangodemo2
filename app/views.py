from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# 注册
def register(request):
    if request.method =='GET':
        return render(request, 'register.html')
    else:
        print(request.POST)

        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        print(password)
        f_pwd= request.POST.get('f_pwd')
        print(f_pwd)

    if username == '123'.strip().upper() and password == '123'.strip().upper() and f_pwd == '123'.strip().upper() :
        return HttpResponse ('注册成功')
    else:
        return HttpResponse('注册失败')


#登录
def login_index(request):
    if request.method =='GET':
        return render(request, 'login_index.html')
    else:
        print(request.POST)
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        print(password)
        IMG = request.POST.get('yzm')
        print(IMG)
    if username == '17621258146'.strip().upper() and password == '123'.strip().upper() and IMG =='123'.strip().upper():
        return HttpResponse ('登录成功')
    else:
        return HttpResponse('登录失败')

def show(request):
    # return render(request,'books.html')

    return HttpResponse('我的第一个Django程序')


