from django.shortcuts import render, redirect
from .models import Produto
from .forms import PedidoForm


def lista_produtos(request):
    produtos = Produto.objects.filter(disponivel=True)
    return render(request, "loja/lista_produtos.html", {"produtos": produtos})


def fazer_pedido(request):
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pedido_sucesso")
    else:
        form = PedidoForm()
    return render(request, "loja/pedido_form.html", {"form": form})


def pedido_sucesso(request):
    return render(request, "loja/pedido_sucesso.html")
