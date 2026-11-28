from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_produtos, name="lista_produtos"),
    path("pedido/", views.fazer_pedido, name="fazer_pedido"),
    path("pedido/sucesso/", views.pedido_sucesso, name="pedido_sucesso"),
]
