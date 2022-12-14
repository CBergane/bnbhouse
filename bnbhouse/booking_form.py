from django import forms


class Availabilety(forms.Form):
    HOUSE_CATAGORIES = (
        ('BAS', 'BASIC'),
        ('STN', 'STANDARD'),
        ('LUX', 'LUXURIUS'),
        ('ROY', 'ROYAL'),
    )
    house_catagory = forms.ChoiceField(choices=HOUSE_CATAGORIES, required=True)
    check_in = forms.DateTimeField(required=True, input_formats=['%Y-%m-%d'])
    check_out = forms.DateTimeField(required=True, input_formats=['%Y-%m-%d'])
