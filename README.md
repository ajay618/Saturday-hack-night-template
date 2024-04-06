
![django notion](https://github.com/TH-Activities/saturday-hack-night-template/assets/117498997/2db31367-8f96-4e88-8a8d-a1a75936204d)




# Project Name
Django ToDo App:
It's a basic Django Todo app with all the CRUD (Create , Read , Update and Delete) operations
We have created a table where we stored all the tasks with a completed flag
User from the UI set "mark as done" and "mark as undone" for each task that updates the completed status.
Also user can add new task to the list that will displayed in the UI
## Team members
1. [Ajay Joy](https://github.com/ajay618/Saturday-hack-night-template.git)

## How it Works ?
1.It's a basic Django Todo app with all the CRUD (Create , Read , Update and Delete) operations
We have created a table where we stored all the tasks with a completed flag
User from the UI set "mark as done" and "mark as undone" for each task that updates the completed status.
Also user can add new task to the list that will displayed in the UI
2. [Embed video of project demo](https://drive.google.com/file/d/1VWSpwqPzb2-sjUoiMo6quHxYO2F9yANb/view?usp=sharing) 
## Libraries used
asgiref==3.8.1
Django==5.0.4  
sqlparse==0.4.4
tzdata==2024.1
## How to configure
download a virtual enviornment : pip install virtualenv
create a virtual enviornment : python -m venv env
activate virtual enviornmnrt : .\env\Scripts\activate 
Install django in virtual enviornment : pip install django
Start django project  :django-admin startproject toDo_main
Create a todo app : python manage.py startapp todo
Configure created app in settings.py
Add path for the template directory
Configure static files in django for css and js files
## How to Run
Follow the above commands and configure the project as given above
Run "python manage.py runserver" command to run in local
