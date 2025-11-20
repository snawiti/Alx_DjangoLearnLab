from django import forms

class ExampleForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        required=True,
        label="Search",
        widget=forms.TextInput(attrs={"placeholder": "Enter search query"})
    )
