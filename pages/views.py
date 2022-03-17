from django.shortcuts import render

from .models import Contact,Newsletter,Gallery,Events,Home
def index(request):
    if request.method =='POST':
           
        email = request.POST['email']

        c = Newsletter( email=email)
        c.save()
        return render(request,'pages/index.html')
    details = Gallery.objects.all()
    
    events = Events.objects.all()
    
    slider =Home.objects.all()

    context ={
        'details': details,
        'events': events,
        'slider': slider,
        
    }      
    return render(request,'pages/index.html',context)

def about(request):
    if request.method =='POST':
           
        email = request.POST['email']

        c = Newsletter( email=email)
        c.save()
        return render(request,'pages/about.html')    
    return render(request,'pages/about.html')



def contact(request):
    if request.method =='POST':
           
        email = request.POST['email']

        c = Newsletter( email=email)
        c.save()
        return render(request,'pages/contact.html')    
    return render(request,'pages/contact.html')




def gallery(request):
    if request.method =='POST':
        
        email = request.POST['email']

        c = Newsletter( email=email)
        c.save()
        return render(request,'pages/gallery.html') 
    details = Gallery.objects.all()

    context ={
        'details': details,
    }   
    return render(request,'pages/gallery.html',context)


def join_now(request):
    if request.method =='POST':
           
        email = request.POST['email']

        c = Newsletter( email=email)
        c.save()
        return render(request,'pages/join_now.html')    
    return render(request,'pages/join_now.html')

def training(request):
    if request.method =='POST':
           
        email = request.POST['email']

        c = Newsletter( email=email)
        c.save()
        return render(request,'pages/training.html')    
    return render(request,'pages/training.html')

def events(request):
    if request.method =='POST':
           
        email = request.POST['email']

        c = Newsletter( email=email)
        c.save()
        return render(request,'pages/events.html')    
    return render(request,'pages/events.html')


def videos(request):
    if request.method =='POST':
           
        email = request.POST['email']

        c = Newsletter( email=email)
        c.save()
        return render(request,'pages/videos.html')    
    return render(request,'pages/videos.html')

def contact(request):
    if request.method =='POST':
        name = request.POST.get('name',False)
        cemail = request.POST.get('cemail',False)
        email = request.POST.get('email',False)
        message = request.POST.get('message',False)   
      

        if(not email):
            contact_details = Contact(name=name, email=cemail, message=message)
            contact_details.save()
        if(not cemail):
            news_letter = Newsletter( email=email)
            news_letter.save()
        return render(request,'pages/contact.html')    
    return render(request,'pages/contact.html')




