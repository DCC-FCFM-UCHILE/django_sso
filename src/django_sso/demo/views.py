from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def index(request):
    return render(request, "demo/authorized.html")


def unauthorized(request):
    return render(request, "demo/unauthorized.html")
