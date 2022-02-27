from multiprocessing import context
from django.shortcuts import render, redirect

from django.contrib import messages
from django.db.models import  Q

from .models import Project

# customised email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import HttpResponse
from solascriptura import settings

from .form import ProjectForm

# Create your views here.
def projects(request):
    search_query = ''
    projects = Project.objects.all()

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query) | 
        Q(author__icontains=search_query) 
    )

    context = {'projects':projects}
    return render(request, 'app/projects.html',context)


def project(request, pk):
    projectObj= Project.objects.get(id=pk)
    context = {'projectObj':projectObj}
    return render(request, 'app/single-project.html',context)



def createProject(request):
    
    form = ProjectForm()

    if request.method == 'POST':
        form  = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save()
            return redirect('projects')
     


    context={'form':form}
    return render(request, 'app/form-template.html', context)

   
def updateProject(request, pk):
    
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES, instance=project)
    if form.is_valid():
        form.save()
        return redirect('projects')
    context={'form':form}
    return render(request, 'projects/project_form.html',context)


def index(request):
    context = {}
    return render(request, 'app/index.html',context)


def bible(request):
    context = {}
    return render(request, 'app/bibleStudies.html',context)

    
def videos(request):
    context = {}
    return render(request, 'app/videos.html',context)

def send_email(request):        
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        body = request.POST.get('body')
        
        html_content = render_to_string('app/email_template.html',{'email': email, 'body':body, 'subject':subject, 'name':name})
        text_content = strip_tags(html_content)

        email = EmailMultiAlternatives(
            subject, # subject
            text_content, #content or body
            settings.EMAIL_HOST, #from email address
            [email],#recepient email list
            # ['ernest6175@gmail.com','elokai6175@gmail.com']  
        )
        email.attach_alternative(html_content,'text/html')
        email.send()
        messages.success(request,'Your mail was successfully sent')
        return redirect('app:projects')
        # return HttpResponse("<h1>Your mail was successfully sent</h1> <br><h1>We will get back to you very soon</h1>")
    return render(request, 'app/single-project.html',context)
