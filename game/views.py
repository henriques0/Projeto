from django.shortcuts import render
#IMPORTA TODAS AS CLASSES DO MODELS
from .models import *
#IMPORTA A FUNCAO QUE CHAMA AS URLS PELO "NAME" DELAS
from django.urls import reverse_lazy
#IMPORTA AS CLASSES VIEWS PARA INSERIR, ALTERAR E EXCLUIR UTILIZANDO FORMULARIOS
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#IMPORTA O TEMPLATEVIEW PARA A CRIACAO DE PAGINAS SIMPLES
from django.views.generic import TemplateView
# Importa o DetailView para ver detalhes de objetos
from django.views.generic.detail import DetailView
# Importa ListView para gerar as telas com tabelas
from django.views.generic.list import ListView
# Importa o Mixin para obrigar login
from django.contrib.auth.mixins import LoginRequiredMixin
# Biblioteca para controlar o acesso por grupo de usuário
from braces.views import GroupRequiredMixin
# Método que busca um objeto. Se não existir, da um erro 404
from django.shortcuts import get_object_or_404

# Create your views here.
class PaginaInicialView(TemplateView):
		template_name = "game/index.html"

class PaginaProjetoView(TemplateView):
		template_name = "game/projeto.html"

class PaginaContatoView(TemplateView):
		template_name = "game/contato.html"

class PaginaCurriculoView(TemplateView):
		template_name = "game/curriculo.html"

class PaginaSobreView(TemplateView):
		template_name = "game/sobre.html"

class PaginaLoginView(TemplateView):
		template_name = "usuarios/login.html"



######################################## 	INSERIR 	##########################################
class EstadoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
		group_required = u"Grupos"
		# DEFINE QUAL E O MODELO DA CLASSE, ESTA CRIA O FORM
		model = Estado
		#QUAL HTML SERA USADO
		template_name = "game/formulario.html"
		#PARA ONDE O USURAIO SERA REDERECIONADO APOS ISERIR UM REGISTRO, INFORME O NOME DA URL
		success_url = reverse_lazy("listar-estados")
		#QUAIS CAOMPOS DEVEM APARECER NO FORMULARIO
		fields = ['sigla', 'nome']

		#METODO PARA ENVIAR DADOS PARA O TEMPLATE
		def get_context_data(self, *args, **kwargs):
    		#CHAMAR O "PAI  PARA QUE SEMPRE TENHA O COMPORTAMANETO PADRAO
			context = super(EstadoCreate, self).get_context_data(*args, **kwargs)
			
			#ADICIONAR COISAS AS CONTEXTO QUE SERA ENVIADA pARA O HTML
			context['titulo'] = "CADASTRAR ESTADO"
			context['botao'] = "CADASTAR"
			context['classeBotao'] = "btn-primary"

			#DEVOLVE/ENVIA O ARQUIVO PARA O SEU COMPORTAMENTO
			return context

class CidadeCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
		group_required = u"Grupos"
		# DEFINE QUAL E O MODELO DA CLASSE, ESTA CRIA O FORM
		model = Cidade
		#QUAL HTML SERA USADO
		template_name = "game/formulario.html"
		#PARA ONDE O USURAIO SERA REDERECIONADO APOS ISERIR UM REGISTRO, INFORME O NOME DA URL
		success_url = reverse_lazy("index")
		#QUAIS CAOMPOS DEVEM APARECER NO FORMULARIO
		fields = ['nome', 'estado', 'descricao']

		def get_context_data(self, *args, **kwargs):
			context = super(CidadeCreate, self).get_context_data(*args, **kwargs)
			context['titulo'] = "CADASTRAR CIDADE"
			context['botao'] = "CADASTRAR"
			context['classeBotao'] = "btn-primary"
			return context

class JogoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
		group_required = u"Administrador"
		# DEFINE QUAL E O MODELO DA CLASSE, ESTA CRIA O FORM
		model = Jogo
		#QUAL HTML SERA USADO
		template_name = "game/formulario.html"
		#PARA ONDE O USURAIO SERA REDERECIONADO APOS ISERIR UM REGISTRO, INFORME O NOME DA URL
		success_url = reverse_lazy("listar-jogos")
		#QUAIS CAOMPOS DEVEM APARECER NO FORMULARIO
		fields = ['nome', 'descricao', 'Plataforma']

		#METODO PARA ENVIAR DADOS PARA O TEMPLATE
		def get_context_data(self, *args, **kwargs):
    		#CHAMAR O "PAI  PARA QUE SEMPRE TENHA O COMPORTAMANETO PADRAO
			context = super(JogoCreate, self).get_context_data(*args, **kwargs)
			
			#ADICIONAR COISAS AS CONTEXTO QUE SERA ENVIADA pARA O HTML
			context['titulo'] = "CADASTRAR Jogo"
			context['botao'] = "CADASTAR"
			context['classeBotao'] = "btn-primary"

			#DEVOLVE/ENVIA O ARQUIVO PARA O SEU COMPORTAMENTO
			return context

class PlataformaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
		group_required = u"Administrador"
		# DEFINE QUAL E O MODELO DA CLASSE, ESTA CRIA O FORM
		model = Plataforma
		#QUAL HTML SERA USADO
		template_name = "game/formulario.html"
		#PARA ONDE O USURAIO SERA REDERECIONADO APOS ISERIR UM REGISTRO, INFORME O NOME DA URL
		success_url = reverse_lazy("listar-plataformas")
		#QUAIS CAOMPOS DEVEM APARECER NO FORMULARIO
		fields = ['nome', 'marca', 'descricao']

		#METODO PARA ENVIAR DADOS PARA O TEMPLATE
		def get_context_data(self, *args, **kwargs):
    		#CHAMAR O "PAI  PARA QUE SEMPRE TENHA O COMPORTAMANETO PADRAO
			context = super(PlataformaCreate, self).get_context_data(*args, **kwargs)
			
			#ADICIONAR COISAS AS CONTEXTO QUE SERA ENVIADA pARA O HTML
			context['titulo'] = "CADASTRAR PLATAFORMA"
			context['botao'] = "CADASTAR"
			context['classeBotao'] = "btn-primary"

			#DEVOLVE/ENVIA O ARQUIVO PARA O SEU COMPORTAMENTO
			return context

######################################## 	EDITAR 	##########################################
class EstadoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
		group_required = u"Grupos"
    	# DEFINE QUAL E O MODELO DA CLASSE, ESTA CRIA O FORM
		model = Estado
		#QUAL HTML SERA USADO
		template_name = "game/formulario.html"
		#PARA ONDE O USURAIO SERA REDERECIONADO APOS ISERIR UM REGISTRO, INFORME O NOME DA URL
		success_url = reverse_lazy("listar-estados")
		#QUAIS CAOMPOS DEVEM APARECER NO FORMULARIO
		fields = ['sigla', 'nome']		

		def get_context_data(self, *args, **kwargs):
			context = super(EstadoUpdate, self).get_context_data(*args, **kwargs)
			context['titulo'] = "ATERAR ESTADO"
			context['botao'] = "ATERAR"
			context['classeBotao'] = "btn-success"
			return context
class CidadeUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
		group_required = u"Grupos"
		# DEFINE QUAL E O MODELO DA CLASSE, ESTA CRIA O FORM
		model = Cidade
		#QUAL HTML SERA USADO
		template_name = "game/formulario.html"
		#PARA ONDE O USURAIO SERA REDERECIONADO APOS ISERIR UM REGISTRO, INFORME O NOME DA URL
		success_url = reverse_lazy("index")
		#QUAIS CAOMPOS DEVEM APARECER NO FORMULARIO
		fields = ['nome', 'estado', 'descricao']

		def get_context_data(self, *args, **kwargs):
			context = super(CidadeUpdate, self).get_context_data(*args, **kwargs)
			context['titulo'] = "ATERAR CIDADE"
			context['botao'] = "ATERAR"
			context['classeBotao'] = "btn-success"

			#DEVOLVE/ENVIA O ARQUIVO PARA O SEU COMPORTAMENTO
			return context

class JogoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
		group_required = u"Administrador"
		# DEFINE QUAL E O MODELO DA CLASSE, ESTA CRIA O FORM
		model = Cidade
		#QUAL HTML SERA USADO
		template_name = "game/formulario.html"
		#PARA ONDE O USURAIO SERA REDERECIONADO APOS ISERIR UM REGISTRO, INFORME O NOME DA URL
		success_url = reverse_lazy("index")
		#QUAIS CAOMPOS DEVEM APARECER NO FORMULARIO
		fields = ['nome', 'descricao', 'Plataforma']



		def get_context_data(self, *args, **kwargs):
			context = super(JogoUpdate, self).get_context_data(*args, **kwargs)
			context['titulo'] = "ATERAR JOGO"
			context['botao'] = "Alterar"
			context['classeBotao'] = "btn-success"

			#DEVOLVE/ENVIA O ARQUIVO PARA O SEU COMPORTAMENTO
			return context

class PlataformaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
		group_required = u"Administrador"
		# DEFINE QUAL E O MODELO DA CLASSE, ESTA CRIA O FORM
		model = Plataforma
		#QUAL HTML SERA USADO
		template_name = "game/formulario.html"
		#PARA ONDE O USURAIO SERA REDERECIONADO APOS ISERIR UM REGISTRO, INFORME O NOME DA URL
		success_url = reverse_lazy("index")
		#QUAIS CAOMPOS DEVEM APARECER NO FORMULARIO
		fields = ['nome', 'marca', 'descricao']


		def get_context_data(self, *args, **kwargs):
			context = super(PlataformaUpdate, self).get_context_data(*args, **kwargs)
			context['titulo'] = "ATERAR Plataforma"
			context['botao'] = "ATERAR"
			context['classeBotao'] = "btn-success"

			#DEVOLVE/ENVIA O ARQUIVO PARA O SEU COMPORTAMENTO
			return context

############################### 	EXCLUIR 	##########################################
class EstadoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
		group_required = u"Administrador"
		# DEFINE QUAL E O MODELO DA CLASSE, ESTA CRIA O FORM
		model = Estado
		#QUAL HTML SERA USADO
		template_name = "game/formulario.html"
		#PARA ONDE O USURAIO SERA REDERECIONADO APOS ISERIR UM REGISTRO, INFORME O NOME DA URL
		success_url = reverse_lazy("index")

		def get_context_data(self, *args, **kwargs):
			context = super(EstadoDelete, self).get_context_data(*args, **kwargs)
			context['titulo'] = "VOCE REALMENTE QUER APAGAR ESTE REGISTRO ???"
			context['botao'] = "ATERAR"
			context['classeBotao'] = "btn-danger"
			return context

class CidadeDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
		group_required = u"Grupos"
		# DEFINE QUAL E O MODELO DA CLASSE, ESTA CRIA O FORM
		model = Estado
		#QUAL HTML SERA USADO
		template_name = "game/formulario.html"
		#PARA ONDE O USURAIO SERA REDERECIONADO APOS ISERIR UM REGISTRO, INFORME O NOME DA URL
		success_url = reverse_lazy("index")

		def get_context_data(self, *args, **kwargs):
			context = super(CidadeDelete, self).get_context_data(*args, **kwargs)
			context['titulo'] = "VOCE REALMENTE QUER APAGAR ESTE REGISTRO ???"
			context['botao'] = "ATERAR"
			context['classeBotao'] = "btn-danger"
			return context

class JogoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
		group_required = u"Administrador"
		# DEFINE QUAL E O MODELO DA CLASSE, ESTA CRIA O FORM
		model = Jogo
		#QUAL HTML SERA USADO
		template_name = "game/formulario.html"
		#PARA ONDE O USURAIO SERA REDERECIONADO APOS ISERIR UM REGISTRO, INFORME O NOME DA URL
		success_url = reverse_lazy("index")


		def get_context_data(self, *args, **kwargs):
			context = super(JogoDelete, self).get_context_data(*args, **kwargs)
			context['titulo'] = "VOCE REALMENTE QUER APAGAR ESTE REGISTRO ???"
			context['botao'] = "Excluir"
			context['classeBotao'] = "btn-danger"
			return context

class PlataformaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
		group_required = u"Grupos"
		# DEFINE QUAL E O MODELO DA CLASSE, ESTA CRIA O FORM
		model = Plataforma
		#QUAL HTML SERA USADO
		template_name = "game/formulario.html"
		#PARA ONDE O USURAIO SERA REDERECIONADO APOS ISERIR UM REGISTRO, INFORME O NOME DA URL
		success_url = reverse_lazy("index")
	

		def get_context_data(self, *args, **kwargs):
			context = super(PlataformaDelete, self).get_context_data(*args, **kwargs)
			context['titulo'] = "VOCE REALMENTE QUER APAGAR ESTE REGISTRO ???"
			context['botao'] = "Excluir"
			context['classeBotao'] = "btn-danger"
			return context
############################### Listar #####################################

class EstadoList(ListView):
	model = Estado
	template_name = 'game/listar_estados.html'
	

class JogoList(ListView):
	model = Jogo
	template_name = 'game/listar_jogos.html'

class PlataformaList(ListView):
	model = Plataforma
	template_name = 'game/listar_plataforma.html'



############################ Detalhes #########################################
class JogoDetalhe(DetailView):
    # Define a classe do objeto a ser detalhado
    model = Jogo
    # Qual o template para essa tela
    template_name = "game/detalhe/jogo.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

class PlataformaDetalhe(DetailView):
    # Define a classe do objeto a ser detalhado
    model = Plataforma
    # Qual o template para essa tela
    template_name = "game/detalhe/plataforma.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

