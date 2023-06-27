from django.shortcuts import render, HttpResponse
from datetime Import datetime
from home.models import Contact
# Create your views here.


def index(request):
    context = {
        "variable1": "I am one",
        "variable2": "I am two"
    }  
    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage")


def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is about page")


def services(request):
    return render(request, 'services.html')
    # return HttpResponse("this is services page")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        continue = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        
        
    return render(request, 'contact.html')
    # return HttpResponse("this is contact page")


def icecream(request):
    return render(request, 'services.html')
    # return HttpResponse("this is IceCream page")
