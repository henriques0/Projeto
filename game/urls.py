from django.urls import path
from .views import *

urlpatterns = [
    path('', PaginaInicialView.as_view(), name="index"),
    path('projeto/', PaginaProjetoView.as_view(), name="projeto"),
    path('contato/', PaginaContatoView.as_view(), name="contato"),
    path('curriculo/', PaginaCurriculoView.as_view(), name="curriculo"),
    path('sobre/', PaginaSobreView.as_view(), name="sobre"),
    path('login/', PaginaLoginView.as_view(), name="login"),
    path('registrar/', PaginaLoginView.as_view(), name="registar"),

    #URLS DE CADASTROS
    path('cadastrar/estado/', EstadoCreate.as_view(), name="cadastrar-estado"),
    path('editar/estado/<int:pk>/', EstadoUpdate.as_view(), name="editar-estado"),
    path('cadastrar/cidade/', CidadeCreate.as_view(), name="cadastrar-cidade"),
    path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name="editar-cidade"),
    path('cadastrar/jogo/', JogoCreate.as_view(), name="cadastrar-jogo"),
    path('editar/jogo/<int:pk>/', JogoUpdate.as_view(), name="editar-jogo"),
    path('excluir/jogo/<int:pk>/', JogoDelete.as_view(), name="excluir-jogo"),
    path('cadastrar/plataforma/', PlataformaCreate.as_view(), name="cadastrar-plataforma"),
    path('editar/plataforma/<int:pk>/', PlataformaUpdate.as_view(), name="editar-plataforma"),
    path('excluir/plataforma/<int:pk>/', PlataformaDelete.as_view(), name="excluir-plataforma"),
    path('excluir/estado/<int:pk>/', EstadoDelete.as_view(), name="excluir-estado"),
    path('excluir/cidade/<int:pk>/', CidadeDelete.as_view(), name="excluir-cidade"),
    path('listar/estados', EstadoList.as_view(), name="listar-estados"),
    path('listar/jogos', JogoList.as_view(), name="listar-jogos"),
    path('listar/plataformas', PlataformaList.as_view(), name="listar-plataformas"),
    path('detalhe/jogo/<int:pk>/', JogoDetalhe.as_view(), name="detalhar-jogo"),
    path('detalhe/plataforma/<int:pk>/', PlataformaDetalhe.as_view(), name="detalhar-plataforma"),
    

]
