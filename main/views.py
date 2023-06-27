from django.shortcuts import render,redirect
from .converter import Convert
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.core.files.base import ContentFile
from .models  import upload
from django.shortcuts import render
import urllib.request
import secrets
import random
import string
from .ytdown import download
from . models import Audio,TimeStamp
from . models import Audio
from .sentiment import printAnalysis
def Login(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/homepage/')
        else:
            print(user)
            # Display an error message
            # print("not found")
            pass
    return render(request, 'main/login.html')

def Logout(request):
    logout(request)
    return redirect('/')

def sign_up(request):
  
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        # print('hello')
        if form.is_valid():
            # print('hello')
            pass
        try:  
            form.save()
            username=form.cleaned_data.get('username')
            print("account created")
            messages.success(request,f'Account created for {username}')
        except Exception as e:
            print(e)   

        return redirect('login')
    else:
        form = UserRegisterForm()
        

    return render(request, 'main/signup.html',{'form':form})
def Home(request):
    allaudios = Audio.objects.filter(uploaded_by=request.user.id)
    print(allaudios)
    context = {
            'allaudios':allaudios
        }
    return render(request,'main/homepage.html',context)

def askconvert(request):

    if request.method=='POST':
        videom = request.FILES.get("vid")
        temp = upload()
        temp.video.save(videom.name.strip().replace(" ","_"),videom)
        temp.save()
        id = Convert("main/media/"+videom.name.strip().replace(" ","_"),request,temp.id)
        temp.delete()
        allaudios = Audio.objects.filter(uploaded_by=request.user.id)
        context = {
            'allaudios':allaudios
        }
        if id==-1:
            return render(request,'main/noaudio.html')
        return redirect('/audio_detail/'+ str(id))
    allaudios = Audio.objects.filter(uploaded_by=request.user.id)
    print(allaudios)
    context = {
            'allaudios':allaudios
        }
    return render(request,'main/homepage.html',context)

def download_view(request):
    
    if request.method=='POST':
        url = request.POST.get("url")
        id = download(url,request)
        if id != -1:
            return redirect('/audio_detail/'+ str(id))
        else:
            return render(request,'main/noaudio.html') 


    return render(request, 'download.html', {'url': url})

def audio_detail(request,pk):
    audio = Audio.objects.get(id=pk)
    print(request.POST.get('time'))
    if request.POST:
        timestamp = TimeStamp()
        timestamp.audio = audio
        timestamp.comment = request.POST.get('comment')
        timestamp.time = '00:' + request.POST.get('time')
        timestamp.save()
    comments = TimeStamp.objects.filter(audio = audio.id).order_by("time").values()
    allaudios = Audio.objects.filter(uploaded_by=request.user.id)
    context = {
        'comments':comments,
        "audio":audio,
        'allaudios':allaudios,
    }
    return render(request,'main/pagetwo.html',context)

def editname(request,pk):
    audio = Audio.objects.get(id=pk)
    audio.audioname=request.POST.get('editname')
    audio.save()
    context = {
        "audio":audio,
    }
    return render(request,'main/pagetwo.html',context)
def audio_display(request,pk):
    audio = Audio.objects.get(id=pk)
    timestamp=TimeStamp.objects.filter(audio=audio).all()
    allaudios = Audio.objects.filter(uploaded_by=request.user.id)
    context={
        'timestamp':timestamp,
        'allaudios':allaudios,
        'pk':pk,
        "audio":audio
    }
    return render(request,'main/detail.html',context)

def deletecomment(request,pk):
    if request.method=='POST':
        print(pk)
        tst=TimeStamp.objects.get(pk=pk)
        tst.delete()
        id=request.POST.get('hiddenfield')
        
    return redirect('/audio_detail/' + str(id))

def delete_audio(request,pk):
    audio = Audio.objects.get(id=pk)
    audio.delete()
    return redirect('/homepage/')

def Analytics(request,pk):
    # print(getURL(request))
    audio = Audio.objects.get(id=pk)
    if audio.positive==0 and audio.negative==0 and audio.neutral==0:
        print(Audio.objects.get(id=pk).url)
        printAnalysis(request,Audio.objects.get(id=pk).url)
    return redirect('/audio_analysis/' + str(pk))

def Analysis(request,pk):
    audio = Audio.objects.get(id=pk)
    pr=(audio.positive)/(audio.negative+audio.positive)
    context={
        'positive': audio.positive,
        'negative': audio.negative,
        'neutral': audio.neutral,
        'ratio': pr
    }
    return render (request,'main/analytics.html', {'context': context})