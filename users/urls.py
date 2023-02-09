from django.urls import path
from . import views

urlpatterns = [
    path('authorization/', views.AuthorizationsAPIView.as_view()),
    path('registration/', views.RegistrationAPIView.as_view())
]
