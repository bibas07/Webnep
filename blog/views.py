from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from .models import Post
from .forms import PostForm
# Create your views here.

def dashboardView(request):
    context = {
        'title':'dashboard',
        'posts': Post.objects.all()
    }
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            sav = form.save(False)
            sav.aurthur = request.user
            sav.save()
            return redirect("dashboard")
    else:
        form = PostForm()
        context["form"]=form          
    return render(request, 'blog/dashboard.html', context)

def postDelete(request, id):
    posts = Post.objects.get(id=id)
    if posts.aurthur == request.user:
        posts.delete()
        return HttpResponseRedirect(reverse(dashboardView))
    else:
        return redirect("dashboard")
