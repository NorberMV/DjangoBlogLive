
""" Posts URLs."""

# Django
from django.urls import path

# Views
from posts import views

urlpatterns = [

    path(
    	route='',
    	view= views.PostsFeedView.as_view(),
    	name='feed'
    ),
    
    path(
    	route='posts/new/', 
    	view=views.CreatePostView.as_view(), 
    	name='create'
    ),
    # Detail of a post.
	path(
    	route='posts/<int:post_id>/', # El template nos pasa el parametro id único de la imagen que querémos ver en detalle
    	view=views.PostDetailView.as_view(), 
    	name='detailPost'
    ),
	# Text channel
	path(
		route='posts/text_feed/',
		view=views.TextFeedView.as_view(),
		name='text_channel'
	)
]	