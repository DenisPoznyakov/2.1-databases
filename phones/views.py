from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


# def show_catalog(request):
#     template = 'catalog.html'
#     context = {'phones': Phone.objects.all()}
#     return render(request, template, context)


def show_catalog(request):
    template = 'catalog.html'
    sort_pages = request.GET.get("sort")
    phone_instanse = Phone.objects.all()
    if sort_pages == "name":
        phone_instanse = Phone.objects.order_by("name")
    elif sort_pages == "max_price":
        phone_instanse = Phone.objects.order_by("price").reverse()
    elif sort_pages == "min_price":
        phone_instanse = Phone.objects.order_by("price")
    context = {"phones": phone_instanse}
    return render(request, template, context=context)

# def sort_name(request):
#     template = 'catalog.html'
#     context = {'phones': Phone.objects.order_by('name')}
#     return render(request, template, context)
#
# def sort_min_price(request):
#     template = 'catalog.html'
#     context = {'phones': Phone.objects.order_by('price')}
#     return render(request, template, context)
#
# def sort_max_price(request):
#     template = 'catalog.html'
#     context = {'phone': Phone.objects.order_by('price').reverse()}
#     return render(request, template, context)

# def show_product(request, slug):
#     template = 'product.html'
#     context = {'phone': Phone.objects.get(price='price', release_date='release_date', lte_exists='lte_exists')}
#     return render(request, template, context)

def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context=context)