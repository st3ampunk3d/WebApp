from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .models import Member, Dog, Breed
from .forms import addMember, addDog
from django.contrib import messages
from time import sleep

# Create your views here

##The home page##
def main(request):
  template = loader.get_template('landing.html')
  return HttpResponse(template.render())

##Page displaying all members and a search field##
def All_Members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('allMembers.html')
    context = {
      'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

##Page displaying members who match the search criteria##
def search_members(request):
  template = loader.get_template('search-results.html')
  
  if request.method == "POST":
    searched = request.POST['searched']
    members = Member.objects.filter(name__icontains=searched)

    context = {
      'searched': searched,
      'mymembers': members,
    }

    return HttpResponse(template.render(context, request))

  else:
    return HttpResponse(template.render(context, request)) 

##Page displaying the details of a single member and the dogs registered to them##
def single_member(request, id):
    mymember = Member.objects.get(id=id)
    mydogs = Dog.objects.filter(owner_id=id).values()
    breeds = Breed.objects.all().values()

    template = loader.get_template('memberDetails.html')


    context = {
      'mymember': mymember,
      'mydogs': mydogs,
      'breeds': breeds,
      'placeholder' : range(3-mydogs.count()),
    }

    return HttpResponse(template.render(context, request))

##Page displaying a form to register a new member##
def newMember(request):
    if request.method == "POST":
      form = addMember(request.POST, request.FILES)

      if form.is_valid():
        form.save()
        messages.success(request, "Member Added Successfully")
        return redirect('members')

    else:
      form = addMember()
    return render(request, 'addMember.html', {'form': form})

##re-uses the same form from the newMember
##The form is auto populated with the values saved for a particular member
def updateMember(request, id):
  mymember = Member.objects.get(id=id)

  form = addMember(request.POST or None, request.FILES or None, instance=mymember,)

  if form.is_valid():
    form.save()
    messages.success(request, 'Member updated Successfully')
    return redirect('members')

  return render(request, 'editmember.html', {'form': form, 'mymember': mymember})

##Removes a member from the database. A message is displayed but there is no HTML page for this view.
def deleteMember(request, id):
  mymember = Member.objects.get(id=id)
  mymember.delete()
  messages.success(request, 'Member removed Successfully')
  return redirect('members')

##All of the views for the dogs mimic the views for the Members
def All_Dogs(request):
    mydogs = Dog.objects.all().values()
    mymembers = Member.objects.all().values()
    breeds = Breed.objects.all().values()

    template = loader.get_template('allDogs.html')
    context = {
        'mydogs': mydogs,
        'mymembers': mymembers,
        'breeds': breeds,
    }
    return HttpResponse(template.render(context, request))


def search_dogs(request):
  template = loader.get_template('search-results.html')
  
  if request.method == "POST":
    searched = request.POST['searched']
    dogs = Dog.objects.filter(name__icontains=searched)

    context = {
      'searched': searched,
      'mymembers': dogs,
    }

    return HttpResponse(template.render(context, request))

  else:
    return HttpResponse(template.render(context, request))


def newDog(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('addDog.html')


    initial_data = {
        'owner': id,
      }

    if request.method == "POST":
      form = addDog(request.POST, request.FILES, initial=initial_data)

      if form.is_valid():
        form.save()
        messages.success(request, 'Dog Registered Successfully')
        return redirect('dogs')

    else:
      form = addDog()

    context = {
      'mymember': mymember,
      'form': form,
    }
    return HttpResponse(template.render(context, request))


def updateDog(request, id):
  mydog = Dog.objects.get(id=id)
  mymembers = Member.objects.all()
  breeds = Breed.objects.all().values()

  form = addDog(request.POST or None, request.FILES or None, instance=mydog)

  context = {
    'form': form,
    'mymembers': mymembers,
    'dog': mydog,
    'breeds': breeds,
  }

  if form.is_valid():
    form.save()
    messages.success(request, 'Dog Updated Successfully')
    sleep(5)
    return redirect('dogs')

  return render(request, 'editDog.html', context)


def deleteDog(request, id):
  mymember = Member.objects.get(id=id)
  mymember.delete()
  messages.success(request, 'Dog Removed Successfully')
  return redirect('dogs')
    

def success(request):
    template = loader.get_template('success.html')
    context = {}
    return HttpResponse(template.render(context, request))