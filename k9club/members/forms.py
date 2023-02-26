from django import forms
from .models import Dog, Member, Breed
from phone_field import PhoneField

class addMember(forms.ModelForm):

    
    class Meta: #This pulls the attributes and datatypes from the associated model
        model = Member #The model for this form is the Member
        fields = ['name', 'city', 'email', 'phone', 'photo']
        

class addDog(forms.ModelForm):
    #By default the name of the object (ex. "(Member object 1)") is displayed.#
    #This changes it to be the members name and sorts them alphabetically
    owner = forms.ModelChoiceField(queryset=Member.objects.order_by('name'))

    #This changes the form options to show the Breed's name and sorts them alphabetically
    breed = forms.ModelChoiceField(queryset=Breed.objects.order_by('name'))

    class Meta: #This pulls the attributes and datatypes from the associated model
        model = Dog #The model for this form is the Member
        fields = ['owner', 'name', 'breed', 'color', 'dob', 'photo']

        labels = {
            'dob': ('Birth Date'),
        }



        
