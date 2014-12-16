from django.shortcuts import render
from .models import Bike

# Create your views here.

def bike_disp(request):
	bikes = Bike.objects.all().order_by('date_created')
	return render(request, 'bikesftw/bike_disp.html', {'bikes': bikes})
