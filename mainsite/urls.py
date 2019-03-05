
from django.urls import path
from . import views
from .views import BlogListView, BlogDetailView, PortfolioListView, PortfolioDetailView
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='mainsite-home'),
    path('about/', views.about, name='mainsite-about'),
    path('blog/', BlogListView.as_view(), name='mainsite-Blog'),
    path('blogpost/<int:pk>/', BlogDetailView.as_view(), name='blogpost-detail'),
    #path('blog/', views.blog, name='mainsite-Blog'),
    #path('portfolio/', views.portfolio, name='mainsite-Portfolio'),
    path('portfolio/', PortfolioListView.as_view(), name='mainsite-Portfolio'),
    path('portfoliopost/<int:pk>/', PortfolioDetailView.as_view(), name='portfoliopost-detail'),
 ]