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
* Next view is PostDetailView
    * Only need to have model in this view
    * And add url in blog_app's urls.py
* Next view is CreatePostView
    * For authentication, we use mixins for class based views as we use decorators for functions based views
    * Import mixins from django.contrib.auth.mixins
    * Import PostForm from App's forms
    * In urls.py of blog_app, 
* Next view is UpdateView
    * All the attributes are same as CreatePostView
    * In blog_app's urls.py, add the re_path
* Next view is DeleteView
    * Add model and success_url
    * Need to use reverse_lazy so that it will get redirected when it is actually deleted
    * Update urls.py of blog_app
* Next view is DraftListView
    * get_queryset's filter published_date is null meaning it doesn't have publication date
    * Add this to urls.py of blog_app
* Templates for the views:
    * post_detail.html which is the default template for DetailView with Post model
    * post_form.html which is the default template for CreateView
    * post_list.html which is the default template for ListView
    * post_confirm_delete.html for DeleteView
    * post_draft_list for ListView
    * comment_form for comment's CreateView
* add_comment_to_post function in views.py
    * Need to import get_object_or_404, redirect, login_required, timezone
    * Take pk that links comment to the post
    * get_object_or_404: Gets the Post object 
    * request.method == 'POST': means form is filled
    * Update urls.py of blog_app
* comment_approved function in views.py
    * Call approve function after getting the comment object
    * return redirect to post pk and this post attribute is present in Comment model as foreign key
    * Update urls.py of blog_app
* comment_remove function in views.py
    * Get post_pk because pk won't be available after comment is deleted
    * Update urls.py of blog_app
* post_publish function in views.py
    * publish the Post
    * Redirect to post_detail
    * Update urls.py of blog_app

##### Authentication system on top of superuser group
* Anyone who wants to create a Post needs to be a superuser
* In urls.py of project my_blog
    * Import views from auth
    * Add paths to login and logout
    * When you logout, the next page is home page, so supply them as kwargs
* Under login of registration template
    * content is used instead of body
    * hidden input has basically has to do with the view we are operating with
        * IN urls.py of project, views.login will provide with the next value
* base.html of blog_app templates
    * Add load staticfiles so that way we can reference blog_app css files
    * Get Bootstrap 3.3.7
    * Get Medium style editor: https://github.com/yabwe/medium-editor
    * Demo link: https://github.com/yabwe/medium-editor/blob/master/demo/textarea.html
        * After you link everthing, i.e, the js and the css
        * Create a script, which is a editor object 
        * Also, make sure we have editable medium-editor-textarea class
    * Make sure custom css goes after all other css
        * Check out codepen for hue loaders, where you will get code of HTML and CSS
        * Copy CSS to blog.css
        * Get rid of b1,b2 and b3 classes
        * Change background to color in loader class
        * Remove positions in loader class
    * Get google fonts 
    * Setup navbar in body
        * Custom bigbrand class for Brand
        * user.is_authenticated comes from auth library Django
* Fill out other templates in blog_app
    * post_detail.html
        * safe filter is for when medium highlight bold makes
            * <b>Hi there<b>
            * The ending tag is made safe
        * linebreaksbr filter if when line breaks are there, HTML will also have line breaks
        * Using span for icons
    * post_form.html
        * Custom class of post-form if we want to do anything in the future
        * form doesn't need an action as Django takes care of it
        * form.as_p has classes in the widgets 
        * save is custom class
        * Injecting script from Medium github
        * .editable class is attached as a widget in the form PostForm
    * post_confirm_delete
        * object is given by Delete_View
    * comment_form.html
        * To have same capabilities as Medium editor, add the script

#### Error corrections
* In urls.py of blog_app, remove extra spaces in regular expressions
* In urls.py of my_blog, replace login and logout with their corresponding Views