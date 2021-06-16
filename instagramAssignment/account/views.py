from django.shortcuts import redirect, render
from .models import CustomUser
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        userId = request.POST["userId"]
        password = request.POST["password"]
        user = authenticate(request=request, username=userId, password=password)
        if user is not None: #유저가 존재하면
            login(request, user)
        return redirect('home')   
    else:
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


def register_view(request):
    if request.method == 'POST':
        new_user = CustomUser()
        new_user.username = request.POST["userId"]
        new_user.name = request.POST["name"]
        new_user.nickName = request.POST["nickName"]
        new_user.set_password(request.POST["password"])
        new_user.save()
        login(request, new_user)
        return redirect('home')

        #form을 활용한 정형화된 회원가입
        #form = UserCreationForm(request.POST)
        #if form.is_valid():
        #    user = form.save()
        #    login(request, user)
        #return redirect('home')
    else:
        return render(request, 'signup.html')

        #form을 활용한 정형화된 회원가입
        #form = UserCreationForm()
        #return render(request, 'signup.html',{'form':form})