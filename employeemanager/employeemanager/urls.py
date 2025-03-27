
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_app.urls')), # Mount the app's routes at the root URL
    path('accounts/', include('django.contrib.auth.urls')),
]
