from django.shortcuts import render,HttpResponse
from .models import Post
# Create your views here.

def index(request):
    posts = Post.objects.order_by('-created_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def detail(request, post_id):
    if post_id:
        rs = list(Post.objects.filter(id=post_id))
        print(rs)
        return render(request, 'blog/post_detail.html', {'post': rs})
    else:
        return HttpResponse('该文章不存在')