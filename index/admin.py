from django.contrib import admin

from .models import *

# Register your models here.
admin.site.site_header = '自动化测试管理系统'
admin.site.site_title = '测试平台'


# 声明高级管理类
class AuthorAdmin(admin.ModelAdmin):
    # 指定在列表页显示的字段
    list_display = ('name', 'age', 'email')
    # 指定能够能够连接到详情页的字段们
    list_display_links = ('name', 'email')
    # 指定在列表页面就允许修改的字段们
    list_editable = ('age',)
    # 指定添加到搜索的字段们
    search_fields = ('name', 'age', 'email')
    # 指定按姓名筛选
    list_filter = ['name']
    # 指定显示字段及显示顺序
    # fields = ('name','email','isActive')
    fieldsets = (
        # 分组１
        ('基本信息', {
            'fields': ('name', 'email'),
        }),
        # 分组２
        ('可选信息', {
            'fields': ('age', 'isActive', 'picture'),
            'classes': ('collapse',),
        })
    )


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'website')
    list_editable = ('address', 'city')
    # 右侧过滤器
    list_filter = ['address', 'city']
    search_fields = ('name', 'website')
    fieldsets = (
        # 分组１
        ('基本选项', {
            'fields': ('address', 'city'),
        }),
        # 分组２
        ('高级选项', {
            'fields': ('country', 'website'),
            'classes': ('collapse',),
        })
    )


# # 注册
admin.site.register(author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(bOOK)

# 高级管理：
# 1.在admin中创建高级管理类并注册
# 1.定义EnthorAdmin类，继承 amdin.ModelAdmin
# class AuthorAdmin(admin.ModelAdmin):
#     pass
# 2.注册高级管理类
# admin.site.rehister(EntryAdmin)
# 2.允许在EntryAdmin中增加属性
# 1.list_display = ('name','age','email')
#     作用：定义在列表页显示的字段们
#     取值：由属性名组成的元组或列表
# 2.list_display_links
#     作用：定义早列表页中也能够连接到详情页的字段们
#     取值：同上
#     注意：取值必须出现在list_display
#     3.list_editable
#     作用：定义在列表页中就允许修改的字段们
#     取值：同上
#     注意：取值必须出现在list_display中但不能出现在list_display_links中
#     4.search_fields
#         作用：添加允许被搜索的字段们
#         取值：同上
#      5.list_filter
#     作用：列表右侧增加过滤器，实现快速筛选
#         取值：同上
#         6.date_hierarchy
#         作用：列表页顶部增加时间选择器
#         取值：DataField或DateTimeField的列名
#
# class BookAdmin(admin.ModelAdmin):
#
#     date_hierarchy = 'publicate_date'

# 7.fields
# 作用：详情页中指定要显示哪些字段并按照什么样顺序去显示
#     取值：元祖或列表
# 8.fieldsets
#     作用：在详情页对字段进行分组显示
#     注意：fields和fieldsets不能共存
#     取值：fields = (
#     分组1('当前分组的名称',{
#     'fields':('属性1','属性2'....),
#       'classes':('collapse',)
#     }),
#     分组2()
#
#     )
