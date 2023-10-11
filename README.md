# ODYSSEY

### **Welcome to Odyssey README.**

XXX

**I hope you enjoy the website as much as enjoyed making it! It's been a roller coaster of emotions, but in the end, I made it through!**

![amiresponsive](XXX)

View live site:
[XXX](XXX)

---

## **CONTENTS**

* [User Experience](#user-experience-ux)

* [Agile Methodology](#agile-methodology)
  * [User Stories](#user-stories)
  * [Iterations](#iterations)
    * [Iteration 1](#iteration-1)
    * [Iteration 2](#iteration-2)
    * [Iteration 3](#iteration-3)
  * [Future Implementations](#future-implementations)

* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)

* [Features](#features)
  * [General Features on Each Page](#general-features-on-each-page)
  * [Accessibility](#accessibility)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)

* [Testing](#testing)

* [Credits](#credits)
  * [Code Used](#code-used)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)

---

## **User Experience (UX)**

### **Initial Discussion**

XXX

#### **Key information for the site**

XXX

### **User Stories**

#### **Client Goals**

XXX

#### **First-Time Visitor Goals**

XXX

#### **Returning Visitor Goals**

XXX

#### **Frequent Visitor Goals**

XXX


## **Agile Methodology**

The Agile Methodology was used to develop this website. It was implemented through GitHub and the Project/Kanban Board: 
[Odyssey](XXX).

### **Kanban Board:**

With the Kanban board, the project was split into four sections;

- Todo
- In Progress
- Done
- Backlog (future additions)

<details>
<summary>Kanban board design:</summary>
<br>

![Kanban](XXX)
</details>

### **User Stories**

#### **Iteration 1**
- *XXX*

#### **Iteration 2**

- *XXX*

#### **Iteration 3**

- *XXX*

## **Design**

### **Colour Scheme**

The purple colours and aesthetic has been generated from the header image.

![XXX](XXX)

### **Typography**

- [XXX](XXX)

### **Imagery**

XXX

**Header**

![XXX](XXX)

**Background**

![XXX](XXX)


### **Wireframes**

The wireframe below is the general idea and vision I had for the website. It follows a basic structure that is the same throughout all pages of the website, with small modifications. 

![Wireframes](XXX)

## **Features**

### **Home Page**

XXX

![Home](XXX)

### **Detail Page**

XXX


![XXX](XXX)

### **Edit Page**

XXX

![XXX](XXX)

### **Delete Page**

XXX

![XXX](XXX)

### **Upload Page**

XXX

![XXX](XXX)

### **About Page**

- Can be accessed from the navbar to anyone.
- Back button to take the user back to the Home Page

![About](media/images/about-page.png)

### **Register Page**

XXX

![Register](XXX)

### **Sign in Page**

XXX

![Sign in](XXX)

### **Sign out Page**

XXX

![Sign out](XXX)

### **404 Page**

XXX

![404](media/images/404-page.png)

### **General features on each page**

XXX

- The navbar as it appears on all pages when a user have not scrolled down on the page.

![Nav](XXX)
 

![Footer](XXX)

### **Future Implementations**

XXX


### **Accessibility**

I have tried my best to be mindful of accessibility, and the steps I've taken for this are the following:

- Alt tags on the header and placement images
- Aria labels to the social media links
- Chose a good colour contrast throughout the website
- Semantic HTML

## **Technologies Used**

### **Languages Used**

- HTML5
- CSS
- Python
- JavaScript

### **Frameworks, Libraries & Programs Used**

- [Django](https://www.djangoproject.com/start/overview/)
- [PostgreSQL](https://www.psycopg.org/docs/)
- [Cloudinary](https://cloudinary.com/)
- [Colormind](http://colormind.io/)
- [Balsamiq](https://balsamiq.com/)
- [ElephantSQL](https://www.elephantsql.com/)
- [Heroku](https://dashboard.heroku.com/login)
- [Canva](https://www.canva.com/)

## **Deployment & Local Development**

### **Deployment**

The site was deployed using Heroku, following the steps offered by Code Institute.
You can find the instructions in a Google Docs [here](https://docs.google.com/document/d/1P5CWvS5cYalkQOLeQiijpSViDPogtKM7ZGyqK-yehhQ/edit#heading=h.5s9novsydyp1).

### **1. Creating the Django Project:**

- Install Django and gunicorn: `pip3 install django gunicorn`
- Install supporting database libraries dj_database_url and psycopg2 library: `pip install dj_database_url psycopg2`
- Install Cloudinary libraries to manage static files: `pip install dj-3-cloudinary-storage`
- Create file for requirements: `pip freeze --local > requirements.txt`
- Create project: `django-admin startproject project_name`
- Create app: `python manage.py startapp app_name`
- Add app to list of `installed apps` in settings.py file: `'app_name'`
- Migrate changes: `python manage.py migrate`
- Test server works locally: `python manage.py runserver`

### **2. Create your Heroku App:**

- Navigate to the Heroku website
- Create a Heroku account by entering your email address and a password (or log in if you have one already).
- Activate the account through the authentication email sent to your email account
- Click the new button on the top right corner of the screen and select Create a new app from the dropdown menu.
- Enter a unique name for the application.
- Select the appropriate region for the application.
- Click Create app
- In the Heroku dashboard click on the Resources tab
- Scroll down to Add-Ons, search for and select 'Heroku Postgres'
- In the Settings tab, scroll down to 'Reveal Config Vars' and copy the text in the box beside DATABASE_URL.

### **3. Set up Environment Variables:**

- In your IDE, create a new env.py file in the top-level directory
- Add env.py to the .gitignore file
- In env.py import the os library
- In env.py add `os.environ["DATABASE_URL"]` = "Paste in the text link copied above from Heroku DATABASE_URL"
- In env.py add `os.environ["SECRET_KEY"]` = "Make up your own random secret key"
- In Heroku Settings tab Config Vars enter the same secret key created in env.py by entering 'SECRET_KEY' in the box for 'KEY' and your randomly created secret key in the 'value' box.

### **4. Setting up settings.py:**
- In your Django 'settings.py' file type:

```
from pathlib import Path
import os
import dj_database_url

if os.path.isfile("env.py"):
    import env
```

- Remove the default insecure secret key in settings.py and replace with the link to the secret key variable in Heroku by typing: SECRET_KEY = os.environ.get(SECRET_KEY)
- Comment out the DATABASES section in settings.py and replace it with:

```
DATABASES = {
  'default': 
  dj_database_url.parse(os.environ.get("DATABASE_URL"))
  }
```

- Create a Cloudinary account and from the 'Dashboard' in Cloudinary copy your url into the env.py file by typing: `os.environ["CLOUDINARY_URL"] = "cloudinary://<insert-your-url>"`
- In Heroku add cloudinary url to 'config vars'
- In Heroku config vars add DISABLE_COLLECTSTATIC with value of '1' (note: this must be removed for final deployment)
- Add Cloudinary libraries to the installed apps section of settings.py file:
```
'cloudinary_storage'
'django.contrib.staticfiles''
'cloudinary'
```

- Connect Cloudinary to the Django app in settings.py:

```
STATIC_URL = '/static'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'STATIC')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE =
'cloudinary_storage.storage.MediaCloudinaryStorage'
* Link file to the templates directory in Heroku 
* Place under the BASE_DIR: TEMPLATES_DIR = os.path.join(BASE_DIR,
'templates')
```

- Change the templates directory to TEMPLATES_DIR. Place within the TEMPLATES array: `'DIRS': [TEMPLATES_DIR]`
- Add Heroku Hostname to ALLOWED_HOSTS: `ALLOWED_HOSTS = ['rhi-book-nook.herokuapp.com', 'localhost']` *Create Procfile at the top level of the file structure and insert the following: web: gunicorn PROJECT_NAME.wsgi
- Make an initial commit and push the code to the GitHub Repository. `git add . git commit -m "Initial deployment" git push`

### **5. Heroku Deployment:**
- Click the Deploy tab in Heroku
- In the 'Deployment method' section select 'Github' and click the 'Connect to GitHub' button to confirm.
- In the 'search' box enter the Github repository name for the project
- Click search and then click connect to link the Heroku app with the GitHub repository. The box will confirm that Heroku is connected to the repository.

### **6. Final Deployment:**
In the IDE:

- When development is complete change the debug setting to: DEBUG = False in settings.py
- In Heroku settings config vars, change the DISABLE_COLLECTSTATIC value to 0
- Because DEBUG must be switched to True for development and False for production it is recommended that only manual deployment is used in Heroku.
- To manually deploy click the button 'Deploy Branch'. The default 'main' option in the dropdown menu should be selected in both cases. When the app is deployed a message 'Your app was successfully deployed' will be shown. Click 'view' to see the deployed app in the browser.

### **Local Development**

#### **How to Fork**

1. Login (or sign up) to GitHub.
2. Go to the repository for this project [here](XXX)
3. Click the Fork button in the top right corner.

#### **How to Clone**

If you wish to clone my project, please see the following steps below:

- Navigate to GitHub: XXX
- Select the 'Clone' button
- Copy the URL or download it as a ZIP file
- Use git clone + the URL in your terminal, or unpack the ZIP containing the project


## **Testing**

Please refer to the [TESTING.md](TESTING.md) file for all testing performed.

## **Credits**

#### Django REST Models
- [Readthedocs Django REST Models](https://readthedocs.org/projects/django-rest-models/downloads/pdf/latest/)

#### Django REST Serializers
- [Django REST Framework](https://www.django-rest-framework.org/api-guide/serializers/)
- [Django REST Framework Tutorials](https://www.django-rest-framework.org/tutorial/1-serialization/)
- [Django REST Framework Relations](https://www.django-rest-framework.org/api-guide/relations/)

#### Other

- [Aggregation from Django documentation](https://docs.djangoproject.com/en/4.2/topics/db/aggregation/)

  
###  **Acknowledgments**

I would like to thank and acknowledge the following people, who have shown invaluable support throughout my fourth project:

- **Dan Ford**, not only as my boyfriend but also as my biggest supporter. His unwavering encouragement and belief in my abilities have been a constant source of motivation and inspiration. I am truly grateful to have him by my side throughout this journey.
- **Joseph Doble** has been instrumental in my project, offering assistance with sourcing relevant information and providing clear explanations of how things work and why. His support has been invaluable.
- **Emelie Hansson**, a fellow Code Institute student, who has provided me with tremendous support throughout my journey. Her encouragement and assistance have been greatly appreciated.
- **Tutor Support**, their patience and willingness to address my endless questions have been instrumental in my learning and growth.
- **Mitko Bachvarov**, my mentor at Code Institute, for the great help and support with my project.
- **Kera Cudmore**, for the README and TESTING template.