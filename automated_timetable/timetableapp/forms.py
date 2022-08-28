from .models import *
from django import forms
from bootstrap_datepicker_plus.widgets import TimePickerInput

# class coursesform(forms.ModelForm):
#     class Meta:
#         model = courses
#         fields = "__all__"
#         widgets={'starttime' : TimePickerInput(),
#         }


class coursesform(forms.ModelForm):
    class Meta:
        model = courses
        fields = "__all__"
        # exclude = ['title']

    