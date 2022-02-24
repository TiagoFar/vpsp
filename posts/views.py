from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Post
from django.db.models import Q, Count, Case, When
from comentarios.forms import FormComentario
from comentarios.models import Comentario
from django.contrib import messages



class PostIndex(ListView):
    model = Post        # aqui a gente sobrescreveu a variável model que vem do ListView.
    template_name = 'posts/index.html'                 # Se apertar ctrl + clique em cima da variável, poderá vê-la.
    paginate_by = 6
    context_object_name = 'posts'  # iterável com o for do index.html

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id').filter(publicado_post=True)  # para colocar as publicações em ordem decrescente
        qs = qs.annotate(
            numero_comentarios=Count(
                Case(
                    When(comentario__publicado_comentario=True, then=1)
                )
            )
        )
        return qs


class PostBusca(PostIndex):
    template_name = 'posts/post_busca.html'

    def get_queryset(self):
        qs = super().get_queryset()
        termo = self.request.GET.get('termo')


        qs=qs.filter(
            Q(titulo_post__icontains=termo) |
            Q(autor_post__first_name__iexact=termo) | # Foreign key
            Q(conteudo_post__icontains=termo) |
            Q(excerto_post__icontains=termo) |
            Q(categoria_post__nome_cat__iexact=termo) # Foreign key
        )

        return qs


class PostCategoria(PostIndex):   # aqui vamos sobrescrever novamente a template_name
    template_name = 'posts/post_categoria.html'

    def get_queryset(self):
        qs = super().get_queryset()
        categoria = self.kwargs.get('categoria', None)

        if not categoria:
            return qs

        qs = qs.filter(categoria_post__nome_cat__iexact=categoria)  # dentro de categoria_post eu vou ver qual é o nome da categoria, e o iexact quer dizer, 'a busca é igual'(tb é cansesentitive)

        return qs

class PostDetalhes(UpdateView):
    template_name = 'posts/post_detalhes.html'
    model = Post
    form_class = FormComentario
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        post = self.get_object()
        comentarios = Comentario.objects.filter(publicado_comentario=True,
                                                post_comentario=post.id)
        contexto['comentarios'] = comentarios
        return contexto

    def form_valid(self, form):
        post = self.get_object()
        comentario = Comentario(**form.cleaned_data)
        comentario.post_comentario = post

        if self.request.user.is_authenticated:
            comentario.usuario_comentario = self.request.user

        comentario.save()
        messages.success(self.request, 'Comentário enviado com sucesso.')
        return redirect('post_detalhes', pk=post.id)

