# Task: Django Models

> ## Brief

- Create a new GitHub repository with a README.md, and Python .gitignore file.

- Clone it to your machine/computer, which will create a new folder on your computer with your repository’s content.

- Create a new virtual environment in that folder named .env and install Django in it.

- Create a new Django project. Use your Zuriboard Student ID as the name of the project.

- Create a new application using the Django startapp command. The app should be called blog.

- Add the blog app to the main_projects INSTALLED_APPS. 

- Create a new model in the blog app called Post. It should have the following fields:

        Title : A string of maxlength 200, use Django’s models.CharField

        Text : Any amount of text, use Django’s TextField

        Author : A Foreign Key to the current user model. Make use of Django’s get_user_model function.

        Created_date : A date-time column, use Django’s models.DateTimeField. 

        Published_date : A date-time column, use Django’s models.DateTimeField. 

- Create migrations for your new model using the makemigrations Django command. 

- Run all migrations using the migrate Django command.

- Stage and Commit your Django project and push your changes to your GitHub repository.

- Ensure your final code/submission is on the default branch of your GitHub repository.

#


>## Solution:

- Created a new public GitHub repository.

- Cloned repository.

        git clone https://github.com/EnebeliEmmanuel/django-models

- Created virtual environment and activated virtual enviroment

        py -m venv env
        source env/bin/activate

- Installed django

        py -m pip install django

- Extracted installed dependencies to a file named requirements.txt

        pip freeze > requirements.txt

- Created a new Django project with my zuriboard ID as the name.
    
        django-admin startproject I4G006916U67

- Added secret key to an enironment variable

- Made migrations

        py manage.py migrate


- Ran the django server

        py manage.py createsuperuser

- Created a new app called blog

        py manage.py startapp blog

- Added the blog app to the I4G006916U67 project's INSTALLED_APPS in settings.py

- Created a new model called Post in the blog app models.py

- Made migrations

        py manage.py makemigrations
        py manage.py migrate

- Git add and commit all files.

        git add .
        git commit -m "blog"

- Pushed the local repository to the remote repository.

        git push -u origin main


