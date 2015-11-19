from django import forms
import models


#Git实验：进行了两处修改。


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
