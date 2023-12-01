from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.views.generic import ListView,CreateView
from django.utils.datastructures import MultiValueDictKeyError
from django.urls import reverse, reverse_lazy
from .forms import SignupForm,SigninForm,BookingForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from reg.models import Booking, review
def about(request):
    return render(request,'about.html')
def ap(request):
    return render(request,'AP.html')
def home(request):
    context={ 'name':'navin'}
    return render(request,'home.html',context)
def ka(request):
    return render(request,'KA.html')
def kl(request):
    return render(request,'KL.html')
def place(request):
    return render(request,'place.html')
def tn(request):
    return render(request,'TN.html')
class show(ListView):
    model=review
@method_decorator(login_required(login_url='signin'), name='dispatch')
class add(CreateView):
    model=review
    fields=('username','feedback','rating','place')
    success_url=reverse_lazy('show')
    
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if password == confirm_password:
                # Create user
                user = User.objects.create_user(username=username, email=email, password=password)
                # Log in the user
                login(request, user)
                return redirect('signin')  # Replace 'home' with the URL name of your home page
            else:
                form.add_error('confirm_password', 'Passwords do not match.')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

def signin_view(request):
    error_message = None 
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                error_message = 'Invalid username or password.'
                form.add_error(None, error_message)
    else:
        form = SigninForm()

    return render(request, 'login.html', {'form': form, 'error_message': error_message})
def logout_view(request):
    logout(request)
    return redirect('home') 
@login_required(login_url='signin')
def book_slot(request):
    if request.method == 'POST':
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booked_slots')
    else:
        booking_form = BookingForm()

    return render(request, 'book_slot.html', {'booking_form': booking_form})

@login_required(login_url='signin')
def booked_slots(request):
    user_bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booked_slots.html', {'user_bookings': user_bookings, 'user': request.user})