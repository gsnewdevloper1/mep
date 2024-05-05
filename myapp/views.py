from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from django.contrib import messages
from myapp.models import pending_work , work_details , contactus
from datetime import datetime


# Create your views here.
def index(request):
    return render(request,'index.html')




def login_page(request):
    if request.method =='POST':
        username = request.POST.get('user')
        password = request.POST.get('pass')
        if not User.objects.filter(username = username).exists():
            messages.error(request , 'Invalid Username')
            return redirect('/login')        
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request , 'Invalid Password')
            return redirect('/login')            
        else:
            login(request , user)
            return redirect('/mep')           
    else:
        return render(request, 'login.html')   



def logout_page(request):
    logout(request)
    return redirect('/login')




def mep(request):
    mepdata = pending_work.objects.all()
    context ={
        'work' : mepdata,
    }
    return render(request, 'mep.html' , context)

    

@login_required(login_url='login')
def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        data = pending_work(title=title , desc=desc)
        data.save()
    return redirect('/mep')




@login_required(login_url='login')
def comment(request, sno):
    pw =pending_work.objects.get(pk=sno)
    wd = work_details.objects.filter(sno_com=sno)
    context = {
        'pending': pw ,
        'work': wd
    }
    if request.method == 'POST':
        desc = request.POST.get('desc')
        
        data = work_details(sno_com_id=sno ,desc=desc )
        data.save()
        return render(request,'comment.html', context)     
    return render(request,'comment.html', context)



@login_required(login_url='login')
def delete_page(request, sno):
    if request.method =='POST':
       pi = pending_work.objects.get(pk=sno)
       pi.delete()
    return redirect('/mep')


def about(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        mes = contactus(name=name,email=email,phone=phone,message=message)
        mes.save()

    return render(request , 'contact.html')