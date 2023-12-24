from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f"Account for {username} has been created, you are now able to login")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, "user/register.html", {'form': form})


@login_required
def profile_change(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid and p_form.is_valid:
            u_form.save()
            p_form.save()
            messages.success(
                request, f"Your account has been updated successfully.")
            return redirect("profile-change")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
            "u_form": u_form,
            "p_form": p_form
        }
    return render(request, "user/profile_change.html", context=context)
