from django.db import models
from django.utils import timezone

from multiselectfield import MultiSelectField


class Reservation(models.Model):
    customer = models.ForeignKey(
        'accounts.User',
        limit_choices_to={'is_staff': False},
        on_delete=models.CASCADE,
        related_name='customer_accounts_user')
    staff = models.ForeignKey('accounts.User',
                              limit_choices_to={'is_staff': True},
                              related_name='staff_accounts_user',
                              blank=True, null=True)
    check_in = models.DateField()
    check_out = models.DateField()
    rooms = models.ManyToManyField('rooms.Room', through='RoomReservationInfo')
    n_adult = models.PositiveSmallIntegerField()
    n_child = models.PositiveSmallIntegerField()
    coupon = models.ForeignKey(
        'reservations.Coupon',
        blank=True, null=True)
    n_breakfast = models.PositiveSmallIntegerField()
    n_baby_bed = models.PositiveSmallIntegerField()
    addendum = models.TextField(blank=True, null=True)

    card_type = models.CharField(
        max_length=2,
        choices=(
            ('VS', 'Visa'),
            ('AE', 'American Express'),
            ('DC', 'Discover')
        ))
    card_number = models.CharField(
        max_length=16)
    card_cvc = models.CharField(
        max_length=3)
    card_expire_month = models.CharField(
        max_length=2)
    card_expire_year = models.CharField(
        max_length=4)

    send_receipt = MultiSelectField(
        choices=(
            ('C', 'Cell Phone'),
            ('E', 'E-mail')
        ),
        blank=True, null=True
    )

    reserved_date = models.DateTimeField(
        default=timezone.now)
    modified_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return str(self.id)


class RoomReservationInfo(models.Model):
    reservation = models.ForeignKey('Reservation', on_delete=models.CASCADE)
    room = models.ForeignKey('rooms.Room', on_delete=models.CASCADE)
    n_room = models.PositiveSmallIntegerField()


class Coupon(models.Model):
    image = models.ImageField()
    discount = models.PositiveSmallIntegerField()

    def __str__(self):
        return "%d%% Discount" % self.discount
