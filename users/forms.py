from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from .models import Post, Comment


class CustomUserCreationForm(UserCreationForm):

	class Meta(UserCreationForm):
		model = CustomUser
		fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

	class Meta:
		models = CustomUser
		fields = ('username', 'email')

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'text', 'imgfile')

class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ('ctext', )
		readonly = ('commment_auth', 'title')