from django.forms import ModelForm
from .models import UserProfile

class UserProfileForm(ModelForm):
    class Meta:
        model=UserProfile
        fields=['profile_pic','dept','reg','session','section','phone','email','phone'] 