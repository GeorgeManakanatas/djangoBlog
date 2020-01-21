from django.shortcuts import render

# Create your views here.
def HomePageView(request):
    return render(request, 'index.html', {})

def SingleBlogView(request):
    return render(request, 'blog-single.html', {})

def AllBlogsView(request):
    return render(request, 'blog.html', {})