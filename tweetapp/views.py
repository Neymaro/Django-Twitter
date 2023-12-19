from django.shortcuts import render,redirect
from . import models
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views import generic

# Create your views here.

def listtweets(request):
     tweets_list = models.Tweet.objects.all()
     dictionarytweet={"tweets":tweets_list}
     return render(request,"tweetapp/listtweets.html",context=dictionarytweet)

@login_required(login_url="/login")
def showmytweet(request):
    mytweets = models.Tweet.objects.filter(username=request.user).all()
    mytweetsdic = {"mytweets":mytweets}
    return render(request,'tweetapp/showmytweet.html',context=mytweetsdic)

@login_required(login_url="/login")
def addtweet(request):
    if request.POST:
        tweet= request.POST['tweet']
        models.Tweet.objects.create(username=request.user,tweet=tweet,time="")
        return redirect(reverse('tweetapp:listtweets'))
    else:
        return render(request,'tweetapp/addtweet.html')
    
@login_required
def deletemytweet(request, id):
    mytweet = models.Tweet.objects.get(pk=id)
    if request.user == mytweet.username:
        models.Tweet.objects.filter(id=id).delete()
        return(redirect('tweetapp:listtweets'))
    
    
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
