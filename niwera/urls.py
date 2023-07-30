from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('niwera_rpg.urls')),
    path('stories/', include('niwera_rpg.urls'))
]
