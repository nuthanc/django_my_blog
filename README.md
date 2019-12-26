# django_my_blog

#### Initial blog setup:
* Create project and app
* Create templates
    * Create base and index html files
* Register app and templates in project's settings.py
* Update base.html with header partials
* Extend base.html in index.html
* Create IndexListView in App's views.py
* Update project urls.py file with IndexListView
* Include app's urls.py file in the project's url
* Create Post models in App's models.py
* Register with admin.py and apply migrations
* Pass posts from IndexListView to index.html 
* On clicking post, load the post's details by giving href the app's url and the post's id
* Update urls.py of app with the re_path of primary key and render PostDetailView
* Create PostDetailView in views.py and give the model and the template

* Next steps: Need to create post form
* End of my implementation

#### Instructor's implementation
##### Basic App setup:
* project called mysite and app called blog
* Update app details in settings.py 
* Create forms.py within application and then apply migrations
* python manage.py runserver
* After basic setup, proceed with either urls or models
##### Models
* Imports: timezone and reverse
* Expecting only one single user with auth privileges: superuser
* author made as ForeignKey
* For timezone settings, can go to settings.py 
* Methods for model Post like publish and approve_comments