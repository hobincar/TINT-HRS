from django import forms

from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['check_in', 'check_out', 'n_adult', 'n_child', 'n_breakfast', 'n_baby_bed', 'addendum',
                  'card_type', 'card_number', 'card_cvc', 'card_expire_month', 'card_expire_year']
        exclude = ('customer', 'staff', 'rooms', 'coupon', 'send_receipt' 'reserved_date', 'modified_date')


class ReservationModificationForm(forms.Form):
    check_in = forms.DateField()
    check_out = forms.DateField()
    n_adult = forms.IntegerField()
    n_child = forms.IntegerField()
    coupon_id = forms.IntegerField(required=False)
    n_breakfast = forms.IntegerField()
    n_baby_bed = forms.IntegerField()
    addendum = forms.CharField(widget=forms.Textarea, required=False)


class ReservationCancelationForm(forms.Form):
    reservation_id = forms.TextInput()