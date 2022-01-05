import json

from django.shortcuts import render
from web.models import Home, About, Project, Contact
from django.http.response import HttpResponse


def index(request):
    homes = Home.objects.get()
    abouts = About.objects.get()
    projects = Project.objects.all()

    context = {
        "homes" : homes,
        "abouts" : abouts,
        "projects" : projects,
    }

    return render(request, "index.html",context=context)


def contact(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    message = request.POST.get("message")

    if not Contact.objects.filter(email=email).exists():

        Contact.objects.create(
            name = name,
            email = email,
            message = message,
        )
        response_data = {
            "status" :"success",
            "message" : "I will contact you soon",
            "title" : "Thank you"
        }
    else:
        response_data = {
            "status" :"warning",
            "message" : "This email address is already being used",
            "title" : "Add another email address that you own"
        }

    return HttpResponse(json.dumps(response_data),content_type="application/javascript")