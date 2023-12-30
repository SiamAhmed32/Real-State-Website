from django.shortcuts import render, redirect, HttpResponse
from listings.models import Listings
# Create your views here.
from listings.forms import ListingsForm
def listings_list(request):
    listings = Listings.objects.all()
    context = {
        'listings' : listings
    }
    return render(request, 'listings/listing.html', context)

def listings_retrieve(request, pk):
    listing = Listings.objects.get(id = pk)
    context = {
        'listing' : listing
    }
    return render(request, 'listings/retrieve.html', context)

def listing_create(request):
    form = ListingsForm()
    if request.method == "POST":
        form = ListingsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "form": form
    }
    return render(request, "listings/listings_create.html", context)

def listing_update(request, pk):
    listing = Listings.objects.get(id = pk)
    form = ListingsForm(instance=listing)
    if request.method == "POST":
        form = ListingsForm(request.POST, instance=listing, files = request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "form": form
    }
    return render(request, "listings/listings_update.html", context)

def listing_delete(request, pk):
    listing = Listings.objects.get(id = pk)
    listing.delete()
    return redirect('/')