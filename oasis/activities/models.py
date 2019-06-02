from django.db import models


"""
1.活动申请信息表
"""
# Create your models here.

class ActivityApplication(models.Model):
    """
    活动申请
    """

    name = models.CharField("活动名称", max_length=20)
    activity_type = models.CharField("活动类型", max_length=5)
    location = models.CharField("位置", max_length=10)
    duration = models.CharField("持续时间", max_length=10)
    profile = models.CharField("活动概要", max_length=200)
    apply_date = models.DateTimeField("申请时间")
    handle_date = models.DateTimeField("审阅时间")
    status = models.CharField("审阅情况", max_length=10)

    class Meta:
        db_table = "activity_application"