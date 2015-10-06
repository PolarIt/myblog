from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from article.models import Article,Tag
from datetime import datetime
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  
from article.forms import BlogForm,TagForm

def home(request):
    posts = Article.objects.all()  
    tags = Tag.objects.all()
    paginator = Paginator(posts, 2) 
    page = request.GET.get('page')
    try :
        post_list = paginator.page(page)
    except PageNotAnInteger :
        post_list = paginator.page(1)
    except EmptyPage :
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'home.html', {'post_list' : post_list, 'tags': tags})

def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
        tags = Tag.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post' : post, 'tags': tags})

def archives(request) :
    try:
        post_list = Article.objects.all()
        tags = Tag.objects.all()
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'archives.html', {'post_list' : post_list, 'tags': tags, 'error' : False})

def aboutme(request) :
    return render(request, 'aboutme.html')

def search_tag(request, tag) :
    try:
        tags = Tag.objects.filter(tag_name__iexact = tag)
        post_list = Article.objects.filter(tags__iexact = tags)
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'home.html', {'post_list' : post_list, 'tags': tags})

def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request,'home.html')
        else:
            post_list = Article.objects.filter(title__icontains = s)
            if len(post_list) == 0 :
                return render(request,'archives.html', {'post_list' : post_list,
                                                    'error' : True})
            else :
                return render(request,'archives.html', {'post_list' : post_list,
                                                    'error' : False})
    return redirect('/')

def del_blog(request, id):
    try:
        blog = Article.objects.get(id=id)
    except Exception:
        raise Http404
    if blog:
        blog.delete()
        return HttpResponseRedirect('/')
    blogs = Article.objects.all()
    return render(request,"home.html", {"blogs": blogs})

def add_blog(request):
    if request.method =='POST':
        form = BlogForm(request.POST)
        tag = TagForm(request.POST)
        if form.is_valid() and tag.is_valid():
            cdtag = tag.cleaned_data
            cd = form.cleaned_data
            tagname = cdtag['tag_name']
            for taglist in tagname.split():
                Tag.objects.get_or_create(tag_name=taglist.strip())
            title = cd['title']
            content = cd['content']
            blog = Article(title=title,content=content)
            blog.save()
            for taglist in tagname.split():
                blog.tags.add(Tag.objects.get(tag_name=taglist.strip()))
                blog.save()
            id = Article.objects.order_by('-date_time')[0].id
            return HttpResponseRedirect('/%s/' % id)
    else:
        form = BlogForm()
        tag = TagForm()
    return render(request, 'add.html', {'form': form, 'tag': tag})

def update(request, id):
    id = id
    if request.method == 'POST':
        form = BlogForm(request.POST)
        tag = TagForm(request.POST)
        if form.is_valid() and tag.is_valid():
            cdtag = tag.cleaned_data
            cd = form.cleaned_data
            tagname = cdtag['tag_name']
            tagnamelist = tagname.split()
            for taglist in tagnamelist:
                Tag.objects.get_or_create(tag_name=taglist.strip())
            title = cd['title']
            content = cd['content']
            blog = Article.objects.get(id=id)
            if blog:
                blog.title = title
                blog.content = content
                blog.save()
                for taglist in tagnamelist:
                    blog.tags.add(Tag.objects.get(tag_name=taglist.strip()))
                    blog.save()
                tags = blog.tags.all()
                for tagname in tags:
                    tagname = str(tagname)
                    if tagname not in tagnamelist:
                        notag = blog.tags.get(tag_name=tagname)
                        blog.tags.remove(notag)
            else:
                blog = Article(title=blog.title, content=blog.content)
                blog.save()
            return HttpResponseRedirect('/%s/' % id)
    else:
        try:
            blog = Article.objects.get(id=id)
        except Exception:
            raise Http404
        form = BlogForm(initial={'title': blog.title, 'content': blog.content}, auto_id=False)
        tags = blog.tags.all()
        if tags:
            taginit = ''
            for x in tags:
                taginit += str(x) + ' '
            tag = TagForm(initial={'tag_name': taginit})
        else:
            tag = TagForm()
    return render(request,'add.html',{'blog': blog, 'form': form, 'id': id, 'tag': tag})
