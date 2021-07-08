
"""Users views."""

# Django
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, FormView, UpdateView
from django.urls import reverse, reverse_lazy

# Models
from django.contrib.auth.models import User
from posts.models import Post

# Forms
from users.forms import ProfileForm, SignupForm

# Utilities
import pdb


class UserDetailView(LoginRequiredMixin,DetailView):
    """User detail View."""
    template_name = "users/detail.html"
    slug_field = 'username'#'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all() # Trae un queryset de todos los usernames de la base de datos
    context_object_name = 'user' # Este es el nombre del query en el contexto y en el template
    #pdb.set_trace()    

    def get_context_data(self, **kwargs): # De donde toma **kwargs?
        """Add user´s posts to context."""
        context = super().get_context_data(**kwargs) # Super(). is used to give access to methods and properties of a parent or sibling class
        #pdb.set_trace()
        user = self.get_object() # Trae el objeto filtrado del queryset por medio del self.kwargs pasado como argumentod del template The object
        context['publicaciones'] = Post.objects.filter(user=user).order_by('-created') #Agrega 'publicaciones al context y lo filtra por medio de user para traer los posts del usuario en particular
        #pdb.set_trace()
        return context 


@login_required  
def update_profile(request):                 # Request es una clase
    """ Update a user´s profile view. """
    profile = request.user.profile  # creamos el objeto profile a partír de instanciar la clase profile
    #pdb.set_trace()

    if request.method =='POST':
        form = ProfileForm(request.POST, request.FILES)
        #pdb.set_trace()
        if form.is_valid():
            data = form.cleaned_data
            #print(data)
            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()

            url = reverse('users:detail',kwargs={'username':request.user.username})
            return redirect(url)
    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )


def login_view(request):
    """Login view."""
    if request.method == 'POST':
        #pdb.set_trace() 
        username = request.POST['username'] # Las variables username y password que recibe nuestro servidor fueron nombradas en login.html
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            return redirect('posts:feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})

    return render(request, 'users/login.html')


class SignupView(FormView):
    """Users sign up view."""

    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)
"""
def signup(request):
    # Sign up view. 

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = SignupForm()

    return render(
        request=request,
        template_name='users/signup.html',
        context={'form': form}
    )
    

    #return render(request, 'users/signup.html')
"""

@login_required
def logout_view(request):
    """Logout a user."""
    logout(request)
    return redirect('users:login')

