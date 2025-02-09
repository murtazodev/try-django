from .views import login_view, logout_view, logged_out_view, register_view
from django.urls import path

urlpatterns = [
    path('login/', login_view, name='login-view'),
    path('logout/', logout_view, name='logout-view'),
    path('logged-out/', logged_out_view, name='logged-out'),
    path('register/', register_view, name='register-view'),
]