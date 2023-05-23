from django.urls import path
from authentication import views

urlpatterns = [
    path("login/", views.login_page),
    path("login/submit", views.submit_login),
    path("logout", views.logout_user)
]
