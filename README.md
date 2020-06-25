# ICAN-Scot-Catalogue

This is a Django app to run a small website for the Catalogue for https://www.ican.scot/
It is intended to be run on a subdomain, https://catalogue.ican.scot/ with navigation links to link users between that and the main site.

It lists and promotes a group of service providers that help with a problem (for iCAN, Dementia).

The data for this list comes from several places:

* Mainly, listings are taken from https://www.aliss.org/ . This means we re-use data so there is less work for us in populating and keeping the catalogue up to date. 
  We also encourage use of an Open Data hub of info.
* We also add a free text field of our own. This is edited directly on the site as markdown and show to the user. This allows the Catalogue to add some information of it's own.
  (For iCAN, this is notes on the evidence base for an organisation and what they do.)

ALISS has 2 data models, Organisation and Service. An Organisation can provide multiple services.

To add something to this Catalogue:

* In the admin interface an admin specifies the ALISS Service they want to add.
* That service and the organisation that provide it are imported and stored in the app.
* Admins can enable or disable services. A disabled service is not shown to the public. 
* Admins can add a free text field in mark down to an organisation.

On the public website:

* Every organisation that has at least one service that is active is listed on the front page, and has it's own page.
* The front page has a free text search box.
* For every such organisation, on it's own page there is full information.

The Admin interface can be found at /catalogueadmin . 
A valid Django User with the permission "catalogueapp | catalogue admin permission | Can Admin The Catalogue" is required to use it.

The Django command update_aliss_data should be run regularly by cron or an automatic system. This downloads the latest data from the ALISS servers to the app. 

## Future Development

Add https://schema.org/ markup and search engine friendly tags to public website.

We wanted to expand the search to include the concept of searching for a service that covers where the user lives. Not all services cover all of Scotland. 
However, this relies on having good data on what areas a service covers, and this is hard to get.

## Requirements & Installation

* Python
* Postgresql
* The Django command update_aliss_data should be run regularly by cron or an automatic system.

This was written with hosting on Heroku in mind. 

## Dev

There is a Vagrant box available.

    vagrant up
    vagrant ssh
    cd /vagrant/
    virtualenv .ve -p python3
    source .ve/bin/activate
    pip3 install -r requirements_dev.txt 
    python manage.py migrate
    python manage.py runserver 0:8080

Go to http://localhost:8080/
    
## Creating A Catalogue Admin User on a fresh install

* Create a superuser using the Django CLI command https://docs.djangoproject.com/en/2.1/intro/tutorial02/#creating-an-admin-user
* Use the superuser to log in to the /admin interface
* Create a normal user in the /admin web interface
* Give the user the "catalogueapp | catalogue admin permission | Can Admin The Catalogue" permission

