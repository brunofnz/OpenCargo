from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView
from .models import Pedido

# Homepage
def home(request):
    pedido = Pedido.objects.all()
    return render(request, 'home1.html', {'object_list': pedido})

# GET Todos los posts.
def posts(request):
    pedidos = Pedido.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'posts1.html', {'posts' : pedidos, 'menus': menus})

    ## COMO SE TRADUCE LO DE ARRIBA EN SQL?
    ## SELECT * FROM Post WHERE publish_date <= DATETIME.NOW() ORDER BY publish_date

# GET Todos los posts usando Class View.
class HomeView(ListView):
    model = Pedido
    template_name = 'home1.html'

# GET Un post por medio de su id (o Primary Key).
class PostDetailView(DetailView):
    model = Pedido
    template_name = 'post_detail1.html'

#POST Crear un nuevo post
class PostCreateView(CreateView):
      model = Pedido
      template_name = 'post_new1.html'
      fields = '__all__'
