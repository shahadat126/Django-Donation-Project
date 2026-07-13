from django.shortcuts import render,redirect
from django.contrib import messages 
from .models import Donation
from .forms import DonationForm,SignupForm
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def create_Donation(request):    
    
    form=DonationForm()
    if request.method == "POST":
        form = DonationForm(request.POST,request.FILES)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.user = request.user   # Logged-in user
            donation.save()
            messages.add_message(request,messages.SUCCESS,'Donation Done')
            return redirect("list")
    return render(request,'createDonation.html',{"form": form})
    
    
def home(request):    
    return render(request,'home.html')

def donation_list(request):
    form=Donation.objects.all()
    total_amount = 0
    for forms in form :
        total_amount += forms.amount
        
    return render (request,'Donation_List.html',{"form" : form ,"total_amount": total_amount})
@login_required
def edit(request,id):
    edit_info= Donation.objects.get(id=id)
    form=DonationForm(instance=edit_info)
    if request.method== "POST":
        form = DonationForm(request.POST,request.FILES,instance=edit_info)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Update Done')
            return redirect("list")
    return render (request,"createDonation.html",{ 'form':form})

@login_required
def delete(request,id):
    form= Donation.objects.get(id=id) 
    form.delete()
    messages.add_message(request,messages.SUCCESS,'Delete Done')
    return redirect('list')
    
        
def Signup(request):
    if request.method == "POST":
        forms = SignupForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.add_message(request,messages.SUCCESS,"successfully submitted")
            return redirect("home")
    else:
        forms = SignupForm()
    return render(request, 'signup.html',{"forms":forms})

def Login(request):
    if request.method == "POST":
        forms = AuthenticationForm( data =request.POST)
        if forms.is_valid():
            username=forms.cleaned_data.get('username')
            password=forms.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                
                login(request, user)
                
                messages.add_message(request,messages.SUCCESS,"login successfully")
                return redirect("home")
            else:
                messages.add_message(request,messages.SUCCESS,"invalid credentials")
    else:
        forms = AuthenticationForm()
    return render(request,"signup.html",{"forms": forms})
def Logout(request):
    logout(request)
    messages.add_message(request,messages.SUCCESS,"logout")
    return  redirect("home")
@login_required
def UserProfile(request): 
    form = Donation.objects.filter(user=request.user)
    return render (request,'profile.html',{"form" : form })               