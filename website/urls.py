from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.HomePageView, name='home'),
    url(r'^singleblog/$', views.SingleBlogView, name='singleBlog'),
    url(r'^blogs/$', views.AllBlogsView, name='allBlogs'),
]
