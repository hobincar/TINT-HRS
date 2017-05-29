from django import forms

from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['check_in', 'check_out', 'n_adult', 'n_child', 'n_breakfast', 'n_baby_bed', 'addendum',
                  'card_type', 'card_number', 'card_cvc', 'card_expire_month', 'card_expire_year']
        exclude = ('customer', 'staff', 'rooms', 'coupon', 'send_receipt' 'reserved_date', 'modified_date')