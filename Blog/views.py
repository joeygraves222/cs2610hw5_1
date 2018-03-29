from django.shortcuts import render, get_object_or_404
from django.utils import timezone

# Create your views here.

from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt
from .models import BlogPost
from .models import Comment
from .forms import BlogForm, CommentForm


def index(request):
    # template = loader.get_template("index.html")
    BlogList = BlogPost.objects.order_by("PostedDate").annotate(Comment_Count=Count('comments'))[:3]
    return (render_to_response("Blog/index.html", {'time': timezone.now(), 'BlogsList': BlogList}))

def About(request):
    return (render_to_response("Blog/About.html", {'time': timezone.now(),}))

def TechTips(request):
    return (render_to_response("Blog/TechTips.html", {'time': timezone.now(),}))

def Archive(request):
    BlogList = BlogPost.objects.all().annotate(Comment_Count=Count('comments'))
    return (render_to_response("Blog/Archive.html", {"time": timezone.now(), 'BlogsList': BlogList}))

def NewPost(request):
    form = BlogForm()
    return (render_to_response("Blog/NewPost.html", {'time': timezone.now(), 'Form': form}))

def Post(request, Id):
    post = BlogPost.objects.get(pk=Id)
    comments = Comment.objects.filter(Blog=Id)
    form = CommentForm()
    return (render_to_response("Blog/Post.html", {"time": timezone.now(), 'Blog': post, 'CommentsList': comments, 'Form': form}))

@csrf_exempt
def CreateNewPost(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            newPost = BlogPost()
            newPost.Title = request.POST['title']
            newPost.AuthorName = request.POST['author']
            newPost.Content = request.POST['content']
            newPost.PostedDate = timezone.now()
            newPost.save()
            BlogList = BlogPost.objects.order_by("PostedDate").annotate(Comment_Count=Count('comments'))[:3]
            return (render_to_response("Blog/index.html", {'time': timezone.now(),  'BlogsList': BlogList}))

@csrf_exempt
def AddNewComment(request, BlogId):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            newPost = Comment()
            newPost.NickName = request.POST['nickname']
            newPost.Email = request.POST['email']
            newPost.Content = request.POST['content']
            newPost.PostedDate = timezone.now()
            post = BlogPost.objects.get(pk=BlogId)
            newPost.Blog = post
            newPost.save()
            form = CommentForm()
            comments = Comment.objects.filter(Blog=post)
            return (render_to_response("Blog/Post.html", {"time": timezone.now(), 'Blog': post, 'CommentsList': comments, 'Form': form}))