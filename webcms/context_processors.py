# webcms/context_processors.py
from .models import WebDetails


def web_details(request):
    # Fetch the first WebDetails object (you can customize the query if necessary)
    details = WebDetails.objects.first()
    return {
        'business': details  # Passing the whole object to access all fields in the template
    }