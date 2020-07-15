# Generated by Django 3.0.7 on 2020-07-12 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20200712_2002'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': '书籍', 'verbose_name_plural': '书籍'},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'verbose_name': '出版社', 'verbose_name_plural': '出版社'},
        ),
        migrations.AlterField(
            model_name='publisher',
            name='address',
            field=models.CharField(max_length=200, verbose_name='详细地址'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='city',
            field=models.CharField(max_length=50, verbose_name='地区'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='country',
            field=models.CharField(max_length=50, verbose_name='国家'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=30, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='website',
            field=models.URLField(verbose_name='地址'),
        ),
        migrations.AlterModelTable(
            name='book',
            table='bOOK',
        ),
    ]