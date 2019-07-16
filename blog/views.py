from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from . models import Author, Category, Blog, Comment
from home.models import Footer, Testimonial
from django.contrib import messages
from . form import *
# Create your views here.


def blog_detail(request, blog_id):
    side_blog = Blog.objects.order_by('-date_publish')[:5]
    blogs = Blog.objects.order_by('date_pub')[:5]
    prev_post = Blog.objects.order_by('date_publish')[:1]
    next_post = Blog.objects.order_by('-date_publish')[:1]
    blog = get_object_or_404(Blog, pk=blog_id)
    footer = Footer.objects.all()[:1]
    authors = Author.objects.all()[:1]
    categories = Category.objects.all()
    testimonials = Testimonial.objects.order_by(
        '-date_create').filter(is_approved=True)[:3]
    comments = blog.comments.filter(approved_comment=True, reply__isnull=True)
    context = {
        'side_blog': side_blog,
        'prev_post': prev_post,
        'next_post': next_post,
        'blog': blog,
        'blogs': blogs,
        'comments': comments,
        'testimonials': testimonials,
        'footer': footer,
        'authors': authors,
        'categories': categories,
    }
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            reply_obj = None
            try:
                reply_id = int(request.POST.get('reply_id'))
            except:
                reply_id = None
            if reply_id:
                reply_obj = Comment.objects.get(id=reply_id)
                if reply_obj:
                    reply_comment = comment_form.save(commit=False)
                    reply_comment.reply = reply_obj
            new_comment = comment_form.save(commit=False)
            new_comment.Post = blog
            new_comment.save()
            messages.success(
                request, 'Your Comment has been submitted')
            return redirect('blog', blog_id)
        else:
            comment_form = CommentForm()
    return render(request, 'blog/blog_detail.html', context)


def search(request):
    queryset_list = Blog.objects.order_by("-date_publish")
    side_blog = Blog.objects.order_by('-date_publish')[:5]
    paginator = Paginator(queryset_list, 3)
    page = request.GET.get('page')
    paged_blogs = paginator.get_page(page)
    testimonials = Testimonial.objects.order_by(
        '-date_create').filter(is_approved=True)[:3]
    footer = Footer.objects.all()[:1]
    authors = Author.objects.all()[:1]
    categories = Category.objects.all()

    # Check for keywords

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)
    context = {
        'testimonials': testimonials,
        'footer': footer,
        'authors': authors,
        'categories': categories,
        'side_blog': side_blog,
        'blogs': paged_blogs,
        'values': request.GET,
    }
    return render(request, 'blog/blog_search.html', context)
