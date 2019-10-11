from django.shortcuts import render, redirect, get_object_or_404
from . models import ShowcaseIntro, Service, About, Skill, Portfolio, Testimonial, Contact, Footer
from blog.models import Author, Category, Blog, Comment
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from . form import *


# Create your views here.


def index(request):
    showcases = ShowcaseIntro.objects.all()[:1]
    services = Service.objects.order_by('added_date')[:6]
    about_me = About.objects.all()[:1]
    skills = Skill.objects.all()
    portfolios = Portfolio.objects.order_by('-date_pub')
    paginator = Paginator(portfolios, 8)
    page = request.GET.get('page')
    paged_portfolios = paginator.get_page(page)
    testimonials = Testimonial.objects.order_by(
        '-date_create').filter(is_approved=True)[:5]
    blogs = Blog.objects.order_by('-date_publish')[:3]
    footer = Footer.objects.all()[:1]

    context = {
        'showcases': showcases,
        'services': services,
        'about_me': about_me,
        'skills': skills,
        'portfolios': paged_portfolios,
        'blogs': blogs,
        'testimonials': testimonials,
        'footer': footer
    }
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        message = request.POST['message']
        subject = request.POST['subject']
        contact = Contact(first_name=first_name, last_name=last_name, email=email, message=message,
                          subject=subject)

        contact.save()
        messages.success(
            request, 'Your message has been submitted, We will get back to you soon')
        return redirect('index')
    return render(request, 'home/index.html', context)


def quote(request):
    if request.method == 'POST':
        # quote = QuoteForm(request.POST, request.FILES)
        quote = request.POST['quote']
        full_name = request.POST['full_name']
        # client_image = request.FILES['client_image']
        testimonial = Testimonial(
            full_name=full_name, quote=quote)
        # if quote.is_valid:
        #     quote.save()
        testimonial.save()
        messages.success(
            request, 'Your quote has been submitted, and will be display in the client testimonials section')
        return redirect('index')
    return render(request, 'home/index.html')

# Portfolio


def portfolio(request, port_id):
    portfolio = get_object_or_404(Portfolio, pk=port_id)
    testimonials = Testimonial.objects.order_by(
        '-date_create').filter(is_approved=True)[:3]
    footer = Footer.objects.all()[:1]
    context = {
        'portfolio': portfolio,
        'testimonials': testimonials,
        'footer': footer

    }
    return render(request, 'home/portfolio_detail.html', context)
