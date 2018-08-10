from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from .models import Article

# Create your views here.
def index(request):
	return render(request, 'index.html')
def list(request):
	names=[]
	return render(request,'list.html',{'names':names})
def detail(request, id):
	#post = Article.objects.all()[id]
	#str=("title=%s,category=%s, date_time=%s, content=%s"
		#%(post.title, post.category, post.date_time,post.content))
	#return HttpResponse (str)
	return HttpResponse (f'article detail with the id of {id}')

def test(request) :
    return render(request, 'test.html', {'current_time': datetime.now()})