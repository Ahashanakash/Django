from django.shortcuts import render
from car.models import Car
from brand.models import Brand
def home(request, category_slug = None):
    data = Car.objects.all()
    if category_slug is not None:
        category = Brand.objects.get(slug = category_slug)
        data = Car.objects.filter(brand = category)
    categories = Brand.objects.all()
    return render(request,'home.html',{'data':data, 'category':categories})