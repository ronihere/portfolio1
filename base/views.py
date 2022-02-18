from django.shortcuts import render,redirect
from .models import Contact,Projects
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.
def home(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        date=request.POST['date']
        message=request.POST['message']
        var=Contact(name=name,email=email,subject=subject,date=date,message=message)
        var.save()
        messages.error(request,f"Thank you {name} !\nYour response has been recieved.I will contact you soon if necessary" ,extra_tags='contact')
        send_mail(f"Roni Mondal",
                  f"Hey {name}! Thank you for your response. I will contact you if necessary!\n ",
                  'from0the0headquarter0of@gmail.com',
                  [email],
                  fail_silently=True)

        return redirect('/')
    else:
        projects=Projects.objects.all()
        return render(request, 'index.html',{'projects':projects})