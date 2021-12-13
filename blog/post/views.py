from django.views.generic import TemplateView
from django.views.generic import ListView

from .models import Post


class homePageView(TemplateView):
    template_name = 'home.html'


class aboutPageView(TemplateView):
    template_name = 'about.html'


class postPageView(ListView):
    template_name = 'post.html'
    model = Post
