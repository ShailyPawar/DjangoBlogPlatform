from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator

# Home Page - Blog Post List View with Pagination
def index(request):
    posts = Post.objects.all().order_by('-created_at')  # Order by latest
    paginator = Paginator(posts, 5)  # Show 5 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/index.html', {'page_obj': page_obj})

# Individual Blog Post Detail View
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})


from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

def index(request):
    posts = Post.objects.all()  # Retrieve all posts from the database
    paginator = Paginator(posts, 5)  # Show 5 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  # Get the current page
    return render(request, 'blog/index.html', {'page_obj': page_obj})
