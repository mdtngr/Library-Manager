from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from users.forms import RegistrationForm,  UserAuthenticationForm, ProfileForm
from users.models import UserData,Userprofile
from django.contrib.auth.decorators import login_required
from transactions.models import TransactionDetails

# Create your views here.

def home_screen_view(request):
    # print(request.headers)
    return render(request, 'items/all_items.html', {})

def dash_view(request):
    context={}
    context['all_users'] =  UserData.objects.all()
    
    return render(request, 'users/dash.html', context)

def all_students_view(request):
    context={}
    context['all_users'] =  UserData.objects.all()
    
    return render(request, 'users/students.html', context)

def  registration_view(request):
    context =   {}

    if request.POST:
        form    =   RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            email               =   form.cleaned_data.get('email')
            raw_password        =   form.cleaned_data.get('password1')
            name                =   form.cleaned_data.get('first_name')


            account = authenticate(email = email, password = raw_password )

            login(request, account)
            profile = Userprofile.objects.create(user=request.user, username = name, email = email)
            profile.save()

            return redirect('home')

        else:
            context['registration_form'] = form
    else: #GET
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'users/register.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):
    context ={}

    user = request.user

    if user.is_authenticated:
        return redirect("home")

    if request.POST:
        form =  UserAuthenticationForm(request.POST)
        
        if form.is_valid():
            email =  request.POST['email']
            password = request.POST['password']

            user = authenticate(email = email, password = password)

            if user:
                login(request, user)
                return redirect("home")

    else:
        form = UserAuthenticationForm()
        
    context['login_form'] = form
    return render( request, 'users/login.html', context)

@login_required
def profile_view(request):
    profile = Userprofile.objects.get(user=request.user)
    transactions = TransactionDetails.objects.filter(user=request.user)
    return render(request, 'users/profile.html', {'profile':profile,'transactions':transactions})

@login_required
def profileedit_view(request):
    show = Userprofile.objects.get(user=request.user)
    if request.method=='GET':
        form = ProfileForm(instance=show)   
        return render(request,'users/profileedit.html',{'profile':show,'form':form})
    else:
        form = ProfileForm(request.POST, request.FILES, instance=show)
        form.save()
        return redirect('profile')



    


