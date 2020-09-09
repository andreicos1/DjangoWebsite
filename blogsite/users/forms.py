'''
At the heart of Django forms lies Django's Form class. Such as a django model
describes the logical strcture of an object, its behavior and the way its parts are
represneted to us, a Form class describes a form and determines how it works and appears

a model's class fields map to database fields; similarly, a form class's fields
map to HTML form <input> elements.

A form filed is presented to a user in the browser as an HTML 'widget', a piece
of user interface machinery. Each field type has an appropriate deafult Widget class,
but can be overridden as required.

we instantiate the form in the view

Form instance has an is_valid() method, if all fields are vaild it return True
and places the form's data in its cleaned_data attribute
#############


Form classes are created as subclasses of either django.forms.Form or
django.forms.ModelForm

ModelForm can be thought of as a subclass of Form

If the form will directly add or edit a Django model, a ModelForm can save time
and code, as it will build a form along with the appropriate fields and their
attributes from a Model class

Forms can be
    -bound: has submitted data, hence can be used to tell if data is valid. it can include error messages for users
    -unbound: has no data associated with it

formsets exist to allow user to work with multiple forms on the same page

ModelForm will create a form with the fields from Model. The Meta class is used
to determine which fields are used and change their appeareance. ModeForm only
generates fields that are MISSING from the form, that weren't defined declaratively.

'''
'''
Extending the default UserCreationForm
'''

from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User, Profile
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class SignUpForm(UserCreationForm):
    class Meta:
        '''
        reset the order in which the fields are displayed to the user
        '''
        model = User
        fields =('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        # first call the 'real' __init__()
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    def clean_value(self, request):
        email=self.cleaned_data['email']
        if email in User.objects.values_list('email', flat=True):
            raise ValidationError("Email must be unique !")


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        # first call the 'real' __init__()
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'

    def clean_value(self, request):
        email=self.cleaned_data['email']
        if request.user.email!=email and email in User.objects.values_list('email', flat=True):
            raise ValidationError("Email must be unique !")



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'location', 'birth_date', 'image')

    def __init__(self, *args, **kwargs):
        # first call the 'real' __init__()
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['bio'].widget.attrs['class'] = 'form-control'
        self.fields['location'].widget.attrs['class'] = 'form-control'
        self.fields['birth_date'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'form-control'
