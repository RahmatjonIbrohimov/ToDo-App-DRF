from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('todo.urls')),
    path('admin/', admin.site.urls),
]
