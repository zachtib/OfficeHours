from django import forms


class TimeSlotRequestForm(forms.Form):
    timeslot_id = forms.HiddenInput()

    name = forms.CharField(max_length=254)
    email_address = forms.EmailField()
    details = forms.CharField(
        widget=forms.Textarea
    )
