# outra forma de criar urls, criando um arquivo de urls para cada aplicativo a fim de facilitar a organização

from django.urls import path
from app_adotantes.views import listar_user, cadastrar_user, listar_adocao, cadastrar_adocao,listar_adocao, editar_user, excluir_user,editar_adocao 

app_name = 'app_adotantes'
urlpatterns = [
    path('user/', listar_user, name='listar_user'),
    path('user/cadastrar/', cadastrar_user, name='cadastrar_user'),
    path('user/editar/<int:user_id>/', editar_user, name='editar_user'),
    path('user/excluir/<int:user_id>/', excluir_user, name='excluir_user'),
    path('', listar_adocao, name='listar_adocao'),
    path('cadastrar', cadastrar_adocao, name='cadastrar_adocao'),
    path('editar/<int:adocao_id>/', editar_adocao, name='editar_adocao'),
]
