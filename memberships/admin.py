from django.contrib import admin
from .models import Coupon, CouponBlockedPeriod

admin.site.register(Coupon)
admin.site.register(CouponBlockedPeriod)
