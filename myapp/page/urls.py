from django.urls import path

import page.views

urlpatterns = [
    path("", page.views.main_page),
]