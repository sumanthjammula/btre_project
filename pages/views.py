from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, state_choices
# Create your views here.

from listings.models import Listing
from realtors.models import Realtor


def hello(request):
    return HttpResponse("Hello World")

def about(request):
    realtors = Realtor.objects.all().order_by('-hire_date')
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors':realtors,
        'mvp_realtors':mvp_realtors,
        
    }    
    return render(request, 'pages/about.html', context)


def index(request):
    listings = Listing.objects.all().order_by('-list_date').filter(is_published = True)[:3]
    context = {
               'listings': listings,
               'state_choices': state_choices,
               'bedroom_choices': bedroom_choices,
               'price_choices': price_choices ,            
               }
    return render(request, 'pages/index.html', context)