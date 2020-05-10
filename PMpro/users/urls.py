from django.urls import path
from .views import signup_view, user_login, user_logout

urlpatterns = [

    path('signup/', signup_view, name="signup"),
    path('accounts/login/', user_login, name="login"),
    path('accounts/logout/', user_logout, name="logout"),


]