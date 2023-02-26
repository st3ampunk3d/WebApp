from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    #landing page URL
    path('', main, name='main'),

    #Member pages URL's
    path('members/', All_Members, name='members'),
    path('members/new/', newMember, name='new-member'),
    path('members/search', search_members, name='search-members'),
    path('members/member=<int:id>', single_member, name='member'),
    path('members/update/member=<int:id>', updateMember, name="update-member"),
    path('members/delete/member=<int:id>', deleteMember, name="delete-member"),
    
    #Dog pages URL's
    path('dogs/', All_Dogs, name='dogs'),
    path('dogs/search', search_dogs, name='search-dogs'),
    path('register/member=<int:id>', newDog, name='register'),
    path('dogs/update/dog=<int:id>', updateDog, name="update-dog"),
    path('dogs/delete/dog=<int:id>', deleteDog, name="delete-dog"),

    #Form submission URL
    path('success/', success, name='success'),
]

#This is needed to allow the /media/ folder references to be created dynamically.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)