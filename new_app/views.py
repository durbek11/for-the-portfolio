from django.shortcuts import render,  redirect, get_object_or_404
from .models import *
from .form import *

def home(request):


    date = Date.objects.all()

    context = {
        "date": date, 
         "products":products,
    }
    return render(request, 'includes/index.html', context)
    
def contact(request):
    return render(request, 'includes/contact.html')

def single(request, pk):
    which_one = Product.objects.get(id=pk)
    post = get_object_or_404(Product, id=pk)
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('/#product')
    else:
        comment_form = CommentForm()

    context= {
        'new_comment': new_comment,
        'comments': comments,
        'comment_form': comment_form,
        "which_one":which_one
        }
   
    return render(request, "includes/single.html", context)
   

    

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



