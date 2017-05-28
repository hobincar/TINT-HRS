import re
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from django.utils import timezone

from .models import RoomReservationInfo, Coupon
from .forms import ReservationForm
from rooms.models import Room
from accounts.models import User


@login_required
def reserve(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)

            # CUSTOMER
            reservation.customer = User.objects.get(id=request.user.id)

            # ROOM
            n_room_list = request.POST.getlist('n_room')
            room_id_list = request.POST.getlist('room_id')
            reservation.save()
            for n_room, room_id in zip(n_room_list, room_id_list):
                if n_room and int(n_room) > 0:
                    r = RoomReservationInfo.objects.create(
                        reservation=reservation,
                        room=Room.objects.get(id=room_id),
                        n_room=n_room
                    )
                    r.save()

            # COUPON
            coupon_id = form.data['coupon']
            if coupon_id:
                coupon = Coupon.objects.get(id=coupon_id)
                reservation.coupon = coupon
                reservation.customer.coupons.remove(coupon)

            # SEND_RECEIPT
            if form.data['b_send_receipt'] == "on":
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

            return redirect(reverse('main'))
        else:
            messages.error(request, "reservation form is not valid")
    else:
        form = ReservationForm()

    rooms = Room.objects.order_by('cost_per_night')
    args = {'form': form, 'rooms': rooms}
    args.update(csrf(request))

    return render(request, 'reservations/reservation.html', args)
