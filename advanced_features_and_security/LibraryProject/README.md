# LibraryProject

This is a Django project created for the "Introduction to Django" module.  
It demonstrates:
- Setting up Django
- Understanding project structure
- Running the development server

## How to Run
1. Install dependencies:
   ```bash
   pip install django
# LibraryProject
A Django project for managing library records.

## Setup
1. pip install -r requirements.txt
2. python manage.py migrate
3. python manage.py runserver

# Groups & Permissions Setup:
# 1. In Django admin → Groups:
#    - Create group: Viewers → assign can_view
#    - Create group: Editors → assign can_view, can_edit, can_create
#    - Create group: Admins  → assign can_view, can_edit, can_create, can_delete
# 2. Assign users to groups through the admin interface.



