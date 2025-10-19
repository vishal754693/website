from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create your views here.
def allposts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})

def detail(request, blog_id):
    detail = get_object_or_404(Post, pk=blog_id)
    return render(request, 'detail.html', {'detail': detail})
