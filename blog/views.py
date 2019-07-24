from django.shortcuts import render, redirect
from .models import Blog, Mentee, Mentor
from .forms import BlogForm, MenteeForm, MentorForm

# Create your views here.
def index(request):
    return (render(request, 'index.html', {}))

def blog(request):
    list_blog = Blog.objects.all()
    return render(request, 'blog.html', {'Blog': list_blog})

def mentee(request):
    list_mentee = Mentee.objects.all()
    return render(request, 'mentee.html', {'Mentee': list_mentee})

def mentor(request):
    list_mentor = Mentor.objects.all()
    return render(request, 'mentor.html', {'Mentor': list_mentor})

def author(request):
    return (render(request, 'author.html', {}))

def input_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog')
    else:
        form = BlogForm()
    return render(request, 'input_blog.html', {'form': form})

def input_mentee(request):
    if request.method == "POST":
        form = MenteeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('mentee')
    else:
        form = MenteeForm()
    return render(request, 'input_mentee.html', {'form': form})

def input_mentor(request):
    if request.method == "POST":
        form = MentorForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('mentor')
    else:
        form = MentorForm()
    return render(request, 'input_mentor.html', {'form': form})