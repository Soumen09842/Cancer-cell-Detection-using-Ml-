from django.shortcuts import render
from django.http import HttpResponse

from joblib import load

model=load("hd.joblib")

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def analysis(request):
    return render(request, "analysis.html")

def team(request):
    return render(request, "team.html")

def contact(request):
    return render(request, "contact.html")


def pred(request):
    mean_radius=float(request.POST['mean_radius'])
    mean_texture=float(request.POST['mean_texture'])

    inp=[[mean_radius,mean_texture]]
    yp=model.predict(inp)

    return HttpResponse (yp)

