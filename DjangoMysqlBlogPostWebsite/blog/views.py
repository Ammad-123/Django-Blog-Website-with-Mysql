from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost  
from .forms import PostForm  
def home_page(request):
    welcome_message = "Welcome to our Blog!"
    return render(request, 'home_page.html', {'welcome_message': welcome_message})
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list') 
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})


def post_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'post_list.html', {'posts': posts})



def post_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'post_detail.html', {'post': post})


