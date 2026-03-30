from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
	posts = Post.objects.all().order_by('-created_at')
	return render(request, 'main/index.html', {'posts': posts})

def post_detail(request, post_id):
	post = get_object_or_404(Post, id=post_id)
	return render(request, 'main/post_detail.html', {'post': post})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('index')
	return render(request, 'registration/login.html')

def logout_view(request):
	logout(request)
	return redirect('index')

@login_required
def create_post(request):
	if request.method = 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('index')
	else:
		form = PostForm()
	return render(request, 'main/create_post.html', {'form': form})
