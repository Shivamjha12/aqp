from calendar import c
from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    categories = Category.objects.all()
    print(categories)
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')
    context= {
        'object_list': featured,
        'latest': latest,
        'categories':categories,
    }
    return render(request, 'home1.html',context)

def category_list(request):
    categories = Category.objects.all()
    context= {
        'categories':categories,
    }
    return render(request, 'all_categories.html', context)

def homepage(request):
    categories = Category.objects.all()
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:4]
    photos = PostImage.objects.all()
    context= {
        'object_list': featured,
        'latest': latest,
        'categories':categories,
        'photos':photos,
        
        
        }
    print(latest)
    return render(request, 'homepage.html', context)

def post(request,slug):
    post = Post.objects.get(slug=slug)
    photos = PostImage.objects.filter(post=post)
    context = {
        'post': post,
        'photos':photos
    }
    return render(request, 'post.html', context)

def category_post_list (request, slug):
    category = Category.objects.get(slug = slug)
    posts = Post.objects.filter(categories__in=[category])
    context = {
        'posts': posts,
    }
    return render(request, 'post_list.html', context)

def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    context = {
        'object_list': queryset
    }
    return render(request, 'search_bar.html', context)

def postlist (request,slug):
    category = Category.objects.get(slug = slug)
    posts = Post.objects.filter(categories__in=[category])

    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'post_list.html', context)

def allposts(request):
    posts = Post.objects.order_by('-timestamp')
    context = {
        'posts': posts,
    }
    return render(request, 'all_posts.html', context)

def about (request):
    return render(request, 'about_page.html')

