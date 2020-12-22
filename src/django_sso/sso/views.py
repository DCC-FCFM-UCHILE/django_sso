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
        if request.META['SCRIPT_NAME']:
            next_url = f"{request.META['SCRIPT_NAME']}/"

        if request.session["next"]:
            next_url += request.session["next"]
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
        return redirect("unauthorized")

    if is_valid(username, secret):
        custom_login(request, user)
        if request.META['SCRIPT_NAME']:
            return redirect(f"{request.META['SCRIPT_NAME']}/")
        return redirect("/")

    return redirect("index")


def unauthorized(request):
    return HttpResponse(unauthorized())


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


def unauthorized():
    return """
<!doctype html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
    <title>Portal Servicios DCC</title>
</head>
<style>
    body {background-color: #333; color: white;}
    .logo {width: 215px; height: 110px; margin: 50px;}
    .wrapper { position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%);}
</style>
<body>
<div class="wrapper">
    <center>
        <img class="logo" src="https://w3.dcc.uchile.cl/static/web_frontend/images/logo_dcc.png">
        <br />
        <div class="alert alert-danger" role="alert">
          Se ha autenticado correctamente pero no está autorizado para utilizar esta App.<br />
          Contacte al Área de Desarrollo de Aplicaciones 
          (<a href="mailto:desarrollo@dcc.uchile.cl">desarrollo@dcc.uchile.cl</a>) para solicitar acceso.
        </div>
    </center>
</div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW"
        crossorigin="anonymous"></script>
</body>
</html>    
"""
