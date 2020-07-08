from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.template import loader
# Create your views here.
def index_views(requet):
    return HttpResponse('分布式路由系统')

# def temp_views(request):
#     t = loader.get_template('01-temp.html')
#     html = t.render()
#     return HttpResponse(html)

def temp_views(request):
    return render(request,'01-temp.html')

def temp2_views(requst):
    return render(requst,'01-temp.html')
# def var_views(request):
#     name = 'wangwc'
#     age = 30
#     return render(request,'03-var.html',locals())

def var_views(request):
    str = '模板中的变量-字符串'
    num = 3306
    tup = ('谢逊','韦一笑','殷素素','金花婆婆')
    list = ['孙悟空','猪八戒','沙和尚']
    dic = {'BJ':'北京','SZ':'深圳','SH':'上海'}
    say = dunc()
    dog = Dog()

    return render(request,'03-var.html',locals())
def dunc():
    return 'Hello,tthis is a views'

class Dog():
    name = '旺财'
    def eat(self):
        return '吃狗粮'

def test_views111(request):
    return HttpResponse('测试首页视图')
# Entry.objects.crate()
def add_views(request):
    # obj = author.objects.create(name = '张老师',age = 32,email='a1822087@163.com')
    # print(obj.id,obj.name,obj.age,obj.email)
    # 方案2 obj.save()
    # obj = author(name = '隔壁老王',age = 32,email='824452650@qq.com')
    # obj.save()
    # print(obj.id,obj.name,obj.age,obj.email)
    # 方案3 用字典构建对象，并save保存
    # dic= {'name':'超哥',
    #       'age':35,
    #       'email':'qiiswns@126.com',
    #       'isActive':False}
    # obj = author(**dic)
    # obj.save()
    # print(obj.id,obj.name,obj.age,obj.email,obj.isActive)
    # Publisher.objects.create(name = '北京大学出版社',address = '北大东路125号',city='北京',country='中国',
    #                          website='http://www.baida.com'
    #                          )
    # obj1 = Publisher(name = '清华大学出版社',address = '清华东路125号',city='北京',country='中国',
    #                          website='http://www.qinghua.com')
    # dic= {'name':'人民教育出版社',
    #       'address':'珠市口大街',
    #       'city' : '北京',
    #       'country' : '中国',
    #       'website':'http://www.pople.com'}
    # obj1 = Publisher(**dic)
    # obj1.save()
    bOOK.objects.create(title='老王的一天',publicate_data='2015-10-12')
    book = bOOK(title='老王的一周',publicate_data='2015-9-12')
    book.save()
    dic = {
        'title':'王老师的幸福生活',
        'publicate_data':'2018-01-01'
    }
    book1 = bOOK(**dic)
    book1.save()
    return HttpResponse('add ok')


def queryall(request):
    # 只能查一条
    # authors = author.objects.get(id=1)
    # print(authors)
    # 查询部分行数据 filter(条件)
    # 查询id为1数据
    # authors = author.objects.filter(id = 1)
    # 查询sql语句
    # print(authors.query)
    # 查询id为1数据，并且name为隔壁老王的信息
    # authors = author.objects.filter(id =1,name='隔壁老王')
    # print(authors.query)
    # 查询age>=30author的信息
    # authors = author.objects.filter(age__gte=30)
    # print(authors.query)
    # 查询所有姓王的信息
    # authors = author.objects.filter(name__startswith='王')
    # print(authors.query)
    # 查询所有email中包含'wang'的信息
    # authors = author.objects.filter(email__contains='王')
    # print(authors)
    # 条件取反 exclude

    # authors = author.objects.exclude(id =1)
    # print(authors.query)

    return HttpResponse('query ok')

你是python1


