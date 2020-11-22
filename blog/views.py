from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
# Create your views here.
def blog_index(request):
    articles=Article.objects.all()
    data={'articles':articles}
    return render(request,'blog/blog_index.html',data)

def article(request,name):
    try:
        article=Article.objects.get(title=name)
        context={'article':article}
    except:
        context={'message':'l\'article n\'existe pas'}
    return render(request,'blog/article.html',context)
