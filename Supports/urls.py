from django.urls import path
from .views import supports


urlpatterns = [
    path('support', supports, name='support')
]
 




