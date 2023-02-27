from django.shortcuts import render,HttpResponse,redirect
from . models import Post,Blogcomment
from django.contrib import messages
from blog.templatetags import extras
from django.contrib.auth.models import User



# Create your views here.
def bloghome(request):
    allposts=Post.objects.all()
    context={"allposts":allposts}
    return render(request,"blog/bloghome.html",context)
def blogpost(request,slug):
    # return HttpResponse(f"this is blogpost: {slug}")
    post=Post.objects.filter(slug=slug).first()
    comments=Blogcomment.objects.filter(post=post,parent=None)
    if request.user.is_authenticated:
        post.views=post.views + 1
        post.save()
    
    replies=Blogcomment.objects.filter(post=post).exclude(parent=None)
    repdict={}
    for reply in replies:
        if reply.parent.s_no not in repdict.keys():
            repdict[reply.parent.s_no]=[reply];
        else:
            repdict[reply.parent.s_no].append(reply)

    # print(repdict)
        
    
    # print(post)
    context={"post":post,"comments":comments,"user":request.user,"repdict":repdict}
    return render(request,"blog/blogpost.html",context)

def postcomment(request):
    if request.method=="POST":
        comment =request.POST.get("comment")
        user =request.user
        postSno =request.POST.get("postSno")
        post =Post.objects.get(s_no=postSno)
        parentsno=request.POST.get("parentsno")

        if parentsno=="":
            comments=Blogcomment(comment=comment,user=user,post=post)
            comments.save()
            
            messages.success(request,"Your comment has been posted successfully")

        else:
            parent=Blogcomment.objects.get(s_no=parentsno)
            comments=Blogcomment(comment=comment,user=user,post=post,parent=parent)
            comments.save()
            messages.success(request,"Your Reply has been posted successfully")
    return redirect(f"/blog/{post.slug}")

        