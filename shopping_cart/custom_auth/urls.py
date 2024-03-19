from django.urls import path
from custom_auth.views import LoginView, LogoutView, RegisterView


urlpatterns = [
    path('user/login/', LoginView.as_view()),
    path('user/register/', RegisterView.as_view()),
    path('user/logout/', LogoutView.as_view()),
]
