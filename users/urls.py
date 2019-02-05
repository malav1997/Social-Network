from django.urls import path, include
from . import views

urlpatterns = [
	path('signup/', views.SignUp.as_view(), name='signup'),
	path('post/list', views.post_list, name='post_list'),
	path('post/new', views.post_new, name='post_new'),
]