from .models import Contact
from .forms import Registration
from django.shortcuts import render, redirect
from django.utils.text import slugify


# Create your views here.

def index(request):
    contacts = Contact.objects.all()

    return render(request, 'contacts/index.html',{
        'contacts': contacts
    })

    
def createContact(request):
    if request.method == 'GET':
        registrationForm = Registration()
    else:
        registrationForm = Registration(request.POST)
        if registrationForm.is_valid():
            user_fname = registrationForm.cleaned_data['first_name']
            user_lname = registrationForm.cleaned_data['last_name']
            user_slug = '-'.join((slugify(user_fname), slugify(user_lname)))
            user_email = registrationForm.cleaned_data['email']
            newContact, _ = Contact.objects.get_or_create(first_name = user_fname, last_name = user_lname, slug=user_slug,email=user_email)
            Contact.save(newContact)
            return redirect('all-contacts')


    return render(request, 'contacts/create-new-contact.html', {
        
            'form': registrationForm
            })

def editContact(request, contact_slug):
    try:
        selectedContact = Contact.objects.get(slug=contact_slug)
        if request.method == 'POST':
            selectedContact.delete()
            return redirect('delete-confirm')

        return render(request, 'contacts/edit-contact.html', {
            'contact': selectedContact,
            'contact_found': True
        })
    except Exception as exc:
        return render(request, 'contacts/edit-contact.html', {
            'contact_found': False
        })


def deleteConfirmation(request):
    return render(request, 'contacts/delete-success.html')


