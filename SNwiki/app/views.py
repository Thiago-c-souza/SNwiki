from django.shortcuts import render, get_object_or_404
from . import models

# View para a home
def home(request):
    post = models.Post.objects.all()
    rotina = models.rotinas.objects.all()  # Retornando todas as rotinas
    tipo_erro = models.Tipo_erro.objects.all()

    context = {
        'post': post,
        'rotina': rotina,
        'erro': tipo_erro,
    }
    return render(request, 'home.html', context)

# View para exibir posts filtrados por rotina
def post(request, id):
    Rotina = get_object_or_404(models.rotinas, N_rotina=id)
    post = models.Post.objects.filter(rotina=Rotina)
    rotina = models.rotinas.objects.all()  # Para listar todas as rotinas no template

    context = {
        'post': post,
        'rotina_1': Rotina,
        'rotina': rotina,
    }
    return render(request, 'post.html', context)

# View para exibir detalhes de um post específico
def post_detail(request, id):
    post = get_object_or_404(models.Post, id=id)  # Filtra por ID único do post
    Post = models.Post.objects.filter(id = id)
    rotina = models.rotinas.objects.all()

    context = {
        'post_1': Post,  # Usando 'post_1' para evitar conflitos
        'rotina': rotina,
    }
    return render(request, 'post_detail.html', context)
