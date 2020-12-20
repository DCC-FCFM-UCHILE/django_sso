from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as custom_login
from django.contrib.auth import logout as custom_logout
from django.conf import settings
from django.contrib import messages


from urllib.parse import urlencode
from urllib.request import urlopen
import json


def index(request):
    if request.user.is_authenticated:
        next_url = "/"
        if request.session["next"]:
            next_url = request.session["next"]
            del request.session["next"]
        return redirect(next_url)

    request.session["next"] = request.GET.get("next", "")
    return redirect(f"{settings.SSO_URL}?externo={settings.SSO_EXTERNO}")


def login(request):
    if not request.GET["username"] or not request.GET["secret"]:
        messages.error(request, "No se pudo validar su sesión.")
        return redirect("index")

    username = request.GET["username"]
    secret = request.GET["secret"]

    if user_exists(username):
        user = User.objects.get(username=username)
    else:
        messages.error(request, "Ha sido autenticado, pero no tiene acceso a esta App.")
        return redirect(settings.UNAUTHORIZED_URL)

    if is_valid(username, secret):
        custom_login(request, user)
        return redirect(settings.AUTHORIZED_URL)

    return redirect("index")


def logout(request):
    custom_logout(request)
    return redirect("index")


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
