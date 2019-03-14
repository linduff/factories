# factories
This project uses Django to create a website. 

### Files of Interest

/tree/forms.py              - defines the Add, Edit, and Delete Factory forms

/tree/models.py             - defines the database objects

/tree/views.py              - functions and data that interact with html data

/tree/templates/index.html  - HTML and javascript for the page

Note: I wanted to put the javascript into a separate file, but for some reason, it wouldn't work correctly. I decided to just put it in the html where it does work.

### Run it Yourself

1. Make sure you have Django installed (This runs on version 2.1.1)

2. Clone the repo, and inside the main directory run:
```
python manage.py runserver
```
3. open 127.0.0.1:8000 in your browser
