from django.shortcuts import render
from .models import WebDetails
from shop.models import Product
from cart.forms import CartAddProductForm

# Create your views here.
def index(request):
    products = Product.objects.filter(available=True)[:4]
    cart_product_form = CartAddProductForm(request.POST)
    business = WebDetails.objects.get(id=1)
    context = {
        "cart_product_form": cart_product_form,
        "business": business,
        'products': products,
    }
    return render(request, "webcms/pages/index.html", context)


def shop(request):
    business = WebDetails.objects.get(id=1)
    context = {
        "business": business,

    }
    return render(request, "webcms/pages/shop.html", context)


def about(request):
    business = WebDetails.objects.get(id=1)

    context = {
        "business": business
    }
    return render(request, "webcms/pages/about.html", context)
