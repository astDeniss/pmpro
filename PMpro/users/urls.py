from django.urls import path
from .views import signup_view, user_login

urlpatterns = [

    path('signup/', signup_view, name="signup"),
    path('accounts/login/', user_login, name="login"),


]