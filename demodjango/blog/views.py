from django.shortcuts import render
from django.http import HttpResponse
from .models import postForm
def blog(request):
    pF = postForm.objects.all() 
    return render(request, 'blog/blog.html',{'pF':pF})

def postDetail(request,id):
    pD=postForm.objects.get(id=id)
    return render(request,'blog/postDetail.html',{'pD':pD})
