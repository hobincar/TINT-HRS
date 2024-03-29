from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from django.utils import timezone

from .models import Reservation, RoomReservationInfo
from memberships.models import Coupon
from accounts.models import User
from rooms.models import Room
from .forms import ReservationForm, ReservationModificationForm, ReservationCancelationForm
from accounts.forms import UserRegistrationForm


@login_required(redirect_field_name='reserve')
def reserve(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)

            # CUSTOMER
            reservation.customer = User.objects.get(id=request.user.id)
            
            reservation.total_cost = 0
            reservation.save()
            try:
                # ROOM
                n_room_list = request.POST.getlist('n_room')
                room_id_list = request.POST.getlist('room_id')
                room_cost = 0
                for n_room, room_id in zip(n_room_list, room_id_list):
                    if n_room and int(n_room) > 0:
                        room = Room.objects.get(id=room_id)
                        r = RoomReservationInfo.objects.create(
                            reservation=reservation,
                            room=room,
                            n_room=n_room
                        )
                        r.save()

                        room_cost += int(n_room) * float(room.cost_per_night)

                total_cost = room_cost + 16.50*float(form.cleaned_data['n_breakfast']) + 10.00*float(form.cleaned_data['n_baby_bed'])

                # COUPON
                coupon_id = form.data['coupon']
                if coupon_id:
                    coupon = Coupon.objects.get(id=coupon_id)
                    reservation.coupon = coupon
                    reservation.customer.coupons.remove(coupon)
                    total_cost = total_cost / 100 * (100-coupon.discount)
                reservation.total_cost = total_cost

                # SEND_RECEIPT
                if 'b_send_receipt' in form.data and form.data['b_send_receipt'] == "on":
                    send_receipt = form.data['send_receipt']
                    reservation.send_receipt = ''
                    if "phone" in send_receipt.lower():
                        reservation.send_receipt += 'C,'
                    if "mail" in send_receipt.lower():
                        reservation.send_receipt += 'E,'

                # RESERVED/MODIFIED DATE
                reservation.reserved_date = timezone.now()
                reservation.modified_date = timezone.now()

                reservation.save()

                return redirect(reverse('mypage'))
            except:
                reservation.delete()
                redirect(reverse('main'))
        else:
            messages.error(request, "reservation form is not valid")
    else:
        if request.GET.items():
            form = ReservationForm(request.GET)
        else:
            form = ReservationForm()
        coupon_id = request.GET.get('coupon', '')

    rooms = Room.objects.order_by('cost_per_night')
    args = {'form': form, 'rooms': rooms, 'coupon_id': coupon_id}
    args.update(csrf(request))

    return render(request, 'reservations/reservation.html', args)


@login_required
def modify(request):
    form = ReservationModificationForm(request.POST)
    if form.is_valid():
        reservation = Reservation.objects.get(id=form.data['reservation_id'])

        # REESTIMATE TOTAL COST
        n_breakfast = int(form.cleaned_data['n_breakfast'])
        n_baby_bed = int(form.cleaned_data['n_baby_bed'])
        if reservation.coupon:
            reservation.total_cost = reservation.total_cost * 100 / reservation.coupon.discount
        reservation.total_cost += 16.50*(n_breakfast-reservation.n_breakfast) + 10.00*(n_baby_bed-reservation.n_baby_bed)
        if form.cleaned_data['coupon_id']:
            coupon_id = form.data['coupon_id']
            coupon = Coupon.objects.get(id=coupon_id)
            reservation.coupon = coupon
            reservation.customer.coupons.remove(coupon)
            reservation.total_cost = reservation.total_cost / 100 * (100 - coupon.discount)

        reservation.check_in = form.cleaned_data['check_in']
        reservation.check_out = form.cleaned_data['check_out']
        reservation.n_breakfast = n_breakfast
        reservation.n_baby_bed = n_baby_bed
        reservation.n_adult = form.cleaned_data['n_adult']
        reservation.n_child = form.cleaned_data['n_child']
        reservation.addendum = form.cleaned_data['addendum']
        reservation.save()

    else:
        print("modify: form is not valid")

    form = ReservationModificationForm()
    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'accounts/mypage.html', args)


@login_required
def cancel(request):
    form = ReservationCancelationForm(request.POST)
    if form.is_valid():
        reservation = Reservation.objects.get(id=form.data['reservation_id'])
        if reservation.customer == request.user:
            reservation.delete()

    reservation_modification_form = ReservationModificationForm()
    registration_form = UserRegistrationForm()
    reservation_cancelation_form = ReservationCancelationForm()
    args = {
        'reservation_modification_form': reservation_modification_form,
        'user_modification_form': registration_form,
        'reservation_cancelation_form': reservation_cancelation_form,
    }
    args.update(csrf(request))
    return render(request, 'accounts/mypage.html', args)