from django.shortcuts import render
from django .http import HttpResponse
from .models import BlogPost, PortfolioPost
from django.views.generic import ListView, DetailView
from .models import BlogPost
# Create your views here.


def home(request):
    context = {
        'posts': BlogPost.objects.all()
    }
    return render(request, 'mainsite/home.html')

class BlogListView(ListView):
    model = BlogPost
    template_name = 'mainsite/blog.html' # Django checks for <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class BlogDetailView(DetailView):
    model = BlogPost

class PortfolioListView(ListView):
    model = PortfolioPost
    template_name = 'mainsite/portfolio.html' # Django checks for <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

class PortfolioDetailView(DetailView):
    model = PortfolioPost

def about(request):
    return render(request, 'mainsite/about.html', {'title': 'About'})






# Create your views here.
def blog(request):
    context = {
        'posts': BlogPost.objects.all()
    }
    return render(request, 'mainsite/blog.html', context)

def portfolio(request):
    context = {
        'posts': PortfolioPost.objects.all()
    }
    return render(request, 'mainsite/portfolio.html', context)


