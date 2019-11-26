from django import forms


class EnigmaForm(forms.Form):
    response = forms.CharField(max_length=30, required=True)
    time = forms.IntegerField(required=True)

    class Meta:
        fields = ('response', 'time')


class ContactForm(forms.Form):
    firstname = forms.CharField(max_length=40, required=True)
    lastname = forms.CharField(max_length=40, required=True)
    mail = forms.EmailField(required=True)

    class Meta:
        fields = ('firstname', 'lastname', 'mail')