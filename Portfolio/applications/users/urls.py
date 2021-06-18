from django.urls import path
from . import views

app_name = "users_app"

urlpatterns = [
    path(
        "contact/",
        views.ContactCreateView.as_view(),
        name="contact",
    ),

]