"""
ASGI config for niwera project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import niwera_rpg.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'niwera.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(niwera_rpg.routing.websocket_urlpatterns)
})
