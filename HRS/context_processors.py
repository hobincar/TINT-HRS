from django.conf import settings # import the settings file
from datetime import date

from memberships.models import CouponBlockedPeriod


def media_url(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'MEDIA_URL': settings.MEDIA_URL}


def coupon_blocked_period(request):
    coupon_blocked_periods = CouponBlockedPeriod.objects.all()
    today = date.today()
    is_coupon_blocked = False
    for period in coupon_blocked_periods:
        if period.start_date <= today <= period.end_date:
            is_coupon_blocked = True
            break

    return {'COUPON_BLOCKED_PERIOD': is_coupon_blocked}
