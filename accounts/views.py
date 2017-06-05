from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required

from .models import User
from .forms import UserRegistrationForm, UserLoginForm, UserModificationForm
from reservations.forms import ReservationModificationForm, ReservationCancelationForm


def register(request, register_form=UserRegistrationForm):
    if request.method == 'POST':
        form = register_form(request.POST)
        if form.is_valid():
            if not User.objects.filter(email=form.cleaned_data['email']).exists():
                form.save()

                user = auth.authenticate(email=request.POST.get('email'),
                                         password=request.POST.get('password1'))

                if user:
                    messages.success(request, "You have successfully registered")
                    return redirect(reverse('login'))

                else:
                    messages.error(request, "unable to log you in at this time!")
            else:
                form.add_error(None, "Your email is already taken!")

    else:
        form = register_form()

    args = {'form': form}
    args.update(csrf(request))

    return render(request, 'accounts/register.html', args)


def login(request, success_url=None):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'),
                                    password=request.POST.get('password'))

            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                if success_url:
                    return redirect(reverse(success_url))
                else:
                    if user.is_superuser == True:
                        return redirect('/admin/')
                    else:
                        return redirect('/')
            else:
                form.add_error(None, "Your email or password was not recognised")

    else:
        form = UserLoginForm()

    args = {'form':form}
    args.update(csrf(request))
    return render(request, 'accounts/login.html', args)


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('main'))


@login_required
def mypage(request):
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


@login_required
def modify_info(request):
    form = UserModificationForm(request.POST)
    if form.is_valid():
        user = auth.authenticate(email=form.data['email'],
                                 password=form.data['old_password'])
        if user is not None:
            print("password valid")
            if form.data['password1']:
                user.set_password(form.data['password1'])
            user.first_name = form.data['first_name']
            user.last_name = form.data['last_name']
            user.phone_number = form.data['phone_number']
            user.save()

            return redirect(reverse('mypage'))
        else:
            print("password is not valid")
            form.add_error(None, "You entered wrong password!")

    reservation_modification_form = ReservationModificationForm()
    reservation_cancelation_form = ReservationCancelationForm()
    args = {
        'reservation_modification_form': reservation_modification_form,
        'user_modification_form': form,
        'reservation_cancelation_form': reservation_cancelation_form,
    }
    args.update(csrf(request))
    return render(request, 'accounts/mypage.html', args)
