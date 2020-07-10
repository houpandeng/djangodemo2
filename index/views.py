from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q, Avg, Count, Sum, Max, Min
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
def query_views(request):
    # 所有的查询接口必须通过Entry.objects 去调用
    # all():查询 author 实体中所有的数据
    # authors = author.objects.all()
    # print(authors.query)
    # print('authors')
    # 循环遍历authors得到每一个数据
    # for i in authors:
    #     print(i.id,i.name,i.age,i.email)

    # values() 查询部分数据封装到字典中在封装到列表中
    # 查询authors实体中所有行所有列封装到字典再封装到列表中
    authors = author.objects.values()
    # 查询authors实体中所有行的name和email列封装到字典再封装
    authors = author.objects.values('name','email')
    # 查询authors实体中所有行的name和email列封装到字典再封装
    # authors = author.objects.all().values('name','email')
    print(authors)
    for au in authors:
        print(au['name'])
    return HttpResponse('query ok')
# def queryall_views(request):
#     authors = author.objects.filter(isActive=True)
#     return render(request,'07-queryall.html',locals())


def queryall_views(request):
    authors = author.objects.filter(isActive=True)
    return render(request,'07-queryall.html',locals())

# 查询到前端页面展示，id
def update_views(request,id):
    authors=author.objects.get(id=id)
    return render(request,'08-update.html',locals())

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
    # 聚合查询（不带分组）
    # author.objects.all().aggregate(avg=聚合函数('列'))
    # 语法：aggregate()
    # authors = author.objects.all().aggregate(avg=Avg('age'))
    # print(authors['avg'])
    # authors1 = author.objects.all().aggregate(avg=Count('age'))
    # print(authors1['avg'])
    # authors2 = author.objects.all().aggregate(avg=Sum('age'))
    # print(authors2['avg'])
    # authors3 = author.objects.all().aggregate(avg=Max('age'))
    # print(authors3['avg'])
    # authors4 = author.objects.all().aggregate(avg=Min('age'))
    # print(authors4['avg'])
    # 聚合查询（带分组）
    # author.objects.all().values('列1','列2').annotate(列 = 聚合函数()).values('列1','列2')
    # 语法：annotate()
    # res = author.objects.values('isActive').annotate(sum=Sum('age')).all()
    # print(res)
    # 排序查询
    # 语法：order_by()
    # Entry.objects.order_by('列1','列2')
    # 默认升序，列名加'-',则按降序排序
    # res = author.objects.order_by('-id')
    # print(res.query)
    return HttpResponse('query ok')


def update09_views(request):
# 修改id为2得author得信息
#     au = author.objects.get(id=2)
#     au.age = 38
#     au.email = 'b1822087@163.com'
#     au.isActive = False
#     au.save()
# 修改isActive更改为True
#     author.objects.filter(isActive=False).update(isActive = True)
# 删除：delete
#      au = author.objects.get(id=1)
#      au.delete()

     return HttpResponse('update success')
def delete_views(request,id):
    authors = author.objects.get(id=id)
    # 通过isActive= False模拟删除
    authors.isActive= False
    authors.save()
    # 查看queryall_views中的内容
    # return queryall_views(request)
# 使用重定向到/07-queryall
#     return HttpResponseRedirect('/index/07-queryall')
    return redirect('/index/07-queryall')