from django.urls import path
from . import views

urlpatterns = [
    path("dados/",views.DadosView.as_view()),
    path("dados/list/",views.ListDados.as_view()),
]