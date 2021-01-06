# SSO/DCC para Proyectos Django

## Descripción

## Características

El App SSO provee un segundo mecanismo de autenticación para su proyecto. Funciona en ambientes de desarrollo que expongan de forma pública el endpoint `https://<url||ip>/sso/login`, el cual es utilizado para comunicarse con el **Portal DCC**.

## Integración

Para integrar esta App en proyecto debe:

- Solicitar al Área de Desarrollo de Aplicaciones <**desarrollo@dcc.uchile.cl**> la creación de su externo indicando:

```dotenv
Externo: (nombre del externo)
Descripción: (descripción corta de la aplicación, será mostrada a los usuarios en el portal)
Endpoint: https://<url o ip>/sso/login
Responsable: (nombre de la persona responsable del proyecto)
Email: (debe proveer un correo @dcc.uchile.cl)
Ambiente: (desarrollo, producción o testing)
```

- [Clonar](https://github.com/DCC-FCFM-UCHILE/django_sso/tree/main) la última versión de la rama main este repositorio
- Crear un link simbólico en su directorio de _apps_ al directorio `_django_sso/src/django_sso/sso_` (este link simbólico no debería ser versionado; se recomienda agregarlo al archivo _.gitignore_)
- Agregar la app en *INSTALLED_APPS* en el archivo _settings.py_

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

- Incluir las siguientes configuraciones en el archivo _settings.py_, reemplazando "externo" por el identificador de su externo

```python
# settings.py (proyecto)
SSO_EXTERNO = "identificador_del_externo"
SSO_URL = "https://w3.dcc.uchile.cl/portal"
LOGIN_URL = "sso:index"
```

- Configurar archivo _urls.py_ para agregar rutas del sso

```python
# urls.py (proyecto)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("sso/", include("sso.urls")),
]
```
