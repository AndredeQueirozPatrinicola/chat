from django.urls import path
from authentication import views

urlpatterns = [
    path("login/", views.Login.as_view(), name='login-get'),
    path("login/submit", views.Login.as_view(), name='login-post'),
    path("logout", views.LogOut.as_view(), name='logout'),
    path("signup", views.SignUp.as_view(), name='signup-get'),
    path("signup/submit", views.SignUp.as_view(), name='signup-post')
]
