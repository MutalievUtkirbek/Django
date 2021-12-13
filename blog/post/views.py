from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView

from .models import Post


class homePageView(TemplateView):
    template_name = 'home.html'


class aboutPageView(TemplateView):
    template_name = 'about.html'


class postPageView(ListView):
    template_name = 'post.html'
    model = Post


class postDetailView(DetailView):
    template_name = 'post_detail.html'
    model = Post
