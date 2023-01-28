from django.db import models
# Create your models here.
from django.utils import timezone


class Department(models.Model):
    """
    部门表
    """
    title = models.CharField(verbose_name="部门标题", max_length=32)
    # 为了链接表查询使用显示部门名称
    def __str__(self) -> str:
        return self.title


class UserInfo(models.Model):
    """
    员工表
    """
    name = models.CharField(verbose_name="名字", max_length=16)
    password = models.CharField(verbose_name="密码", max_length=64)
    # 在django中的约束 通关chices来约束
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    sex = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)
    age = models.IntegerField(verbose_name="年龄")
    # 作用说明：十进制小数类型，保留几位小数
    # 数据类型：decimal
    # 最大位数max_digits = 10 和小数位decimal_places = 2
    account = models.DecimalField(
        verbose_name="工资", max_digits=10, decimal_places=2, default=0)

    create_time = models.DateField(
        verbose_name="入职时间", default=timezone.now)
    # 存储部门id 需要有约束 只能是部门表里面的id
    #   to 与那张表关联
    #   to_field 表中的那一列关联

    # 写下depart名称但是django会变成Department_id
    # 级联删除
    depart = models.ForeignKey(
        verbose_name="部门",
        to="Department", to_field="id", null=True, blank=True, on_delete=models.CASCADE)


class Gameaccount(models.Model):
    # 账号名称
    account = models.CharField(verbose_name="账号数据",max_length=64)
    # 账号密码
    password =models.CharField(verbose_name="账号密码",max_length=64)
    # 账号价格
    price = models.DecimalField(verbose_name="价格", max_digits=10, decimal_places=2, default=0)
    # 账号状态
    gender_choices = (
        (1, "已出售"),
        (2, "未出售"),
    )
    status=models.SmallIntegerField(verbose_name="游戏账号状态",choices=gender_choices,default=2)
    #账号封进
    ban_choices= {
        (1,"封禁状态"),
        (2,"未封禁状态")
    }
    isban_status  = models.SmallIntegerField(verbose_name="游戏账号封禁状态",choices=ban_choices,default=2)

    # 游戏类型
    # 游戏对应资源

# class GameType(models):
#     # 游戏名称
#     gamename=models.CharField(verbose_name="游戏名称",max_length=16)

# class ResourcesList(models):
#     pass

class Admin(models.Model):
    """管理员 列表"""
    username = models.CharField(verbose_name="用户名",max_length=32)
    password = models.CharField(verbose_name="密码",max_length=64)
