from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import login, authenticate







# Create your views here.
def index(request):
    articles = Article.objects.all()
    return render(request, 'main/index.html', {'title': 'Home', 'articles': articles})

from django.contrib.auth import authenticate, login

from django.contrib.auth import authenticate, login as auth_login

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'main/register.html', {'form': form})

def login_view(request):
    return render(request, 'main/login.html')

@login_required
def profile(request):
    return render(request, 'main/profile.html')

def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            if request.user.is_authenticated:
                article.author = request.user
            article.save()
            return redirect('index')  # Consider redirecting to the article's detail page
    else:
        form = ArticleForm()
    return render(request, 'main/create_articles.html', {'form': form})






def edit_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'main/edit_article.html', {'form': form, 'article': article})


def delete_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        article.delete()
        return redirect('index')
    return render(request, 'main/delete_article.html', {'article': article})


