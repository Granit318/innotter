"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import user
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from page.views import PageViewSet, PostViewSet, TagViewSet
from rest_framework import routers
from user import views as user_views
from user.views import UserViewSet
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"pages", PageViewSet)
router.register(r"tags", TagViewSet)
router.register(r"posts", PostViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("page/", include("page.urls")),
    path("user/", include("user.urls")),
    path('post/', include("page.posts_urls")),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("register/", user.views.register, name="register"),
    path("profile/", user_views.profile, name="profile"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html", next_page='/profile/'),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="users/logout.html"),
        name="logout",
    )
]
