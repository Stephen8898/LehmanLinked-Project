from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm, RegisterFormProfile

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        # form_p = RegisterFormProfile(request.POST)
        if form.is_valid():
            form.save()
            # form_p.save()
            name = form.cleaned_data.get('first_name')
            messages.success(request, f'Account made for {name}')
            return redirect('login')
    else:
        form = RegisterForm()
        form_p = RegisterFormProfile()

    context = {
        'form': form,
        # 'usertype': form_p
    }
    return render(request, 'users/register.html', context)


def profile(request):
    return render(request, 'users/profile.html')

def update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(request, f'Profile has been Updated')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': u_form,
        'profile_form': p_form
    }
    return render(request, 'users/updatepage.html', context)
