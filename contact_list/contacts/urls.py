from django.urls import path
from . import views

urlpatterns = [
    path('contacts/', views.index, name='all-contacts'),
    path('contacts/createcontact', views.createContact, name='create-contact'),
    path('contacts/success', views.deleteConfirmation, name='delete-confirm'),
    path('contacts/<slug:contact_slug>', views.editContact, name='edit-contact') # our-domain.com/meetups/<dynamic-path-segment>
    #path('contacts/success', views.deleteConfirmation, name='delete-confirm')
]