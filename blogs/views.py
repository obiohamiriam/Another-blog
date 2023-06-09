from django.shortcuts import render, get_object_or_404
from.models import Post
from django.core.paginator import Paginator


# Create your views here.
def post_list(request):
    posts_list = Post.published.all()


    # Pagination with 3 posts per page
    paginator = Paginator(posts_list, 3)
    page_number = request.GET.get('page', 1 )
    posts = paginator.page(page_number)
    return render(request,
                           'blogs/post/list.html',
                           {'posts':posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED, )
    return render(request, 'blogs/post/detail.html',  {'post':post})

