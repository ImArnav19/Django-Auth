from django.shortcuts import render, redirect
from .forms import Regis
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required,permission_required
from .forms import Postform
from .models import Post


# Create your views here.
@login_required(login_url="/login")
def home(request):
    posts = Post.objects.all()

    if request.method == 'POST':
        post_id = request.POST['post_id']
        post = Post.objects.filter(id = post_id).first()
        if post and ((post.author == request.user) or (request.user.has_perm("myapp.delete_post"))):
            post.delete()

    return render(request,'myapp/home.html',{"posts":posts})

@login_required(login_url="/login")
@permission_required("myapp.add_post",login_url='/login',raise_exception=True)
def create_post(request):
    if request.method == "POST":
        p_form = Postform(request.POST)
        if p_form.is_valid():
            post = p_form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/home')
    else:
        p_form = Postform()

    return render(request, 'myapp/create_post.html',{"form":p_form})

def sign_up(request):
    if request.method == 'POST':
        form = Regis(request.POST)
        if form.is_valid():
            
            user = form.save()
            login(request,user)
            return redirect('/home')

    else:
        form = Regis()

    return render(request,'registration/sign_up.html',{"form":form})
