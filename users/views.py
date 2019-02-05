from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .models import Post, Comment
from .forms import CustomUserCreationForm
from django.utils import timezone
from .forms import PostForm, CommentForm

# Create your views here.
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
			
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'users/post_edit.html', {'form': form})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # post = get_object_or_404(Post, title=title)
    cform = CommentForm()
    comments = Comment.objects.all()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
         #if comment_form.is_valid():
    #         new_comment = comment_form.save(commit=False)
    #         new_comment.post = post
    #         new_comment.save()

            #cform = CommentForm(request.GET)
            #data = {}
            #Comment.ctext(**data)
        if cform.is_valid():
            comment={}
            comment['ctext'] = request.POST['ctext']            
            cform.changed_data['comment_auth'] = request.user
        #cform['comment_auth'] = request.user
        #cform['comment_auth_id_id'] = request.user

        cform.save()
            
        return render(request, 'users/post_list.html', {'posts': posts, 'comments': comments, 'form': cform})
    else:
        form = CommentForm()

    return render(request, 'users/post_list.html', {'posts': posts, 'comments': comments, 'form': cform})
	 

class SignUp(generic.CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'signup.html'

