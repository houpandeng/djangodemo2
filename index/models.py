from django.db import models

# Create your models here.
# 创建实体类--  Publisher
# 属性 1.name:出版社名称（varchar(30)）
# 2. adddress:出版社地址（varchar(200)）
# city:出版社所在城市（varchar(50)）
# country:出版社国家（varchar(50)）
# website :出版社的网址（varchar（200））
class Publisher(models.Model):
    name = models.CharField(max_length=30,verbose_name='名称')
    address = models.CharField(max_length=200,verbose_name='详细地址')
    city = models.CharField(max_length=50,verbose_name='地区')
    country = models.CharField(max_length=50,verbose_name='国家')
    website = models.URLField(verbose_name='地址')
    def __str__(self):
        return self.name
    class Meta:
        # 1.修改表名为author
        db_table = 'Publisher'
        verbose_name = '出版社'
        verbose_name_plural = verbose_name

def __repr__(self):
    return '<author:%r>'% self.name

class author(models.Model):
    name = models.CharField(max_length=30,verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    email = models.EmailField(null=True,verbose_name='邮件')
# 由于是新增列，所以必须为默认值或者允许为空
# BooleanField 默认不允许为空，所以此处选择了增加默认
    isActive = models.BooleanField(default=True,verbose_name='激活用户')
    # 重写 __str__来定义该对象的字符串表示,展示的前端页面
    def __str__(self):
        return self.name
  #增加内部的类Meta来定义展现形式
    class Meta:
       # 1.修改表名为author
        db_table = 'author'
    # 2.指定后台管理，指定的名字
        verbose_name = '作者'
        verbose_name_plural = verbose_name
        # 3.指定按age年龄排序
        ordering = ['-age']



class bOOK(models.Model):
    title = models.CharField(max_length=50)
    publicate_data = models.DateField()

    class Meta:
        # 1.修改表名为author
        db_table = 'booK'
        verbose_name = '书籍'
        verbose_name_plural = verbose_name
# 通过Models类的内部类Meta来定义展示形式
# class author(models.Model):
#     ................
#     class Meta:
#         1.db_table
#         指定该实体类映射到表的名称
#         （该属性设置完成后需要同步回数据库）
#            2.verbose_name
#         定义实体类在admin中显示的名字（单数形式）
#             3.verbose_name_plural
#         定义实体类在admin中显示的名字（复数形式）
            # 4.ordering
            # 指定数据在后台管理中的排序方式，取值是一个列表，将排序的列表式在列表，默认升序，降序使用







