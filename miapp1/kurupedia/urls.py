from django.contrib import admin
from django.urls import path, include
from kurupedia import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.logedHome, name='home'),
    path('admin/', admin.site.urls),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
