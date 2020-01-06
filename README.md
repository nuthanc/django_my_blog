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

### Instructor's implementation

##### Basic App setup:
* project called mysite and app called blog
* Update app details in settings.py 
* Another concept of LOGIN_REDIRECT_URL in settings.py which is for Redirection to home page after login
* Create forms.py within application and then apply migrations
* python manage.py runserver
* After basic setup, proceed with either urls or models

##### Models
* Imports: timezone and reverse
* Expecting only one single user with auth privileges: superuser
* author made as ForeignKey and connected to superuser
* For timezone settings, can go to settings.py 
* Methods for model Post like publish and approve_comments
* related_name where each Comment is connected to a Post
* The foreign key is for linking Comment and Post
* get_absolute_url in Post models is after creating Post, where should we go. Go to this absolute_url and render post_detail of the Post whose pk was just created

##### Forms and Widgets to correspond to CSS classes
* Add widgets attribute to a Meta class, like TextArea given medium.com styling
* Widget attributes is actually a dictionary
* Update forms.py with Post and Comment forms taking from their models
* After that, for widgets let's say red border to text area box of PostForm:
    * field as key and value is Widget name
    * attrs is a sub-dictionary which has a class
    * class of editable medium-editor-textarea postcontent means it is connected to 3 classes
        * editable and medium-editor-textarea are not our classes

##### Static folder
* It's better to have static folder within an app so that it can moved along with the Application if we want to move this App to another project
* static folder created directly within blog_app
* Add static folder in settings.py file


##### Views, Templates and Urls
* First start with views and connect it to templates
* A lot of CBV have default template name
* TEMPLATE_DIR within settings.py file set as template within App
    * Ex: TEMPLATE_DIR = os.path.join(BASE_DIR, "blog_app/templates/blog_app")
* Template created is within App 
* Under blog_app template, create base.html
* In views.py start with About page
    * Use TemplateView for this and create about.html
* Use blog_app's urls.py for the about page
* Instructor connects Project's urls with App's urls
* In App's urls.py file
    * Setup 'about' path and render AboutView as view
* The homepage is gonna be a list of all the Posts
    * So create PostListView in views.py file
    * Import directly the models Post and Comment
    * Custom list view shown in PostListView
        * Django's ORM for custom touch
        * Django docs link: https://docs.djangoproject.com/en/3.0/topics/db/queries/
            * Search for __(underscore-underscore) and also Field Lookups
        * get_queryset method is used
            * It's like a SQL query
            * Grab the published_dates that are <= Current time
            * Then order them published date, where - is for descending order
        * Most recent blogPost comes up first
    * Add this view in urls.py of blog_app
        

