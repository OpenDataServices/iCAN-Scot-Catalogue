# ICAN-Scot-Catalogue

## Run a Dev Server

    vagrant up
    vagrant ssh
    cd /vagrant/
    virtualenv .ve -p python3
    source .ve/bin/activate
    pip3 install -r requirements_dev.txt 
    python manage.py migrate
    python manage.py runserver 0:8080

Go to http://localhost:8080/
    
## Create A Catalogue Admin User

* Create a superuser using the Django CLI command https://docs.djangoproject.com/en/2.1/intro/tutorial02/#creating-an-admin-user
* Use the superuser to log in to the /admin interface
* Create a normal user in the /admin web interface
* Give the user the "catalogueapp | catalogue admin permission | Can Admin The Catalogue" permission

## Using Catalogue Admin

Go to /catalogueadmin
