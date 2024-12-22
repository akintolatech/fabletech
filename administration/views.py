from django.http import JsonResponse
from django.shortcuts import render
from orders.models import Order
from shop.models import Product
from account.models import Profile



# Create your views here.
def administration_dashboard(request):
    total_orders = Order.objects.all()
    products = Product.objects.all()
    total_profiles = Profile.objects.all()
    context = {
        "total_orders": total_orders.count(),
        "total_products": products.count(),
        "total_profiles": total_profiles.count(),
        "products": products
    }
    return render( request, "administration/administration_dashboard.html", context)


def fetch_orders(request):
    total_orders = Order.objects.all()

    # Data for all logs
    total_orders_data = [
        {"counter": idx + 1, "details": order.email, "created": order.created.strftime('%Y-%m-%d %H:%M:%S')}
        for idx, order in enumerate(total_orders)
    ]

    return JsonResponse(
        {
            # "recent_logs": recent_log_data,
            "all_orders": total_orders_data
        },
        safe=False
    )
