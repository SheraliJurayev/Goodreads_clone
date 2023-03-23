from django.http import HttpResponse

def landing_page(request):
    return HttpResponse(f"Django is working {request.META['HTTP_USER_AGENT']}")