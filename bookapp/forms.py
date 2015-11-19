from django import forms
import models


class AuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        exclude = []


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        exclude = []

    # PublishDate = forms.DateField(widget=forms.TextInput(attrs=
    # {
    #     'class': 'datepicker'
    # }))
