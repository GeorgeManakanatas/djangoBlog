from django.shortcuts import render
from .models import StaticText
# Create your views here.
def HomePageView(request):
    if request.method == "GET":
        print('\n!!! we have a get !!!\n')
        db_query_text = StaticText.objects.all()
    if len(db_query_text) == 0:
        serv_gen_text = 'At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate. At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium.'
    else:
        serv_gen_text = db_query_text
    
    return render(request, 'index.html', {'serv_gen_text':serv_gen_text})

def SingleBlogView(request):
    return render(request, 'blog-single.html', {})

def AllBlogsView(request):
    return render(request, 'blog.html', {})