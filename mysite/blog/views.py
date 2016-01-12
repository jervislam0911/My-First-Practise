from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import post as post_p
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.http import Http404
from django.shortcuts import HttpResponse
import os


def main_page(request):
    visits = request.session.get('visits')
    if not visits:
        visits = 0
    # print('before', visits)
    reset_last_visit_time = False
    last_visit = request.session.get('last_visit')

    if last_visit:
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
        if (datetime.now() - last_visit_time).seconds > 0:
            visits += 1
            reset_last_visit_time = True
    else:
        reset_last_visit_time = True

    request.session['visits'] = visits
    # request.session.save()

    if reset_last_visit_time:
        request.session['last_visit'] = str(datetime.now())
    response = render(request, 'blog/index.html')
    print('Total visit: ', visits)
    return response


@login_required(login_url='/login/')
# Create your views here.
def post_list(request):
    posts = post_p.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required(login_url='/login/')
def post_group(request, post_type):
    posts_type = post_p.objects.filter(type=post_type).order_by('publish_date')
    return render(request, 'blog/post_list.html', {'posts': posts_type})
    # django_posts = post_p.objects.filter(type='Django').order_by('publish_date')
    # github_posts = post_p.objects.filter(type='GitHub').order_by('publish_date')
    # posts = post_p.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    # return render(request, 'blog/post_list.html', {'posts': posts})

@login_required(login_url='/login/')
def post_detail(request, pk):
    post_info = get_object_or_404(post_p, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post_info})

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
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








@login_required(login_url='/login/')
def python(request):
    return render(request, 'blog/python.html')
@login_required(login_url='/login/')
def django(request):
    return render(request, 'blog/django.html')
@login_required(login_url='/login/')
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
    #     username = request.POST.get('un')
    #     password = request.POST.get('ps')
    #     m = post_p.objects.get(username=request.POST['us'])
    #     if m.password == request.POST['ps']:
    #         request.session['member_id'] = m.id
    #         return HttpResponse("You're logged in.")
    #     else:
    #         return HttpResponse("Your username and password didn't match.")
    if request.method == "POST":
        username = request.POST.get('un')
        password = request.POST.get('ps')
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:

            # print(request.session.session_key)
            login(request, user)
            # print(request.session.session_key)
            return redirect('blog.views.post_list')
        elif not request.user.is_authenticated():
            return render(request, 'blog/errorlogin.html')
    else:
        return render(request, 'blog/login.html')


def logout_view(request):
    # print(request.session.session_key)
    logout(request)
    return redirect('blog.views.main_page')









@login_required(login_url='/login/')
def daily_life(request):
    return render(request, 'blog/daily_life.html')

@login_required(login_url='/login/')
def thumbnail_list(request):
    pic_list = []
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    img_path = os.path.join(base_dir, 'blog/static/img_thumbnail')
    img_dir = os.listdir(img_path)
    for fn in img_dir[1:]:
        pic_list.append(fn)
    return render(request, 'blog/daily_life.html', {'pic_list': pic_list})
