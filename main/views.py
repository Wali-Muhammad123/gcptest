from django.shortcuts import render
from .models import Subscribe
from django.http import JsonResponse, HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

def subscribe(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        # Do something with the name and email, e.g. save to database
        subscription=Subscribe.objects.create(name=name,email=email)
        subscription.save()
        return JsonResponse({"message": "Subscribed successfully."})
    return JsonResponse({"error": "Invalid request method."})

def buygold(request):
    return render(request,'buygold.html')
def invest(request):
    #extract cookie from the request
    #set the default value of investment to 0
    cookie=request.GET.get('invest')
        #set a cookie with the name invest and value 0
    if cookie is None:
        cookie=0
    response=HttpResponse(request,'invest.html',status=200)
    response.set_cookie('invest',cookie)
    return response