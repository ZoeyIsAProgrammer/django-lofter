from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
# def home(request):
#     # return HttpResponse("<h1>Home Page</h1>")
#     posts = Post.objects.all()
#     return render(request, "blog/home.html", {"posts": posts})
class HomeView(ListView):
    model = Post
    paginate_by = 5
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = "-date_posted"


class UserDetailView(ListView):
    model = Post
    paginate_by = 5
    template_name = "blog/user_detail.html"
    context_object_name = "posts"
    ordering = "-date_posted"

    def get_queryset(self):
        username = self.kwargs.get("username")
        user = get_object_or_404(User, username=username)
        posts = user.post_set.all().order_by("-date_posted")
        return posts

    def this_user(self):
        username = self.kwargs.get("username")
        user = get_object_or_404(User, username=username)        
        return user


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post.html"

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        curr_post = Post.objects.get(id=self.kwargs['pk'])
        liked = False
        if curr_post.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = curr_post.likes.count()
        data['is_liked'] = liked
        return data


def post_like(request, pk):
    post = get_object_or_404(Post, id=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect(f'/post/{pk}/#likepart')


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'subtitle', 'content', 'image']
    # fields = '__all__'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['view_type'] = "create"
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'subtitle', 'content', 'image']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['view_type'] = "update"
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        else:
            return False