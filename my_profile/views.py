from django.contrib import messages
from django.shortcuts import render, redirect
from . import models


def profile_page(request):
    me = models.Profile.objects.first()
    skills = models.Skill.objects.all()
    projects = models.Projects.objects.all()
    context = {
        'profile': me,
        'skills': skills,
        'projects': projects
    }
    if request.method == 'POST':
        get_name = request.POST.get('name')
        get_email = request.POST.get('email')
        get_message = request.POST.get('message')
        models.Contact.objects.create(name=get_name, email=get_email, message_text=get_message)
        messages.success(request, 'Successfully Message was Sent')
        print("Sent")
        return redirect('profile')
    return render(request, 'profile/index-particle.html', context)
