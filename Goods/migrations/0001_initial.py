# Generated by Django 3.2.2 on 2021-05-07 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodInfo',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('Barcode', models.CharField(max_length=30, verbose_name='商品ID')),
                ('Name', models.CharField(max_length=100, verbose_name='商品名称')),
                ('Price', models.FloatField(default=0, verbose_name='价格')),
                ('Company', models.CharField(max_length=10, verbose_name='单位')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品列表',
            },
        ),
    ]
