from django.shortcuts import render
from .models import WebDetails, Testimonial
from shop.models import Product
from cart.forms import CartAddProductForm


# Create your views here.
def index(request):
    products = Product.objects.filter(available=True)[:8]
    new_products = Product.objects.filter(available=True)[:3]
    cart_product_form = CartAddProductForm(request.POST)
    business = WebDetails.objects.get(id=1)
    testimonials = Testimonial.objects.all()
    context = {
        "cart_product_form": cart_product_form,
        "business": business,
        'products': products,
        "testimonials": testimonials,
        "new_products": new_products
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
