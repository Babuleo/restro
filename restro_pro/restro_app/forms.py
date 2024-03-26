from django import forms
from multiupload.fields import MultiFileField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class MyImageForm(forms.Form):
    files = MultiFileField(max_file_size=1024 * 1024 * 5, max_num=5, required=False)

class customuserform(UserCreationForm):
    phone_number=forms.CharField(required=True)
    class Meta:
        model=User
        fields=('username','email','phone_number','password1','password2')