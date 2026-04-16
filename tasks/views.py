from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Trip
from .forms import TripForm
from django.contrib.auth.models import User

def trip_list(request):
    query = request.GET.get('q')
    if query:
        trips = Trip.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    else:
        trips = Trip.objects.all()

    return render(request, 'trip_list.html', {'trips': trips})


def trip_detail(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    return render(request, 'trip_details.html', {'trip': trip})


def trip_create(request):
    if request.method == "POST":
        form = TripForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            if request.user.is_authenticated:
                trip.user = request.user
            else:
                user = User.objects.first()
                if not user:
                    user = User.objects.create(username="default_user")
                trip.user = user
                
            trip.save()
            return redirect('trip_list')
    else:
        form = TripForm()
    return render(request, 'trip_form.html', {'form': form})

def trip_update(request, pk):
    trip = get_object_or_404(Trip, pk=pk)

    if request.method == "POST":
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():
            form.save()
            return redirect('trip_detail', pk=trip.pk)
    else:
        form = TripForm(instance=trip)

    return render(request, 'trip_form.html', {'form': form})


def trip_delete(request, pk):
    trip = get_object_or_404(Trip, pk=pk)

    if request.method == "POST":
        trip.delete()
        return redirect('trip_list')

    return render(request, 'trip_confirm_delete.html', {'trip': trip})

def profile_view(request):
    if request.user.is_authenticated:
        current_user = request.user
        trips = Trip.objects.filter(user=current_user)
    else:
        current_user = User.objects.first()
        if not current_user:
            current_user = User.objects.create(username="default_user")
        trips = Trip.objects.filter(user=current_user)
        
    return render(request, 'profile.html', {'trips': trips, 'current_user': current_user})