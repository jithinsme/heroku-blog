from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin)
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    )


def home(request):

    context = {
                'posts' : Post.objects.all(),
                'title' : "Home"
            }
    return render(request, 'blog/home.html', context)

class PostDetailView(DetailView):
    model = Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # blog/post_list.html <app-name>/<model>_<viewtype>
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_home.html' # blog/post_list.html <app-name>/<model>_<viewtype>
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        self.user = get_object_or_404(User, username=self.kwargs['username'])
        return Post.objects.filter(author=self.user).order_by('-date_posted')



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = '/'

    def test_func(self):
        """ custom code for checking user pass  """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    LoginRequiredMixin for class view,
    UserPassesTestMixin for same user created can update the post
    """
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_update.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """ custom code for checking user pass  """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def about(request):
    return render(request, 'blog/about.html')
