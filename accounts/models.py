from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone


class AccountUserManager(UserManager):
    def _create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given username must be set')

        email = self.normalize_email(email)

        user = self.model(username=email, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          date_joined=now, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractUser):
    # now that we've abstracted this class we can add any
    # number of custom attribute to our user class

    # in later units we'll be adding things like payment details!
    coupons = models.ManyToManyField('reservations.Coupon', blank=True)

    phone_regex = RegexValidator(regex=r'^\d{3}-\d{3,4}-\d{4}$',
                                 message="Phone number must be entered in the format: '010-1010-1010'. Up to 11 digits allowed.")
    phone_number = models.TextField(validators=[phone_regex])

    objects = AccountUserManager()