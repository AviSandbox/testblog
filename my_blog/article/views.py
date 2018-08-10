from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from .models import Article
from datetime import datetime
from django.http import Http404

# Create your views here.
def index(request):
	post_list=Article.objects.all()
	return render(request,'index.html', {'post_list':post_list})
	#return render(request, 'index.html')
# did not in use yet (list)
def list(request):
	names=[]
	return render(request,'list.html',{'names':names})
def detail(request, id):
	try:
		post = Article.objects.get(id=str(id))
	except Article.DoesNotExist:
		raise Http404
	#str=("title=%s,category=%s, date_time=%s, content=%s"
	#	%(post.title, post.category, post.date_time,post.content))
	#return HttpResponse (str)
	#return HttpResponse (f'article detail with the id of {id}')
	return render(request, 'post.html',{'post':post})

def test(request) :
    return render(request, 'test.html', {'current_time': datetime.now()})