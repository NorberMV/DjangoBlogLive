
"""Posts views."""

# Django
#from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import  DetailView, ListView, CreateView

# Models
from posts.models import Post
from django.contrib.auth.models import User
from users.models import Profile

# Forms
from posts.forms import PostForm


# Utilities
from datetime import datetime
import pdb
    

class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts."""

    template_name = 'posts/feed.html'
    model = Post
    #pdb.set_trace()
    ordering = ('-created',)
    paginate_by = 4
    context_object_name = 'posts'

"""Version vista funcional anterior
@login_required  
def list_posts(request):
    List existing posts.
    posts = Post.objects.all().order_by('-created')
    return render(request, 'posts/feed.html', {'posts':posts})"""


class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post."""

    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')
    
    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context

""" Versión funcional de la vista create_post()
@login_required
def create_post(request):
    # Create new post view.
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES) # Mandamos el formulario, con los datos que vengan en el request, adicional como vamos a mandar una foto usamos request.FILE para que ek archivo este presente
        if form.is_valid():
            form.save() # Esta funcion automaticamente termina de crear el post
            return redirect('posts:feed') # Redireccionamos al feed de los posts

    else:
        form = PostForm()

    return render(
        request=request,
        template_name='posts/new.html',
        context= {
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    ) """

"""***************Working on a new class-view****************"""
class PostDetailView(LoginRequiredMixin,DetailView):
    """Post detail View."""
    #pdb.set_trace()
    template_name = "posts/detail_post.html"
    slug_field = 'id'
    slug_url_kwarg = 'post_id'
    queryset = Post.objects.all()
    #model = Post
    """slug_field = ''
    slug_url_kwarg = 'id'
    queryset = Post.objects.get() # Trae un queryset de todos los usernames de la base de datos
    pdb.set_trace()
    context_object_name = 'post'#'title' # Este es el nombre del query en el contexto y en el template
    #pdb.set_trace()
    def get_context_data(self, **kwargs): # De donde toma **kwargs? del context_object_name
       #Add user´s posts to context."""
    """context = super().get_context_data(**kwargs) # Super(). is used to give access to methods and properties of a parent or sibling class
        pdb.set_trace()
        id = self.get_object()
        pdb.set_trace()
        context['post1'] = Post.objects.filter(id=id)
        
        return context """

"""********NEW CLASS TEXT CHANNEL!****************"""
class TextFeedView(LoginRequiredMixin, ListView):
    """Return all the existing user´s biographies!"""
    template_name = 'posts/text_channel.html'
    model = Profile
    #pdb.set_trace()
    ordering = ('id',) # Ordenarlo por 'id'
    paginate_by = 15
    context_object_name = 'profiles'

    """ queryset = Profile.objects.all() # Trae un queryset de todos los profiles de la base de datos
    context_object_name = 'profiles' # Este es el nombre del query en el contexto y en el template
    #pdb.set_trace()

    def get_context_data(self, **kwargs): # De donde toma **kwargs?
        
        context = super().get_context_data(**kwargs) # Super(). is used to give access to methods and properties of a parent or sibling class
        pdb.set_trace()
        #user = self.get_object() # The object
        #context['publicaciones'] = Post.objects.filter(user=user).order_by('-created')
        #pdb.set_trace()
        return context """