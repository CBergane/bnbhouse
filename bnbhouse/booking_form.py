from django import forms
from datetime import datetime


class Availabilety(forms.Form):
    check_in = forms.DateTimeField(
        required=True, input_formats=("%Y-%B-%d"))
    check_out = forms.DateTimeField(
        required=True, input_formats=("%Y-%B-%d"))
