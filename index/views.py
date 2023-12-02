from django.shortcuts import render
from django.http import HttpResponse
from index.models import Brand, Smartphone

def index(request):
    heading = "Главная страница"
    all_brands = Brand.objects.all()
    all_smartphones = Smartphone.objects.all()

    data = {
        "heading": heading,
        "brands" : all_brands, 
        "smartphones": all_smartphones
        }

    return render(request, "index.html", context=data)

def appl(request):

    applesm = Smartphone.objects.filter(brandId=1)

    data = {"applesm": applesm}
    return render(request, "apple.html", context=data)


def aboutPage(request):
    return HttpResponse("Hello")