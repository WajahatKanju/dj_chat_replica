from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rooms/', include('room.urls')),
    path('', include('chat.urls'))
]
