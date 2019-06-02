from django.db import models


"""
1.铺位信息表
2.入驻申请信息表
3.用户信息表
"""

# Create your models here.
class Unit(models.Model):
    """
    铺位
    """

    loacation = models.CharField("店铺位置(x层y号)", max_length=10, unique=True)
    area = models.CharField("店铺面积", max_length=10)
    rent = models.CharField("店铺租金", max_length=10)
    status = models.CharField("铺位情况(租-0\闲-1\修-2)", max_length=2)

    class Meta:
        db_table = 'unit'


class EnterApplication(models.Model):
    """
    入驻申请
    """

    unit_id = models.IntegerField("铺位ID")
    lease_id = models.IntegerField("租约ID")
    user_id = models.IntegerField("用户ID")
    deadline = models.DateTimeField("租用期限")
    apply_date = models.DateTimeField("申请日期")
    handle_date = models.DateTimeField("审阅日期")
    status = models.CharField("审阅情况", max_length=6)
    # 附件 连接到附件表1对多 ？

    class Meta:
        db_table = 'enter_application'


class User(models.Model):
    """
    用户
    """

    user_type = models.CharField("用户类型", max_length=10)
    phone = models.CharField("手机号码", max_length=20)
    password = models.CharField("密码", max_length=256)
    idCard = models.CharField("身份证", max_length=18)
    name = models.CharField("姓名", max_length=20)
    email = models.CharField("邮箱", max_length=320)

    class Meta:
        db_table = 'user'