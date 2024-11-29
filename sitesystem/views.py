from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import MyPost, Comment
from .forms import CommentCreateForm
from django import forms

# Create your views here.
class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'orderby_records'
    queryset = MyPost.objects.order_by('-posted_at')
    paginate_by = 4

class PostDetail(DetailView):
    template_name = 'post.html'
    model = MyPost

class StrategyView(ListView):
    template_name = 'strategy_list.html'
    model = MyPost
    context_object_name = 'strategy_records'
    queryset = MyPost.objects.filter(category='strategy').order_by('-posted_at')
    paginate_by = 2

class CheatcodeView(ListView):
    template_name = 'cheatcode_list.html'
    model = MyPost
    context_object_name = 'cheatcode_records'
    queryset = MyPost.objects.filter(category='cheatcode').order_by('-posted_at')
    paginate_by = 2

class RtaView(ListView):
    template_name = 'rta_list.html'
    model = MyPost
    context_object_name = 'rta_records'
    queryset = MyPost.objects.filter(category='rta').order_by('-posted_at')
    paginate_by = 2

class NewsView(ListView):
    template_name = 'news_list.html'
    model = MyPost
    context_object_name = 'news_records'
    queryset = MyPost.objects.filter(category='news').order_by('-posted_at')
    paginate_by = 2

class CommentView(CreateView):
    template_name = 'comment_form.html'
    model = Comment
    form_class = CommentCreateForm

    def form_valid(self, form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(MyPost, pk=post_pk)
        comment = form.save(commit=False)
        comment.target = post
        comment.save()
        return render('sitesystem:post', pk=post_pk)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(MyPost, pk=self.kwargs['pk'])
        return context


def viewer(request, post_id):
    post = get_object_or_404(MyPost, id=post_id)
    post.views += 1 #閲覧数をインクリメント
    post.save()
    return render(request, 'index.html', {'post': post})