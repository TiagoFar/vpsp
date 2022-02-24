from django.urls import path
from . import views

# views precisam ser callable, como se fosse uma function.
#  vai chamar a class. Ex: PostIndex e a função vem na sequência.

urlpatterns = [
    path('', views.PostIndex.as_view(), name='index'),
    path('categorias/<str:categoria>', views.PostCategoria.as_view(), name='post_categoria'),
    path('busca/', views.PostBusca.as_view(), name='post_busca'),
    path('post/<int:pk>', views.PostDetalhes.as_view(), name='post_detalhes'),

]
