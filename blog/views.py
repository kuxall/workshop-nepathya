from django.shortcuts import render
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse


from blog.models import Post
# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'list.html', {'abc': posts})


def post_new(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created = timezone.now()
            post.save()
            return redirect('postssss')

    else:
        form = PostForm()
        return render(request, 'new_post.html', {'form': form})


def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_details.html', {'post': post})


def edit_post(request, pk):
    template = 'new_post.html'
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = PostForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }
    return render(request, template, context)


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return HttpResponse("deleted")
