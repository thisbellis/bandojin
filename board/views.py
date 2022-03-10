from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Article


def community(request):
  articles = Article.objects.order_by('-pk')
  context = {
    'articles': articles,
  }
  return render(request, 'board/community.html', context)

def detail(request, pk):
  article = Article.objects.get(pk=pk)
  context = {
    'article': article,
  }
  return render(request, 'board/detail.html', context)

def write(request):
  return render(request, 'board/write.html')

def create(request):
  article = Article()
  article.title = request.POST['title']
  article.content = request.POST['content']
  article.save()
  return redirect('board:detail', article.pk)

def update(request, pk):
  article = Article.objects.get(pk=pk)
  article.title = request.POST['title']
  article.content = request.POST['content']
  article.save()
  return redirect('board:detail', article.pk)
  

def edit(request, pk):
  article = Article.objects.get(pk=pk)
  context = {
    'article': article,
  }
  return render(request, 'board/edit.html', context)

def delete(request, pk):
  article = Article.objects.get(pk=pk)
  if request.method == 'POST':
    article.delete()
    return redirect('board:community')
  elif request.method == 'GET':
    return redirect('board:detail', article.pk)
  
