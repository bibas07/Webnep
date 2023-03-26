from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from .models import Post, Document
from .forms import PostForm,DocumentForm
from .functions import handle_uploaded_file
from django.db import OperationalError
import hashlib
# Create your views here.

def dashboardView(request):
    context = {
        'title':'dashboard',
    }
    try:
        context['documents'] = Document.objects.all()
        context['posts'] = Post.objects.all()
    except OperationalError:
        print("No any posts found")
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            sav = form.save(False)
            sav.aurthur = request.user
            # handle_uploaded_file(request.FILES['file'])
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
    

def docDelete(request, id):
    posts = Document.objects.get(id=id)
    if posts.aurthur == request.user:
        posts.delete()
        return HttpResponseRedirect(reverse(dashboardView))
    else:
        return redirect("dashboard")

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            sav = form.save(commit=False)
            sav.aurthur = request.user
            # file_hash = hashlib.sha384().update(sav)
            # print(file_hash)
            sav.save()
            return redirect('dashboard')
    else:
        form = DocumentForm()
    return render(request, 'blog/file_upload.html', {
        'form': form
    })
