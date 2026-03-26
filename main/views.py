from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
	posts = Post.objects.all().order_by('-created_at')
	return render(request, 'main/index.html', {'posts': posts})

def post_detail(request, post_id):
	post = Post.objects.get(id=post_id)
	return render(request, 'main/post_detail.html', {'post': post})
