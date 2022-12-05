from django import forms
from blog.models import *

class CommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        # for remove label names from form
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""

    class Meta:
        model = Comment
        fields = ['message']
    

