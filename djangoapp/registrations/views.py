from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Welcome to the Registrations App</h1>")
