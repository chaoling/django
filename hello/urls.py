from django.urls import path
from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path("bob", views.bob, name="bob"),
     path("david", views.david, name="david"),
     path("<str:name>", views.greet, name="greet")
 ]
