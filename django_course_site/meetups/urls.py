from django.urls import path
from . import views

urlpatterns = [
    path('meetups/', views.index, name='all-meetups'), # our.domain/meetups
    path('meetups/<slug:meetup_slug>/success', views.confirmRegistration, name='confirm-registration'), 
    path('meetups/<slug:meetup_slug>', views.meetupDetails, name='meetup-detail') # our-domain.com/meetups/<dynamic-path-segment>
]