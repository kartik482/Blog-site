from email import message
from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from blog.models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q #for multiple queryset in search function (title and author)


# Create your views here.
from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("this is home")
    return render(request,"home/home.html")
def contact(request):
    # messages.success(request, 'welcome to contact')
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        content=request.POST.get("content")
        # print(name,email,content,phone)
        if len(name)<2 or len(email)<5 or len(phone)<5 or len(content)<4:
            messages.error(request, 'Please Fill The Form Correctly')
        else:
            contact=Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request, 'your query has been sent')


    return render(request,"home/contact.html")
    # return HttpResponse("this is contact")
def about(request):
    messages.success(request, 'Welcome to About')
    return render(request,"home/about.html")
    # return HttpResponse("this is about")


def search(request):
    query=request.GET.get("query")
    if len(query)<=2:
        allposts=Post.objects.all()
        messages.error(request, 'Please Search For Valid Data')
    else:
        allposts=Post.objects.filter(Q(title__icontains=query) | Q(author__icontains=query)) # Q is used for multiple queryset in search function (title and author)
        if len(allposts)==0:
            messages.warning(request, 'Please Fill The Form Correctly')
    params={"allposts":allposts,"query":query}
    return render(request,"home/search.html",params)

def handlesignup(request):
    if request.method=="POST":
        #get the signup parameters
        username=request.POST.get("username")
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        email=request.POST.get("email")
        pass1=request.POST.get("pass1")
        pass2=request.POST.get("pass2")


        #validation
        if len(username)>13:
            messages.error(request,"username must be of 12 characters or less")
            return redirect("/")
        if not username.isalnum():
            messages.error(request,"username should contain letters and numbers only")
            return redirect("/")
        if len(pass1)<5 :
            messages.error(request,"password should be of 6 characters or more")
            return redirect("/")
        if pass1 != pass2:
            messages.error(request,"passwords does not match")
            return redirect("/")
    
        #create userr
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=firstname
        myuser.last_name=lastname
        myuser.save()
        messages.success(request,"your BLOGSite account has been successfully created")
        return redirect("/")

    else:
        return HttpResponse("error-404=not found")




def handlelogin(request):
    if request.method=="POST":
        #get the login parameters
        loginusername=request.POST.get("loginusername")
        loginpassword=request.POST.get("loginpassword")
        user=authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"successfully logged in")
            return redirect("/")
        else:
            messages.error(request,"invalid credentials entered.Please try again")
            return redirect("/")

    return HttpResponse("error-404=not found")
    
    
    
    
def handlelogout(request):
    logout(request)
    messages.success(request,"successfully logged out")
    return redirect("home")

    # return HttpResponse("error-404=not found")
