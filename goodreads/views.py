from django.http import HttpResponse

def landing_page(request):
    return HttpResponse(f"<h1> DJANGO IS WORKING</h1>")