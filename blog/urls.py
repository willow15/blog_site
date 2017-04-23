from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^add/$', views.CreateArticleView.as_view(), name='create_article'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.DeleteArticleView.as_view(), name='delete_article'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.UpdateArticleView.as_view(), name='update_article'),
]
