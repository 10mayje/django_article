
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile,Image,Image2,Blog,Comment,Like





# Create your views here.s
def delete(request,pk):
    detail = Blog.objects.get(id=pk)
    if request.method == 'POST':
        Blog.objects.get(id=pk).delete()
        return redirect('/my/')

    return render(request,"myapp/deletepost.html",{'p':detail})

def home(request):
    pos=Blog.objects.all()
    if request.method == 'POST':
        pk=request.POST['post']
        t=Blog.objects.get(id=pk)
        if Like.objects.filter(user=request.user,post=t).exists():
            return redirect('/')
        else:
            f=Like.objects.create(user=request.user,post=t)
            f.save()
        n = Like.objects.filter(post=t).count()
        Blog.objects.filter(id=pk).update(likeno=n)

        return redirect('/')




    return render(request,"myapp/home.html",{'post':pos})
def my(request):
    post=Blog.objects.filter(author=request.user)
    if request.method == 'POST':
        pk = request.POST['post']
        t = Blog.objects.get(id=pk)
        if Like.objects.filter(user=request.user,post=t).exists():
            return redirect('/my/')
        else:
            f = Like.objects.create(user=request.user, post=t)
            f.save()
        n = Like.objects.filter(post=t).count()
        Blog.objects.filter(id=pk).update(likeno=n)

        return redirect('/my/')

    return render(request,"myapp/mypost.html",{'post':post})
def detailpost(request,pk):
    detail = Blog.objects.get(id=pk)
    comit = Comment.objects.filter(post=detail)
    if request.method == 'POST':
        content = request.POST['content']

        comitt = Comment.objects.create(user=request.user, content=content, post=detail,pic=request.user.image.Image)
        comitt.save
        n=Comment.objects.filter(post=detail).count()
        Blog.objects.filter(id=pk).update(commtno=n)

        redirect('detail/{pk}')


    return render(request,"myapp/detail.html",{'p':detail,'text':comit})

def addpost(request):
    if request.method == 'POST' and request.FILES['image']:
        Title=request.POST['Title']
        image=request.FILES['image']
        Contents=request.POST['Content']
        i = Image2.objects.create(Image=image)
        i.save()

        t=Blog.objects.create(author=request.user,Title=Title,Image=i.Image,Contents=Contents,pro=request.user.image.Image)
        t.save()
        return redirect('/')
    return render(request,"myapp/Addpost.html")

def profile(request):
    use=UserProfile.objects.filter(user=request.user)
    return render(request,"myapp/profile.html",{'us':use})
def otherprofile(request,u):
    use=User.objects.filter(user=u)

    return render(request,"myapp/profile.html",{'us':use})
def updateprofile(request):
    if request.method == 'POST' and request.FILES['Image']:
        nicname=request.POST['nicname']
        Phoneno=request.POST['phoneno']
        image=request.FILES['Image']
        Adres=request.POST['adres']
        im = Image2.objects.create(Image=image)
        im.save()


        Image.objects.filter(user=request.user).update(Image=im.Image)
        Blog.objects.filter(author=request.user).update(pro=im.Image)
        Comment.objects.filter(user=request.user).update(pic=im.Image)

        UserProfile.objects.filter(user=request.user).update(nicname=nicname,Phoneno=Phoneno,Adres=Adres)
        return redirect('/upprofile/')
    return render(request,'myapp/editprofile.html')


def reg(request):
    if request.method=='POST':
        username=request.POST['Username']
        email=request.POST['email']

        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('/reg/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken ')
                return redirect('/reg/')

            else:


                user=User.objects.create_user(username=username,password=password1,email=email)
                user.save()


                return redirect("/login/")

        else:
            messages.info(request,'password is not equal to conform password')
            return redirect('/reg/')


    return render(request,"myapp/registation.html")
def login(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid username or password')
            return redirect("/login/")


    return render(request,"myapp/login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')