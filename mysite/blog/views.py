from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import post as post_p
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
import os


def main_page(request):
    return render(request, 'blog/index.html')


@login_required
# Create your views here.
def post_list(request):

    posts = post_p.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def post_group(request, post_type):
    posts_type = post_p.objects.filter(type=post_type).order_by('publish_date')
    return render(request, 'blog/post_list.html', {'posts': posts_type})
    # django_posts = post_p.objects.filter(type='Django').order_by('publish_date')
    # github_posts = post_p.objects.filter(type='GitHub').order_by('publish_date')
    # posts = post_p.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    # return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def post_detail(request, pk):
    post_info = get_object_or_404(post_p, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post_info})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(post_p, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def python(request):
    return render(request, 'blog/python.html')
@login_required
def django(request):
    return render(request, 'blog/django.html')
@login_required
def github(request):
    return render(request, 'blog/github.html')

def signup_view(request):
    if request.method == "POST":
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            new_user = signup_form.save()
            return redirect('blog.views.login_view')
    else:
        signup_form = UserCreationForm()
    return render(request, 'blog/signup.html', {'signup_form': signup_form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('un')
        password = request.POST.get('ps')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('blog.views.post_list')
            else:
                raise Http404("not active")
        else:
            raise Http404("please sign up")
    else:
        return render(request, 'blog/login.html')


def logout_view(request):
    logout(request)
    return redirect('blog.views.post_list')

@login_required
def daily_life(request):
    return render(request, 'blog/daily_life.html')

@login_required
def thumbnail_list(request):
    pic_list = []
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    img_path = os.path.join(base_dir, 'blog/static/img_thumbnail')
    img_dir = os.listdir(img_path)
    for fn in img_dir[1:]:
        pic_list.append(fn)
    return render(request, 'blog/daily_life.html', {'pic_list': pic_list})
