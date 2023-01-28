from django.urls import path
from . import views

urlpatterns = [
    path('', views.alunoView, name='aluno-listas'),
    path('aluno/<int:id>', views.alunoIDview, name='aluno-view'),
    path('newaluno/', views.newAluno, name='new-aluno'),
    path('exemplo', views.exemplo, name='exemplo'),
    path('edit/<int:id>', views.editAluno, name="edit-aluno"),
    path('delete/<int:id>', views.deleteAluno, name='delete-aluno')
]
