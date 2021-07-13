from django.shortcuts import render, redirect
from contacts.models import Contact

# Create your views here.

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact(name=name, email=email, phone=phone ,  subject=subject, message=message)
        contact.save()
        return redirect('contact')

    return render(request, 'pages/contact.html')