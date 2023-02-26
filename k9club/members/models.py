from django.db import models

# Create your models here.
from django.db import models
from phone_field import PhoneField
from datetime import date
from dateutil import relativedelta


# Create your models here.
class Member(models.Model):
    name           = models.CharField(max_length=45, null='-')
    city           = models.CharField(max_length=45, null='-')
    email          = models.EmailField(max_length=254, null='-')
    phone          = PhoneField(blank=True,)
    membershipdate = models.DateField(null=date.today())
    photo          = models.ImageField(upload_to='images/people/', null='images/people/noProfilephoto.png')

    def memberTier(self):
        diff = relativedelta.relativedelta(date.today(), self.membershipdate)
        if diff.years >= 8:
            return "Platinum"
        elif diff.years >= 4:
            return "Gold"
        elif diff.years >= 2:
            return "Silver"
        else:
            return "Bronze"

    def __str__(self):
        return u'{0}'.format(self.name)

class Breed(models.Model):
    name      = models.CharField(max_length=45, null='-')
    minHeight = models.IntegerField(null=0)
    maxHeight = models.IntegerField(null=0)
    minLife   = models.IntegerField(null=0)
    maxLife   = models.IntegerField(null=0)
    traits    = models.CharField(max_length=200)
    health    = models.CharField(max_length=200)
    desc      = models.CharField(max_length=300)

    def __str__(self):
        return u'{0}'.format(self.name)

class Dog(models.Model):
    name  = models.CharField(max_length=45, null='-')
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    owner = models.ForeignKey(Member, on_delete=models.CASCADE)
    color = models.CharField(max_length=15)
    dob   = models.DateField(null=date.today())
    photo = models.ImageField(upload_to='images/dogs/', null='images/dogs/nophoto.png')

    def __str__(self):
        return u'{0}'.format(self.name)





'''
This is data used to seed the database.
run python manage.py shell and paste the following lines to populate the tables for members, breeds, and dogs.
#############################################################################################################

from members.models import Dog, Member, Breed

member0 = Member(name='Radley Crown',    city='Big city',        email='radley.crown@bluefalcon.com', phone='258-332-5266', membershipdate='2012-05-20', photo='images/people/blue_falcon.png')
member1 = Member(name='Charles Brown',   city='Minneapolis',     email='charlie.brown@peanuts.com',   phone='426-563-2665', membershipdate='2015-06-09', photo='images/people/charlie_brown.png')
member2 = Member(name='Emily Elizabeth', city='Birdwell Island', email='e.elizabeth@bigred.com',      phone='484-373-3364', membershipdate='2015-09-07', photo='images/people/emily_elizabeth.png')
member3 = Member(name='George Jetson',   city='Orbit city',      email='george@spacelysprokets.net',  phone='526-353-8766', membershipdate='2018-01-30', photo='images/people/george_jetson.png')
member4 = Member(name='Jonny Quest',     city='Florida Keys',    email='jonny@questlabs.org',         phone='566-697-8378', membershipdate='2018-04-10', photo='images/people/jonny_quest.png')
member5 = Member(name='Jon Arbuckle',    city='Muice',           email='jonarbuckle@thatdarncat.com', phone='664-273-4353', membershipdate='2019-08-02', photo='images/people/jon_arbuckle.png')
member6 = Member(name='Muriel Bagge',    city='Nowhere',         email='muriel@havecourage.com',      phone='268-724-3364', membershipdate='2019-11-13', photo='images/people/muriel_bagge.png')
member7 = Member(name='Norville Rogers', city='Coolsville',      email='shaggy@mysteryinc.org',       phone='726-629-3662', membershipdate='2020-06-14', photo='images/people/norville_rogers.png')
member8 = Member(name='Rick',            city='New York',        email='just_rick@tj.net',            phone='866-263-5379', membershipdate='2021-12-15', photo='images/people/rick.png')
member9 = Member(name='Sherman Peabody', city='Manhattan',       email='mr.peabody@WABAC.edu',        phone='732-263-9269', membershipdate='2023-01-11', photo='images/people/sherman_peabody.png')

member_list = [member0, member1, member2, member3, member4, member5, member6, member7, member8, member9]

for member in member_list: member.save()

breed0 = Breed(name='Doberman',           minHeight=24, maxHeight=28, minLife=12, maxLife=15, traits='loyal, energetic, intelligent, protective',             health='hip dysplasia, heart conditions, cancer',              desc='-')
breed1 = Breed(name='Beagle',             minHeight=13, maxHeight=15, minLife=12, maxLife=15, traits='Curious, friendly, energetic, good-natured',            health='ear infections, hip dysplasia, epilepsy',              desc='-')
breed2 = Breed(name='Labrador Retriever', minHeight=21, maxHeight=24, minLife=10, maxLife=12, traits='loyal, friendly, intelligent, energetic, good-natured', health='hip dysplasia, obesity, ear infections',               desc='-')
breed3 = Breed(name='Great Dane',         minHeight=28, maxHeight=34, minLife=8,  maxLife=10, traits='gentle, loyal, intelligent, good-natured',              health='hip dysplasia, cancer, heart conditions',              desc='-')
breed4 = Breed(name='Bulldog',            minHeight=12, maxHeight=16, minLife=8,  maxLife=10, traits='loyal, calm, gentle, brave',                            health='skin Allergies, respiratory issues, obesity',          desc='-')
breed5 = Breed(name='Dachshund',          minHeight=5,  maxHeight=9,  minLife=12, maxLife=15, traits='loyal, energetic, playful, curious',                    health='intervertebral disc disease, hip dysplasia, diabetes', desc='-')

breed_list = [breed0, breed1, breed2, breed3, breed4, breed5]

for breed in breed_list: breed.save()

dog0  = Dog(name='Dynomutt',    breed=breed0, owner=member0,  color='grey',   dob='2015-09-10', photo='images/dogs/dynomutt.png')
dog1  = Dog(name='Snoopy',      breed=breed1, owner=member1,  color='white',  dob='2015-10-02', photo='images/dogs/snoopy.png')
dog2  = Dog(name='Clifford',    breed=breed2, owner=member2,  color='red',    dob='2021-11-10', photo='images/dogs/clifford.png')
dog3  = Dog(name='Astro',       breed=breed3, owner=member3,  color='grey',   dob='2016-09-23', photo='images/dogs/astro.png')
dog4  = Dog(name='Bandit',      breed=breed4, owner=member4,  color='white',  dob='2018-09-18', photo='images/dogs/bandit.png')
dog5  = Dog(name='Odie',        breed=breed5, owner=member5,  color='yellow', dob='2017-06-19', photo='images/dogs/odie.png')
dog6  = Dog(name='Courage',     breed=breed1, owner=member6,  color='pink',   dob='2020-02-18', photo='images/dogs/courage.png')
dog7  = Dog(name='Scooby-Doo',  breed=breed3, owner=member7,  color='brown',  dob='2015-09-13', photo='images/dogs/scooby_doo.png')
dog8  = Dog(name='Spike',       breed=breed4, owner=member8,  color='grey',   dob='2013-02-10', photo='images/dogs/spike.png')
dog9  = Dog(name='Mr. Peabody', breed=breed1, owner=member9,  color='white',  dob='2014-03-07', photo='images/dogs/mr_peabody.png')
dog10 = Dog(name='Scrappy-Doo', breed=breed3, owner=member7,  color='brown',  dob='2022-09-22', photo='images/dogs/scrappy_doo.png')

dog_list = [dog0, dog1, dog2, dog3, dog4, dog5, dog6, dog7, dog8, dog9, dog10]

for dog in dog_list: dog.save()

###############################################################################################################
'''