from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User as UserModel   
from PIL import Image, ImageOps


class UserCreationFormulario(UserCreationForm):
    email = forms.EmailField(label="Email", widget=forms.TextInput)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput)


    class Meta:
        model = UserModel
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k: "" for k in fields}



class UserEditionFormulario(UserChangeForm):
    email = forms.EmailField(required=False)
    first_name = forms.CharField(label="Name", required=False)
    last_name = forms.CharField(label="Last Name", required=False)

    delete_avatar = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.CheckboxInput(attrs={'class': 'delete-avatar-checkbox'}),
    )

    class Meta:
        model = UserModel
        fields = ["email", "first_name", "last_name", "delete_avatar"]
        help_texts = {k: "" for k in fields}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Exclude password fields if needed
        self.fields.pop('password', None)



# class UserEditionFormulario(UserChangeForm):
#     email = forms.EmailField(required=False)
#     first_name = forms.CharField(label="Name", required=False)
#     last_name = forms.CharField(label="Last Name", required=False)
#     delete_avatar = forms.BooleanField(
#         required=False,
#         initial=False,
#         widget=forms.CheckboxInput(attrs={'class': 'delete-avatar-checkbox'}),  # Add a class to style the checkbox
#     )

#     class Meta:
#         model = UserModel
#         fields = ["email", "first_name", "last_name", "delete_avatar"]
#         help_texts = {k: "" for k in fields}

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Exclude password fields if needed
#         self.fields.pop('password', None)



class UserAvatarFormulario(forms.ModelForm):

    class Meta:
        model = models.Avatar
        fields = ["imagen"]



class CustomPasswordChangeForm(PasswordChangeForm):
    
    # Customize error messages for the form
    error_messages = {
        'password_incorrect': '',
        'password_mismatch': '',
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Make the new password field optional
        self.fields['new_password1'].required = False
        self.fields['new_password2'].required = False

    def set_password(self, user):
        # Override the set_password method to avoid raising validation errors
        pass

    def clean_new_password1(self):
        # Override clean_new_password1 to allow an empty new password
        return self.cleaned_data.get('new_password1', None)

    def clean_new_password2(self):
        # Override clean_new_password2 to allow an empty password confirmation
        return self.cleaned_data.get('new_password2', None)

    def clean(self):
        cleaned_data = super().clean()
        
        # Check if 'new_password1' is in cleaned_data and is empty
        if 'new_password1' in cleaned_data and not cleaned_data['new_password1']:
            # Remove the error message for an empty new password
            self._errors.pop('new_password1', None)
        
        # Check if 'new_password2' is in cleaned_data and is empty
        if 'new_password2' in cleaned_data and not cleaned_data['new_password2']:
            # Remove the error message for an empty confirmation password
            self._errors.pop('new_password2', None)

        return cleaned_data
    



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields = ['bio']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        }