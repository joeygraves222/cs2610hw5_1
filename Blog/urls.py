from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('About', views.About, name='About'),
    path('TechTips', views.TechTips, name='TechTips'),
    path('Archive', views.Archive, name='Archive'),
    path('NewPost', views.NewPost, name='NewPost'),
    path('CreateNewPost', views.CreateNewPost, name='CreateNewPost'),
    path('AddNewComment/(?P<BlogId>[1-9]+)$', views.AddNewComment, name='AddNewComment'),
    path('Post/(?P<Id>[1-9]+)$', views.Post, name='Post'),
]
