from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Board
from .models import Post
from .models import Purchase
from .models import Request
from .forms import PostForm
from .forms import PurchaseRequestForm
from django.shortcuts import render, get_object_or_404


from django.views.generic import TemplateView
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the Inventory App index.")

class AboutPageView(TemplateView):
    template_name = 'about.html'

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'inven_app/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'inven_app/post_detail.html', {'post': post})   

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'inven_app/post_edit.html', {'form': form})


#def purchase_request_new(request)
#    form = PostForm()
#    return render(request, 'inven_app/purchase_request_edit.html', {'form': form})
#def purchase_request_detail(request, pk):

def purchase_list(request):
    listitems = Request.objects.all()
    return render(request, 'inven_app/purchase_list.html', {'listitems': listitems})

def purchase_request_new(request):
    if request.method == "POST":
        form = PurchaseRequestForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.requester = request.user
            post.save()
            return redirect('purchase_request_detail')
    else:
        form = PurchaseRequestForm()
    return render(request, 'inven_app/purchase_request_edit.html', {'form': form})


