# accounts/urls.py

from django.urls import path
from .views import register, home, login_view, logout_view, stream

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('stream/', stream, name='stream'),  # Маршрут для стриминга
]