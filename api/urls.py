
from django.contrib import admin
from django.urls import path, include
from .routes.get_blog import GetBlog
from .routes.post_blog import PostBlog
from .routes.edit_blog import EditBlog
from .routes.delete_blog import DeleteBlog

urlpatterns = [
   	 path('get_blog/', GetBlog.as_view()),
   	 path('post_blog/', PostBlog.as_view()),
   	 path('edit_blog/', EditBlog.as_view()),
   	 path('delete_blog/', DeleteBlog.as_view()),
]
