#Inventory-Management-System
Welcome to the Inventory Management System! This full-stack Django application helps you manage and keep track of all the products stored in a store. It provides a complete CRUD (Create, Read, Update, Delete) functionality, allowing users to: Add new products View the list of existing products Update product details Delete products

#Steps for project setup

1. create virtual environment and activate it.
2. Install Django inside virtual environment.
3. Start the project inside virtual environment running command :- django-admin startproject project_name
4. change directory to project_name
5. Create an app running this command : - python manage.py startapp app_name.
6. Now, add app_name in Installed_Apps section inside settings.py file.
7. Also add mentioned below code in settings.py file for rendering of static files(css files): STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

#Following these above mentioned steps you can run this project on your local system.
