from django.db import models

# Create your models here.


class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()


'''
create table app01_ userinfo{
id bigint auto_increment primary key,
name varchar(32),
password varchar(64) ，
age int
}
'''


class Department(models.Model):
    title = models.CharField(max_length=16)
    author = models.CharField(max_length=32)
    age = models.IntegerField(default=10)
    data = models.CharField(max_length=32, null=True, blank=True)


class Role(models.Model):
    caption = models.CharField(max_length=16)


# class Role1(models.Model):
#     caption = models.CharField(max_length=16)
# 向表里面写数据
