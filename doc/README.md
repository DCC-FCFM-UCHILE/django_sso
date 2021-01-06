# Documentación

Este proyecto es un ejemplo de cómo integrar la autenticación del **`portal`** en un proyecto basado en Framework Django.

El flujo de autenticación para las aplicaciones que utilicen esta integración es el siguiente:

```mermaid
sequenceDiagram

Usuario->>Aplicación: ingresa a una aplicación

activate Aplicación
Aplicación->>Aplicación: revisa sesión
Aplicación->>Portal: redirige al Portal, identifica aplicación
deactivate Aplicación

Portal->>Upasaporte: redirige browser, identifica externo
Upasaporte->>Usuario: solicita credenciales Pasaporte Uchile
Usuario->>Upasaporte: ingresa credenciales, hace clic en Ingresar

activate Upasaporte
Upasaporte->>Upasaporte: valida credenciales del usuario
deactivate Upasaporte

alt error credenciales
    Upasaporte->>Usuario: informa error en autenticación
end

Upasaporte->>Portal: ticket

activate Portal
Portal->>Portal: obtiene información del ticket
deactivate Portal

Portal->>Aplicación: redirige browser

activate Aplicación
Aplicación->>Aplicación: autoriza, inicia sesión
deactivate Aplicación

Aplicación->>Usuario: despliega aplicación
```

## Otros

- La documentación oficial del Portal: <https://github.com/DCC-FCFM-UCHILE/portal/tree/develop/doc>
- Diagramas de Secuencia: <https://mermaid-js.github.io/mermaid/#/sequenceDiagram>
- Actualmente GitHub no soporta el renderizado de mermaid, pero existe esta extensión: <https://github.com/BackMarket/github-mermaid-extension#install> (Chrome, Firefox, Opera)