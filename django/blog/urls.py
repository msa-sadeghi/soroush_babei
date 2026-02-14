from django.urls import path
from .views import home, post_detail

app_name = "blog"
urlpatterns = [
    path("", home, name="home"),
    path("post/<slug:slug>/", post_detail, name="post_detail"),
]
