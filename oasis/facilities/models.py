from django.db import models


"""
1.设施
2.设施检查记录
"""

# Create your models here.
class Facility(models.Model):
    """
    设施
    """

    facility_type = models.CharField("设施类型", max_length=10)
    facility_name = models.CharField("设施名字", max_length=10)
    location = models.CharField("位置", max_length=10)
    deadline = models.DateTimeField("失效期")

    class Meta:
        db_table = "facility"


class CheckRecord(models.Model):
    """
    检查记录
    """

    facility_id = models.IntegerField("设施ID")
    status = models.CharField("检查情况", max_length=10)
    check_date = models.DateTimeField("检查日期")
    user_id = models.IntegerField("检查者ID")

    class Meta:
        db_table = "check_record"