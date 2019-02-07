from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .models import Post, Comment
from .forms import CustomUserCreationForm
from django.utils import timezone
from .forms import PostForm, CommentForm
from django.shortcuts import redirect
# Create your views here.
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
			
            post.save()
            return redirect('post_list', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'users/post_edit.html', {'form': form})

def post_list(request):

    #RUNNING
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # comment_form = CommentForm()

    # comments = Comment.objects.all()
    # if request.method == "POST":
    #     data = {
    #         'ctext': request.POST['ctext'],
    #         'comment_auth_id': request.user.id,
    #         'title_id': request.POST['title_id']
    #     }
    #     comment_form = CommentForm(data=data)
    #     if comment_form.is_valid():            
    #         Comment.objects.create(**data)
    #     return render(request, 'users/post_list.html', {
    #         'posts': posts, 
    #         'comments': comments, 
    #         'form': comment_form
    #         })
    # else:

    #     return render(request, 'users/post_list.html', {
    #         'posts': posts, 
    #         'comments': comments, 
    #         'form': comment_form
    #     })

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    comments = Comment.objects.all()
    form = CommentForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_auth = request.user
            comment.title_id = request.POST['title_id']
            comment.published_date = timezone.now()
            comment.save()
            return redirect('post_list')
           
    else:
        return render(request, 'users/post_list.html', {
            'posts': posts, 
            'comments': comments, 
            'form': form,
            })




class SignUp(generic.CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'signup.html'

