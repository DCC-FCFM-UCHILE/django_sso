# SSO/DCC para Proyectos Django

## Descripción

Este proyecto provee un ejemplo para las Apps basadas en Django para integrarse con el Portal DCC, aplicación que provee autenticación utilizando cuenta Mi Uchile mediante el uso de Upasaporte del Centro Ucampus.

## Características

El App **SSO** (`_django_sso/app/sso_`) en este proyecto provee un segundo mecanismo de autenticación para su proyecto. Funciona exponiendo el endpoint `https://<url||ip>/sso/login`, el cual es utilizado para comunicarse con el [**Portal DCC**](https://apps.dcc.uchile.cl/portal).

## Integración

Para integrar esta App en proyecto debe:

- Solicitar al Área de Desarrollo de Aplicaciones <**desarrollo@dcc.uchile.cl**> la creación de su app indicando:

```dotenv
Nombre: (nombre de la app)
Descripción: (descripción corta de la aplicación, será mostrada a los usuarios en el Portal)
Endpoint: https://<url o ip>/sso/login
Responsable: (nombre de la persona responsable del proyecto)
Email: (debe proveer un correo @*.uchile.cl)
Ambiente: (desarrollo, produccion, localhost)
```

Tiene varias opciones para utilizar la App SSO incluida en este proyecto:

- Puede crear una App basándose en el código de fuente de la misma.
- Puede copiar el código de la App a su proyecto.

No obstante, debido a que este es un proyecto que está en constante mejora se recomienda incluir este proyecto como un submodulo en su repositorio, asegurándose que siempre apunte a la última versión de la rama **main** y crear un link simbólico de la App SSO a su proyecto Django.

Si utiliza la App, como es provista, debe incluir las siguientes configuraciones en su proyecto Django:

```python
# settings.py (proyecto)
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "sso.apps.SsoConfig",
]
```

- Incluir las siguientes configuraciones en el archivo _settings.py_, reemplazando "identificador_app" por el identificador de su App.

```python
# settings.py (proyecto)

# DCC SSO
LOGIN_URL = "sso:index"
SSO_URL = "https://portal.dcc.uchile.cl/"
SSO_APP = <IDENTIFICADOR_APP>
SSO_AUTH = <True|False>
```

Si SSO_AUTH = True, la App se basará en el mecanismo de autorización provisto por el Portal para las Apps. Si desea controlar la autorización en su App, setee SSO_AUTH = False. 

- Configurar archivo _urls.py_ para agregar rutas del sso

```python
# urls.py (proyecto)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("sso/", include("sso.urls")),
]
```

## Consideraciones

Este proyecto se encuentra configurado con Docker para levantar un ambiente local de desarrollo. El portal es compatible para trabajar con Apps que funcionen en localhost, para más información contacte al Área de Desarrollo del DCC.


```ps
docker-compose up -d --build
docker-compose exec django python manage.py migrate
docker-compose exec django python manage.py createsuperuser
```

**NO SE RECOMIENDA UTILIZAR ESTE PROYECTO COMO BASE PARA CONSTRUIR SU APP.** Solicite documentación al Área de Desarrollo del DCC sobre como iniciar un nuevo proyecto Django que sea compatible con los ambientes de desarrollo y productivos del DCC.
