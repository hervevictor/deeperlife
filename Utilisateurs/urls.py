from django.urls import path
from .views import UserRegistration, UserEditeProfile, PasswordsChangeView, UserEditProfile2View
from django.contrib.auth import views as auth_views
from . import views 

urlpatterns = [
    path('register/', UserRegistration.as_view(), name="register"),
    path('edit_profile/', UserEditeProfile.as_view(), name="edit_profile"),
    path('edit_profile2', UserEditProfile2View.as_view(), name='edit_profile2'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change_password.html')),
    path('password_success', views.password_success, name='password_success'),

]




