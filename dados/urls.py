from django.urls import path
from . import views

urlpatterns = [
    path(
        "dados/",views.DadosView.as_view(),

    )
]