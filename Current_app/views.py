from django.shortcuts import render
from django.http import HttpResponse
from .models import Current, Topic, Post
# Create your views here.
from django.contrib.auth.decorators import permission_required


@permission_required('Current_app.home')
def home(request):
    currents = Current.objects.all()
    posts = Post.objects.all()
    topics = Topic.objects.all()

    context = {"currents": currents,
               "posts": posts,
               "topics": topics
               }
    return render(request, 'Current_app/index.html', context)
