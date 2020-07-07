from django.db import models

# Create your models here.
# 创建实体类--  Publisher
# 属性 1.name:出版社名称（varchar(30)）
# 2. adddress:出版社地址（varchar(200)）
# city:出版社所在城市（varchar(50)）
# country:出版社国家（varchar(50)）
# website :出版社的网址（varchar（200））
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    website = models.URLField()
def __repr__(self):
    return '<author:%r>'% self.name

class author(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(null=True)
# 由于是新增列，所以必须为默认值或者允许为空
# BooleanField 默认不允许为空，所以此处选择了增加默认
    isActive = models.BooleanField(default=True)
class bOOK(models.Model):
    title = models.CharField(max_length=50)
    publicate_data = models.DateField()
