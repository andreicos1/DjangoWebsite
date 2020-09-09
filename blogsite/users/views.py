from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User as Super_user
#@login_required redirects user to settings.LOGIN_URL if he's not logged in,
#or a custom redirect field name can be defined
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError

#below so that either all changes to the view are committed if no errors,
# or no changes at all, may get too costly for large traffic websites
#atomic: Atomicity is the defining property of db transactions
from django.db import transaction

from .models import User
from .forms import SignUpForm, UserForm, ProfileForm
superusers=Super_user.objects.filter(is_superuser=True)

class UserList(generic.ListView):
    model = User
    template_name = 'users/list_of_users.html'

    def get_context_data(self, **kwargs):
        context = super(UserList, self).get_context_data(**kwargs)
        context.update({'superusers':superusers})
        return context


class UserDetail(generic.DetailView):
    model = User
    template_name = 'users/profile.html'
    context_object_name = 'this_user'

def sign_up_view(request):
    # if post request, data needs to be processed
    if request.user.is_authenticated:
        return redirect('welcome')
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignUpForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            #process data
            form.clean_value(request)
            form.save() #save the user
            #below we perform the authentification, so user doesn't have to log in after signing up
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password) #this will always return success
            login(request, user) #so we can login the authenticated user
            return redirect('users:profile',user.pk) #redirect to new URL
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'signup_form':form})


@login_required
@transaction.atomic
def update_profile(request):
    current_user = get_object_or_404(User, username=request.user.username)
    if request.method=='POST':
        user_form = UserForm(request.POST, instance = request.user)
        profile_form = ProfileForm(request.POST, request.FILES,
                                instance = current_user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.clean_value(request)
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated !'))
            return redirect('users:profile',current_user.pk)
    else:
        user_form = UserForm(initial={'first_name':current_user.first_name,
                                    'last_name':current_user.last_name,
                                    'email':current_user.email,})
        profile_form = ProfileForm(initial = {
                                        'bio':current_user.profile.bio,
                                        'location':current_user.profile.location,
                                        'birth_date':current_user.profile.birth_date,
                                        'image': current_user.profile.image,})
    return render(request, 'users/update_profile.html',{
            'user_form':user_form,
            'profile_form':profile_form,
            'user': current_user
            })
