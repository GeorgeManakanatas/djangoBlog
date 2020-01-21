from django.shortcuts import render

# Create your views here.
def myPersonalPage(request):
    return render(request, 'mycvindex.html', {})