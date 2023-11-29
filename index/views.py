from django.shortcuts import render
from index.models import Brand, Smartphone

def index(request):

    all_brands = Brand.objects.all()
    all_smartphones = Smartphone.objects.all()

    data = {"brands" : all_brands, "smartphones": all_smartphones}

    return render(request, "index.html", context=data)

def appl(request):

    applesm = Smartphone.objects.filter(brandId=1)

    data = {"applesm": applesm}
    return render(request, "apple.html", context=data)