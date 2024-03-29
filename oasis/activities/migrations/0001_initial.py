# Generated by Django 2.1.5 on 2019-05-27 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='活动名称')),
                ('activity_type', models.CharField(max_length=5, verbose_name='活动类型')),
                ('location', models.CharField(max_length=10, verbose_name='位置')),
                ('duration', models.CharField(max_length=10, verbose_name='持续时间')),
                ('profile', models.CharField(max_length=200, verbose_name='活动概要')),
                ('apply_date', models.DateTimeField(verbose_name='申请时间')),
                ('handle_date', models.DateTimeField(verbose_name='审阅时间')),
                ('status', models.CharField(max_length=10, verbose_name='审阅情况')),
            ],
            options={
                'db_table': 'activity_application',
            },
        ),
    ]
