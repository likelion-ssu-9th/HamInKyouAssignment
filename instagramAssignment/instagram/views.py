from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone #pub_date 위해서
from .models import Post

# 페이지 렌더링할 때는 .html로 하고
# 페이지 리다이렉션할 때는 그냥 url name으로 하는구나!

# Create your views here.
# 메인페이지 렌더링
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts':posts})
# 디테일 페이지 렌더링
def detail(request, postId):
    post = get_object_or_404(Post, pk = postId)
    return render(request, 'detail.html', {'post':post})

# 생성 페이지 렌더링
def new(request):
    return render(request,'new.html')

# 생성하는 API
def create(request):
    new_post = Post()
    new_post.writer = request.POST["writer"]
    new_post.body = request.POST["body"]
    new_post.pub_date = timezone.now()
    new_post.save()
    return redirect('detail', new_post.id)

# 수정 페이지 렌더링
def edit(request, postId):
    edit_post = Post.objects.get(id= postId)
    return render(request,'edit.html',{'post': edit_post})

# 수정하는 API
def update(request, postId):
    update_post = Post.objects.get(id = postId)
    update_post.writer = request.POST["writer"]
    update_post.body = request.POST["body"]
    update_post.pub_date = timezone.now()
    update_post.save()
    return redirect('detail', update_post.id)

# 삭제하는 API
def delete(request, postId):
    delete_post = Post.objects.get(id=postId)
    delete_post.delete()
    return redirect('home')