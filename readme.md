# K9 Kennel Club - Django Web App

## Overview

### What's the point?
This project revisits the [SQL database project](https://github.com/st3ampunk3d/KennelClub) I did previously. The project has been migrated from a desktop application to a web application.
The web application provides the user interface and data management tools for a local Kennel Club.
The intent was to make the software more deployable and accesible to users. All of the dependencies exist on the server instead of on the local computer, eliminating any setup on the end user's part.

### Running the App:
Required Pagages:
 - [Django](https://pypi.org/project/Django/)
 - [Django Phone Field](https://pypi.org/project/django-phone-field/)
 
After cloning the repository navigate to "/WebApp/k9club"
Run the command `python manage.py runserver` The development server will start.
In your browser navigate to: http://127.0.0.1:8000/

### See it in action:
Watch the [demo video](https://cdnapisec.kaltura.com/index.php/extwidget/preview/partner_id/1157612/uiconf_id/42438192/entry_id/1_ww3diov1/embed/dynamic) to see the web app in action.


## Web Pages

### Home
The home page is static. The content is written in plain HTML with the use of Django templates for maintenance ease. There is a call to action promtping the user to join the kennel club with a link to the member registration form.

### Members
All of the content on this page is dynamically populated from the database and Django models.
This page shows a grid of media cards representing each of the members of the kennel club.
There is a search bar that allows you to filter by the members' names. The search results page includes a button to return to the full list.
Clicking on a particluar member will take you to the member's details page.

### Member Details
All of the content on this page is dynamically populated from the database and Django models.
The member details page features a sidebar containing the membership ID, membership tier, city, contact information, and photo for the member. The main body of the page shows a list of all of the canines registered to that member. If there are fewer than 3 canines registered, placeholders for future canines are shown. Clicking on one of the placeholders will take you to the registration form for a new dog. Members are allowed a maximum of 3 dogs.
From this page you can also choose to update the member's information or remove the member from the database. Removing the member will also remove any canines registered to them.
Clicking on a particular canine will take you to the Canine's detail page.

### Canines
All of the content on this page is dynamically populated from the database and Django models.
The canines page follows the same formatting and logic as the Members page.
You can search by Canines' names or select a particluar canine to view. Since we cannot have a canine without an owner, there is no option to add a canine here. That must be done from the Member Details page.
Clicking on a particular canine will take you to the Canine's detail page.

### Canine Details
All of the content on this page is dynamically populated from the database and Django models.
The canine details page features a sidebar containing the registration number, owner, age, color, and breed of the canine. The main body of the page contains a form used to update the canine's information. Changing the Owner in the form will transfer ownership of the canine when the form is submitted.

### General Navigation:
The navigation bar is displayed on each page to allow easy transition betwen the home page, Members page, and Canines page. A link to the github repo can be found in the footer.

## Development Environment

This software was developed with Visual Studio Code and tested in Goolge Chrome. I made use of the Chrome Developer tools to assist with debugging and some styling.

Languages and Frameworks used:
 - Python 3.11
 - Django 4.1.7
 - HTML 5
 - CSS 3

## Useful Websites
I relied heavily on these sites during the creation of this application:
* [Django Documentation](https://www.djangoproject.com/)
* [W3 Schools: Django tutorial](https://www.w3schools.com/django/)

## Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* The website is not currently responsive. I would like to adapt it for mobile views.
* When removing a member or canine there is no prompt to confirm the action. This could be dangerous
* Right now the website is primarily for admin use. I would like to expand it so members can use it as a kind of community site.