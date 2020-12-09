from django.shortcuts import render,HttpResponseRedirect,redirect
from .models import Post,User,Login
from .forms import UserForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate

def home(request):
    posts = Post.objects.all()
    return render(request,'blogapp\home.html',{'posts':posts})

def about(request):
    return render(request,'blogapp\habout.html',{'title':'Abaout'})


def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            user = User.objects.filter(email=request.POST.get('email')).first()
            if not user:
                form.save(commit=False)
                form.save()
                username = form.cleaned_data.get('first_name')
                messages.success(request,f'Account created for {username} ! Now you are able to Login')
                return redirect('user-login')
            else:
                messages.warning(request,f'Already Account Exist for {user.email}')
        else:
            form = UserForm()
            messages.warning(request,'Please Enter valid credentials..!')
            return render(request, 'blogapp\Register.html', {'form': form})

    return render(request,'blogapp\Register.html',{'form':form})


def login(request):
    post = Post.objects.all()
    if request.method == 'POST':
        femail = request.POST.get('email')
        fpassword = request.POST.get('password')
        user = User.objects.filter(email = femail).first()
        if user:
            if user.email == femail and user.password == fpassword :
                post=Post.objects.filter(author = user.id)
                request.session['user'] = user.id
                return redirect('blog-home')
            else :
                messagess = messages.warning(request,'Please create user account first..!')
        else:
            messagess = messages.warning(request,'Please Enter valid credentials..!')
    else:
        form = LoginForm()
        messagess = messages.info(request, 'Please Login Here..!')

    return render(request, 'blogapp\Login.html', {'form': form})


def profileview(request):
    uid = request.session.get('user')
    user = User.objects.get(id=uid)
    return render(request, 'blogapp\profile.html', {'user': user})

def logout(request):
    return render(request, 'blogapp\logout.html')
