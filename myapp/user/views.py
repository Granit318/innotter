from rest_framework import mixins, viewsets
from user.models import User
from user.serializer import UserSerializer
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from user.forms import UserUpdateForm, ProfileUpdateForm
from services.user_service import UserService


class UserViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def register(request):
    return UserService().register(request)


@login_required
def profile(request):
    return UserService().profile(request)
