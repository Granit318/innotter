import uuid

from django.contrib import messages
from django.shortcuts import redirect, render

from page.models import Page
from user.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from user.models import Profile


class UserService:
    def register(self, request):
        if request.method == "POST":
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get("username")
                messages.success(request, f"Ваш аккаунт создан: можно войти на сайт.")
                Profile(user_id=user.id).save()
                Page(owner_id=user.id, uuid=uuid.uuid4()).save()

                return redirect("login")
        else:
            form = UserRegisterForm()
        return render(request, "users/register.html", {"form": form})

    def profile(self, request):
        if request.method == 'POST':
            u_form = UserUpdateForm(request.POST, instance=request.user)
            p_form = ProfileUpdateForm(request.POST,
                                       request.FILES,
                                       instance=request.user.profile)
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, f'Ваш профиль успешно обновлен.')
                return redirect('profile')

        else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'u_form': u_form,
            'p_form': p_form
        }

        return render(request, 'users/profile.html', context)
