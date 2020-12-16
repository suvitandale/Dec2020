from django.shortcuts import render,HttpResponseRedirect,redirect,get_object_or_404
from .models import Post,User,Login
from .forms import UserForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


class PostListView(ListView):
    model = Post
    template_name = 'blogapp\home.html'  #default template django looks for blogapp/post_list.html
    context_object_name = 'posts'
    ordering = ['created']
    paginate_by = 3


class UserPostListView(ListView):
    model = Post
    template_name = 'blogapp\home.html'  #default template django looks for blogapp/post_list.html
    context_object_name = 'posts'
    ordering = ['created']
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User,email=self.kwargs.get('email'))
        return Post.objects.filter(author=user)

class PostDetailView(DetailView):
    model = Post
    # template_name = 'blogapp\post_detail.html'  #default template django looks for blogapp/post_list.html
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.filter(id=self.request.session['user']).first()
        context["user1"] = user
        return context

class PostCreateView(CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        user = User.objects.filter(id=self.request.session['user']).first()
        form.instance.author = user #user is instance assigned to author key of Post moodel
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blogapp\post_update.html'

    def form_valid(self,form):
        user = User.objects.filter(id=self.request.session['user']).first()
        form.instance.author = user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        user = User.objects.filter(id=self.request.session['user']).first()
        if self.request.user == post.author:
            return True
        return False


from django.urls import reverse
class PostDeleteView(UserPassesTestMixin,DeleteView):
    model = Post
    template_name = 'blogapp/post_delete.html'
    success_url = '/'



def about(request):
    return render(request,'blogapp\habout.html',{'title':'Abaout'})


from django.contrib.auth.hashers import check_password,make_password


def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES)
        print('form---->',form)
        file = request.FILES
        if form.is_valid():
            user = User.objects.filter(email=request.POST.get('email')).first()
            if not user:
                user= User(first_name=request.POST.get('first_name'),last_name=request.POST.get('last_name'),image=file.get('image'),
                           phone=request.POST.get('phone'),email=request.POST.get('email'),password=request.POST.get('password'))
                user.save()
                username = form.cleaned_data.get('first_name')
                messages.success(request,f'Account created for {username} ! Now you are able to Login')
                return redirect('user-login')
            else:
                messages.warning(request,f'Already Account Exist for {user.email}')
        else:
            form = UserForm()
            messages.warning(request,'Please Enter valid credentials..!')
            return render(request, 'blogapp\Register.html', {'form': form})
    else:
        messages.info(request, 'Please create account here..!')
        return render(request,'blogapp\Register.html',{'form':form})


def login(request):
    post = Post.objects.all()
    form = LoginForm()
    if request.method == 'POST':
        femail = request.POST.get('email')
        fpassword = request.POST.get('password')
        user = User.objects.filter(email = femail).first()
        if user:
            if user.password == fpassword:
                post=Post.objects.filter(author = user.id)
                request.session['user'] = user.id
                return redirect('blog-home')
            elif user.is_authenticated:
                return redirect('blog-home')
            else :
                messagess = messages.warning(request,'Please Enter valid credentials..!')
        else:
            messagess = messages.warning(request,'Please create user account first..!')
    return render(request,'blogapp\Login.html', {'form': form})


def profileview(request):
    uid = request.session.get('user')
    user = User.objects.get(id=uid)
    if request.method == 'POST':
        u_form = UserForm(request.POST,files=request.FILES,instance=user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, 'Profile Has Successfully Updated..!')
            return redirect('user-profile')
    else:
        messages.success(request, 'Profile Has Successfully Updated..!')
        u_form = UserForm(instance=user)
    return render(request, 'blogapp\profile.html', {'u_form': u_form,'user':user})

def logout(request):
    return render(request, 'blogapp\logout.html')






