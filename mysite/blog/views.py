from django.shortcuts import render, get_object_or_404,redirect, HttpResponse
from django.utils import timezone
from django.core.mail import send_mail, BadHeaderError
from .models import Post as post_p, Comment as comment_s, PostSection as post_s
from .forms import PostForm, CommentForm, RequiredFormSet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.conf import settings
from django.forms import modelformset_factory
import os

###############################################
# Main page request along with visits session #
###############################################


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
    # return HttpResponse(visits)
    return response


###############################################
# Post list, groups, and detail section       #
###############################################


@login_required(login_url='/login/')
# Create your views here.
def post_list(request):
    posts = post_p.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


@login_required(login_url='/login/')
def post_group(request, post_type):
    posts_type = post_p.objects.filter(type=post_type).order_by('publish_date')
    return render(request, 'blog/post_list.html', {'posts': posts_type})


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
def post_section(request, pk):
    post = get_object_or_404(post_p, pk=pk)
    post_section_formset = modelformset_factory(post_s, fields=('text', 'code'), formset=RequiredFormSet)
    if request.method == "POST":
        formset = post_section_formset(request.POST, request.FILES)
        if formset.is_valid():
            for i in range(0, formset.total_form_count()):
                form = formset.forms[i]
                form.empty_permitted = False
                post_sections = form.save(commit=False)
                post_sections.post = post
                post_sections.save()
            return redirect('blog.views.post_detail', pk=post_sections.post.pk)
            # formset.save()
    else:
        formset = post_section_formset(queryset=post_s.objects.filter(post__id=post.pk))
    return render(request, 'blog/post_edit.html', {'formset': formset})


@login_required(login_url='/login/')
def post_detail(request, pk):
    post_info = get_object_or_404(post_p, pk=pk)
    # print(post_info.text)
    return render(request, 'blog/post_detail.html', {'post': post_info})


@login_required(login_url='/login/')
def post_edit(request, pk):
    post = get_object_or_404(post_p, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
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
def add_comment_to_post(request, pk):
    post = get_object_or_404(post_p, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


@login_required(login_url='/login/')
def comment_approve(request, pk):
    comment = get_object_or_404(comment_s, pk=pk)
    comment.approve()
    return redirect('blog.views.post_detail', pk=comment.post.pk)


@login_required(login_url='/login/')
def comment_remove(request, pk):
    comment = get_object_or_404(comment_s, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog.views.post_detail', pk=post_pk)


#################################################
# Documentation(Python, Django, GitHub) section #
#################################################

@login_required(login_url='/login/')
def python(request):
    return render(request, 'blog/python.html')


@login_required(login_url='/login/')
def django(request):
    return render(request, 'blog/django.html')


@login_required(login_url='/login/')
def github(request):
    return render(request, 'blog/github.html')


###############################################
# User section (Registration, Login, Logout)  #
###############################################

def signup_view(request):
    if request.method == "POST":
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            new_user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            login(request, new_user)
            return redirect('blog.views.post_list')
    else:
        signup_form = UserCreationForm()
    return render(request, 'blog/signup.html', {'signup_form': signup_form})


def login_view(request):
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
    logout(request)
    return redirect('blog.views.main_page')

###############################################
# Picture and Image section                   #
###############################################


@login_required(login_url='/login/')
def contact(request):
    if request.method == "POST":
        subject = request.POST.get("subject")
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        if subject and name and message:
            try:
                send_mail(subject, message, "%s from %s <do_not_replay@domain.com>" %(name, email), [settings.EMAIL_HOST_USER], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponse('Thank you for your message.')
        else:
            return HttpResponse('Please make sure fields are filled and valid.')
    return render(request, 'blog/contact.html')









