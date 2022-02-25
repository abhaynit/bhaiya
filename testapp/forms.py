from django.forms import ModelForm
from testapp.models import addimg

class addim(ModelForm):
    class Meta:
        model = addimg
        fields = ['im']