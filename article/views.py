from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  #添加包

def home(request):
    posts = Article.objects.all()  
    paginator = Paginator(posts, 2) 
    page = request.GET.get('page')
    try :
        post_list = paginator.page(page)
    except PageNotAnInteger :
        post_list = paginator.page(1)
    except EmptyPage :
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'home.html', {'post_list' : post_list})

def detail(request,id):
	try:
		post = Article.objects.get(id = str(id))
	except Article.DoesNotExist:
		raise Http404
	return render(request,'post.html',{'post': post})

def archives(request) :
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'archives.html', {'post_list' : post_list, 'error' : False})

def aboutme(request) :
    return render(request, 'aboutme.html')

def search_tag(request, tag) :
    try:
        post_list = Article.objects.filter(category__iexact = tag) #contains
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'home.html', {'post_list' : post_list})