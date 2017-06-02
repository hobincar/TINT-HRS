from django.db import models


class Coupon(models.Model):
    image = models.ImageField()
    discount = models.PositiveSmallIntegerField()

    def __str__(self):
        return "%d%% Discount" % self.discount


class CouponBlockedPeriod(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return "%s ~ %s" % (self.start_date, self.end_date)
