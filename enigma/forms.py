from django import forms


class EnigmaForm(forms.ModelForm):
    response = forms.CharField(max_length=30, required=True)

    class Meta:
        fields = 'response'
