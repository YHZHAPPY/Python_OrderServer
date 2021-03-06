# Generated by Django 3.2.2 on 2021-05-07 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_userinfo_telephone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='Gender',
            field=models.NullBooleanField(default=None, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='ID',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='序号'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='RealName',
            field=models.CharField(max_length=50, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='Role',
            field=models.IntegerField(default=0, verbose_name='用户类型'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='Telephone',
            field=models.CharField(default=None, max_length=11, verbose_name='电话'),
        ),
    ]
