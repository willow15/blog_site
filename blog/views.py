from .models import Article
from .forms import ArticleForm, UserForm
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth import authenticate
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit = False)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        user = authenticate(request, username = username, password = password)

        if user is not None and user.is_active:
            return redirect('login')
    return render(request, 'blog/register.html', {'form':form})


class IndexView(ListView):
    def get_queryset(self):
        return Article.objects.filter(user=self.request.user)

    def get(self, request):
        if not request.user.is_authenticated():
            return redirect('login')
        else:
            object_list = self.get_queryset()
            return render(request, 'blog/index.html', {'articles': object_list})


@method_decorator(login_required, name='dispatch')
class DetailView(DetailView):
    template_name = 'blog/detail.html'
    model = Article

    def get_queryset(self):
        return Article.objects.filter(user=self.request.user)

@method_decorator(login_required, name='dispatch')
class CreateArticleView(CreateView):
    template_name = 'blog/create_article.html'
    form_class = ArticleForm
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateArticleView, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class DeleteArticleView(DeleteView):
    template_name = 'blog/delete_article.html'
    model = Article
    success_url = reverse_lazy('blog:index')

@method_decorator(login_required, name='dispatch')
class UpdateArticleView(UpdateView):
    template_name = 'blog/update_article.html'
    model = Article
    fields = ['title', 'content']
    success_url = reverse_lazy('blog:index')
