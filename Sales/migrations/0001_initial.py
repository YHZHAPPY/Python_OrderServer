# Generated by Django 3.2.2 on 2021-05-07 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SaleDetails',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('CustomerID', models.CharField(max_length=20, verbose_name='商户ID')),
                ('Time', models.DateTimeField(verbose_name='时间')),
                ('UserName', models.CharField(max_length=10, verbose_name='下单用户')),
                ('Flag', models.IntegerField(verbose_name='录入标记')),
                ('CustomerName', models.CharField(max_length=20, verbose_name='商户名称')),
                ('Amount', models.FloatField(verbose_name='订单金额')),
            ],
            options={
                'verbose_name': '订单详情',
                'verbose_name_plural': '订单详情列表',
            },
        ),
        migrations.CreateModel(
            name='SaleInfo',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False, verbose_name='订单序号')),
                ('SaleID', models.IntegerField()),
                ('GoodID', models.CharField(max_length=20, verbose_name='商品信息')),
                ('Price', models.FloatField(verbose_name='单价')),
                ('Company', models.CharField(max_length=10, verbose_name='单位')),
                ('Count', models.IntegerField(verbose_name='数量')),
                ('Remarks', models.CharField(max_length=20, verbose_name='备注')),
                ('Flag', models.IntegerField(verbose_name='录入标记')),
            ],
            options={
                'verbose_name': '订单',
                'verbose_name_plural': '订单信息',
            },
        ),
    ]
