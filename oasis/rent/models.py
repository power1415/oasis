from django.db import models


"""
1.租约
2.支付记录
3.退租申请
4.延付申请
"""

class Lease(models.Model):
    """
    租约
    """

    user_id = models.IntegerField("用户ID")
    name = models.CharField("店铺名称", max_length=20)
    rent = models.CharField("租金", max_length=10)
    duration = models.CharField("持续时间", max_length=10)
    start_date = models.DateTimeField("起效时间")

    class Meta:
        db_table = "lease"


class Paymemt(models.Model):
    """
    支付记录
    """

    lease_id = models.IntegerField("租约ID")
    payer_id = models.IntegerField("支付者ID")
    pay_amount = models.FloatField("支付金额")
    pay_date = models.DateTimeField("支付时间")

    class Meta:
        db_table = "payment"



class RefundApplication(models.Model):
    """
    退租申请
    """

    user_id = models.IntegerField("用户ID")
    lease_id = models.IntegerField("租约ID")
    default_value = models.FloatField("违约金")
    apply_date = models.DateTimeField("申请时间")
    handle_date = models.DateTimeField("处理时间")
    status = models.CharField("审阅情况", max_length=10)

    class Meta:
        db_table = "refund_application"


class DeferPayApplication(models.Model):
    """
    延付申请
    """

    lease_id = models.IntegerField("租约ID")
    original_date = models.DateTimeField("原支付日期")
    current_date = models.DateTimeField("现支付日期")
    apply_date = models.DateTimeField("申请日期")
    handle_date = models.DateTimeField("处理日期")
    status = models.CharField("审阅情况", max_length=10)

    class Meta:
        db_table = "defer_pay_application"