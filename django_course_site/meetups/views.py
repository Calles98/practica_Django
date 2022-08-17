from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Meetup, Participant
from .forms import Registration
# Create your views here.

def index(request):
    meetups = Meetup.objects.all()

    return render(request, 'meetups/index.html',{
        'meetups': meetups
    })


def meetupDetails(request, meetup_slug):
    try:
        selectedMeetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registrationForm = Registration()
        else:
            registrationForm = Registration(request.POST)
            if registrationForm.is_valid():
                user_email = registrationForm.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email)
                selectedMeetup.participants.add(participant)
                return redirect('confirm-registration', meetup_slug=meetup_slug)

        return render(request, 'meetups/meetups-details.html', {
                'meetup_found': True,
                'meetup': selectedMeetup,
                'form': registrationForm
            })
    except Exception as exc:
        print(exc)
        return render(request, 'meetups/meetups-details.html', {
            'meetup_found': False
        })

def confirmRegistration(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request, 'meetups/registration-success.html', {
        'organizer_email': meetup.Organizer.OrgEmail
    })