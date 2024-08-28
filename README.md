# Plane Spotter

![plane spotter name](https://i.imgur.com/goCTk5k.png)

## Welcome to Plane Spotter. A digital log of your favorite planes and their spottings.

I built this app because of my background as a pilot and aviation enthusiast. I've always loved plane spotting and I wanted to build a fun and practical application for that purpose.

## Getting Started

[Deployed Website](https://plane-spotter-2944dbb5733c.herokuapp.com/)

[Trello Planning Materials](https://trello.com/b/0DFiVZm1/project-4-plane-spotter)

### Description

The purpose of this application is to allow a user to not only make a log or list of their favorite airplanes, but also log any sightings of that aircraft. There are links for widely-used websites in the aviation community hard-coded in the application that will guide a user on where to get certain information.

### Instructions

The user has the option to create a new aircraft on their profile based on:

- name
- model
- category
- image URL

> The image must be a URL. Getting the URL is accomplished through simply copying the image address from any webpage. The category field is a drop-down menu that allows a user to select an option from several different aircraft categories. GA will be automatically selected if the user does not manually select an option.

At that point, a drop down form will appear and the user has the option to add a sighting of that aircraft based on:

- the date and time (UTC)
- the location
- the aircraft's registration (Tail Number)
- the track log ([Flightradar24](https://www.flightradar24.com))

### Technologies Used:

- Python
- Django
- HTML
- POSTGRESQL
- Bootstrap5

### Sources/Attributes

- [Bootstrap](https://getbootstrap.com/)

- `verbose_name`: [Django Docs](https://docs.djangoproject.com/en/5.1/ref/models/options/)

- Aircraft icons: [SVG repo](https://www.svgrepo.com/)

- Custom signup-form widget troubleshooting:

  [Stack Overflow 1](https://stackoverflow.com/questions/61533472/cant-add-widget-to-usercreationform)

  [Stack Overflow 2](https://stackoverflow.com/questions/49413185/django-password-fields-placeholder/49413451#49413451)

### Planned Enhancements

- The user can upload a photo of their own when creating an aircraft

- The user can upload their own photos for a sighting, as many plane spotters are aviation photographers as well

- The application allows users to view eachother's profiles and create communities based on interests in different categories
