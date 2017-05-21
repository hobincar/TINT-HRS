from django.db import models
from django.utils import timezone


class Room(models.Model):
    creator = models.ForeignKey('accounts.User', limit_choices_to={'is_staff': True})
    type = models.CharField(
        max_length=2,
        choices=(
            ('SG', 'Single Room'),
            ('DB', 'Double Room'),
            ('TW', 'Twin Room'),
            ('ST', 'Suite Room'),
            ('DX', 'Deluxe Room'),
            ('PR', 'Premier Room'),
            ('FM', 'Family Room'),
        )
    )
    description = models.TextField()
    feature1 = models.CharField(
        max_length=100,
        blank=True)
    feature2 = models.CharField(
        max_length=100,
        blank=True)
    feature3 = models.CharField(
        max_length=100,
        blank=True)
    f_promotion = models.BooleanField(
        default=False)
    f_recommendation = models.BooleanField(
        default=False)
    image = models.ImageField()
    capacity = models.PositiveSmallIntegerField()
    cost_per_day = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0)
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return "%s_%d_%s" % (self.type, self.capacity, self.creator)