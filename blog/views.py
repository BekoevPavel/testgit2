from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponseRedirect


def index(request):
    return render(request, "blog/index.html")
