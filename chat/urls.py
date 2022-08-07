# mysite/urls.py
from django.contrib import admin
from django.urls import include, path
from register import views as v
urlpatterns = [
    path('chat/', include('chatapp.urls')),
    path('admin/', admin.site.urls),
    path('register/', v.register, name="register"),
    path('', include('django.contrib.auth.urls')),
]   