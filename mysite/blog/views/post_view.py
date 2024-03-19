from django.http import HttpResponse
from django.views import generic

from mysite.blog.models import Post


class PostView(generic.ListView):
    query = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
