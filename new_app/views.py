from django.shortcuts import render,  redirect, get_object_or_404
from .models import *
from .form import *


def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

def home(request):


    date = Date.objects.all()

    context = {
        "date": date, 
    }
    return render(request, 'includes/index.html', context)
    
def contact(request):
    return render(request, 'includes/contact.html')

def single(request):
    
    return render(request, "includes/single.html")
   

    

def category(request):
    return render(request, 'includes/category.html')

def signup(request):
    form = Registration()
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Login/')
    
    return render(request, 'registration/signup.html', {"form":form})



