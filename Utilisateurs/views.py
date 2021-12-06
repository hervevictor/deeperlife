from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm , UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import UserSignUpForm, EditProfileForm, PasswordChangingForm
from django.contrib.auth.views import PasswordChangeView



def password_success(request):
    return render(request, 'registration/password_success.html', {})


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')
     

class UserEditProfile2View(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'registration/edit_profile2.html' 
    success_url = reverse_lazy('home')
    
    def get_object(self) :
        return self.request.user



class UserRegistration(generic.CreateView):
    form_class = UserSignUpForm
    template_name = 'registration/register.html' 
    success_url = reverse_lazy('login')


class UserEditeProfile(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html' 
    success_url = reverse_lazy('login')
    
    def get_object(self):
        return self.request.user
        


