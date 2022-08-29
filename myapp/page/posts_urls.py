from django.urls import path

import page.views

urlpatterns = [
    path("create/", page.views.create_post)
]
