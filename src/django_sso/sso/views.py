from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import login as custom_login
from django.contrib.auth import logout as custom_logout
from django.conf import settings

from urllib.parse import urlencode
from urllib.request import urlopen
import json


def index(request):
    if request.user.is_authenticated:
        return HttpResponse("Usuario Atenticado!")
    return redirect(f"{settings.SSO_URL}/&externo={settings.SSO_EXTERNO}")


def login(request):
    if not request.GET["username"] or not request.GET["secret"]:
        print("*** error username o secret")
        return redirect("sso/index")

    username = request.GET["username"]
    secret = request.GET["secret"]

    if user_exists(username):
        user = User.objects.get(username=username)
    else:
        return HttpResponse("Ha sido autenticado, pero no tiene acceso a esta App.")
        print(f"*** error user no encontrado: username={username}")

    if is_valid(username, secret):
        custom_login(request, user)
        return HttpResponse("Ha sido autenticado y tiene acceso a esta App.")

    return redirect("sso/index")


def logout(request):
    custom_logout(request)
    return redirect("sso/index")


def is_valid(username, secret):
    params = {"externo": settings.SSO_EXTERNO, "secret": secret, "username": username}
    data = urlopen(f"{settings.SSO_URL}/is_valid?{urlencode(params)}").read()
    if data:
        data = json.loads(data)
        return data["valid"]
    return False


def user_exists(username):
    if User.objects.filter(username=username):
        return True
    return False
