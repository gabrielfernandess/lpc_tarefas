from tastypie.resources import ModelResource
from tastypie import fields, utils
from tastypie.authorization import Authorization
from tarefa.models import *
from django.contrib.auth.models import User
from tastypie.exceptions import Unauthorized

class ProjetoUsuarioResource(ModelResource):
    def obj_delete_list(self, bundle, **kwargs):
        raise Unauthorized("Não é possível deletar toda a lista");

    class Meta:
        queryset = ProjetoUsuario.objects.all() 
        allowed_methods = ['get','post','put','delete']
        filtering = {
            "projeto": ('exact', 'startswith',)
        }
        authorization = Authorization()

class UsuarioResource(ModelResource):
    def obj_delete_list(self, bundle, **kwargs):
        raise Unauthorized("Não é possível deletar toda a lista");

    class Meta:
        queryset = Usuario.objects.all()
        allowed_methods = ['get','post','put','delete']
        filtering = {
            "nome": ('exact', 'startswith',)
        }
        authorization = Authorization()

class ProjetoResource(ModelResource):
    def obj_delete_list(self, bundle, **kwargs):
        raise Unauthorized("Não é possível deletar toda a lista");

    class Meta:
        queryset = Projeto.objects.all()
        allowed_methods = ['get','post','put','delete']
        filtering = {
            "nome": ('exact', 'startswith',)
        }
        authorization = Authorization()

class TarefaResource(ModelResource):
    def obj_create(self, bundle, **kwargs):
        nome = bundle.data['nome']
        projeto = bundle.data['projeto'].split("/")
        usuario = bundle.data['usuario'].split("/")
        if not(Tarefa.objects.filter(nome=nome)):
            tarefa = Tarefa()
            tarefa.nome = nome
            tarefa.projeto = Projeto.objects.get(pk=projeto[4])
            tarefa.usuario = Usuario.objects.get(pk=usuario[4])
            tarefa.save()
            bundle.obj = tarefa
            return bundle
        else:
            raise Unauthorized('A Tarefa especificada já possui um projeto cadastrado');

    def obj_delete_list(self, bundle, **kwargs):
        raise Unauthorized("Não é possível deletar toda a lista");

    def obj_delete(self, bundle, **kwargs):
        return bundle.obj.user == bundle.request.user

    def obj_update(self, object_list, bundle):
        return bundle.obj.user == bundle.request.user

    class Meta:
        queryset = Tarefa.objects.all()
        allowed_methods = ['get','post','put','delete']
        filtering = {
            "nome": ('exact', 'startswith',)
        }
