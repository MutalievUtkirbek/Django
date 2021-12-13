from django.urls import path
from .views import homePageView, aboutPageView, postPageView, postDetailView

urlpatterns = [
    path('', homePageView.as_view(), name="home"),
    path('about', aboutPageView.as_view(), name="about"),
    path('post', postPageView.as_view(), name="post"),
    path('post/<int:pk>', postDetailView.as_view(), name="post.detail"),
]
