from django import forms
from .models import Post,Document

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = "__all__"
        exclude = ["aurthur"]

class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = "__all__"
        exclude = ["aurthur"]