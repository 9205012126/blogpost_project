from django.shortcuts import render , get_object_or_404
from .models import Blog


def allblog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/allblog.html',
                  {'blogs': blogs})


def detail(request,blog_id):
    detail_blog = get_object_or_404(Blog, pk = blog_id)
    return render(request,'blog/details.html',{'blogs':detail_blog})