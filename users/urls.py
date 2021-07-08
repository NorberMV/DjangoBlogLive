""" Users URLs."""

# Django
from django.urls import path

# View
from users import views


urlpatterns = [

    
    # Management
    path(
        route='accounts/login/',
        view=views.login_view,
        name='login'
    ),
    path(
        route='accounts/logout/',
        #view=views.UserDetailView.as_view(),
        view=views.logout_view,
        name='logout'
    ),
    path(
        route='signup/',
        view=views.SignupView.as_view(),
        name='signup'
    ),
    path(
        route='me/profile/',
        view=views.update_profile,
        name='update_profile'
    ),

    # Posts
    path(
        route='<str:username>/', # Must to be the same as the slug_url_kwarg 
        view=views.UserDetailView.as_view(),
        name='detail'
    ),

]
    
"""
    # Posts
    path(
        route='<str:username>/',
        view=TemplateView.as_view(template_name='users/detail'),
        name='detail'
    ),  
 """