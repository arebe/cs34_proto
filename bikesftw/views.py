from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Bike

# Create your views here.

def bike_disp(request):
	bikes = Bike.objects.all().order_by('date_created')
	return render(request, 'bikesftw/bike_disp.html', {'bikes': bikes})

def bike_edit(request):
	bikes = Bike.objects.all().order_by('date_created')
	return render(request, 'bikesftw/bike_disp.html', {'bikes': bikes})

