from django import forms


class EnigmaForm(forms.Form):
    response = forms.CharField(max_length=30, required=True)
    time = forms.IntegerField(required=True)

    class Meta:
        fields = ('response', 'time')
