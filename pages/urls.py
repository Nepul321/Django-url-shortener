from .views import (
    HomeView,
    RedirectView,
    CreateURLView
)
from django.urls import path

urlpatterns = [
    path('', HomeView, name="home"),
    path('create/', CreateURLView, name="create"),
    path('<str:pk>/', RedirectView, name="url-redirect")
]
