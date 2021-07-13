from django.shortcuts import render, get_object_or_404
from .models import Blog, Comment
from .forms import CommentForm
from django.contrib import messages
from category.models import Category

# Create your views here.

def blog(request, category_slug=None):
    categories = None
    blogs = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        blogs = Blog.objects.filter(category=categories).order_by('-created_date')

    else:
        blogs =Blog.objects.all()
  
    return render(request, 'blog/blog.html', {'blogs': blogs})


def blog_detail(request, id, category_slug):
    blog =Blog.objects.get(category__slug=category_slug,id=id)


    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                blog=blog
            )
            comment.save()
            comment= CommentForm()
            messages.success(request, 'Comment is successfully added')

        else: 
            form = CommentForm()
    else:
        form = CommentForm()

    comments = Comment.objects.filter(blog=blog)
    context = {
        "blog": blog,
        "comments": comments,
        "form": form,
      

    }   
    #if you as passing several things you can wrap them up in the function and pass the function itself 

    return render(request, 'blog/blog_detail.html', context)


def search(request):
    bloglist = blog.objects.all

    #for keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            bloglist = bloglist.filter(description__icontains=keywords)

    return render(request,'blog/search.html' , {'bloglist' : bloglist})


