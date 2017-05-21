from django.db import models
from django.utils import timezone


class Reservation(models.Model):
    customer = models.ForeignKey(
        'accounts.User',
        limit_choices_to={'is_staff': False},
        on_delete=models.CASCADE,
        related_name='customer_accounts_user')
    staff = models.ForeignKey('accounts.User',
                              limit_choices_to={'is_staff': True},
                              related_name='staff_accounts_user',
                              blank=True)
    check_in = models.DateField()
    check_out = models.DateField()
    n_room = models.PositiveSmallIntegerField()
    n_adult = models.PositiveSmallIntegerField()
    n_child = models.PositiveSmallIntegerField()
    coupon = models.BooleanField()
    discount = models.PositiveSmallIntegerField()
    room = models.ForeignKey('rooms.Room')
    n_breakfase = models.PositiveSmallIntegerField()
    n_babybed = models.PositiveSmallIntegerField()
    addendum = models.TextField()

    card_type = models.CharField(
        max_length=2,
        choices=(
            ('VS', 'Visa'),
            ('MS', 'Master'),
            ('AE', 'American Express'),
            ('DC', 'Discover')
        ))
    card_number = models.CharField(
        max_length=16)
    cvc = models.CharField(
        max_length=3)
    expiration_month = models.CharField(
        max_length=2)
    expiration_year = models.CharField(
        max_length=4)

    send_receipt = models.CharField(
        max_length=1,
        choices=(
            ('C', 'Cell Phone'),
            ('E', 'E-mail')
        ),
        blank=True
    )


    reserved_date = models.DateTimeField(
        default=timezone.now)
